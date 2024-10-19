from fastapi import FastAPI
from app.api.user_routes import router as user_router
from app.db.database import Base, engine

# Inicializa as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registra o roteamento de usuários
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "User Service API"}
