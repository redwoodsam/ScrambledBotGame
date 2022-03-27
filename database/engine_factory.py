from sqlalchemy import create_engine

def generate_engine(DB_HOST: str, DB_PORT: str, DB_NAME: str, DB_USER: str, DB_PASSWORD: str, DB_ENCODING:str):
    return create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset={DB_ENCODING}',
                            echo=False)