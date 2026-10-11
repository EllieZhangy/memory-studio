import base64
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch
from PIL import Image
from fastapi.testclient import TestClient
from app import main


def png(size=(32, 32)):
    buf = io.BytesIO()
    Image.new('RGB', size, '#b0bdad').save(buf, 'PNG')
    return buf.getvalue()


class AppTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(main.app)
        self.style = 'travel-memory-sticker-card'

    def test_page_and_four_styles(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        styles = self.client.get('/api/styles').json()
        self.assertEqual(len(styles), 4)
        self.assertTrue(all('label' in s and 'prompt' not in s for s in styles))

    def test_invalid_image(self):
        r = self.client.post('/api/generate', data={'style': self.style}, files={'image': ('x.png', b'broken')})
        self.assertEqual(r.status_code, 400)

    def test_missing_credentials(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': ''}):
            r = self.client.post('/api/generate', data={'style': self.style}, files={'image': ('x.png', png())})
        self.assertEqual(r.status_code, 503)

    def test_unknown_style(self):
        r = self.client.post('/api/generate', data={'style': 'unknown'}, files={'image': ('x.png', png())})
        self.assertEqual(r.status_code, 400)

    def test_generate_and_download(self):
        import httpx
        response = httpx.Response(200, json={'data': [{'b64_json': base64.b64encode(png((1024,1536))).decode()}]})
        provider = AsyncMock()
        provider.post.return_value = response
        with tempfile.TemporaryDirectory() as folder, patch.object(main, 'OUTPUT', Path(folder)), patch.dict(os.environ, {'OPENAI_API_KEY':'test-only'}), patch('app.main.httpx.AsyncClient') as factory:
            factory.return_value.__aenter__.return_value = provider
            r = self.client.post('/api/generate', data={'style': self.style, 'title': 'My Favorite Travel Buddy'}, files={'image': ('x.png', png())})
            self.assertEqual(r.status_code, 200, r.text)
            payload = r.json()
            downloaded = self.client.get(payload['download_url'])
            self.assertIn('attachment', downloaded.headers['content-disposition'])
            with Image.open(io.BytesIO(downloaded.content)) as image:
                image.load()
                self.assertEqual(image.size, (1080,1440))
            call = provider.post.call_args.kwargs
            self.assertIn('exactly two stickers', call['data']['prompt'])
            self.assertIn('My Favorite Travel Buddy', call['data']['prompt'])
            self.assertEqual(call['files']['image'][2], 'image/png')

    def test_provider_failure(self):
        import httpx
        provider = AsyncMock()
        provider.post.return_value = httpx.Response(429)
        with patch.dict(os.environ, {'OPENAI_API_KEY':'test-only'}), patch('app.main.httpx.AsyncClient') as factory:
            factory.return_value.__aenter__.return_value = provider
            r = self.client.post('/api/generate', data={'style':self.style}, files={'image':('x.png',png())})
            self.assertEqual(r.status_code,429)

    def test_download_rejects_bad_path(self):
        self.assertEqual(self.client.get('/api/images/not-a-valid-file.png').status_code,404)


if __name__ == '__main__':
    unittest.main()
