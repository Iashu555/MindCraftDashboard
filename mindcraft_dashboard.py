import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Load Player Data
DATA_FILE = "mindcraft_player_data.txt"

try:
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

# ===============================
# Parse lines
data = []
for line in lines:
    parts = line.strip().split("|")
    if len(parts) >= 5:
        dt = parts[0].strip()
        player = parts[1].replace("Player:", "").strip()
        subject = parts[2].replace("Subject:", "").strip()
        score = parts[3].replace("Score:", "").strip()
        
        # Avg Time parsing
        try:
            avg_time_part = [p for p in parts if "Avg Time" in p][0]
            avg_time = float(avg_time_part.replace("Avg Time:", "").replace("sec","").strip())
        except:
            avg_time = 0.0
        
        # Level parsing
        try:
            level_part = [p for p in parts if "Level" in p][0]
            level = int(level_part.replace("Level:","").strip())
        except:
            level = 1
        
        data.append([dt, player, subject, score, avg_time, level])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date","Player","Subject","Score","AvgTime","Level"])
