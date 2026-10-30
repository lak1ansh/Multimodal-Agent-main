import streamlit as st
import pandas as pd
import time
import random

# --- Page Configuration ---
st.set_page_config(page_title="Attendance & Engagement Agent", page_icon="🎓", layout="wide")

st.title("🎓 Multimodal Attendance & Engagement Agent")
st.markdown("An AI-powered, privacy-preserving classroom intelligence system.")

# Create two columns for the layout
col1, col2 = st.columns(2)

# --- LEFT COLUMN: VISION (Attendance) ---
with col1:
    st.header("👁️ Vision Module (Attendance)")
    st.write("Sustained presence detection (2+ seconds).")
    
    if st.button("📷 Start Camera & Log Attendance"):
        st.info("Camera simulated! In your final version, this will open OpenCV.")
        
        # Simulating the CSV data your vision_module creates
        mock_data = {
            "Student ID": ["Student_1", "Student_2", "Student_3"],
            "Timestamp": [
                time.strftime("%Y-%m-%d %H:%M:%S"),
                time.strftime("%Y-%m-%d %H:%M:%S"),
                time.strftime("%Y-%m-%d %H:%M:%S")
            ]
        }
        df = pd.DataFrame(mock_data)
        st.dataframe(df, use_container_width=True)
        st.success("Attendance saved to CSV!")

# --- RIGHT COLUMN: AUDIO & AI (Engagement) ---
with col2:
    st.header("👂 Audio & AI Agent")
    st.write("Analyzes classroom dynamics to generate teaching suggestions.")
    
    if st.button("🎙️ Analyze Current Engagement"):
        with st.spinner("Listening to classroom and analyzing..."):
            time.sleep(1.5) # Fake loading time
            
            # Simulate real data
            simulated_people = random.randint(1, 10)
            simulated_audio = random.choice(["High", "Low"])
            
            # Logic from ai_agent.py
            score = 50
            if simulated_people > 0: score += 20
            if simulated_people > 5: score += 10
            if simulated_audio == "High": score += 30
            elif simulated_audio == "Low": score -= 20
            score = max(0, min(100, score))
            
            # Display Metrics
            st.metric(label="Engagement Score", value=f"{score}/100", delta=f"{simulated_audio} Audio")
            
            # Display AI Suggestion
            if score >= 80:
                st.success("💡 **AI Suggestion:** Excellent engagement! The class is highly interactive. Keep up the current pace.")
            elif score >= 50:
                st.warning("💡 **AI Suggestion:** Moderate engagement. Consider asking the class an open-ended question to wake them up.")
            else:
                st.error("💡 **AI Suggestion:** Low engagement detected! The class seems distracted or tired. Suggest a 2-minute stretch break.")

# --- BOTTOM SECTION: ARCHITECTURE ---
st.divider()
st.header("🛠️ System Architecture")
st.markdown("""
*   **Vision:** OpenCV (Haar Cascades) for sustained face detection.
*   **Audio:** SoundDevice & Numpy for RMS volume analysis.
*   **AI Agent:** Rule-based fusion engine for engagement scoring.
*   **Privacy:** 100% Offline. No data leaves the local machine.
""")