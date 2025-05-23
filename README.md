# 🎧 Spotify Data Pipeline

Este projeto é um estudo e tem como objetivo construir um pipeline de engenharia de dados completo que coleta informações da API do Spotify, armazena os dados na AWS, realiza transformações e disponibiliza análises interativas com Python e ferramentas modernas.

---

## 📌 Objetivos

- Coletar dados de artistas, músicas e popularidade diretamente da API do Spotify.
- Armazenar dados brutos e tratados na AWS S3 (simulando um Data Lake).
- Transformar dados com Pandas ou PySpark.
- Criar visualizações interativas com insights musicais.
- Automatizar o pipeline com Airflow.

---

## 🔁 Arquitetura do Pipeline

```mermaid
graph LR
  A[API Spotify] --> B[Script de Ingestão (Python)]
  B --> C[Armazenamento Raw (AWS S3)]
  C --> D[Transformação (Pandas ou PySpark)]
  D --> E[Armazenamento Limpo (S3 Parquet)]
  E --> F[Visualizações (Streamlit / Jupyter)]
