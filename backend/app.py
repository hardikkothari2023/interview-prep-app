from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.generator import generate_qa

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Interview Prep API!"})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    topic = data.get("topic", "")
    
    if not topic:
        return jsonify({"error": "Topic is required"}), 400
    
    qas = generate_qa(topic)
    return jsonify({"topic": topic, "questions": qas})
from flask import Flask, request, jsonify
import fitz  # PyMuPDF

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400

    file = request.files['resume']
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Only PDF files allowed"}), 400

    # Extract text from PDF using PyMuPDF (fitz)
    doc = fitz.open(stream=file.read(), filetype="pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()

    # Dummy skill detection (you can improve this later)
    topics_found = []
    known_topics = [
    "data structures", 
    "machine learning", 
    "python", 
    "sql", 
    "operating systems", 
    "algorithms", 
    "javascript", 
    "web development", 
    "databases", 
    "object-oriented programming", 
    "computer networks", 
    "software engineering", 
    "cloud computing", 
    "artificial intelligence", 
    "deep learning", 
    "natural language processing", 
    "data analysis"

]

    for topic in known_topics:
        if topic.lower() in resume_text.lower():
            topics_found.append(topic)

    return jsonify({"topics": topics_found})
@app.route('/api/get_questions', methods=['GET'])
def get_questions():
    topic = request.args.get('topic', '')
    if not topic:
        return jsonify({"error": "Topic is required"}), 400
    
    questions = generate_qa(topic)
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
