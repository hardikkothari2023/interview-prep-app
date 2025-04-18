# 🧠 AI Quiz App

Welcome to the **AI Quiz App** — a modern, full-stack web application designed to test and enhance your knowledge across various computer science topics using interactive multiple-choice quizzes.

![Quiz App Banner](/home/hardik/All Project  By Hardik/interview-prep-app/app.png)

---

## 📁 Project Structure

```
AI-Quiz-App/
├── README.md
├── backend
│   ├── app.py                # Flask backend to serve quiz questions via API
│   ├── requirements.txt      # Python dependencies for the backend
│   └── utils/                # Utility files such as question generators per topic
└── client
    ├── README.md             # Frontend-specific documentation (React)
    ├── node_modules/         # Auto-generated React dependencies
    ├── package-lock.json     # Dependency lock file
    ├── package.json          # Lists dependencies and scripts for React app
    ├── public/
    │   └── A_digital_educational_graphic_focusing_on_data_ana.png  # Banner image
    └── src/
        ├── App.js            # Main React component
        ├── index.js          # Entry point for React app
        └── components/       # All reusable React components (e.g., QuizCard, TopicSelector)
```

---

## 🛠️ Technologies Used

### Backend
- Python 3
- Flask (for building REST APIs)
- Custom utility functions to generate topic-specific quiz data

### Frontend
- React.js (for interactive UI)
- HTML5 + CSS3
- JavaScript (ES6+)

---

## 🚀 Getting Started

### 🔧 Backend Setup

1. Navigate to the `backend` directory:
```bash
cd backend
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Unix/macOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```
Your backend API will be live at: `http://localhost:5000`

---

### 🎨 Frontend Setup

1. Navigate to the `client` directory:
```bash
cd client
```

2. Install React dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```
The frontend will run at: `http://localhost:3000`

---

## 🌐 How It Works

- When a user selects a topic on the frontend, a GET request is sent to the Flask backend API endpoint.
- The backend responds with a JSON object containing multiple-choice questions.
- The frontend renders those questions dynamically and provides instant feedback after each answer.
- At the end of the quiz, the user sees their total score and can retry.

---

## 🧠 Topics Covered

- SQL
- Algorithms
- JavaScript
- Object-Oriented Programming (OOP)
- Computer Networks
- Software Engineering
- Deep Learning
- Natural Language Processing (NLP)
- Data Analysis

---

## 📷 Preview

Make sure the banner image is placed at:
```
/home/hardik/All Project  By Hardik/interview-prep-app/app.png


---

Enjoy learning with quizzes! 🎓✨