# 🛡️ SCAMGUARD AI - LLM-Powered Fraud Detection System

✨ **LIVE DEMO:** [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://scamguard-ai.streamlit.app/)

---

## 📌 PROJECT OVERVIEW
A production-ready AI shield against digital fraud! ScamGuard AI analyzes messages in real-time using Google's Gemini model to detect and classify 15+ scam patterns with detailed reasoning.

---

## 🚀 WHAT IT DOES
• 🔍 **Analyzes Messages** – SMS, emails, chat messages  
• 🏷️ **Classifies Scam Types** – Phishing, fake authority, urgency, loan scams, impersonation, etc.  
• 💡 **Provides Reasoning** – Explains WHY it's flagged as scam  
• 📊 **Live Intelligence Dashboard** – Real-time scam news & trends  

---

## 🌟 KEY FEATURES
• 🤖 Advanced LLM Integration (Google Gemini via LangChain)  
• 🎯 Structured JSON Output (Predictable, parseable results)  
• 🔄 Real-time Web Search (Tavily API for latest scam intel)  
• 🎨 Streamlit Web Interface (Clean, interactive dashboard)  
• 📈 Evaluation Framework (Accuracy testing & metrics)  

---

## ⚙️ TECHNICAL ARCHITECTURE
**User Input** → **Prompt Engineering** → **Google Gemini** → **JSON Output**  
*(Streamlit App)* → *(Few-shot Examples)* → *(AI Model)* → *(Structured Results)*  

---

## 💼 WHAT THIS DEMONSTRATES

### **CORE SKILLS**
• API Integration (Gemini)  
• Prompt Engineering  
• LLM Wrapper Development  
• Full-Stack Development  
• Production Practices  

### **ADVANCED AI CONCEPTS**
• Few-Shot Learning  
• Multi-Intent Classification  
• Structured Generation  
• AI Chain Design  
• Real-time Intelligence  

---

## 📁 FILE STRUCTURE
```
scamguard-ai/
├── 🎨 app.py                    # Streamlit web interface
├── 🤖 scam_classifier.py        # Core LLM wrapper
├── 📝 prompt.py                 # Advanced prompt templates
├── 🌐 internet_search.py        # Real-time web intelligence
├── 📊 evaluation.py             # Performance testing
├── 🧪 test_evaluation.py        # Unit tests
├── 🏃 run_evaluation.py         # Evaluation runner
├── 📦 dataset_loader.py         # Data utilities
├── 🏗️ schema.py                # JSON structure definition
├── ⚙️ config.py                # Configuration
├── 📋 requirements.txt          # Dependencies
├── 🚫 .gitignore               # Security (excludes .env)
├── 📁 dataset.csv              # Training/evaluation data
├── 📁 prediction.json          # Single output example
└── 📁 predictions.json         # Batch results
```

---

## ⚡ QUICK START

### 1. 📦 INSTALL DEPENDENCIES
```bash
pip install -r requirements.txt
```

### 2. 🔐 CONFIGURE API KEYS
Create `.env` file (from `.env.example`):
```
GOOGLE_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```
⚠️ **IMPORTANT:** `.env` is in `.gitignore` – NEVER uploaded to GitHub!

### 3. 🚀 RUN APPLICATION
```bash
streamlit run app.py
```
Open → http://localhost:8501

### 4. 🧪 RUN EVALUATION (Optional)
```bash
python run_evaluation.py
```

---

## 🎯 SCAM CATEGORIES DETECTED
• ⚡ Fear & Urgency Tactics  
• 👑 Fake Authority Impersonation  
• 🎣 Phishing Attempts  
• 🔢 OTP Fraud  
• 💰 Loan Scams  
• 📦 Delivery/Logistics Scams  
• 💼 Job/Income Opportunity Scams  
• 📢 Promotional Manipulation  
• 🔓 Account Threat Scams  
• +6 other sophisticated patterns  

---

## 📊 SAMPLE OUTPUT
**Input:** "Your bank account will be suspended! Click here to verify."

```json
{
  "classification": "scam",
  "intents": ["fear", "urgency", "phishing"],
  "reasoning": "Message creates false urgency about bank account with suspicious link",
  "flag_reason": "Uses fear tactics with unverified link - common phishing pattern"
}
```

---

## 🌍 WHY THIS PROJECT MATTERS
This isn't just another AI tutorial! Scams cost billions annually, and this tool demonstrates practical AI application for real-world protection. It shows you can ship production systems, not just run notebooks.

✅ From concept to deployed application  
✅ Solves actual user protection needs  
✅ Demonstrates full-stack AI development  
✅ Ready for production scaling  

---

👨💻 **Built by Ahmed Kadiwala**  
🚀 **Demonstrating practical AI/LLM application development skills**