import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Personalized Movie Recommendation Engine",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).parent

REPORT_DIR = PROJECT_ROOT / "runs" / "reports"

RECOMMENDATIONS_PATH = (
    REPORT_DIR / "final_ranked_recommendations.csv"
)

# --------------------------------------------------
# LOAD RECOMMENDATIONS
# --------------------------------------------------

@st.cache_data
def load_recommendations():

    recommendations = pd.read_csv(
        RECOMMENDATIONS_PATH
    )

    return recommendations


# --------------------------------------------------
# APPLICATION UI
# --------------------------------------------------

st.title("Personalized Movie Recommendation Engine")

st.markdown(
    """
    Discover movies personalized to your interests.

    This application uses a Two-Tower Retrieval Model,
    FAISS candidate generation, and a Random Forest
    ranking model.
    """
)

st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

try:

    recommendations_df = load_recommendations()

except FileNotFoundError:

    st.error(
        "Recommendation file not found. "
        "Please run the recommendation pipeline first."
    )

    st.stop()


# --------------------------------------------------
# USER SELECTION
# --------------------------------------------------

available_users = sorted(
    recommendations_df["user_idx"].unique()
)

selected_user = st.selectbox(
    "Select a User Profile",
    available_users
)

# --------------------------------------------------
# FILTER RECOMMENDATIONS
# --------------------------------------------------

user_recommendations = (
    recommendations_df[
        recommendations_df["user_idx"] == selected_user
    ]
    .sort_values("final_rank")
)

# --------------------------------------------------
# DISPLAY USER INFORMATION
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "User Profile",
    selected_user
)

col2.metric(
    "Recommended Movies",
    len(user_recommendations)
)

col3.metric(
    "Recommendation Method",
    "Two-Stage ML"
)

st.divider()

# --------------------------------------------------
# DISPLAY RECOMMENDATIONS
# --------------------------------------------------

st.subheader("Your Top Movie Recommendations")

for _, row in user_recommendations.iterrows():

    st.markdown(
        f"""
        **{int(row['final_rank'])}. {row['title']}**

        Genres: {row['genres']}

        Ranking Score: {row['ranking_score']:.4f}
        """
    )

    st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "MovieLens Personalized Recommendation Engine | "
    "Machine Learning Project"
)
