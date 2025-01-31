import chromadb
from flask import Flask

app = Flask(__name__)

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="/tmp/chroma_db")

@app.route("/")
def home():
    return "ChromaDB is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
