🤖 AskBase API
A REST API built with FastAPI that serves as the foundation for an AI-powered Internal Knowledge Base. Currently serves as the backend skeleton 

🚀 Features

Create and manage chat sessions
Send messages and receive AI responses
Retrieve conversation history with pagination
Auto-generated interactive API documentation
Full input validation with Pydantic
RESTful API design


🛠️ Built With

Python 3.9
FastAPI — modern, fast web framework
Pydantic — data validation
Uvicorn — ASGI server
REST API design principles


📋 API Endpoints
MethodEndpointDescriptionGET/Welcome messageGET/healthAPI health checkPOST/sessionsCreate new chat sessionGET/sessions/{id}Get session detailsGET/sessions/{id}/messagesGet session messagesPOST/sessions/{id}/chatSend a message

⚙️ Setup & Run
1. Clone the repo
bashgit clone https://github.com/balaji-code/askbase.git
cd askbase
2. Create virtual environment
bashpython3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Run the server
bashuvicorn askbase:app --reload
5. Open API docs
http://localhost:8000/docs

📸 Sample Usage
Create a session:
jsonPOST /sessions
{
    "name": "Product FAQ",
    "description": "Customer product questions"
}
Send a message:
jsonPOST /sessions/1/chat
{
    "message": "What is RAG?",
    "model": "claude-sonnet",
    "max_tokens": 1024
}
Response:
json{
    "session_id": 1,
    "user_message": {
        "role": "user",
        "content": "What is RAG?",
        "timestamp": "2026-05-12 16:59"
    },
    "ai_response": {
        "role": "assistant",
        "content": "Claude will answer this in Phase 2!",
        "model": "claude-sonnet",
        "timestamp": "2026-05-12 16:59"
    }
}
Get last 2 messages:
GET /sessions/1/messages?limit=2

🗺️ Roadmap

 Phase 1 — FastAPI skeleton with session management
 Phase 2 — Claude API integration for real AI responses
 Phase 3 — RAG pipeline with document upload
 Phase 4 — Vector database for semantic search
 Phase 5 — Deploy to production


📚 Concepts Practised

REST API design — GET, POST, path params, query params
Pydantic models for request validation
In-memory session and message storage
FastAPI auto documentation (Swagger UI)
Error handling for missing resources
Timestamp management with datetime


👨‍💻 Author
Balaji — AI Engineer in training
Building towards a full AI-powered Internal Knowledge Base using Claude API, RAG, and vector databases.