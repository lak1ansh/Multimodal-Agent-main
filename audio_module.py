import sounddevice as sd
import numpy as np

def check_audio_activity(duration=2):
    print(f"Listening for {duration} seconds... Please speak or make a noise.")
    
    # Record audio for the specified duration at 44100 Hz
    try:
        recording = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
        sd.wait() # Wait until recording is finished
    except Exception as e:
        print(f"Error accessing microphone: {e}")
        return None

    # Calculate the Root Mean Square (RMS) to find the average volume
    rms = np.sqrt(np.mean(recording**2))
    
    # Print the raw value so we can see what a "loud" vs "quiet" room looks like
    print(f"Calculated Volume (RMS): {rms:.4f}")
    
    # Determine engagement based on volume
    # Note: You might need to adjust these numbers based on your microphone sensitivity!
    if rms > 0.02:
        print("🔊 High Interaction detected (Talking/Noise).")
        return "High"
    else:
        print("🤫 Low Interaction detected (Silence/Inactivity).")
        return "Low"

# Run the function
if __name__ == "__main__":
    activity_level = check_audio_activity()