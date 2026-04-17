import psycopg2 as pg
from psycopg2 import Error
import psycopg2.extras
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def connect():
    try:
        conn = pg.connect(
            database='postgres',
            user='postgres',
            password='dskjfsdknfsjkdfhsdjkf',
            host='db.kegawbegcqwwrczfrrcl.supabase.co',
            port=5432,
            sslmode='require',
            options='-c hostaddr=IPv4_DO_SUPABASE'
        )
        return conn

    except Exception as e:
        print("Erro ao conectar:", e)
        return None


def encerra_conexao(connect):
    if connect:
        connect.close()
        print("Conexão encerrada")
