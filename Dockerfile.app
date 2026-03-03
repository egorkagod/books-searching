FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV HF_HOME=/opt/hf
ENV TRANSFORMERS_CACHE=/opt/hf/transformers
ENV SENTENCE_TRANSFORMERS_HOME=/opt/hf/sentence-transformers

RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('BAAI/bge-m3')"

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]