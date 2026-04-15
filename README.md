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

### Deployment

```bash
gcloud run deploy langgraph-service \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8000 \
  --set-env-vars="OPENAI_API_KEY=your_key_here"
```

<img width="1707" height="984" alt="Screenshot 2026-04-15 at 9 33 11 a m" src="https://github.com/user-attachments/assets/3f312af7-44dc-45b6-9f8b-fd2f20aa9d26" />

<img width="1054" height="175" alt="Screenshot 2026-04-15 at 10 09 49 a m" src="https://github.com/user-attachments/assets/e8afdf80-b1e2-41d7-a2f9-fdadbe64b6ee" />

