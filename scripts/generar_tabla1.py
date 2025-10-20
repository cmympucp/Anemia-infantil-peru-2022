import pandas as pd

df = pd.read_csv("data/Tabla_referente_1.csv")

cols_first_two = df.columns[:2]                  # dos primeras columnas
cols_hv = [f"HV{str(i).zfill(3)}" for i in range(25, 41)]  # HV025 a HV040
df_subset = df[list(cols_first_two) + cols_hv]

df_preview = df_subset.head(20)

df_preview.to_markdown("Tabla_referente_1_preview.md", index=False)

print("Tabla Markdown creada: Tabla_referente_1_preview.md")
