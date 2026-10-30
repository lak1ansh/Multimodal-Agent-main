import time
import random

# We are simulating the data inputs for now to build the logic.
# Later, you can connect this directly to your vision and audio scripts!

def calculate_engagement(people_present, audio_level):
    """
    Fuses Vision and Audio data to create an Engagement Score.
    """
    score = 50 # Base score
    
    # Vision Logic: More people usually means higher baseline engagement
    if people_present > 0:
        score += 20
    if people_present > 5:
        score += 10
        
    # Audio Logic: Talking implies interaction, but too much noise could be distraction
    if audio_level == "High":
        score += 30
    elif audio_level == "Low":
        score -= 20
        
    # Cap the score between 0 and 100
    score = max(0, min(100, score))
    return score

def generate_teaching_suggestion(score):
    """
    The AI Agent's Recommendation Engine.
    """
    if score >= 80:
        return "Excellent engagement! The class is highly interactive. Keep up the current pace."
    elif score >= 50:
        return "Moderate engagement. Consider asking the class an open-ended question to wake them up."
    else:
        return "Low engagement detected! The class seems distracted or tired. Suggest a 2-minute stretch break or a group activity."

# --- SIMULATE A CLASSROOM SESSION ---
print("🤖 AI Agent Started. Simulating classroom session...")
print("-" * 50)

# Simulating a timeline (e.g., 3 checks during a class)
time_intervals = ["15 mins", "30 mins", "45 mins"]

for interval in time_intervals:
    # Simulate our modules picking up data
    # In reality, this would come from vision_module.py and audio_module.py
    simulated_people = random.randint(0, 8) 
    simulated_audio = random.choice(["High", "Low"])
    
    print(f"⏱️ Time: {interval}")
    print(f"👁️ Vision: {simulated_people} people detected.")
    print(f"👂 Audio: {simulated_audio} activity.")
    
    # 1. Calculate Score
    engagement_score = calculate_engagement(simulated_people, simulated_audio)
    print(f"📊 Engagement Score: {engagement_score}/100")
    
    # 2. Get AI Suggestion
    suggestion = generate_teaching_suggestion(engagement_score)
    print(f"💡 AI Suggestion: {suggestion}")
    
    print("-" * 50)
    time.sleep(2) # Wait 2 seconds before the next check