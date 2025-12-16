import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="MindCraft Dashboard", layout="wide")

st.title("🧠 MindCraft – Smart Math Game Dashboard")
st.write("Live performance analytics")

# ---------------- DATA FILE ----------------
DATA_FILE = "mindcraft_player_data.txt"

if not os.path.exists(DATA_FILE):
    st.error("❌ Data file not found: mindcraft_player_data.txt")
    st.stop()

# ---------------- READ & CLEAN DATA ----------------
data = []

with open(DATA_FILE, "r") as f:
    for line in f:
        parts = line.strip().split("|")

        if len(parts) != 6:
            continue

        date, player, subject, score, avg_time, level = parts

        try:
            # score like "5/5"
            score = int(score.split("/")[0])

            # avg time
            avg_time = float(avg_time)

            # level like "Level: 4"
            level = int(level.replace("Level:", "").strip())

            data.append([date, player, subject, score, avg_time, level])

        except:
            continue

# ---------------- DATAFRAME ----------------
df = pd.DataFrame(
    data,
    columns=["Date", "Player", "Subject", "Score", "Avg Time (sec)", "Level"]
)

if df.empty:
    st.warning("⚠️ No valid data found yet.")
    st.stop()

# ---------------- SHOW DATA ----------------
st.subheader("📋 Player Records")
st.dataframe(df, use_container_width=True)

# ---------------- LEADERBOARD ----------------
st.subheader("🏆 Leaderboard")
leaderboard = df.sort_values(["Score", "Level"], ascending=False)
st.table(leaderboard[["Player", "Score", "Level"]].head(5))

# ---------------- AI INSIGHT ----------------
st.subheader("🤖 AI Insight")

top_player = leaderboard.iloc[0]

st.success(
    f"Top performer is **{top_player['Player']}** "
    f"with score **{top_player['Score']}** "
    f"at level **{top_player['Level']}** 🚀"
)
