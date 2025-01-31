import chromadb
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize ChromaDB client with persistent storage
chroma_client = chromadb.PersistentClient(path="/tmp/chroma_db")

@app.route("/")
def home():
    return "ChromaDB is running!"

@app.route("/collections", methods=['GET'])
def list_collections():
    collections = chroma_client.list_collections()
    return jsonify([collection.name for collection in collections])

@app.route("/create_collection", methods=['POST'])
def create_collection():
    collection_name = request.json.get('name')
    try:
        collection = chroma_client.create_collection(name=collection_name)
        return jsonify({"status": "Collection created", "name": collection_name})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)