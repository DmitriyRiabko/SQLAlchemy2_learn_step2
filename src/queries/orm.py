from models import WorkersOrm
from database import sync_engine,session_factory, Base
from sqlalchemy import select, update




class SyncOrm:

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(bind=sync_engine)
        Base.metadata.create_all(bind=sync_engine)
        sync_engine.echo = True
        
        
    @staticmethod
    def insert_data():
        with session_factory() as session:
            worker_bobr = WorkersOrm(username='bobr')
            worker_zhmix = WorkersOrm(username='zhmix')
            
            session.add_all([worker_bobr,worker_zhmix])
            session.commit()    
            
            
            
    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            ...
          
            
            
    @staticmethod
    def update_workers(new_username:str ='Pcheluk',worker_id:int=2):
        with sync_engine.connect() as conn:
          ...