from sqlalchemy import text, insert
from database import sync_engine
from models import metadat_obj, workers_table




def create_tables():
    sync_engine.echo = False
    metadat_obj.drop_all(bind=sync_engine)
    metadat_obj.create_all(bind=sync_engine)
    sync_engine.echo = True
    
    
    
def insert_data():
    with sync_engine.connect() as conn:
        # stmt = """
        # INSERT INTO  workers (username) VALUES
        # ('pchel'), ('vovk');
        # """
        
        stmt = insert(workers_table).values(username='chelik')
        conn.execute(stmt)
        conn.commit()
        