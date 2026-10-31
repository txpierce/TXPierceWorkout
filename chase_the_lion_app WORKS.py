#!/usr/init/env python3
"""
TX Pierce Workout App - v18 Master Edition
Complete 12-Week Training Architecture with ALL A, B, C, and D Series across every workout.
"""

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="TX Pierce Workout & Nutrition", page_icon="🦁", layout="wide")

# Master 12-Week Dataset with Complete A, B, C, D Series
WORKOUTS = {
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
                {"Series": "C-Series", "Exercise": "Split Squat ISO Hold", "Sets": 3, "Reps": "20-30s", "Rest": "90 sec", "RPE": "8", "Wt": "BW"},
                {"Series": "D-Series", "Exercise": "Standing Calf Burnout", "Sets": 2, "Reps": "20-25", "Rest": "60 sec", "RPE": "-", "Wt": "BW"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit & Diaphragmatic Breaths", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Machine Chest Press", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "7", "Wt": "110 lbs"},
                {"Series": "B1", "Exercise": "V-Grip Cable Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "110 lbs"},
                {"Series": "B2", "Exercise": "Cable Lateral Raise", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Tricep Rope Pushdown", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Arm Pulldown", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "7", "Wt": "60 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "Low-to-High Cable Fly → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "25 lbs / 35 lbs / 40 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Extension", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Preacher Curl", "Sets": 3, "Reps": "10-12", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "Accessory", "Exercise": "Tibialis Raise", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Cable Crunch", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "50 lbs"},
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
                {"Series": "C-Series", "Exercise": "Rope Overhead", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "35 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Pendlay Row", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Chin-Up", "Sets": 4, "Reps": "AMRAP", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Face Pull", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Incline DB Y-Raise", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "EZ Bar Preacher Curl", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "D-Series", "Exercise": "Lat Pulldown → DB Curl", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "100 lbs / 25 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Front Squat", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Romanian Deadlift", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "DB Walking Lunges", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Glute Ham Raise", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B2", "Exercise": "Seated Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "90 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 3, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "50 lbs"},
                {"Series": "C-Series", "Exercise": "Split Squat ISO Hold", "Sets": 3, "Reps": "20-30s", "Rest": "90 sec", "RPE": "8", "Wt": "BW"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Machine Chest Press", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "7", "Wt": "110 lbs"},
                {"Series": "B1", "Exercise": "V-Grip Cable Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "110 lbs"},
                {"Series": "B2", "Exercise": "Cable Lateral Raise", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Tricep Rope Pushdown", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Arm Pulldown", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "Low-to-High Cable Fly → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "25 lbs / 35 lbs / 40 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Extension", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Preacher Curl", "Sets": 3, "Reps": "10-12", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "Accessory", "Exercise": "Shoulder Complex", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Cable Crunch", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "50 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Knee Raise", "Sets": 3, "Reps": "10-12", "Rest": "60 sec", "RPE": "7", "Wt": "BW"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 3: Overload": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Overhead Barbell Press", "Sets": 6, "Reps": "4", "Rest": "2-3 min", "RPE": "8-9", "Wt": "105 lbs"},
                {"Series": "B1", "Exercise": "Incline DB Press", "Sets": 4, "Reps": "8-10", "Rest": "-", "RPE": "8-9", "Wt": "55 lbs"},
                {"Series": "B1", "Exercise": "Face Pull", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8-9", "Wt": "45 lbs"},
                {"Series": "B2", "Exercise": "Seated DB Arnold Press", "Sets": 4, "Reps": "8-10", "Rest": "-", "RPE": "8-9", "Wt": "35 lbs"},
                {"Series": "B2", "Exercise": "Skull Crushers", "Sets": 4, "Reps": "6-8", "Rest": "90 sec", "RPE": "8-9", "Wt": "45 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Press-Out", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8-9", "Wt": "30 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Tricep", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "8-9", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Pendlay Row", "Sets": 6, "Reps": "4", "Rest": "2-3 min", "RPE": "8-9", "Wt": "145 lbs"},
                {"Series": "B1", "Exercise": "Chin-Up", "Sets": 4, "Reps": "AMRAP", "Rest": "-", "RPE": "8-9", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Face Pull", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8-9", "Wt": "45 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8-9", "Wt": "110 lbs"},
                {"Series": "B2", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8-9", "Wt": "30 lbs"},
                {"Series": "C-Series", "Exercise": "Incline DB Y-Raise", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8-9", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "EZ Bar Preacher Curl", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "8-9", "Wt": "40 lbs"},
                {"Series": "D-Series", "Exercise": "Lat Pulldown → DB Curl", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "100 lbs / 25 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Front Squat", "Sets": 6, "Reps": "4", "Rest": "2-3 min", "RPE": "8-9", "Wt": "145 lbs"},
                {"Series": "B1", "Exercise": "Romanian Deadlift", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "8-9", "Wt": "145 lbs"},
                {"Series": "B1", "Exercise": "DB Walking Lunges", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8-9", "Wt": "35 lbs"},
                {"Series": "B2", "Exercise": "Glute Ham Raise", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8-9", "Wt": "BW"},
                {"Series": "B2", "Exercise": "Seated Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8-9", "Wt": "100 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8-9", "Wt": "60 lbs"},
                {"Series": "C-Series", "Exercise": "Split Squat ISO Hold", "Sets": 4, "Reps": "20-30s", "Rest": "90 sec", "RPE": "8-9", "Wt": "BW"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit & Diaphragmatic Breaths", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 4, "Reps": "8-10", "Rest": "90 sec", "RPE": "8", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Machine Chest Press", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "120 lbs"},
                {"Series": "B1", "Exercise": "V-Grip Cable Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "120 lbs"},
                {"Series": "B2", "Exercise": "Cable Lateral Raise", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Tricep Rope Pushdown", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "45 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Arm Pulldown", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "Low-to-High Cable Fly → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "25 lbs / 35 lbs / 40 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Extension", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Preacher Curl", "Sets": 4, "Reps": "10-12", "Rest": "60 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "8", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "145 lbs"},
                {"Series": "Accessory", "Exercise": "Shoulder Complex", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "8", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Cable Crunch", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "50 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Knee Raise", "Sets": 4, "Reps": "10-12", "Rest": "60 sec", "RPE": "8", "Wt": "BW"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 4: Deload": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Overhead Barbell Press", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "7-8", "Wt": "90 lbs"},
                {"Series": "B1", "Exercise": "Machine Press", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "110 lbs"},
                {"Series": "B1", "Exercise": "Chest-Supported Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "50 lbs"},
                {"Series": "B2", "Exercise": "Seated DB Arnold Press", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "B2", "Exercise": "Skull Crushers", "Sets": 4, "Reps": "8-10", "Rest": "90 sec", "RPE": "8", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "Pec Deck", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7-8", "Wt": "100 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Bar Pushdown", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "7-8", "Wt": "40 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Pendlay Row", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "7-8", "Wt": "125 lbs"},
                {"Series": "B1", "Exercise": "Chin-Up", "Sets": 4, "Reps": "AMRAP", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Face Pull", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Incline DB Y-Raise", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7-8", "Wt": "12.5 lbs"},
                {"Series": "C-Series", "Exercise": "EZ Bar Preacher Curl", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "7-8", "Wt": "35 lbs"},
                {"Series": "D-Series", "Exercise": "Lat Pulldown → DB Curl", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "90 lbs / 20 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Front Squat", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "7-8", "Wt": "125 lbs"},
                {"Series": "B1", "Exercise": "Romanian Deadlift", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "8", "Wt": "125 lbs"},
                {"Series": "B1", "Exercise": "DB Walking Lunges", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "B2", "Exercise": "Glute Ham Raise", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "BW"},
                {"Series": "B2", "Exercise": "Seated Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "80 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7-8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Split Squat ISO Hold", "Sets": 4, "Reps": "20-30s", "Rest": "90 sec", "RPE": "7-8", "Wt": "BW"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit & Diaphragmatic Breaths", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Incline DB Press", "Sets": 3, "Reps": "12", "Rest": "90 sec", "RPE": "7", "Wt": "50 lbs"},
                {"Series": "B1", "Exercise": "Machine Chest Press", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "7", "Wt": "100 lbs"},
                {"Series": "B1", "Exercise": "V-Grip Cable Row", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "Cable Lateral Raise", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7", "Wt": "15 lbs"},
                {"Series": "B2", "Exercise": "Tricep Rope Pushdown", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Arm Pulldown", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "D-Series", "Exercise": "Low-to-High Cable Fly → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "20 lbs / 30 lbs / 35 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Cable Curl", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Extension", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "Accessory", "Exercise": "Preacher Curl", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "120 lbs"},
                {"Series": "Accessory", "Exercise": "Shoulder Complex", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Cable Crunch", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "45 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Knee Raise", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "BW"}
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
                {"Series": "B1", "Exercise": "Chest-Supported High Row", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "55 lbs"},
                {"Series": "B2", "Exercise": "DB Arnold Press", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Overhead Cable Tricep Extension", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Low-to-High Cable Fly", "Sets": 3, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 3, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "BW + 10 lbs"},
                {"Series": "B1", "Exercise": "Meadows Row / Landmine Row", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Cable Face Pull w/ External Rotation", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "45 lbs"},
                {"Series": "B2", "Exercise": "Lat Pulldown (Neutral Grip)", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "Incline DB Bicep Curl", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly", "Sets": 3, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "EZ-Bar Preacher Curl", "Sets": 3, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "D-Series", "Exercise": "Straight-Arm Lat Pulldown → DB Hammer Curl", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "40 lbs / 25 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "6-8", "Rest": "2-3 min", "RPE": "8", "Wt": "145 lbs"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Bulgarian Split Squats", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Lying Leg Curl", "Sets": 3, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "60 lbs"},
                {"Series": "B2", "Exercise": "Standing Calf Raise", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 3, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "50 lbs"},
                {"Series": "C-Series", "Exercise": "Seated Calf Raise", "Sets": 3, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "90 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "10-12", "Rest": "90 sec", "RPE": "7-8", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Incline Cable Fly", "Sets": 3, "Reps": "12-15", "Rest": "-", "RPE": "7-8", "Wt": "25 lbs"},
                {"Series": "B1", "Exercise": "Seated Cable Row (Wide Grip)", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "7-8", "Wt": "110 lbs"},
                {"Series": "B2", "Exercise": "Lean-Away Cable Lateral Raise", "Sets": 3, "Reps": "15-20", "Rest": "-", "RPE": "7-8", "Wt": "15 lbs"},
                {"Series": "B2", "Exercise": "Tricep Straight-Bar Pushdown", "Sets": 3, "Reps": "12-15", "Rest": "90 sec", "RPE": "7-8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Lat Pulldown (Underhand Grip)", "Sets": 3, "Reps": "15-20", "Rest": "-", "RPE": "7-8", "Wt": "90 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 3, "Reps": "15-20", "Rest": "90 sec", "RPE": "7-8", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "25 lbs / 35 lbs / 40 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 3, "Reps": "10-12", "Rest": "60 sec", "RPE": "7", "Wt": "30 lbs"},
                {"Series": "Accessory", "Exercise": "Triceps Extensions", "Sets": 3, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "145 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 3, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "50 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 6: Structural Build": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Barbell Bench Press", "Sets": 4, "Reps": "8", "Rest": "2-3 min", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Volume Press", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Chest-Supported High Row", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "55 lbs"},
                {"Series": "B2", "Exercise": "DB Arnold Press", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Overhead Cable Tricep Extension", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Low-to-High Cable Fly", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 4, "Reps": "6", "Rest": "2-3 min", "RPE": "8", "Wt": "BW + 10 lbs"},
                {"Series": "B1", "Exercise": "Meadows Row / Landmine Row", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Cable Face Pull w/ External Rotation", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "45 lbs"},
                {"Series": "B2", "Exercise": "Lat Pulldown (Neutral Grip)", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "Incline DB Bicep Curl", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "EZ-Bar Preacher Curl", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "D-Series", "Exercise": "Straight-Arm Lat Pulldown → DB Hammer Curl", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "40 lbs / 25 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "10", "Rest": "2-3 min", "RPE": "8", "Wt": "145 lbs"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Bulgarian Split Squats", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Lying Leg Curl", "Sets": 4, "Reps": "10-12", "Rest": "-", "RPE": "8", "Wt": "60 lbs"},
                {"Series": "B2", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "8", "Wt": "50 lbs"},
                {"Series": "C-Series", "Exercise": "Seated Calf Raise", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "8", "Wt": "90 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 4, "Reps": "10-12", "Rest": "90 sec", "RPE": "7-8", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Incline Cable Fly", "Sets": 4, "Reps": "12-15", "Rest": "-", "RPE": "7-8", "Wt": "25 lbs"},
                {"Series": "B1", "Exercise": "Seated Cable Row (Wide Grip)", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7-8", "Wt": "110 lbs"},
                {"Series": "B2", "Exercise": "Lean-Away Cable Lateral Raise", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7-8", "Wt": "15 lbs"},
                {"Series": "B2", "Exercise": "Tricep Straight-Bar Pushdown", "Sets": 4, "Reps": "12-15", "Rest": "90 sec", "RPE": "7-8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Lat Pulldown (Underhand Grip)", "Sets": 4, "Reps": "15-20", "Rest": "-", "RPE": "7-8", "Wt": "90 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 4, "Reps": "15-20", "Rest": "90 sec", "RPE": "7-8", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15-20", "Rest": "60 sec", "RPE": "-", "Wt": "25 lbs / 35 lbs / 40 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "10-12", "Rest": "60 sec", "RPE": "7", "Wt": "30 lbs"},
                {"Series": "Accessory", "Exercise": "Parallel Bar / Bench Dips", "Sets": 4, "Reps": "15-20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "8", "Wt": "145 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 4, "Reps": "12-15", "Rest": "60 sec", "RPE": "7", "Wt": "50 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 7: Intensity Peak": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Barbell Bench Press", "Sets": 4, "Reps": "5", "Rest": "60-90s", "RPE": "7-8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Volume Press (Mid-Range Strength)", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "135 lbs"},
                {"Series": "B2", "Exercise": "Chest-Supported High Row (Long-Range Stretch)", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "55 lbs"},
                {"Series": "B3", "Exercise": "Low-to-High Cable Fly (Short-Range Contraction)", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "B1", "Exercise": "DB Arnold Press", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Overhead Cable Tricep Extension", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "40 lbs"},
                {"Series": "B3", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "Pec Deck (Pure Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "8", "Wt": "90 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Bar Pushdown (Pure Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "8", "Wt": "35 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 4, "Reps": "6", "Rest": "60-90s", "RPE": "7-8", "Wt": "BW + 10 lbs"},
                {"Series": "B1", "Exercise": "Meadows Row / Landmine Row (Mid-Range)", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "60 lbs"},
                {"Series": "B2", "Exercise": "Lat Pulldown - Neutral Grip (Long-Range Stretch)", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "100 lbs"},
                {"Series": "B3", "Exercise": "Cable Face Pull w/ External Rotation (Short-Range)", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "40 lbs"},
                {"Series": "B1", "Exercise": "Incline DB Bicep Curl", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "25 lbs"},
                {"Series": "B2", "Exercise": "EZ-Bar Preacher Curl", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "40 lbs"},
                {"Series": "B3", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly (Pure Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Arm Lat Pulldown (Pure Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "8", "Wt": "35 lbs"},
                {"Series": "D-Series", "Exercise": "Lat Pulldown → DB Curl", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "90 lbs / 20 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "8", "Rest": "60-90s", "RPE": "7-8", "Wt": "135 lbs"},
                {"Series": "B1", "Exercise": "Hack Squat (Mid-Range)", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "135 lbs"},
                {"Series": "B2", "Exercise": "Leg Extension (Short-Range Contraction)", "Sets": 4, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "50 lbs"},
                {"Series": "B3", "Exercise": "Tibialis Raise (Long-Range Stretch)", "Sets": 4, "Reps": "15–20", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "135 lbs"},
                {"Series": "B2", "Exercise": "Lying Leg Curl", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "7–8", "Wt": "60 lbs"},
                {"Series": "B3", "Exercise": "Bulgarian Split Squats", "Sets": 4, "Reps": "10–12", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Standing Calf Raise (Pure Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "8", "Wt": "120 lbs"},
                {"Series": "C-Series", "Exercise": "Seated Calf Raise (Pure Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "8", "Wt": "80 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 4, "Reps": "10-12", "Rest": "60-90s", "RPE": "7", "Wt": "55 lbs"},
                {"Series": "B1", "Exercise": "Incline Cable Fly", "Sets": 4, "Reps": "12–15", "Rest": "-", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row (Wide Grip)", "Sets": 4, "Reps": "12–15", "Rest": "-", "RPE": "7", "Wt": "100 lbs"},
                {"Series": "B3", "Exercise": "Lean-Away Cable Lateral Raise", "Sets": 4, "Reps": "15–20", "Rest": "60–75 sec", "RPE": "7", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Tricep Rope Pushdown (Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "7–8", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl (Pump Isolation)", "Sets": 3, "Reps": "15–25", "Rest": "Minimal", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "20 lbs / 30 lbs / 35 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 4, "Reps": "15–20", "Rest": "45s", "RPE": "7", "Wt": "30 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 4, "Reps": "15–20", "Rest": "45s", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "12–15", "Rest": "45s", "RPE": "7", "Wt": "25 lbs"},
                {"Series": "Accessory", "Exercise": "Parallel Bar / Bench Dips", "Sets": 4, "Reps": "15–20", "Rest": "45s", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "15–25", "Rest": "45s", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "Accessory", "Exercise": "Tibialis Raise", "Sets": 3, "Reps": "20–25", "Rest": "45s", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 4, "Reps": "12–15", "Rest": "45s", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 4, "Reps": "15–20", "Rest": "45s", "RPE": "7", "Wt": "45 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 8: Deload Phase 2": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Barbell Bench Press", "Sets": 3, "Reps": "10", "Rest": "2-3 min", "RPE": "7", "Wt": "115 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Press → Chest Fly (Mechanical Drop Set)", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "115 lbs / 25 lbs"},
                {"Series": "B2", "Exercise": "Chest-Supported High Row", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "55 lbs"},
                {"Series": "B3", "Exercise": "Push-Up (To Failure / High Density)", "Sets": 4, "Reps": "AMRAP", "Rest": "60–75 sec", "RPE": "8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "DB Arnold Press", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B2", "Exercise": "Overhead Cable Tricep Extension", "Sets": 4, "Reps": "10–12", "Rest": "60–75 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Low-to-High Cable Fly (Pure Isolation / Pump)", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Up", "Sets": 3, "Reps": "6", "Rest": "2-3 min", "RPE": "7", "Wt": "BW + 5 lbs"},
                {"Series": "B1", "Exercise": "Meadows Row / Landmine Row", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "60 lbs"},
                {"Series": "B2", "Exercise": "Neutral-Grip Lat Pulldown → Straight-Arm Pullover", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "100 lbs / 40 lbs"},
                {"Series": "B3", "Exercise": "Cable Face Pull w/ External Rotation", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "B1", "Exercise": "Incline DB Bicep Curl", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "B2", "Exercise": "EZ-Bar Preacher Curl", "Sets": 4, "Reps": "10–12", "Rest": "60–75 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly (Pure Pump Isolation)", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Straight-Arm Lat Pulldown", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "D-Series", "Exercise": "Lat Pulldown → DB Curl", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "90 lbs / 20 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 3, "Reps": "12", "Rest": "2-3 min", "RPE": "7", "Wt": "115 lbs"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "135 lbs"},
                {"Series": "B2", "Exercise": "Lying Leg Curl → Hip Extension / Glute Bridge", "Sets": 4, "Reps": "10–12", "Rest": "60–75 sec", "RPE": "8", "Wt": "60 lbs / BW"},
                {"Series": "B1", "Exercise": "Bulgarian Split Squats", "Sets": 4, "Reps": "10–12", "Rest": "-", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "B2", "Exercise": "Leg Extension", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "8", "Wt": "45 lbs"},
                {"Series": "C-Series", "Exercise": "Standing Calf Raise (Pure Pump Isolation)", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "110 lbs"},
                {"Series": "C-Series", "Exercise": "Seated Calf Raise (Pure Pump Isolation)", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "70 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "12", "Rest": "90 sec", "RPE": "7", "Wt": "50 lbs"},
                {"Series": "B1", "Exercise": "Incline Cable Fly", "Sets": 4, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row (Wide Grip)", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "100 lbs"},
                {"Series": "B1", "Exercise": "Lean-Away Cable Lateral Raise", "Sets": 4, "Reps": "15–20", "Rest": "-", "RPE": "7–8", "Wt": "15 lbs"},
                {"Series": "B2", "Exercise": "Tricep Straight-Bar Pushdown", "Sets": 4, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "Lat Pulldown (Underhand Grip)", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "80 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 4, "Reps": "20–30", "Rest": "Minimal", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "20 lbs / 30 lbs / 35 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 4, "Reps": "20–30", "Rest": "60 sec", "RPE": "7", "Wt": "25 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 4, "Reps": "20–30", "Rest": "60 sec", "RPE": "7", "Wt": "30 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 4, "Reps": "15–20", "Rest": "60 sec", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 4, "Reps": "20–30", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "20–30", "Rest": "60 sec", "RPE": "7", "Wt": "120 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 4, "Reps": "15–20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 4, "Reps": "20–30", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"}
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
                {"Series": "B1", "Exercise": "Flat Barbell Press (Chest)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "115 lbs"},
                {"Series": "B2", "Exercise": "Chest-Supported High Row (Back)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "50 lbs"},
                {"Series": "B1", "Exercise": "DB Arnold Press (Shoulders)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "25 lbs"},
                {"Series": "B2", "Exercise": "Overhead Cable Tricep Extension (Triceps)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "Low-to-High Cable Fly (Long Range / Slow Tempo)", "Sets": 3, "Reps": "15–20", "Rest": "-", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 3, "Reps": "15–20", "Rest": "60–75 sec", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Ups", "Sets": 3, "Reps": "6–8", "Rest": "2 min", "RPE": "7", "Wt": "BW + 5 lbs"},
                {"Series": "B1", "Exercise": "Neutral-Grip Lat Pulldown (Vertical Pull)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "90 lbs"},
                {"Series": "B2", "Exercise": "Cable Face Pull w/ External Rotation (Rear Delts)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "35 lbs"},
                {"Series": "B1", "Exercise": "Meadows Row / Landmine Row (Mid-Back)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "50 lbs"},
                {"Series": "B2", "Exercise": "Incline DB Bicep Curl (Biceps)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly (Slow Tempo / Long Range)", "Sets": 3, "Reps": "15–20", "Rest": "-", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "EZ-Bar Preacher Curl", "Sets": 3, "Reps": "15–20", "Rest": "60–75 sec", "RPE": "8", "Wt": "35 lbs"},
                {"Series": "D-Series", "Exercise": "Straight-Arm Lat Pulldown → DB Hammer Curl", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "35 lbs / 20 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "12", "Rest": "2 min", "RPE": "7", "Wt": "115 lbs"},
                {"Series": "B1", "Exercise": "Lying Leg Curl (Hamstrings)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "50 lbs"},
                {"Series": "B2", "Exercise": "Leg Extension (Quads)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "40 lbs"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift (Posterior Chain)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "115 lbs"},
                {"Series": "B2", "Exercise": "Bulgarian Split Squats (Quads/Glutes)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "Standing Calf Raise (Slow Tempo / Long Range)", "Sets": 3, "Reps": "15–20", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "C-Series", "Exercise": "Seated Calf Raise", "Sets": 3, "Reps": "15–20", "Rest": "60–75 sec", "RPE": "8", "Wt": "70 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "12", "Rest": "90 sec", "RPE": "7", "Wt": "45 lbs"},
                {"Series": "B1", "Exercise": "Incline Cable Fly (Chest)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row (Back)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7", "Wt": "90 lbs"},
                {"Series": "B1", "Exercise": "Lean-Away Cable Lateral Raise (Shoulders)", "Sets": 3, "Reps": "15–20", "Rest": "-", "RPE": "7", "Wt": "12.5 lbs"},
                {"Series": "B2", "Exercise": "Tricep Rope Pushdown (Triceps)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "7", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "Underhand Lat Pulldown (Long Range / Slow)", "Sets": 3, "Reps": "15–20", "Rest": "-", "RPE": "8", "Wt": "80 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 3, "Reps": "15–20", "Rest": "60–75 sec", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "20 lbs / 30 lbs / 35 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "15–20", "Rest": "60 sec", "RPE": "7", "Wt": "25 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 3, "Reps": "15–20", "Rest": "60 sec", "RPE": "7", "Wt": "30 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 3, "Reps": "12–15", "Rest": "60 sec", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 3, "Reps": "15–20", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "15–20", "Rest": "60 sec", "RPE": "8", "Wt": "110 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 3, "Reps": "12–15", "Rest": "60 sec", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 3, "Reps": "15–20", "Rest": "60 sec", "RPE": "7", "Wt": "40 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 10: Hypertrophy Overload": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Dumbbell Press", "Sets": 4, "Reps": "10", "Rest": "75-90s", "RPE": "7", "Wt": "50 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Press (Mid-Range Strength)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "115 lbs"},
                {"Series": "B2", "Exercise": "Incline Cable Fly (Stretch-Mediated)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "B3", "Exercise": "Push-Up (Short-Range Contraction)", "Sets": 3, "Reps": "AMRAP", "Rest": "45–60 sec", "RPE": "8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "DB Arnold Press (Mid-Range)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "25 lbs"},
                {"Series": "B2", "Exercise": "Lateral Raise (Stretch/Mid-Range)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "15 lbs"},
                {"Series": "B3", "Exercise": "Overhead Cable Tricep Extension (Short-Range)", "Sets": 3, "Reps": "12–15", "Rest": "45–60 sec", "RPE": "7–8", "Wt": "35 lbs"},
                {"Series": "C-Series", "Exercise": "Low-to-High Cable Fly (Pure Isolation / Pump)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Ups", "Sets": 3, "Reps": "6-8", "Rest": "75-90s", "RPE": "7", "Wt": "BW + 5 lbs"},
                {"Series": "B1", "Exercise": "Chest-Supported Row (Mid-Range Strength)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "50 lbs"},
                {"Series": "B2", "Exercise": "Neutral-Grip Lat Pulldown (Stretch-Mediated)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "90 lbs"},
                {"Series": "B3", "Exercise": "Straight-Arm Pullover (Short-Range Contraction)", "Sets": 3, "Reps": "12–15", "Rest": "45–60 sec", "RPE": "7–8", "Wt": "35 lbs"},
                {"Series": "B1", "Exercise": "Incline DB Bicep Curl (Stretch)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "EZ-Bar Preacher Curl (Mid-Range)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "35 lbs"},
                {"Series": "B3", "Exercise": "DB Hammer Curl (Short-Range)", "Sets": 3, "Reps": "12–15", "Rest": "45–60 sec", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Face Pull (Pure Pump Isolation)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "D-Series", "Exercise": "Straight-Arm Lat Pulldown → DB Hammer Curl", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "35 lbs / 20 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat", "Sets": 4, "Reps": "12", "Rest": "75-90s", "RPE": "7", "Wt": "115 lbs"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift (Stretch-Mediated)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "115 lbs"},
                {"Series": "B2", "Exercise": "Lying Leg Curl (Mid-Range Strength)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "50 lbs"},
                {"Series": "B3", "Exercise": "Glute Bridge / Hip Extension (Short-Range)", "Sets": 3, "Reps": "12–15", "Rest": "45–60 sec", "RPE": "7–8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Bulgarian Split Squats (Mid-Range)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7–8", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Leg Extension (Short-Range Contraction)", "Sets": 3, "Reps": "12–15", "Rest": "45–60 sec", "RPE": "7–8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Standing Calf Raise (Pure Pump Isolation)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "C-Series", "Exercise": "Seated Calf Raise (Pure Pump Isolation)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "70 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press", "Sets": 3, "Reps": "12", "Rest": "75-90s", "RPE": "7", "Wt": "45 lbs"},
                {"Series": "B1", "Exercise": "Incline Cable Fly (Stretch)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row (Mid-Range)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "7", "Wt": "90 lbs"},
                {"Series": "B3", "Exercise": "Lean-Away Cable Lateral Raise (Short-Range)", "Sets": 3, "Reps": "15–20", "Rest": "45–60 sec", "RPE": "7", "Wt": "12.5 lbs"},
                {"Series": "C-Series", "Exercise": "Underhand Lat Pulldown (Pure Pump)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "70 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl (Pure Pump)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Tricep Rope Pushdown (Pure Pump)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "20 lbs / 30 lbs / 35 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "20–25", "Rest": "45s", "RPE": "7", "Wt": "20 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 3, "Reps": "20–25", "Rest": "45s", "RPE": "7", "Wt": "25 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 3, "Reps": "15–20", "Rest": "45s", "RPE": "7", "Wt": "15 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 3, "Reps": "20–25", "Rest": "45s", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "20–25", "Rest": "45s", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 3, "Reps": "15–20", "Rest": "45s", "RPE": "7", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 3, "Reps": "20–25", "Rest": "45s", "RPE": "7", "Wt": "35 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 11: Eccentric Focus": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline Dumbbell Press (4-sec eccentric)", "Sets": 4, "Reps": "12-15", "Rest": "90s", "RPE": "6-7", "Wt": "40 lbs"},
                {"Series": "B1", "Exercise": "Flat Chest Press (Mid-Range)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "100 lbs"},
                {"Series": "B2", "Exercise": "Incline Chest Press (Upper Angle Change)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "80 lbs"},
                {"Series": "B3", "Exercise": "Chest Fly (Short-Range Stretch)", "Sets": 3, "Reps": "12–15", "Rest": "30–45 sec", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "B1", "Exercise": "DB Arnold Press", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "B2", "Exercise": "Lateral Raise", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "12.5 lbs"},
                {"Series": "B3", "Exercise": "Overhead Cable Tricep Extension", "Sets": 3, "Reps": "12–15", "Rest": "30–45 sec", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "C-Series", "Exercise": "Low-to-High Cable Fly (Burnout / End-Range Hold)", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "12.5 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up", "Sets": 2, "Reps": "20–25", "Rest": "60 sec", "RPE": "-", "Wt": "12.5 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Weighted Pull-Ups (4-sec eccentric)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6-7", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Chest-Supported Mid Row", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "B2", "Exercise": "High Row (Upper Angle Change)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "B3", "Exercise": "Cable Rear Delt Fly (Short-Range)", "Sets": 3, "Reps": "12–15", "Rest": "30–45 sec", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "B1", "Exercise": "Incline DB Bicep Curl", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "B2", "Exercise": "EZ-Bar Preacher Curl", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "30 lbs"},
                {"Series": "B3", "Exercise": "DB Hammer Curl", "Sets": 3, "Reps": "12–15", "Rest": "30–45 sec", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly (Occlusion Burnout)", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "10 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Straight-Arm Pulldown", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "30 lbs"},
                {"Series": "D-Series", "Exercise": "Lat Pulldown → DB Hammer Curl", "Sets": 2, "Reps": "20–25", "Rest": "60 sec", "RPE": "-", "Wt": "70 lbs / 15 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat (4-sec eccentric)", "Sets": 4, "Reps": "12-15", "Rest": "90s", "RPE": "6-7", "Wt": "90 lbs"},
                {"Series": "B1", "Exercise": "Leg Press (Standard Foot Placement)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "180 lbs"},
                {"Series": "B2", "Exercise": "Leg Press (Narrow Foot / Low Placement)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "140 lbs"},
                {"Series": "B3", "Exercise": "Sissy Squat / Bodyweight Squat Hold", "Sets": 3, "Reps": "15–20", "Rest": "30–45 sec", "RPE": "8", "Wt": "BW"},
                {"Series": "B1", "Exercise": "Deficit Romanian Deadlift", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "95 lbs"},
                {"Series": "B2", "Exercise": "Lying Leg Curl", "Sets": 3, "Reps": "12–15", "Rest": "30–45 sec", "RPE": "8", "Wt": "40 lbs"},
                {"Series": "C-Series", "Exercise": "Standing Calf Raise (Burnout / End-Range Hold)", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "80 lbs"},
                {"Series": "C-Series", "Exercise": "Leg Extension", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "30 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press (4-sec eccentric)", "Sets": 3, "Reps": "12-15", "Rest": "90s", "RPE": "6-7", "Wt": "35 lbs"},
                {"Series": "B1", "Exercise": "Flat Bench Press → Incline Press → Cable Fly", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "8", "Wt": "95 lbs / 75 lbs / 15 lbs"},
                {"Series": "B2", "Exercise": "Cable Row → High Row → Face Pull", "Sets": 3, "Reps": "12–15", "Rest": "30–45 sec", "RPE": "8", "Wt": "80 lbs / 70 lbs / 30 lbs"},
                {"Series": "C-Series", "Exercise": "Lean-Away Cable Lateral Raise (Burnout)", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "10 lbs"},
                {"Series": "C-Series", "Exercise": "Tricep Rope Pushdown", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 3, "Reps": "25–30", "Rest": "Minimal", "RPE": "9", "Wt": "12.5 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "20–25", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / 25 lbs / 30 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "25–30", "Rest": "30s", "RPE": "8", "Wt": "20 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 3, "Reps": "25–30", "Rest": "30s", "RPE": "8", "Wt": "25 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 3, "Reps": "20–25", "Rest": "30s", "RPE": "8", "Wt": "15 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 3, "Reps": "25–30", "Rest": "30s", "RPE": "8", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 4, "Reps": "25–30", "Rest": "30s", "RPE": "9", "Wt": "90 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 3, "Reps": "15–20", "Rest": "30s", "RPE": "8", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 3, "Reps": "25–30", "Rest": "30s", "RPE": "8", "Wt": "30 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk", "Sets": 1, "Reps": "20 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        },
        "Week 12: Championship Peak": {
            "Day 1: Push": [
                {"Series": "A-Series", "Exercise": "Incline DB Press (Light/Controlled)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "30 lbs"},
                {"Series": "B1", "Exercise": "Flat Barbell Press (Chest)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "6–7", "Wt": "85 lbs"},
                {"Series": "B2", "Exercise": "Chest-Supported High Row (Back)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "35 lbs"},
                {"Series": "B1", "Exercise": "DB Arnold Press (Shoulders)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "6–7", "Wt": "15 lbs"},
                {"Series": "B2", "Exercise": "Overhead Cable Tricep Extension (Triceps)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Low-to-High Cable Fly (Slow Tempo / Long Range)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "10 lbs"},
                {"Series": "C-Series", "Exercise": "Single-Arm Cross-Body Tricep Extension", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "10 lbs"},
                {"Series": "D-Series", "Exercise": "DB Lateral Raise → Push-Up (Easy Flow)", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "10 lbs / BW"}
            ],
            "Day 2: Pull": [
                {"Series": "A-Series", "Exercise": "Neutral Lat Pulldown (Light)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Neutral-Grip Lat Pulldown (Vertical Pull)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "6–7", "Wt": "70 lbs"},
                {"Series": "B2", "Exercise": "Cable Face Pull w/ External Rotation (Rear Delts)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "25 lbs"},
                {"Series": "B1", "Exercise": "Cable Row (Mid-Back)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "6–7", "Wt": "60 lbs"},
                {"Series": "B2", "Exercise": "Incline DB Bicep Curl (Biceps)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "15 lbs"},
                {"Series": "C-Series", "Exercise": "Cable Reverse Fly (Slow Tempo / Long Range)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "10 lbs"},
                {"Series": "C-Series", "Exercise": "EZ-Bar Preacher Curl", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "25 lbs"},
                {"Series": "D-Series", "Exercise": "Straight-Arm Lat Pulldown → DB Hammer Curl", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "25 lbs / 15 lbs"}
            ],
            "Day 3: Lower": [
                {"Series": "A-Series", "Exercise": "Hack Squat (Light)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "70 lbs"},
                {"Series": "B1", "Exercise": "Lying Leg Curl (Hamstrings)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "6–7", "Wt": "35 lbs"},
                {"Series": "B2", "Exercise": "Leg Extension (Quads)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "30 lbs"},
                {"Series": "B1", "Exercise": "Romanian Deadlift (Light Posterior Chain)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "6–7", "Wt": "75 lbs"},
                {"Series": "B2", "Exercise": "Goblet Squat (Quads/Glutes)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Standing Calf Raise (Slow Tempo / Long Range)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "60 lbs"},
                {"Series": "C-Series", "Exercise": "Seated Calf Raise", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "45 lbs"}
            ],
            "Day 4: Recovery / Mobility": [
                {"Series": "Mobility", "Exercise": "Mobility Circuit", "Sets": 2, "Reps": "10 reps each", "Rest": "-", "RPE": "3", "Wt": "BW"}
            ],
            "Day 5: Upper Pump": [
                {"Series": "A-Series", "Exercise": "Flat DB Press (Light)", "Sets": 3, "Reps": "10-12", "Rest": "90s", "RPE": "6", "Wt": "30 lbs"},
                {"Series": "B1", "Exercise": "Incline Cable Fly (Chest)", "Sets": 3, "Reps": "12–15", "Rest": "-", "RPE": "6–7", "Wt": "15 lbs"},
                {"Series": "B2", "Exercise": "Seated Cable Row (Back)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "60 lbs"},
                {"Series": "B1", "Exercise": "Cable Lateral Raise (Shoulders)", "Sets": 3, "Reps": "15–20", "Rest": "-", "RPE": "6–7", "Wt": "10 lbs"},
                {"Series": "B2", "Exercise": "Tricep Rope Pushdown (Triceps)", "Sets": 3, "Reps": "12–15", "Rest": "60–75 sec", "RPE": "6–7", "Wt": "25 lbs"},
                {"Series": "C-Series", "Exercise": "Underhand Lat Pulldown (Long Range / Slow)", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "60 lbs"},
                {"Series": "C-Series", "Exercise": "DB Spider Curl", "Sets": 3, "Reps": "20–25", "Rest": "Minimal", "RPE": "6", "Wt": "10 lbs"},
                {"Series": "D-Series", "Exercise": "Cable Crossover → Overhead Rope Ext → Face Pull", "Sets": 2, "Reps": "15–20", "Rest": "60 sec", "RPE": "-", "Wt": "15 lbs / 20 lbs / 25 lbs"}
            ],
            "Day 6: Arms / Calves / Abs": [
                {"Series": "Accessory", "Exercise": "Dual-Cable Bicep Curl", "Sets": 3, "Reps": "20–25", "Rest": "60s", "RPE": "6", "Wt": "15 lbs"},
                {"Series": "Accessory", "Exercise": "Overhead Rope Tricep Extension", "Sets": 3, "Reps": "20–25", "Rest": "60s", "RPE": "6", "Wt": "20 lbs"},
                {"Series": "Accessory", "Exercise": "DB Hammer Curl", "Sets": 3, "Reps": "15–20", "Rest": "60s", "RPE": "6", "Wt": "15 lbs"},
                {"Series": "Accessory", "Exercise": "Bench Dips", "Sets": 3, "Reps": "15–20", "Rest": "60s", "RPE": "6", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Standing Calf Raise", "Sets": 3, "Reps": "20–25", "Rest": "60s", "RPE": "6", "Wt": "70 lbs"},
                {"Series": "Accessory", "Exercise": "Hanging Leg/Knee Raise", "Sets": 3, "Reps": "12–15", "Rest": "60s", "RPE": "6", "Wt": "BW"},
                {"Series": "Accessory", "Exercise": "Declined Cable Crunch", "Sets": 3, "Reps": "20–25", "Rest": "60s", "RPE": "6", "Wt": "30 lbs"}
            ],
            "Day 7: Off / Recovery": [
                {"Series": "Recovery", "Exercise": "Walk & Reset", "Sets": 1, "Reps": "20-30 min", "Rest": "-", "RPE": "2", "Wt": "BW"}
            ]
        }
    }
}

st.sidebar.title("🦁 TX Pierce Tracker")
st.sidebar.markdown("---")

phase_selected = st.sidebar.selectbox("Select Phase", list(WORKOUTS.keys()))
weeks_dict = WORKOUTS[phase_selected]
week_selected = st.sidebar.selectbox("Select Week", list(weeks_dict.keys()))
days_dict = weeks_dict[week_selected]
day_selected = st.sidebar.selectbox("Select Day", list(days_dict.keys()))

st.title(f"🦁 TX Pierce Workout Tracker")
st.subheader(f"{phase_selected} | {week_selected} | {day_selected}")

exercises = days_dict[day_selected]

df = pd.DataFrame(exercises)
st.markdown("### 📋 Today's Training Hierarchy (A, B, C, D Series)")
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("### ✅ Log Your Workout & RPE")
with st.form("workout_log"):
    completed = []
    for idx, row in df.iterrows():
        col1, col2, col3 = st.columns([3, 1, 2])
        with col1:
            st.write(f"**{row['Series']}**: {row['Exercise']} ({row['Sets']} sets × {row['Reps']} reps)")
        with col2:
            done = st.checkbox("Done", key=f"done_{idx}")
            completed.append(done)
        with col3:
            actual_wt = st.text_input("Weight Used", value=row['Wt'], key=f"wt_{idx}")
            
    submit_btn = st.form_submit_button("💾 Save Workout Log")
    if submit_btn:
        st.success("🎉 Workout logged successfully! Your progress is saved for this session.")

st.markdown("---")
st.markdown("### 🥗 Daily Nutrition & Macro Targets (~2,800 kcal)")
col_n1, col_n2, col_n3 = st.columns(3)
with col_n1:
    st.info("**Protein:** 200g")
with col_n2:
    st.warning("**Carbohydrates:** 315g (Leg Day: 355g | Rest: 220g)")
with col_n3:
    st.success("**Fat:** 80g (Rest: 100g)")
