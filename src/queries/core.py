from sqlalchemy import text, insert,select, update
from database import sync_engine
from models import metadat_obj, workers_table





class SyncCore:

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadat_obj.drop_all(bind=sync_engine)
        metadat_obj.create_all(bind=sync_engine)
        sync_engine.echo = True
        
        
        
    @staticmethod
    def insert_data():
        with sync_engine.connect() as conn:
            stmt = insert(workers_table).values(username='zhmix')
            conn.execute(stmt)
            conn.commit()
            
            
    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table)
            result = conn.execute(query)
            workers = result.all()
            print(f'{workers=}')
            
            
    @staticmethod
    def update_workers(new_username:str ='Pcheluk',worker_id:int=2):
        with sync_engine.connect() as conn:
            stmt = (
                update(workers_table)
                .values(username=new_username)
                .where(workers_table.c.id==worker_id)
            )
            conn.execute(stmt)
            conn.commit()