import React, { useState, useEffect } from "react";
import { Container, Button, Grid, Typography, Card, CardContent, Box, CircularProgress, Snackbar, AppBar, Toolbar, Alert, Tabs, Tab } from "@mui/material";
import { motion } from "framer-motion";
import axios from "axios";
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

function App() {
  const [file, setFile] = useState(null);
  const [topics, setTopics] = useState([]);
  const [qa, setQa] = useState([]);
  const [currentTopicIndex, setCurrentTopicIndex] = useState(0);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);
  const [score, setScore] = useState(0);
  const [answerFeedback, setAnswerFeedback] = useState("");  // For feedback on answers
  const [selectedTopic, setSelectedTopic] = useState("");  // To hold the selected topic
  const [selectedAnswer, setSelectedAnswer] = useState("");  // To highlight correct/incorrect answers
  const [selectedOption, setSelectedOption] = useState("");  // For handling selected option style

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSuccess(false);
    setAnswerFeedback("");  // Reset feedback when uploading a new file

    if (!file) {
      setError("Please upload a resume.");
      setLoading(false);
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await axios.post("http://localhost:5000/upload-resume", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setTopics(response.data.topics);
      setCurrentTopicIndex(0);
      setSuccess(true);
    } catch (err) {
      setError("Error uploading resume or extracting topics.");
    } finally {
      setLoading(false);
    }
  };

  const fetchQuestions = async (topic) => {
    try {
      const response = await axios.post("http://localhost:5000/generate", { topic });
      setQa(response.data.questions);
      setCurrentQuestionIndex(0);  // Reset question index when new topic is selected
      setAnswerFeedback("");  // Reset feedback
    } catch (err) {
      setError("Error fetching questions from backend.");
    }
  };

  const handleAnswer = (selectedAnswer, correctAnswer, option) => {
    setSelectedAnswer(selectedAnswer);
    setSelectedOption(option); // To highlight the correct/incorrect option
    
    if (selectedAnswer === correctAnswer) {
      setScore(score + 1);
      setAnswerFeedback("Correct!");
    } else {
      setAnswerFeedback("Incorrect! The correct answer was: " + correctAnswer);
    }
    // Move to next question after answering
    setTimeout(() => moveToNextQuestion(), 1000); // Delay for feedback
  };

  const moveToNextQuestion = () => {
    if (currentQuestionIndex < qa.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
      setAnswerFeedback("");  // Reset feedback for next question
    } else {
      // All questions answered, move to next topic
      moveToNextTopic();
    }
  };

  const moveToNextTopic = () => {
    if (currentTopicIndex < topics.length - 1) {
      fetchQuestions(topics[currentTopicIndex + 1]);
      setCurrentTopicIndex(currentTopicIndex + 1);
      setSelectedTopic(""); // Reset selected topic
    }
  };

  const handleTopicChange = (event, newValue) => {
    setSelectedTopic(newValue);
    fetchQuestions(newValue); // Fetch questions for the selected topic
  };

  useEffect(() => {
    if (topics.length > 0 && currentTopicIndex === 0) {
      fetchQuestions(topics[0]);
    }
  }, [topics, currentTopicIndex]);

  return (
    <div>
      {/* Header */}
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" style={{ flexGrow: 1 }}>
            ChatGPT-powered Interview Prep App
          </Typography>
        </Toolbar>
      </AppBar>

      <Container maxWidth="sm" sx={{ padding: "20px", marginTop: "20px" }}>
        <Typography variant="h6" align="center" gutterBottom>
          Upload your resume to get interview questions based on your skills
        </Typography>

        {/* Resume Upload Form */}
        <form onSubmit={handleUpload}>
          <Box display="flex" justifyContent="center" marginTop="20px">
            <input type="file" accept=".pdf" onChange={handleFileChange} required />
            <Button
              variant="contained"
              color="primary"
              type="submit"
              disabled={loading || !file}
              style={{ marginLeft: "10px" }}
              startIcon={<CloudUploadIcon />}
            >
              {loading ? <CircularProgress size={24} /> : "Upload Resume"}
            </Button>
          </Box>
        </form>

        {/* Error/Success Notifications */}
        {error && (
          <Snackbar open={true} autoHideDuration={6000} onClose={() => setError("")}>
            <Alert onClose={() => setError("")} severity="error">
              {error}
            </Alert>
          </Snackbar>
        )}
        {success && (
          <Snackbar open={true} autoHideDuration={6000} onClose={() => setSuccess(false)}>
            <Alert onClose={() => setSuccess(false)} severity="success">
              Topics extracted successfully!
            </Alert>
          </Snackbar>
        )}

        {/* Display Topic Selection */}
        {topics.length > 0 && (
          <Tabs value={selectedTopic} onChange={handleTopicChange} variant="scrollable" scrollButtons="auto" aria-label="Topics Tabs" centered>
            {topics.map((topic, index) => (
              <Tab key={index} label={topic} value={topic} />
            ))}
          </Tabs>
        )}

        {/* Display Current Topic and Questions */}
        {qa.length > 0 && selectedTopic && (
          <div>
            <Typography variant="h6" gutterBottom>
              Current Topic: {selectedTopic}
            </Typography>
            <Typography variant="h6" align="center" gutterBottom style={{ marginBottom: "20px" }}>
              Question: {currentQuestionIndex + 1} of {qa.length}
            </Typography>
            <Grid container spacing={2} marginTop="20px">
              <Grid item xs={12}>
                <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
                  <Card>
                    <CardContent>
                      <Typography variant="h6" gutterBottom>
                        {qa[currentQuestionIndex].question}
                      </Typography>
                      {qa[currentQuestionIndex].options.map((option, idx) => (
                        <Button
                          key={idx}
                          variant="outlined"
                          onClick={() => handleAnswer(option, qa[currentQuestionIndex].correctAnswer, option)}
                          fullWidth
                          style={{
                            backgroundColor: selectedAnswer === option
                              ? option === qa[currentQuestionIndex].correctAnswer
                                ? "green"
                                : "red"
                              : "transparent",
                            color: selectedAnswer === option ? "white" : "black"
                          }}
                        >
                          {option}
                        </Button>
                      ))}
                    </CardContent>
                  </Card>
                </motion.div>
              </Grid>
            </Grid>

            {/* Answer Feedback */}
            {answerFeedback && (
              <Typography variant="body1" align="center" color={answerFeedback === "Correct!" ? "green" : "red"} style={{ marginTop: "20px" }}>
                {answerFeedback}
              </Typography>
            )}

            {/* Score Display */}
            <Typography variant="h6" align="center" gutterBottom style={{ marginTop: "20px" }}>
              Score: {score}
            </Typography>
          </div>
        )}
      </Container>
    </div>
  );
}

export default App;
