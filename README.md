# 👨‍🏫 CDF Voice AI Teaching Assistant

A practical, human-centered digital solution built for **Haryana government schools** to assist teachers in live classroom sessions. The tool accepts voice commands in **Hinglish**, processes them using advanced LLMs, and delivers interactive visual-textual support alongside voice playback on the smartboard.

---

## 🚀 Key Features Built (Option A)

1. **Live Concept Simplification:** Transcribes the teacher's voice commands, breaks down complex topics (e.g., Photosynthesis, Water Cycle) into highly engaging, simplified Hinglish text, and reads it aloud to the class.
2. **Voice-Triggered Quizzing:** Dynamically generates interactive multiple-choice questions (MCQs) on the smartboard screen with options based on verbal requests, optimizing student engagement.

---

## 🛠️ Tech Stack & Architecture

* **Frontend UI:** `Streamlit` (Optimized for clean, large-font smartboard viewing)
* **Speech-to-Text (STT):** `Groq Whisper Cloud (whisper-large-v3)` (Ultra-fast Hinglish transcription)
* **LLM Brain:** `Groq Llama-3.3-70b-versatile` (Configured with rigorous prompt guardrails for localized teacher persona)
* **Text-to-Speech (TTS):** `gTTS (Google Text-to-Speech)` (Bilingual vocal output tailored for Indian classrooms)

---

## 🎯 Human-Centered Design (Empathy & UX)

* **Language Localization:** Designed strictly around a system prompt that enforces simple Hinglish sentences, reflecting the organic blend of Hindi and English spoken by grassroots students.
* **Smartboard-Optimized UI:** High-contrast buttons and a wide double-column canvas structure ensure maximum visibility from the back rows of a classroom.
* **Resilient Infrastructure:** Powered by Groq Cloud's low-latency inference engine to guarantee smooth operation even on standard school network speeds.

---

## 🏃‍♂️ How to Run the App Locally

1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install streamlit openai gTTS python-dotenv streamlit-mic-recorder
