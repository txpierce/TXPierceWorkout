import streamlit as st
import pandas as pd
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Chase the Lion - Complete 12-Week Program",
    page_icon="🦁",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR MOBILE OPTIMIZATION ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #fafafa; }
    .stSelectbox label { font-weight: bold; color: #f59e0b; }
    div.stButton > button { width: 100%; background-color: #f59e0b; color: #0f172a; font-weight: bold; border-radius: 8px; }
    div.stButton > button:hover { background-color: #d97706; color: white; }
    .exercise-card { background-color: #1a1c23; padding: 12px; border-radius: 10px; border: 1px solid #30333f; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.title("🦁 Chase the Lion: Complete 12-Week Lift Program")
st.caption("Full Master Architecture | Mobile Dropdown Navigation")

# --- COMPLETE 12-WEEK MASTER PROGRAM DATA STRUCTURE ---
PROGRAM_DATA = {
    "Phase 1: Base Phase (Weeks 1-4)": {
        "Week 1: Baseline": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Overhead Barbell Press", "Sets": 5, "Reps": "5", "Rest": "2-3 min", "RPE": "8", "Wt": "90 lbs"},
                {"Series": "B1", "Exercise": "Flat DB Bench Press", "Sets": 3, "Reps": "8-10", "Rest": "-", "RPE": "8", "Wt": "55 lbs"},
                {"Series": "B1", "Exercise": "Chest-Supported T-Bar Row", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "45 lbs"},
                {"Series": "B2", "Exercise": "Seated DB Arnold Press", "Sets": 3, "Reps": "8-10", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Skull Crushers", "Sets": 3, "Reps": "6-8", "Rest": "90 sec", "RPE": "8", "Wt": "80 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Crossover", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "C-Series", "Exercise": "Tricep Extension", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "80 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Pendlay Row", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Chin-Up", "Sets": 3, "Reps": "AMRAP", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Face Pull", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "DB Hammer Curl", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Incline DB Y-Raise", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "EZ Bar Preacher Curl", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "D-Series", "Exercise": "Lat Pulldown → DB Curl", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "100 lbs / 25 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Front Squat", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Romanian Deadlift", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "DB Walking Lunges", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Glute Ham Raise", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B2", "Exercise": "Seated Calf Raise", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "90 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 3, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "50 lbs"},
                {"Series": "C-Series", "Exercise": "Split Squat ISO Hold", "Sets": 3, "Reps": "20-30s", "Rest": "90 sec", "RPE": "8", "Wt": "BW"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit & Diaphragmatic Breaths", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Machine Chest Press", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "7", "Wt": "110 lbs"},
                {"Series": "B1", "Exercise": "V-Grip Cable Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "110 lbs"},
                {"Series": "C-Series", "Exercise": "Lateral Raise Machine", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "8", "Wt": "30 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Tricep Pushdown", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "50 lbs"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "8", "Wt": "120 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Knee Raise", "Sets": 3, "Reps": "10-12", "Rest": "60 sec", "RPE": "7", "Wt": "BW"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Outdoor Walk & Hydration", "Sets": 1, "Reps": "20-30 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 2: Progression": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Overhead Barbell Press", "Sets": 5, "Reps": "6", "Rest": "2-3 min", "RPE": "8", "Wt": "95 lbs"},
                {"Series": "B1", "Exercise": "Close-Grip Press", "Sets": 4, "Reps": "8-10", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "High-Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "50 lbs"},
                {"Series": "B2", "Exercise": "Seated DB Arnold Press", "Sets": 4, "Reps": "8-10", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Skull Crushers", "Sets": 4, "Reps": "6-8", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "High-to-Low Fly", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "C-Series", "Exercise": "Rope Overhead", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "35 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Pendlay Row", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Chin-Up", "Sets": 4, "Reps": "AMRAP", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Face Pull", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Incline DB Y-Raise", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "EZ Bar Preacher Curl", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Front Squat", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Romanian Deadlift", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "DB Walking Lunges", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Glute Ham Raise", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B2", "Exercise": "Seated Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "90 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "50 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit & Diaphragmatic Breaths", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Machine Chest Press", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "7", "Wt": "110 lbs"},
                {"Series": "B1", "Exercise": "V-Grip Cable Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "110 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Tricep Pushdown", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "50 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Outdoor Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 3: Overload": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Overhead Barbell Press", "Sets": 6, "Reps": "4", "Rest": "2-3 min", "RPE": "9", "Wt": "100 lbs"},
                {"Series": "B1", "Exercise": "Incline DB Press", "Sets": 4, "Reps": "8-10", "Rest": "-", "RPE": "9", "Wt": "55 lbs"},
                {"Series": "B1", "Exercise": "Face Pull", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "9", "Wt": "45 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Press-Out", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "9", "Wt": "30 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Pendlay Row", "Sets": 6, "Reps": "4", "Rest": "2-3 min", "RPE": "9", "Wt": "140 lbs"},
                {"Series": "B1", "Exercise": "Chin-Up", "Sets": 4, "Reps": "AMRAP", "Rest": "-", "RPE": "9", "Wt": "BW"},
                {"Series": "C-Series", "Exercise": "Incline DB Y-Raise", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "9", "Wt": "15 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Front Squat", "Sets": 6, "Reps": "4", "Rest": "2-3 min", "RPE": "9", "Wt": "140 lbs"},
                {"Series": "B1", "Exercise": "Romanian Deadlift", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "9", "Wt": "140 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "9", "Wt": "55 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit & Diaphragmatic Breaths", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 4, "Reps": "8-10", "Rest": "90 sec", "RPE": "8", "Wt": "60 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "40 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 4: Deload": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Overhead Barbell Press", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "7", "Wt": "85 lbs"},
                {"Series": "B1", "Exercise": "Machine Press", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "110 lbs"},
                {"Series": "C-Series", "Exercise": "Pec Deck", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "100 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Pendlay Row", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "7", "Wt": "120 lbs"},
                {"Series": "B1", "Exercise": "Lat Pulldown", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "7", "Wt": "90 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Front Squat", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "7", "Wt": "120 lbs"},
                {"Series": "B1", "Exercise": "Leg Press", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "180 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit & Diaphragmatic Breaths", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 3, "Reps": "12", "Rest": "90 sec", "RPE": "7", "Wt": "50 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        }
    },
    "Phase 2: Structural Shift (Weeks 5-8)": {
        "Week 5: Shift Baseline": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Barbell Bench Press", "Sets": 5, "Reps": "5", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Volume Press", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Chest-Supported High Row", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "55 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "BW + 10 lbs"},
                {"Series": "B1", "Exercise": "Meadows Row / Landmine Row", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "60 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "145 lbs"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "135 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "60 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 6: Structural Build": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Barbell Bench Press", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Volume Press", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "135 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 4, "Reps": "6", "Rest": "2-3 min", "RPE": "8", "Wt": "BW + 10 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "10", "Rest": "2-3 min", "RPE": "8", "Wt": "145 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "60 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 7: Intensity Peak": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Barbell Bench Press", "Sets": 4, "Reps": "5", "Rest": "60-90s", "RPE": "8", "Wt": "135 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 4, "Reps": "6", "Rest": "60-90s", "RPE": "8", "Wt": "BW + 10 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "8", "Rest": "60-90s", "RPE": "8", "Wt": "135 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 4, "Reps": "10-12", "Rest": "60s", "RPE": "7", "Wt": "55 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 4, "Reps": "15-20", "Rest": "45s", "RPE": "7", "Wt": "30 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 8: Deload Phase 2": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Barbell Bench Press", "Sets": 3, "Reps": "10", "Rest": "2-3 min", "RPE": "7", "Wt": "115 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 3, "Reps": "6", "Rest": "2-3 min", "RPE": "7", "Wt": "BW + 5 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 3, "Reps": "12", "Rest": "2-3 min", "RPE": "7", "Wt": "115 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "12", "Rest": "90 sec", "RPE": "7", "Wt": "50 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 4, "Reps": "20-30", "Rest": "60 sec", "RPE": "7", "Wt": "25 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        }
    },
    "Phase 3: Peak Hypertrophy (Weeks 9-12)": {
        "Week 9: Peak Baseline": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Dumbbell Press", "Sets": 4, "Reps": "10", "Rest": "2 min", "RPE": "7", "Wt": "50 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Press (Chest)", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "7-8", "Wt": "115 lbs"},
                {"Series": "B2", "Exercise": "Chest-Supported High Row", "Sets": 3, "Reps": "12-15", "Rest": "60-75 sec", "RPE": "7-8", "Wt": "50 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Ups", "Sets": 3, "Reps": "6-8", "Rest": "2 min", "RPE": "7", "Wt": "BW + 5 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "12", "Rest": "2 min", "RPE": "7", "Wt": "115 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "12", "Rest": "90 sec", "RPE": "7", "Wt": "45 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "25 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 10: Hypertrophy Overload": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Dumbbell Press", "Sets": 4, "Reps": "10", "Rest": "75-90s", "RPE": "7", "Wt": "50 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Press (Tri-Set)", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "7-8", "Wt": "115 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Ups", "Sets": 3, "Reps": "6-8", "Rest": "75-90s", "RPE": "7", "Wt": "BW + 5 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "12", "Rest": "75-90s", "RPE": "7", "Wt": "115 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "12", "Rest": "75-90s", "RPE": "7", "Wt": "45 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "20-25", "Rest": "45s", "RPE": "7", "Wt": "20 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 11: Eccentric Focus": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Dumbbell Press (4-sec eccentric)", "Sets": 4, "Reps": "12-15", "Rest": "90s", "RPE": "6", "Wt": "40 lbs"},
                {"Series": "B1", "Exercise": "Flat Chest Press (Mechanical Drop)", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "100 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Ups (4-sec eccentric)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "BW"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat (4-sec eccentric)", "Sets": 4, "Reps": "12-15", "Rest": "90s", "RPE": "6", "Wt": "90 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press (4-sec eccentric)", "Sets": 3, "Reps": "12-15", "Rest": "90s", "RPE": "6", "Wt": "35 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "25-30", "Rest": "30s", "RPE": "8", "Wt": "20 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 12: Championship Peak": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline DB Press (Light/Controlled)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "30 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Press", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "6-7", "Wt": "85 lbs"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Neutral Lat Pulldown (Light)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "60 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat (Light)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "70 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press (Light)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "30 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "20-25", "Rest": "60s", "RPE": "6", "Wt": "15 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk & Reset", "Sets": 1, "Reps": "20-30 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        }
    }
}

# --- MOBILE DROPDOWN NAVIGATION ---
st.markdown("### 📅 Program Navigation")
selected_phase = st.selectbox("Select Phase", list(PROGRAM_DATA.keys()))
selected_week = st.selectbox("Select Week", list(PROGRAM_DATA[selected_phase].keys()))
selected_day = st.selectbox("Select Training Day", list(PROGRAM_DATA[selected_phase][selected_week].keys()))

st.markdown("---")
st.subheader(f"📍 {selected_week} — {selected_day}")

# --- WORKOUT DISPLAY TABLE WITH SET CHECKING ---
workout_exercises = PROGRAM_DATA[selected_phase][selected_week][selected_day]

for idx, ex in enumerate(workout_exercises):
    with st.container():
        st.markdown(f"""
        <div class="exercise-card">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 10px; font-weight: bold; background-color: rgba(245, 158, 11, 0.1); color: #f59e0b; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(245, 158, 11, 0.2);">{ex['Series']}</span>
                <span style="font-size: 11px; color: #94a3b8;">Wt: <strong style="color: #f1f5f9;">{ex['Wt']}</strong></span>
            </div>
            <div style="font-weight: bold; font-size: 13px; color: #f8fafc; margin-top: 4px;">{ex['Exercise']}</div>
            <div style="display: flex; justify-content: space-between; font-size: 11px; color: #94a3b8; margin-top: 2px;">
                <span>Sets: <strong>{ex['Sets']}</strong> | Reps: <strong>{ex['Reps']}</strong></span>
                <span>Rest: <strong>{ex['Rest']}</strong> | RPE: <strong>{ex['RPE']}</strong></span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- NUTRITION & MACRO QUICK GUIDE ---
with st.expander("🍽️ View Daily Nutrition & Macro Targets"):
    st.markdown("""
    * **Daily Target:** ~2,800 Calories (200g Protein, 315g Carbs, 80g Fat)
    * **4:15 AM Pre-Workout:** 30g-40g Carbs | 10g Protein (Banana + 1/2 scoop whey)
    * **6:30 AM Post-Workout Breakfast:** 40g Protein | 75g-85g Carbs | 10g-15g Fat
    * **12:00 PM Lunch:** 45g Protein | 75g Carbs | 20g Fat (Chicken, Rice, Avocado)
    * **3:30 PM Afternoon Snack:** 35g Protein | 40g Carbs | 15g Fat (Greek Yogurt, Almonds, Berries)
    * **7:00 PM Dinner:** 50g Protein | 70g Carbs | 25g Fat (Steak, Sweet Potato, Green Beans)
    * **Rest Day Adjustments (Thurs/Sun):** Lower carbs (~50g per meal), slightly higher fats for hormone recovery.
    """)

# --- EXPORT HISTORY SECTION ---
st.markdown("### 📊 Workout Log & History")
if st.button("Export Workout History (.CSV)"):
    history_df = pd.DataFrame(workout_exercises)
    csv_data = history_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name=f"chase_the_lion_workout_{datetime.today().strftime('%Y-%m-%d')}.csv",
        mime='text/csv'
    )
