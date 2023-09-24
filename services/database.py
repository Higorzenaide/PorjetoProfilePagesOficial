from dotenv import load_dotenv
import os
from supabase import create_client

class SupabaseConnection:
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.supabase = None

    def conectar(self):
        # Cria e retorna o cliente do Supabase
        if self.url and self.key:
            self.supabase = create_client(self.url, self.key)
            print("Conexão com o Supabase bem-sucedida")
            return self.supabase
        else:
            raise ValueError("As variáveis de ambiente SUPABASE_URL e SUPABASE_KEY não estão definidas corretamente.")