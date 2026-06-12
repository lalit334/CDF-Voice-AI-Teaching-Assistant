import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder

load_dotenv()
# Groq API Key को लोड करना
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq के सर्वर से कनेक्ट करना (यह बिल्कुल OpenAI जैसा ही काम करता है)
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)

def speech_to_text(audio_bytes):
    if audio_bytes:
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_bytes)
        
        with open("temp_audio.wav", "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-large-v3", # Groq का सुपरफास्ट मॉडल
                file=audio_file
            )
        return transcript.text
    return None

def ask_ai_teacher(teacher_text, mode):
    system_prompt = (
        "You are a friendly, enthusiastic AI Teaching Assistant in a Haryana government school. "
        "The students speak a mix of Hindi and English (Hinglish). "
        "Explain the concept in easy-to-understand, engaging Hinglish text. Keep sentences short. "
        "Always end your response by providing a single relevant visual search keyword enclosed in brackets like [VISUAL: keyword]."
    )
    
    if mode == "Quiz Mode":
        system_prompt += (
            " Create a single simple multiple-choice question (MCQ) based on the topic with 4 options. "
            "Format it clearly so students can read it on a smartboard."
        )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # Groq का सबसे ताकतवर और सटीक मॉडल
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": teacher_text}
        ]
    )
    return response.choices[0].message.content

def text_to_speech(text_input):
    tts = gTTS(text=text_input, lang='hi', slow=False)
    tts.save("response.mp3")
    return "response.mp3"


st.set_page_config(layout="wide")
st.title("👨‍🏫 CDF Voice AI Teaching Assistant")
st.write("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🛠️ Teacher Controls")
    mode = st.selectbox("Select Feature:", ["Concept Simplification", "Quiz Mode"])
    st.write("")
    st.write("🎤 **Record your voice:**")
    audio_data = mic_recorder(start_prompt="Record Audio", stop_prompt="Stop Recording", key='recorder')

with col2:
    st.markdown("### 🖥️ Smartboard Canvas")
    
    if audio_data and audio_data['bytes']:
        with st.spinner("Processing voice..."):
            teacher_text = speech_to_text(audio_data['bytes'])
            
        if teacher_text:
            st.info(f"**Teacher said:** \"{teacher_text}\"")
            
            with st.spinner("AI Teacher is thinking..."):
                ai_response = ask_ai_teacher(teacher_text, mode)
            
            clean_text = ai_response.split("[VISUAL:")[0]
            
            st.success("**AI Response:**")
            st.write(clean_text)
            
            audio_file = text_to_speech(clean_text)
            st.audio(audio_file, format="audio/mp3", autoplay=True)
            
            if "[VISUAL:" in ai_response:
                keyword = ai_response.split("[VISUAL:")[1].replace("]", "").strip()
                st.caption(f"💡 *Visual suggestion keyword: {keyword}*")
    else:
        st.warning("Click the 'Record Audio' button on the left and start speaking to teach the class.")