# =============================
# 1) Base image
# =============================
FROM python:3.10

# =============================
# 2) Set work directory
# =============================
WORKDIR /app

# =============================
# 3) Copy project files
# =============================
COPY . /app

# =============================
# 4) Install dependencies
# =============================
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# =============================
# 5) Expose Streamlit port
# =============================
EXPOSE 8501

# =============================
# 6) Run Streamlit app
# =============================
CMD ["streamlit", "run", "app/main.py", "--server.address=0.0.0.0", "--server.port=8501"]
