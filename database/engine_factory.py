from sqlalchemy import create_engine

def generate_engine(DB_HOST: str, DB_PORT: str, DB_NAME: str, DB_USER: str, DB_PASSWORD: str):
    return create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
                            echo=False)