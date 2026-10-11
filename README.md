# Memory Studio

上传照片，选择风格，生成可下载的 3:4 竖版海报。A small photo-to-poster web studio with an image-generation API.

## Run locally

Requires Python 3.12. From this repository:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
# Set OPENAI_API_KEY securely in your shell or hosting environment.
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000`. API documentation: `/docs`. `.env.example` lists settings; `.env` is not automatically loaded. The API key stays on the server. The default provider is OpenAI Images Edit with `gpt-image-1`; the account needs model access and billing. Each generation is chargeable. The uploaded photo is sent to OpenAI; consider its data policies before uploading personal photos.

## Styles

| Style ID | English label | Direction |
| --- | --- | --- |
| `scenes-gathered-zine-v1-3` | Collage Zine | Layered scenes and handmade paper fragments |
| `photo-to-zine-postcard` | Illustrated Postcard | Original photo paired with a flat illustration |
| `travel-memory-sticker-card` | Memory Sticker Card | Photo above, illustration below left, stickers below right |
| `gc-minimal-zine-poster-v0-3` | Minimal Editorial Poster | Restrained palette, typography, and generous whitespace |

These are editable prompt templates in `skills/styles.json`, **not imported copies of the original skills**: their original definitions were unavailable. Replace their prompts with your canonical skill instructions if you have them. The person-and-dog sticker template explicitly requests only two stickers. Other scenes request 5–7. Image-generation instructions are probabilistic; review composition and lettering before printing.

The provider returns a 1024 × 1536 portrait. A centered safe-area crop and resampling creates an exact **1080 × 1440 (3:4)** PNG. The uploaded original is not retained on disk; generated images are stored in `.runtime/generated`. The photo region is recreated by the image model, so it is not a pixel-identical paste of the upload. EXIF metadata is removed before transmission. Generated files have unguessable IDs but no per-user access control; do not treat links as private storage. Delete old files periodically to manage storage.

## API

- `GET /api/styles` — available styles and English descriptions
- `GET /api/health` — service and credential-presence status
- `POST /api/generate` — multipart `image`, `style`, optional `title` (up to 100 characters)
- `GET /api/images/{id}.png` — preview; add `?download=true` for an attachment

```bash
curl -X POST http://127.0.0.1:8000/api/generate \
  -F 'image=@your-photo.jpg' \
  -F 'style=travel-memory-sticker-card' \
  -F 'title=My Favorite Travel Buddy'
```

Uploads: JPG, PNG, WebP; maximum 15 MB / approximately 24 megapixels. Large photos are reduced to a maximum 2048-pixel edge for the provider. Generation may take several minutes; configure deployment request timeouts accordingly.

## Deployment

Use a Docker-capable host such as Render, Railway, or your own server. Build the included Dockerfile, expose port 8000, and set `OPENAI_API_KEY` in the host's secret settings. Optional settings: `POSTER_IMAGE_MODEL`, `POSTER_OUTPUT_DIR`. For durable downloads, mount a writable persistent disk and point `POSTER_OUTPUT_DIR` to it. This synchronous API is best for small private use. Before sharing publicly, place it behind your hosting provider's authentication and request/concurrency limits to prevent unauthorized paid API calls. Multi-user public operation needs authentication, per-user storage, quota management, and a background job queue.

```bash
docker build -t memory-studio .
docker run --rm -p 8000:8000 --env OPENAI_API_KEY memory-studio
```

GitHub stores the source and sample artwork; GitHub Pages alone cannot run the Python API. Deploy the server separately to get a public website URL. No automatic public deployment or image push is performed by the app.

## Validation

```bash
python -m unittest discover -s tests -v
```

Tests exercise upload validation, missing credentials, provider errors, generated-image decoding, exact 3:4 export, and attachment downloads using a mocked provider. Real paid image generation must be checked after configuring your API key.

### Render quick start

[Deploy to Render](https://render.com/deploy?repo=https://github.com/EllieZhangy/my-ai-poster-skills)

The included `render.yaml` creates a paid Starter web service and 1 GB persistent disk. Review Render's pricing before creating it. Enter `OPENAI_API_KEY` securely during setup. The resulting Render service URL opens the studio; this GitHub repository URL does not. Keep the service private or protect access at your hosting layer before sharing it widely.
