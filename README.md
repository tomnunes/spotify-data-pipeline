# Spotify Data Pipeline

Este projeto é um estudo e tem como objetivo construir um pipeline de engenharia de dados completo que coleta informações da API do Spotify, armazena os dados na AWS, realiza transformações e disponibiliza análises interativas com Python e ferramentas modernas.

---

## Objetivos

- Coletar dados de artistas, músicas e popularidade diretamente da API do Spotify.
- Armazenar dados brutos e tratados na AWS S3 (simulando um Data Lake).
- Transformar dados com Pandas ou PySpark.
- Criar visualizações interativas com insights musicais.
- Automatizar o pipeline com Airflow.

---

## Arquitetura do Pipeline

```mermaid
graph LR
  A[API Spotify] --> B[Script de Ingestão (Python)]
  B --> C[Armazenamento Raw (AWS S3)]
  C --> D[Transformação (Pandas ou PySpark)]
  D --> E[Armazenamento Limpo (S3 Parquet)]
  E --> F[Visualizações (Streamlit / Jupyter)]
```
---

## Tecnologias e Ferramentas

- Python 3.10+
- spotipy (SDK do Spotify)
- pandas / pyspark
- AWS S3
- Apache Airflow
- Jupyter Notebook / Streamlit
- Git & GitHub

---

## Estrutura do Projeto

```spotify-data-pipeline/
├── README.md
├── notebooks/         # Análises e testes locais
├── scripts/           # Scripts de ingestão e transformação
├── data/              # Dados locais para testes
├── dags/              # DAGs para orquestração (Airflow)
└── requirements.txt   # Dependências Python
```

--- 

## Autor
Feito por Thomas Nunes.
