from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="To-Do List API",
    description="API REST para gerenciar tarefas usando FastAPI",
    version="1.0.0"
)

# Modelo Pydantic para uma tarefa
class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, description="Título da tarefa")
    description: Optional[str] = Field(None, description="Descrição detalhada da tarefa")
    status: str = Field("pending", description="Status da tarefa: pending, in_progress, completed")
    created_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Estudar FastAPI",
                "description": "Completar a tarefa de APIs REST",
                "status": "pending"
            }
        }

# Modelo para atualização de tarefa (campos opcionais)
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    status: Optional[str] = None

# Armazenamento temporário de tarefas (substitua por um banco de dados em produção)
tasks_db = []
next_id = 1

@app.get("/")
def root():
    """Endpoint raiz com informações sobre a API"""
    return {
        "message": "Bem-vindo à To-Do List API!",
        "docs": "/docs",
        "endpoints": {
            "GET /tasks": "Listar todas as tarefas",
            "GET /tasks/{task_id}": "Obter uma tarefa específica",
            "POST /tasks": "Criar uma nova tarefa",
            "PUT /tasks/{task_id}": "Atualizar uma tarefa",
            "DELETE /tasks/{task_id}": "Deletar uma tarefa"
        }
    }

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    """
    Retorna todas as tarefas da lista
    """
    # TODO: Implementar a lógica para retornar todas as tarefas
    pass

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """
    Retorna uma tarefa específica pelo ID
    """
    # TODO: Implementar a lógica para buscar uma tarefa pelo ID
    # Lembre-se de retornar HTTPException(404) se a tarefa não for encontrada
    pass

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    """
    Cria uma nova tarefa
    """
    # TODO: Implementar a lógica para criar uma nova tarefa
    # Atribua um ID único e defina created_at
    pass

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    """
    Atualiza uma tarefa existente
    """
    # TODO: Implementar a lógica para atualizar uma tarefa
    # Lembre-se de retornar HTTPException(404) se a tarefa não for encontrada
    pass

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """
    Deleta uma tarefa
    """
    # TODO: Implementar a lógica para deletar uma tarefa
    # Lembre-se de retornar HTTPException(404) se a tarefa não for encontrada
    pass

# Para executar o servidor:
# uvicorn starter-code:app --reload
