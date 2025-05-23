# Spotify Data Pipeline

Este é um projeto educacional de Engenharia de Dados que coleta informações da API do Spotify e salva os dados de artistas em arquivos CSV.

## Objetivo

- Aprender a se conectar com a API do Spotify.
- Realizar ingestão de dados.
- Armazenar dados localmente (ou futuramente na nuvem).
- Praticar boas práticas de organização de projetos de dados.

## Tecnologias

- Python 3.10+
- Spotipy (cliente Python para API do Spotify)
- Pandas
- python-dotenv

## Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/tomnunes/spotify-data-pipeline.git
   cd spotify-data-pipeline
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie o arquivo `.env` com suas credenciais da API do Spotify:
   ```
   SPOTIPY_CLIENT_ID=client-id
   SPOTIPY_CLIENT_SECRET=client-secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

5. Execute o script de ingestão:
   ```bash
   python scripts/ingest_spotify_data.py
   ```

## Estrutura de Pastas

```
spotify-data-pipeline/
├── scripts/
│   └── ingest_spotify_data.py
├── data/
│   └── raw/
├── venv/
├── .env
├── requirements.txt
└── README.md
```

## Próximos módulos

- Armazenamento no AWS S3
- Transformações com Pandas e PySpark
- Orquestração com Apache Airflow