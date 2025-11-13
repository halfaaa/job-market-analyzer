import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="AI Job Market Analyzer",
    layout="wide",
    page_icon="💼"
)

@st.cache_data
def load_data():
    path = Path("data/processed/jobs_with_skills.parquet")
    if not path.exists():
        st.error("Processed data not found! Please run ETL notebook first.")
        return pd.DataFrame()
    return pd.read_parquet(path)

df = load_data()

st.title("AI Job Market Analyzer – Germany")
st.markdown(
    "This dashboard displays Data/ML job postings in Germany and analyzes in-demand skills."
)

st.markdown(
    """
    **Built with:** 🐍 Python | 🧠 NLP (RapidFuzz) | 📊 Streamlit | 🐳 Docker | ⚙️ CI/CD  
    _Created by Nima Arabi_
    """
)

if df.empty:
    st.stop()


with st.sidebar:
    st.header("🔍 Filters")
    city = st.multiselect(
        "Location", options=sorted(df["location"].unique()), default=df["location"].unique()
    )

    skill = st.text_input("Search Skill (e.g., Python, SQL, Docker)", "")


filtered = df[df["location"].isin(city)]

if skill:
    filtered = filtered[filtered["skills"].apply(lambda s: any(skill.lower() in x.lower() for x in s))]

st.subheader(f"Found {len(filtered)} job postings")
st.dataframe(filtered[["title", "company", "location", "skills", "url"]].reset_index(drop=True), use_container_width=True)


skills_flat = [s for sublist in filtered["skills"] for s in sublist]
skills_df = pd.Series(skills_flat, name="skill").value_counts().reset_index()
skills_df.columns = ["skill", "count"]

fig = px.bar(skills_df.head(15), x="skill", y="count", title="Top 15 Skills in Job Postings")
st.plotly_chart(fig, use_container_width=True)
