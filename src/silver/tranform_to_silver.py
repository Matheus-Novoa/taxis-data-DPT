import duckdb
from pathlib import Path


root_path = Path().absolute()
bronze_db_path = root_path / 'data/bronze/banco.db'
query = (root_path / 'src/silver/transform.sql').read_text()

with duckdb.connect(bronze_db_path) as con:
    print("Criando tabela 'silver'")
    con.sql("DROP TABLE IF EXISTS taxi_data_silver")
    con.sql(f'CREATE TABLE taxi_data_silver AS {query}')

    total = con.sql("SELECT count(*) FROM taxi_data_silver").fetchone()[0]
    print(f"Total de registros na tabela 'taxi_data_silver': {total}")