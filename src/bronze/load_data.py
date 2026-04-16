import duckdb
from pathlib import Path


db_path = 'data/bronze/banco.db'
data_dir = Path('data/raw') 

print(f"Verificando pasta de dados: {data_dir.resolve()}")

arquivos_encontrados = list(data_dir.glob('yellow_tripdata_*.csv'))
print(f"Arquivos CSV encontrados: {len(arquivos_encontrados)}")

for f in arquivos_encontrados:
    print(f" - {f.name}")

if len(arquivos_encontrados) == 0:
    print("❌ ERRO: Nenhum arquivo CSV encontrado! Verifique se a variável 'data_dir' está correta.")
else:
    with duckdb.connect(db_path) as con:
        print("\nLimpando e reimportando...")
        con.sql("DROP TABLE IF EXISTS taxi_data")
        con.sql(f"""
            CREATE TABLE taxi_data AS 
            SELECT * FROM read_csv('{data_dir}/yellow_tripdata_*.csv', 
                                   header=True, 
                                   union_by_name=True)
        """)
        
        total = con.sql("SELECT count(*) FROM taxi_data").fetchone()[0]
        print(f"✅ SUCESSO! Agora a tabela tem {total} linhas.")
        