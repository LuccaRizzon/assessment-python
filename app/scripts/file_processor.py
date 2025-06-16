import pandas as pd

def process_pld(caminho_arquivo='files/PLD.xlsx'):
    xls = pd.ExcelFile(caminho_arquivo)
    df = pd.read_excel(xls, sheet_name='Planilha1')
    datas = pd.to_datetime(df.iloc[0, 2:], errors='coerce')
    dados = df.iloc[1:6, 2:].copy()

    dados.columns = datas
    dados.insert(0, 'Submercado', df.iloc[1:6, 1].values)

    df_longo = dados.melt(id_vars='Submercado', var_name='Data', value_name='PLD')
    df_longo.dropna(subset=['Data', 'PLD'], inplace=True)
    df_longo['Data'] = pd.to_datetime(df_longo['Data'], errors='coerce')
    df_longo['Ano'] = df_longo['Data'].dt.year

    maiores_valores = df_longo.groupby(['Submercado', 'Ano'])['PLD'].max().reset_index()

    return maiores_valores.to_dict(orient='records')
