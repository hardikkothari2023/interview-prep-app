import React, { useState, useEffect } from "react";
import axios from "axios";

const Quiz = () => {
  const [questions, setQuestions] = useState([]);
  const [score, setScore] = useState(0);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);

  const topic = "data structures"; // Hardcoded topic, you can make this dynamic later

  useEffect(() => {
    // Fetch questions from Flask backend
    axios
      .get(`http://localhost:5000/api/get_questions?topic=${topic}`)
      .then((response) => {
        setQuestions(response.data);
      })
      .catch((error) => {
        console.error("Error fetching questions:", error);
      });
  }, [topic]);

  const handleAnswer = (selectedOption) => {
    const correctAnswer = questions[currentQuestionIndex].correctAnswer;
    if (selectedOption === correctAnswer) {
      setScore(score + 1); // Increment score for correct answer
    }

    // Move to the next question
    setCurrentQuestionIndex(currentQuestionIndex + 1);
  };

  if (questions.length === 0) {
    return <div>Loading questions...</div>;
  }

  if (currentQuestionIndex >= questions.length) {
    return <div>Your final score is: {score}</div>;
  }

  const currentQuestion = questions[currentQuestionIndex];

  return (
    <div>
      <h3>{currentQuestion.question}</h3>
      <div>
        {currentQuestion.options.map((option, index) => (
          <button key={index} onClick={() => handleAnswer(option)}>
            {option}
          </button>
        ))}
      </div>
      <p>Score: {score}</p>
    </div>
  );
};

export default Quiz;
