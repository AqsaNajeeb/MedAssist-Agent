import streamlit as st
import os
import csv
import base64
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from groq import Groq

# =========================
# STREAMLIT CONFIG
# =========================
st.set_page_config(page_title="MedAssist AI 🏥", layout="wide")

st.title("🏥 MedAssist AI Chatbot")
st.caption("AI Medical Assistant powered by Groq + PubMed + Vision AI")


# =========================
# SAFE GROQ SETUP (FIXED)
# =========================
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found. Add it in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)


def generate(prompt, system="You are a helpful medical assistant."):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024
    )
    return response.choices[0].message.content


# =========================
# LANGUAGE DETECTION (UNCHANGED)
# =========================
def detect_language(text):
    for char in text:
        if '\u0600' <= char <= '\u06FF':
            return "URDU"

    roman_urdu_words = [
        "mjy", "mujhe", "karo", "batao", "hai", "hain", "ky", "ka",
        "ki", "ko", "mn", "mein", "ap", "aap", "kya", "nahi", "aur",
        "krny", "karna", "wala", "hua", "thi", "tha", "hoga"
    ]

    text_lower = text.lower()
    for word in roman_urdu_words:
        if word in text_lower.split():
            return "URDU"

    return "ENGLISH"


# =========================
# TASK CLASSIFICATION (UNCHANGED)
# =========================
def classify_task(text):
    text_lower = text.lower()

    lab_keywords = [
        "hba1c", "hemoglobin", "wbc", "rbc", "glucose", "cholesterol",
        "test", "result", "blood", "urine", "report", "normal", "abnormal"
    ]

    term_keywords = [
        "what is", "meaning", "define", "explain", "kya hai", "matlab"
    ]

    lit_keywords = [
        "research", "study", "pubmed", "treatment", "therapy", "cure", "anxiety"
    ]

    if any(w in text_lower for w in lab_keywords):
        return "LAB_TEST"
    if any(w in text_lower for w in term_keywords):
        return "TERMINOLOGY"
    if any(w in text_lower for w in lit_keywords):
        return "LITERATURE"

    return "TERMINOLOGY"


# =========================
# HANDLERS (UNCHANGED)
# =========================
def lab_test_interpreter(user_input, language):
    system = "You are a medical assistant." if language == "ENGLISH" else "آپ ایک طبی معاون ہیں۔"
    return generate(f"Interpret lab results:\n{user_input}", system)


def terminology_explainer(user_input, language):
    system = "Explain simply." if language == "ENGLISH" else "سادہ اردو میں سمجھائیں۔"
    return generate(f"Explain medical terms:\n{user_input}", system)


# =========================
# PUBMED (UNCHANGED)
# =========================
def search_pubmed(query, max_results=3):
    try:
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {"db": "pubmed", "term": query, "retmax": max_results, "retmode": "json"}
        res = requests.get(url, params=params).json()
        ids = res["esearchresult"]["idlist"]

        if not ids:
            return "No papers found."

        url2 = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        params2 = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
        res2 = requests.get(url2, params=params2)

        root = ET.fromstring(res2.content)

        papers = []
        for a in root.findall(".//PubmedArticle"):
            title = a.findtext(".//ArticleTitle", "No title")
            abstract = a.findtext(".//AbstractText", "No abstract")
            papers.append(f"{title}\n{abstract[:200]}...")

        return "\n\n".join(papers)

    except Exception as e:
        return str(e)


def literature_analyzer(user_input, language):
    pubmed = search_pubmed(user_input)

    prompt = f"""
User: {user_input}

PubMed research:
{pubmed}

Summarize in simple terms.
"""
    return generate(prompt, "Medical research assistant")


# =========================
# IMAGE ANALYSIS (FIXED LOGIC)
# =========================
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def analyze_image(image_path, language):
    if not Path(image_path).exists():
        return "Image not found"

    image_data = encode_image(image_path)

    prompt = "Analyze this medical image."
    
    # FIX: Groq vision requires supported vision model
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/jpeg;base64,{image_data}"
                }}
            ]
        }],
        max_tokens=1024
    )

    return response.choices[0].message.content


# =========================
# LOGGING
# =========================
LOG_FILE = "medassist_log.csv"

def save_log(user_input, language, task, result):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_input,
            language,
            task,
            result[:500]
        ])


# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================
# SIDEBAR
# =========================
mode = st.sidebar.radio("Choose Mode", ["💬 Chat", "🖼️ Image Analysis"])

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []


# =========================
# CHAT MODE
# =========================
if mode == "💬 Chat":

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask your medical question...")

    if user_input:

        st.session_state.messages.append({"role": "user", "content": user_input})

        language = detect_language(user_input)
        task = classify_task(user_input)

        if task == "LAB_TEST":
            result = lab_test_interpreter(user_input, language)
        elif task == "TERMINOLOGY":
            result = terminology_explainer(user_input, language)
        else:
            result = literature_analyzer(user_input, language)

        save_log(user_input, language, task, result)

        st.session_state.messages.append({"role": "assistant", "content": result})


# =========================
# IMAGE MODE
# =========================
else:

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    question = st.text_input("Optional question")

    if uploaded_file:

        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        st.image(temp_path)

        if st.button("Analyze"):

            language = detect_language(question) if question else "ENGLISH"

            result = analyze_image(temp_path, language)

            st.write(result)

            save_log(
                f"[IMAGE] {uploaded_file.name}",
                language,
                "IMAGE",
                result
            )

        if os.path.exists(temp_path):
            os.remove(temp_path)
