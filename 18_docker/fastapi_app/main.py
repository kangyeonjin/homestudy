from fastapi import FastAPI
import pinecone

app = FastAPI()

pinecone.init(api_key="PINECONE_API_KEY", environment="PINECONE_ENVIRONMENT")

index = pinecone.Index("buzz-conversations")

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}
