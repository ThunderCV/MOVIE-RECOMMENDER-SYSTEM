import streamlit as st
from pipeline.pipeline import MovieRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Movie Recommendation System", page_icon=":clapper:", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return MovieRecommendationPipeline()

pipeline = init_pipeline()

st.title("Movie Recommendation System :clapper:")

query = st.text_input("Enter a movie title or description eg. : A space adventure with aliens")
if query:
    with st.spinner("Generating recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommended Movies:")
        st.write(response)