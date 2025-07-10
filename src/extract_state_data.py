import tabula
import pandas as pd
#Importar páginas do PDF a serem extraídos os dados - Rodoviar Estaduais
dfs = tabula.read_pdf(r"C:/Users/gusta/Git/projetos/rodovias_files/Relatorio_SRE2024_SC-1.pdf", pages=('20-28'), multiple_tables=False)
sc_fed = dfs[0]
#Renomeando colunas
sc_fed.columns = ['Código do trecho', 'Início do trecho', 'Fim do trecho', 'Início (km)', 'Fim (km)', 'Ext. (km)', 'Situação física', 'Estadual coincid.', 'Federal superp.', 'TMD']
#Removendo linhas que começam com "CÓDIGO DO" e "TRECHO"
sc_fed = sc_fed[sc_fed['Código do trecho'] != 'CÓDIGO DO']
sc_fed = sc_fed[sc_fed['Código do trecho'] != 'TRECHO']
#Resetando index após filtrar os valores
sc_fed.reset_index(drop=True, inplace=True)
del dfs
dfs = tabula.read_pdf(r"C:/Users/gusta/Git/projetos/rodovias_files/Relatorio_SRE2024_SC-1.pdf", pages=('29-51'), multiple_tables=False)
sc_est = dfs[0]
sc_est.columns = ['Código do trecho', 'Início do trecho', 'Fim do trecho', 'Início (km)', 'Fim (km)', 'Ext. (km)', 'Situação física', 'Tipo revest.', 'Estadual coincid.', 'Federal superp.', 'TMD']
sc_est = sc_est[sc_est['Código do trecho'] != 'CÓDIGO DO']
sc_est = sc_est[sc_est['Código do trecho'] != 'TRECHO']
sc_est.reset_index(drop=True, inplace=True)
#Incluindo dados do excel - Rodovias Federais
df_fed = pd.read_excel("C:/Users/gusta/Git/projetos/rodovias_files/VMDa 2023.xlsx", sheet_name="SNV202401A")
df_fed_sc = df_fed[df_fed['sg_uf'] == 'SC']
print("finish")