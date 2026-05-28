import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém a URI de conexão de forma segura
DATABASE_URL = os.getenv("DB_URI")

def conectar_banco():
    try:
        # Estabelece a conexão
        conexao = psycopg2.connect(DATABASE_URL)
        cursor = conexao.cursor()
        
        # Exemplo de query
        cursor.execute("SELECT version();")
        versao = cursor.fetchone()
        print(f"Conectado ao banco de dados! Versão: {versao}")
        
        cursor.close()
        conexao.close()
    except Exception as error:
        print(f"Erro ao conectar: {error}")

if __name__ == "__main__":
    conectar_banco()
