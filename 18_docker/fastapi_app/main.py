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

# 생성
# pinecone.create_index("prac01", dimension=8, metric="euclidean")
# print(pinecone.describe_index("prac01"))

# idx = pinecone.Index("prac01")

# 데이터 삽입해보기
# idx.upsert(
#     vectors=[
#         {"id":"comdalin", "values":[0.1, 0.5, 0.4, 0.11, -0.5, 200.0, 0.0, -200.0]},
#         {"id":"quitar", "values":[1.0, 800.1, -.1, 11., 5.0, 0.2, 8.0, -200.02]}
#     ]
# )

#검색해보기
# result = pinecone.Index(
#     vector=[],
#     top_k=1,
#     include_values=True
# )

# print(result)

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