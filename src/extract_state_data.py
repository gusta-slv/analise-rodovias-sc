import tabula
import pandas as pd
dfs = tabula.read_pdf(r"C:/Users/gusta/Git/projetos/rodovias_files/Relatorio_SRE2024_SC-1.pdf", pages=(20))
print(dfs)
print(type(dfs))
print(type(dfs[0]))
print(dfs[0])