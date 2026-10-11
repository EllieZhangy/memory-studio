FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
COPY skills skills
RUN useradd --create-home studio && mkdir -p /app/.runtime/generated && chown -R studio:studio /app/.runtime
USER studio
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
