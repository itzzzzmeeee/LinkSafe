# 🔗 LinkSafe - URL Scanner & Cybersecurity Tool

![LinkSafe Banner](https://img.shields.io/badge/LinkSafe-Secure%20Your%20Links-blueviolet)  

LinkSafe is a **FastAPI-based web application** that allows you to **scan any URL** and check its authenticity, helping users stay safe from phishing, malware, and malicious websites.  

---

## 🚀 Features

- ✅ **Real-time URL scanning**  
- ✅ **Detailed results** with:
  - Label (Safe / Suspicious / Malicious)
  - Explanation
  - Security advice  
- ✅ **Modern, user-friendly UI** with a clean interface  
- ✅ **Lightweight & fast** — built using FastAPI and Python  


---

## ⚡ How It Works

1. Enter a URL in the input box.
2. Click **Scan URL**.
3. Get a **detailed analysis** instantly with explanation and safety advice.

---

## 🛠 Tech Stack

- **Backend:** FastAPI, Python 3.11  
- **Frontend:** HTML5, CSS3, JavaScript  
- **Machine Learning:** scikit-learn (for URL classification model)  

---

## 🔧 Installation

1. Clone the repo:  
```bash
git clone https://github.com/itzzzzmeeee/LinkSafe.git
cd LinkSafe
```

2. Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Run the application:

python -m uvicorn app:app --reload


5. Open your browser and go to:
 
http://127.0.0.1:8000



📝 Usage

Paste any URL you want to check.

Click Scan URL to see results.

Read the explanation and advice to understand potential risks.

📂 Project Structure
LinkSafe/
│
├─ app.py               # FastAPI backend
├─ dataset.py           # URL dataset processing
├─ train_model.py       # Model training
├─ templates/
│   └─ index.html       # Frontend HTML
├─ static/              # CSS/JS files (if any)
├─ requirements.txt     # Dependencies
└─ README.md

👨‍💻 Author :
Saransh Singh
Cybersecurity & Python Enthusiast

📢 Note

This project is for educational purposes. Do not rely solely on this tool for professional cybersecurity decisions. Always verify suspicious links with multiple trusted sources.
