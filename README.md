# langgraph-api-template
A clean architecture for building stateful LLM agents with FastAPI.

### Docker Setup

```bash
docker build -t langgraph-agent .
docker run -p 8000:8000 --env-file .env langgraph-agent
```

### Testing the API

```bash
curl -X POST http://localhost:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hola, ¿quién eres?", "user_id": "ricardo_test_1"}'
```