# VTU Genius AI — Study Buddy & Placement Prep

**VTU Genius AI** is an AI-powered study companion, exam tutor, and placement preparation portal designed specifically for students under **Visvesvaraya Technological University (VTU)**. 

Built using a **FastAPI** backend, a single-page **HTML5/CSS3/JS** frontend, and integrated with **Groq LLaMA 3.1**, the platform provides localized academic resources, intelligent tutoring through Retrieval-Augmented Generation (RAG), and interactive mock interviews to boost student placement readiness.

---

## 🚀 Key Features

### 1. 📚 Smart Syllabus & Notes Explorer
* Lists subjects dynamically by **Scheme (e.g., 2022)** and **Semester**.
* Fetches detailed module-wise syllabus notes pre-seeded in the local SQLite database.
* Exports study notes directly to high-quality offline **PDF** documents.

### 2. 🤖 AI Tutor & Chat (RAG)
* Interactive chatbot that answers questions based **exclusively** on the VTU syllabus notes.
* Uses Retrieval-Augmented Generation (RAG) to ensure responses are accurate, concise, and structured specifically for VTU scoring patterns.
* Seamlessly falls back to a descriptive **Mock AI Mode** if API keys are not configured.

### 3. 📄 PDF Material Uploader
* Students can upload their own notes, lecture slides, or textbooks (PDF format).
* The backend extracts text and indexes the content for personalized AI study sessions.

### 4. 📝 Mock Exam Center & PyQs
* Practice with **Previous Year Questions (PYQs)**, **Important Questions**, and **Expected Questions**.
* Start a simulated Mock Exam featuring random PYQs.
* Submit answers for instant grading and evaluation.
* Download question banks as printable PDFs.

### 5. 🎯 Placement & Aptitude Prep
* Company-specific aptitude questions (TCS, Infosys, Wipro, etc.).
* Quantitative, Logical, and Verbal reasoning practice.
* Interactive aptitude quizzes with instant explanations.

### 6. 🎙️ Live Technical & Behavioral Mock Interviews
* Real-time technical and behavioral interview simulator tailored for specific companies and roles.
* Speech-to-text integration utilizing **Faster Whisper** for transcript processing.
* AI acts as the interviewer, evaluating answers, scoring responses (1-10), giving instant constructive feedback, and proceeding with dynamic follow-up questions.

### 7. 🤖 Telegram Bot Integration (`bot.py`)
* Fully-functional Telegram bot interface for studying on the go.
* Commands to query subjects, get notes, practice mock exams, and ask the AI chatbot directly from Telegram.

---

## 🛠️ Tech Stack

* **Frontend:** Single Page Application (SPA) built using Vanilla HTML5, Custom CSS3 (Modern, responsive UI with sleek gradients, hover effects, and cards), and Javascript.
* **Backend:** FastAPI (Python), SQLAlchemy ORM, Uvicorn, Python-Dotenv.
* **Database:** SQLite (`vtu.db`), pre-seeded with semester notes, PYQs, and aptitude patterns.
* **AI Engine:** Groq SDK (utilizing `llama-3.1-8b-instant`), Faster Whisper (local speech transcription).
* **Document Engine:** FPDF2 (PDF generation).

---

## ⚙️ Setup & Installation

### Prerequisites
* Python 3.10 or higher installed.
* A Groq API Key (for real AI functionality). Get one from [Groq Console](https://console.groq.com/).
* (Optional) Telegram Bot Token from [@BotFather](https://t.me/BotFather) for running the Telegram bot.

### Step-by-Step Installation

1. **Clone the Repository:**
   ```bash
   git clone <your-repository-url>
   cd vtu-ai-study-buddy-main
   ```

2. **Set up the Python Virtual Environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the `Backend/` directory and configure the following variables:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   BOT_API_BASE=http://127.0.0.1:8001
   ```

5. **Initialize & Seed the SQLite Database:**
   Populate the database with pre-packaged VTU notes and placement questions:
   ```bash
   cd Backend
   python seed.py
   ```

6. **Run the FastAPI Server:**
   ```bash
   python main.py
   ```
   The backend API and frontend dashboard will be available at: **`http://127.0.0.1:8001`**

7. **Run the Telegram Bot (Optional):**
   Open another terminal, activate the virtual environment, and run:
   ```bash
   cd Backend
   python bot.py
   ```

---

## 📁 Repository Structure

```
├── Backend/
│   ├── uploads/               # User-uploaded PDFs
│   ├── ai_engine.py           # Logic for Groq AI queries, aptitude, & mock interviews
│   ├── auth.py                # JWT Token authentication & security helpers
│   ├── bot.py                 # Telegram Bot client & handlers
│   ├── database.py            # SQLite database initialization
│   ├── main.py                # FastAPI routes, RAG pipeline, & server bootstrap
│   ├── models.py              # SQLAlchemy DB models (Subject, Note, Question, User, etc.)
│   ├── seed.py                # DB Seed scripts with mock syllabus notes and mock exams
│   ├── vtu.db                 # Seeded SQLite database file
│   └── requirements.txt       # Backend dependencies list
├── frontend/
│   └── index.html             # The main Single-Page App dashboard
├── .gitignore                 # Files excluded from version control
├── render.yaml                # Render cloud deployment config
├── requirements.txt           # Unified project requirements list
└── README.md                  # Project documentation (this file)
```

---

## 💡 Fallback Mode
If you run the project without a `GROQ_API_KEY`, the application automatically enters **Mock AI Mode**. You will still be able to search notes, take mock exams, practice aptitude prep, and interact with the tutor via realistic placeholder AI responses.
