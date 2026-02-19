import pandas as pd
from sqlalchemy import create_engine
import urllib

import os
from dotenv import load_dotenv

load_dotenv() 

server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

def processar_rfm():
    try:
        print("Conectado ao SQL Server. Extraindo dados...")
        df = pd.read_sql("SELECT * FROM tb_vendas_brutas", engine)
        
        if df.empty:
            print("Erro: A tabela 'tb_vendas_brutas' está vazia.")
            return
 
        # Tratamento de Dados
        df['valor_total'] = pd.to_numeric(df['valor_total'], errors='coerce')
        df['data_compra'] = pd.to_datetime(df['data_compra'], errors='coerce')
        df = df.dropna(subset=['id_cliente', 'data_compra', 'valor_total'])

        # Cálculo do RFM
        print("Calculando métricas")
        data_ref = df['data_compra'].max() + pd.Timedelta(days=1)

        rfm = df.groupby('id_cliente').agg({
            'data_compra': lambda x: (data_ref - x.max()).days,
            'id_pedido': 'nunique',
            'valor_total': 'sum'
        }).rename(columns={'data_compra': 'Recencia', 'id_pedido': 'Frequencia', 'valor_total': 'Valor'})

        # Scores do rfm (1-5)
        rfm['R_Score'] = pd.qcut(rfm['Recencia'].rank(method='first'), 5, labels=[5, 4, 3, 2, 1])
        rfm['F_Score'] = pd.qcut(rfm['Frequencia'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
        rfm['M_Score'] = pd.qcut(rfm['Valor'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
        rfm['RFM_Score_Geral'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

        # Conversão do id_cliente em coluna
        rfm_final = rfm.reset_index()
        rfm_final.to_sql('tb_resultado_rfm', engine, if_exists='replace', index=False)
        
        print("\n--- SUCESSO ---")
        print(f"Clientes processados: {len(rfm_final)}")
        print("A tabela 'tb_resultado_rfm' foi criada com sucesso.")

    except Exception as e: 
        print(f"Ocorreu um erro durante o processamento: {e}")

if __name__ == "__main__":
    processar_rfm()