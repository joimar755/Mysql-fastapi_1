from fastapi import FastAPI  
from routes.products import VH
from models import db_p
from config.db import engine, get_db, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

db_p.Base.metadata.create_all(bind=engine)




app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:3000'
    ],  # En producción, especifica los dominios permitidos en lugar de "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(VH)

