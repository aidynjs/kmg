from fastapi import FastAPI
from app.api.company import router as company_router
from app.api.mine import router as mine_router
from app.api.employee import router as employee_router

app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs")


@app.on_event("startup")
async def startup():
    from sqlalchemy import create_engine
    from sqlalchemy_utils import create_database, database_exists

    from app.core.config import settings
    from app.db.base import Base

    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(bind=engine)
    else:
        Base.metadata.drop_all(bind=engine)
        engine.connect()
        Base.metadata.create_all(bind=engine)




app.include_router(company_router, prefix='/api/v1/company', tags=['company'])
app.include_router(mine_router, prefix='/api/v1/mine', tags=['mine'])
app.include_router(employee_router, prefix='/api/v1/employee', tags=['employee'])