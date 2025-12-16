import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="MindCraft Dashboard", layout="wide")

st.title("🧠 MindCraft – Smart Math Game Dashboard")
st.write("Live performance analytics")

DATA_FILE = "mindcraft_player_data.txt"

# ---------- SAFETY CHECK ----------
if not os.path.exists(DATA_FILE):
    st.error("❌ Data file not found: mindcraft_player_data.txt")
    st.stop()

# ---------- READ DATA ----------
data = []
with open(DATA_FILE, "r") as f:
    for line in f:
        parts = line.strip().split("|")
        if len(parts) != 6:
            continue

        date, player, subject, score, avg_time, level = parts

        score = int(score)
        avg_time = float(avg_time)
        level = int(level.replace("Level:", "").strip())

        data.append([date, player, subject, score, avg_time, level])

df = pd.DataFrame(
    data,
    columns=["Date", "Player", "Subject", "Score", "Avg Time", "Level"]
)

# ---------- SHOW DATA ----------
st.subheader("📋 Player Records")
st.dataframe(df)

# ---------- LEADERBOARD ----------
st.subheader("🏆 Leaderboard")
leaderboard = df.sort_values(["Score", "Level"], ascending=False)
st.table(leaderboard[["Player", "Score", "Level"]].head(5))

# ---------- INSIGHT ----------
st.subheader("🤖 AI Insight")
best = leaderboard.iloc[0]
st.success(
    f"Top player is **{best['Player']}** "
    f"with score {best['Score']} at level {best['Level']} 🚀"
)
