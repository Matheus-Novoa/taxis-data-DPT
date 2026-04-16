import duckdb
from pathlib import Path


bronze_db_path = 'data/bronze/banco.db'
query = Path('transform_query.sql').read_text()

with duckdb.connect(bronze_db_path) as con:
    print("Criando tabela 'metricas'")
    con.sql("DROP TABLE IF EXISTS metricas")
    con.sql(f"CREATE TABLE metricas AS {query}")  # Create the table first
    con.sql("COPY metricas TO 'data/parquet/metricas.parquet' (FORMAT 'parquet')")  # Then export it

    total = con.sql("SELECT count(*) FROM metricas").fetchone()[0]
print(f"✅ SUCESSO! A tabela 'metricas' na camada Silver tem {total} linhas.")
