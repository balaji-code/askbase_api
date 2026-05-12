from fastapi import FastAPI
from pydantic import BaseModel  

app = FastAPI() 
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/about")
def about():
    return {"message": "I am Balaji and this is a simple FastAPI application."}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/square/{number}")
def square(number: int):
    return {"square": number ** 2}

@app.get("/users/{user_id}/profile")
def user_profile(user_id: int):       
    return {"user_id": user_id, "name": f"User{user_id}", "active": True}

@app.get("/search")
def search(
    query: str,
    limit: int = 5,
    category: str = "all"):
    return {
    "query":query,
    "limit": limit,
    "category": category,
    "results": []
    }


@app.get("/expenses")
def get_expenses(
    category:str = 'all',
    sort :str = "date",
    limit: int = 10):
    return {"category": category, "sort": sort, "limit": limit}

@app.get("/users/{user_id}/expenses") 
def get_user_orders(
    user_id: int,
    status: str = "all",
    limit: int = 10):
    return {"user_id": user_id, "status": status, "limit": limit}


class ChatMessage(BaseModel):
       role: str
       content: str

class ChatRequest(BaseModel):
      message : str
      model  : str = "claude-sonnet"
      max_tokens : int = 1024

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "model": request.model,            # ✅ from request
        "message_received": request.message, # ✅ from request
        "max_tokens": request.max_tokens,  # ✅ from request
        "response": "I received your message!"
    }

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    category: str
  
@app.post("/expenses")
def create_expense(expense: ExpenseCreate):
    return {
            "id": 1,
            "description": "Lunch",
            "amount": 150.0,
            "category": "food",
            "status": "created"
        }
