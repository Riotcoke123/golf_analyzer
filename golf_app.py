import streamlit as st
from golf_utils import *

st.set_page_config(page_title="Open Championship Golf Analyzer", layout="centered")
create_table()

st.title("🏌️ Open Championship Golf Analyzer")


if st.button("📊 View All Scores"):
    df = get_all_scores()
    st.dataframe(df)

st.subheader("⬆️ Import Scores via CSV")
csv_file = st.file_uploader("Upload a CSV file", type="csv")
if csv_file:
    import_csv(csv_file)
    st.success("CSV data imported into the database.")

st.subheader("⬇️ Export Data to CSV")
if st.button("Export Backup"):
    export_csv("golf_backup.csv")
    st.success("Data exported to golf_backup.csv")

st.subheader("➕ Manually Add Score Entry")
with st.form("entry_form"):
    col1, col2 = st.columns(2)
    with col1:
        player = st.text_input("Player Name")
        course = st.text_input("Course")
        year = st.number_input("Year", min_value=1900, max_value=2100, value=2024)
        round_num = st.selectbox("Round", [1, 2, 3, 4])
    with col2:
        score = st.number_input("Score", min_value=50, max_value=100)
        weather = st.text_input("Weather")
        wind_kph = st.number_input("Wind (kph)", min_value=0.0, max_value=100.0)
        difficulty = st.selectbox("Hole Difficulty", ['Easy', 'Medium', 'Hard'])

    submitted = st.form_submit_button("Add Entry")
    if submitted:
        insert_score(player, course, year, round_num, score, weather, wind_kph, difficulty)
        st.success("Score entry added!")

st.markdown("---")
st.caption("Developed for golf fans.")
