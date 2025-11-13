# AI Job Market Analyzer – Germany

This project analyzes the German AI/Data job market by extracting required skills from job postings and visualizing trends using an interactive Streamlit dashboard.

Built with:  
🐍 **Python** | 🔍 **NLP (RapidFuzz)** | 🎨 **Streamlit** | 📦 **Docker** | ⚙️ **CI/CD**

---

## 🚀 Features

### 🔎 Job Postings ETL Pipeline
- Load job listings from CSV/JSON/API  
- Clean and normalize columns  
- Save processed results as Parquet  

### 🧠 Skill Extraction (NLP)
- Uses fuzzy matching (RapidFuzz)  
- Detects most common AI/Data skills  
- Fully configurable skills dictionary  

### 📈 Interactive Streamlit Dashboard
- Filter by location  
- Search by desired skill (Python, SQL, Docker…)  
- Explore top skills in the job market  
- Direct links to job pages  

### 🐳 Docker Support
Fully containerized — run anywhere:
```bash
docker run -p 8501:8501 job-analyzer
```

### 🔄 CI/CD (GitHub Actions)
- Automatic Docker image build  
- Future: Auto-deploy to HuggingFace Spaces  

---

## 🏗️ Project Structure

```
job-market-analyzer/
│
├── app/
│   └── main.py              # Streamlit dashboard
│
├── data/
│   ├── raw/                 # Raw input data
│   └── processed/           # ETL output (.parquet)
│
├── src/
│   ├── etl/                 # ETL pipeline scripts
│   ├── nlp/                 # Skill extraction logic
│   └── viz/                 # Charts
│
├── notebooks/
│   └── 01_etl_eda.ipynb     # ETL notebook
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Locally

### 1) Create and activate virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run the ETL notebook
Open and run:

```
notebooks/01_etl_eda.ipynb
```

This produces:

```
data/processed/jobs_with_skills.parquet
```

### 3) Start the Streamlit app
```bash
streamlit run app/main.py
```

---

## 🐳 Run with Docker

### 1) Build image
```bash
docker build -t job-analyzer .
```

### 2) Run container
```bash
docker run -p 8501:8501 job-analyzer
```

Open:

👉 http://localhost:8501

---

## 🌐 Deployment (Coming)
Planned improvements:
- Deploy to **Hugging Face Spaces**
- Add **GitHub Actions CI/CD workflow**
- Auto-build and auto-deploy the dashboard

---

## ✨ Future Enhancements
- ML-based skill extraction using transformers  
- Trend forecasting model  
- Real-time scraping via API  
- Auto-updating dashboard (cron jobs)  

---

## 📬 Contact
🌐 GitHub: https://github.com/halfaaa

