import pandas as pd


df = pd.read_parquet("data/parquet/metricas.parquet")
print(df.to_dict(orient="records"))
