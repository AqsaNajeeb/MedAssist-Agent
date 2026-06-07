# 🏥 MedAssist Agent

> An LLM-Based Integrated AI Agent for Bilingual Medical Report Interpretation, Medical Terminology Clarification, Biomedical Literature Analysis, and Medical Image Understanding

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red)
![Groq](https://img.shields.io/badge/Groq-LLM-green)
![PubMed](https://img.shields.io/badge/PubMed-Biomedical%20Research-orange)
![Healthcare AI](https://img.shields.io/badge/Domain-Healthcare_AI-purple)

---

## 🌐 Live Demo

**🚀 Try MedAssist Agent Online**

🔗 https://medassist-agent-vmrykpch7tasrfs66eblfs.streamlit.app/

---

# 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [System Architecture](#️-system-architecture)
- [Workflow](#️-system-workflow)
- [Technology Stack](#️-technology-stack)
- [Installation & Setup](#-installation--setup)
- [Usage Guidelines](#-usage-guidelines)
- [Project Structure](#-project-structure)
- [Experimental Results](#-experimental-results)
- [Comparative Analysis](#-comparative-analysis)
- [Novel Contributions](#-novel-contributions)
- [Limitations](#️-limitations)
- [Future Enhancements](#-future-enhancements)
- [Ethical Considerations](#️-ethical-considerations)

---

# 🏥 Project Overview

MedAssist Agent is a patient-centric healthcare AI assistant that combines the capabilities of Large Language Models (LLMs), biomedical literature retrieval, multilingual Natural Language Processing (NLP), and multimodal vision AI into a unified platform.

The system helps users understand:

- Laboratory test reports
- Medical terminology
- Biomedical research literature
- Medical images

without requiring specialized medical knowledge.

Unlike most healthcare AI systems that focus on only one task, MedAssist Agent integrates multiple healthcare assistance capabilities into a single intelligent workflow while supporting both English and Urdu-speaking users.

The project was developed as part of research in Healthcare AI and Medical Informatics at the University of Engineering and Technology (UET) Taxila.

---

# ❗ Problem Statement

Medical information is often difficult for non-specialists to understand.

Patients regularly receive:

- Blood reports
- Laboratory test results
- Clinical notes
- Diagnostic findings
- Research information

containing:

- Medical abbreviations
- Technical terminology
- Numerical values
- Clinical jargon

that can cause confusion, anxiety, and misinterpretation.

Current healthcare AI systems typically:

- Focus on only one healthcare task
- Lack Urdu language support
- Do not integrate biomedical literature retrieval
- Have limited patient accessibility
- Rarely support medical image analysis

MedAssist Agent addresses these limitations through a unified AI-powered healthcare assistant.

---

# 🎯 Project Objectives

The primary objective of MedAssist Agent is to make healthcare information accessible, understandable, and actionable.

## 1. Laboratory Test Interpretation

Interpret laboratory values and explain:

- Whether values are normal or abnormal
- Clinical significance
- Possible health implications
- Practical recommendations

---

## 2. Medical Terminology Simplification

Convert complex medical language into patient-friendly explanations.

### Example

**Input**

```text
What is hypertension?
```

**Output**

```text
Hypertension means high blood pressure.
```

---

## 3. Biomedical Literature Analysis

Retrieve relevant scientific publications from PubMed and summarize findings in simple language.

---

## 4. Bilingual Healthcare Assistance

Provide healthcare explanations in:

- English
- Urdu
- Roman Urdu

to improve accessibility for Urdu-speaking populations.

---

## 5. Medical Image Understanding

Allow users to upload medical images and receive AI-generated explanations using a vision-language model.

---

# 🌟 Key Features

## 🔬 Laboratory Test Interpretation

Supports interpretation of:

- HbA1c
- CBC
- WBC
- RBC
- Blood Glucose
- Cholesterol
- Urine Reports

Provides:

- Clinical explanation
- Reference ranges
- Health implications
- Recommendations

---

## 📖 Medical Terminology Clarification

Explains medical concepts in plain language.

Examples:

- Hypertension
- Diabetes
- Cancer
- Anemia
- Anxiety

---

## 📚 Biomedical Literature Analysis

Connects directly to PubMed.

Capabilities:

- Search biomedical papers
- Retrieve abstracts
- Summarize findings
- Present research in simple language

---

## 🖼️ Medical Image Analysis

Supports:

- JPG
- JPEG
- PNG

Uses a multimodal vision model to:

- Understand uploaded images
- Extract findings
- Explain observations

---

## 🌍 Bilingual Output

Automatic language detection:

- English
- Urdu Script
- Roman Urdu

Example:

```text
stress kia hai urdu mein samjhao
```

Generates output in Urdu.

---

## 📝 Session Logging

Automatically stores:

- Timestamp
- Query
- Language
- Task Type
- Generated Response

inside:

```text
medassist_log.csv
```

---

# 🏗️ System Architecture

```text
┌─────────────────────────────┐
│         User Input          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Language Detection      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Task Classification     │
└──────────────┬──────────────┘
               │
 ┌─────────────┼─────────────┬─────────────┐
 ▼             ▼             ▼             ▼
Lab Test   Terminology   Literature    Image
Module      Module        Module       Module
 │             │             │             │
 └─────────────┼─────────────┴─────────────┘
               ▼
┌─────────────────────────────┐
│      Groq LLM Backbone      │
│  Llama-3.3-70B-Versatile    │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│   Bilingual Output Layer    │
└─────────────────────────────┘
```

---

# ⚙️ System Workflow

### Step 1 – User Input

User submits:

- Medical query
- Laboratory report
- Research question
- Medical image

### Step 2 – Language Detection

The system determines whether the input is:

- English
- Urdu
- Roman Urdu

### Step 3 – Task Classification

The query is classified as:

```text
LAB_TEST
TERMINOLOGY
LITERATURE
IMAGE
```

### Step 4 – Module Routing

The request is sent to the corresponding processing module.

### Step 5 – AI Reasoning

The LLM analyzes the request and generates medically relevant explanations.

### Step 6 – Response Generation

Results are returned in the detected language.

---

# 🛠️ Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python 3.10+ |
| Frontend | Streamlit |
| LLM API | Groq |
| Text Model | Llama-3.3-70B-Versatile |
| Vision Model | Llama-4-Scout-17B-16E-Instruct |
| Biomedical Database | PubMed |
| HTTP Requests | Requests |
| XML Parsing | ElementTree |
| Logging | CSV |
| Image Processing | Base64 |

---

# 🚀 Installation & Setup

## Clone Repository

```bash
git clone https://github.com/AqsaNajeeb/MedAssist-Agent.git
cd MedAssist-Agent
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure API Key

### Windows

```cmd
set GROQ_API_KEY=YOUR_API_KEY
```

### Linux / Mac

```bash
export GROQ_API_KEY=YOUR_API_KEY
```

## Run Application

```bash
streamlit run ai_project.py
```

---

# 📘 Usage Guidelines

## 💬 Chat Mode

Use Chat Mode for:

- Medical terminology explanations
- Laboratory report interpretation
- Biomedical literature summaries

### Example Queries

```text
What is hypertension?
```

```text
My HbA1c is 8.2%
```

```text
Latest treatment for anxiety
```

### Urdu Examples

```text
ذیابیطس کیا ہے؟
```

```text
stress kia hai urdu mein samjhao
```

The system automatically detects language and responds accordingly.

---

## 🖼️ Image Analysis Mode

1. Select Image Analysis from the sidebar
2. Upload an image
3. Enter an optional question
4. Click Analyze

Example:

```text
What does this medical report indicate?
```

The image is analyzed using the vision model and explained in simple language.

---

# 📂 Project Structure

```text
MedAssist-Agent/
│
├── ai_project.py
├── requirements.txt
├── README.md
└── AI_Project.ipynb
```

---

# 📊 Experimental Results

The system was evaluated using six representative healthcare scenarios.

| Metric | Result |
|----------|---------|
| Language Detection Accuracy | 100% |
| Task Classification Accuracy | 100% |
| Module Routing Accuracy | 100% |
| English Output Quality | Correct |
| Urdu Output Quality | Correct |
| Image Analysis Functionality | Correct |

---

# 📈 Comparative Analysis

| Feature | Lab2Life  | MedAssist Agent |
|----------|-----------|-----------|-----------|
| Lab Test Interpretation | ✅  | ✅ |
| Terminology Simplification | Partial  | ✅ |
| PubMed Literature Analysis | ❌  | ✅ |
| Urdu Language Support | ❌ |  ✅ |
| Medical Image Analysis | OCR Only  | ✅ |
| Patient-Facing Interface | ✅  | ✅ |
| Unified Pipeline | ❌  | ✅ |
| Multimodal AI | ❌ |  ✅ |

---

# 🚀 Novel Contributions

### First Urdu-Centric Medical AI Assistant

Addresses a major healthcare accessibility gap.

### Unified Healthcare Pipeline

Combines:

- Lab interpretation
- Terminology clarification
- Literature analysis
- Image understanding

inside one platform.

### Real-Time PubMed Integration

Uses live biomedical research rather than static datasets.

### Multimodal Healthcare AI

Supports both text and image understanding.

### Patient-Friendly Design

Generates explanations understandable by non-medical users.

---

# ⚠️ Limitations

- Rule-based task classification
- Limited Roman Urdu coverage
- Dependence on external APIs
- Not a replacement for professional medical advice

---

# 🔮 Future Enhancements

- LLM-based task classification
- OCR for medical reports
- Retrieval-Augmented Generation (RAG)
- Voice interaction support
- Mobile application deployment
- Clinical risk prediction modules

---

# ⚖️ Ethical Considerations

MedAssist Agent is designed for educational and informational purposes only.

The system:

✅ Explains medical information

✅ Summarizes research

✅ Assists understanding

The system does NOT:

❌ Diagnose diseases

❌ Prescribe medication

❌ Replace healthcare professionals

Users should always consult qualified healthcare professionals before making medical decisions.

---

# 👨‍💻 Authors

### Aqsa Najeeb

Software Engineering Department

University of Engineering and Technology Taxila

### Iqra Hafeez

Software Engineering Department

University of Engineering and Technology Taxila

### Supervisor

**Dr. Kanwal Yousaf**

Department of Software Engineering

University of Engineering and Technology Taxila

---

## ⭐ If you found this project useful, please consider starring the repository.
