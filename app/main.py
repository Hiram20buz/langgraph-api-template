from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_openai import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")

def chatbot(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

workflow = StateGraph(MessagesState)
workflow.add_node("chatbot", chatbot)
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

memory = MemorySaver()
graph = workflow.compile(checkpointer=memory)

app = FastAPI(title="Multi-User LangGraph API")

class ChatRequest(BaseModel):
    message: str
    user_id: str  

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    config = {"configurable": {"thread_id": request.user_id}}
    
    input_message = {"messages": [("user", request.message)]}
    result = await graph.ainvoke(input_message, config)
    
    return {"response": result["messages"][-1].content}
