from models import metadat_obj,WorkersOrm
from database import sync_engine,session_factory






def create_tables():
    sync_engine.echo = False
    metadat_obj.drop_all(bind=sync_engine)
    metadat_obj.create_all(bind=sync_engine)
    sync_engine.echo = True
    
    
def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersOrm(username='bobr')
        worker_zhmix = WorkersOrm(username='zhmix')
        
        session.add_all([worker_bobr,worker_zhmix])
        session.commit()    