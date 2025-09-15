# Pipeline de Dados com IoT e Docker

## Descrição
Este projeto implementa um pipeline de dados para processar leituras de temperatura de dispositivos IoT. 
Os dados são armazenados em um banco PostgreSQL via Docker e visualizados em um dashboard interativo com Streamlit.

## Estrutura do Projeto
- `src/pipeline.py`: Script para ingestão dos dados no PostgreSQL.
- `src/dashboard.py`: Dashboard interativo com Streamlit.
- `sql/views.sql`: Views SQL utilizadas para análise.
- `docker-compose.yml`: Configuração do container PostgreSQL.

## Pré-requisitos
- Python 3.8+
- Docker
- Docker Compose
- Bibliotecas Python:
  ```bash
  pip install pandas psycopg2-binary sqlalchemy streamlit plotly
  ```

## Passos para Execução

1. **Subir o PostgreSQL com Docker**
   ```bash
   docker-compose up -d
   ```

2. **Executar o pipeline**
   ```bash
   python src/pipeline.py
   ```

3. **Criar as views no banco**
   ```bash
   psql -U postgres -d iot_db -f sql/views.sql
   ```

4. **Rodar o dashboard**
   ```bash
   streamlit run src/dashboard.py
   ```

## Dataset
O dataset utilizado é o [Temperature Readings: IoT Devices](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices).

## Insights
- Média de temperatura por dispositivo.
- Frequência de leituras por hora.
- Variação diária das temperaturas (máximas e mínimas).

## Autor
Projeto desenvolvido como parte da disciplina **Disruptive Architectures: IoT, Big Data e IA**.
