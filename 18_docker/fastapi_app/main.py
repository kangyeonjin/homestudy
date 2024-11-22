from fastapi import FastAPI, HTTPException
import pinecone
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Pinecone 초기화
# pinecone.init(api_key="PINECONE_API_KEY", environment="PINECONE_ENVIRONMENT")
pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

host = "https://buzz-conversations-zi2m3tr.svc.aped-4627-b74a.pinecone.io" 

index = pinecone.Index("quickstart", host=host)

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.post("/generate")
def generate_text(prompt: str):
    try:
        # Ollama를 사용하여 텍스트 생성
        response = ollama.generate(prompt=prompt, model="llama-2-7b-chat")  # 모델명은 필요에 따라 변경
        return {"prompt": prompt, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))