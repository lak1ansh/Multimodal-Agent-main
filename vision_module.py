import cv2
import csv
import time
import os

# 1. Load the pre-trained face detector that comes with OpenCV
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. Start the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0) 

# A dictionary to keep track of who has been marked present
attendance_log = {}

# A dictionary to track how long a face has been continuously seen (Sustained Presence)
# We will use simple face IDs for now to get it working
presence_timers = {}

print("Camera starting... Press 'q' to quit.")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert the image to grayscale (face detection works better in gray)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    current_time = time.time()

    # Loop through every face found in the frame
    for i, (x, y, w, h) in enumerate(faces):
        # Draw a blue rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # For simplicity in this MVP (Minimum Viable Product), we identify faces by their position
        # In the future, we would use facial recognition (like DeepSORT) to give them real names
        face_id = f"Student_{i+1}" 
        
        # --- SUSTAINED PRESENCE LOGIC ---
        if face_id not in presence_timers:
            # First time seeing this face in this session
            presence_timers[face_id] = current_time
        else:
            # Calculate how long we have seen this face
            time_seen = current_time - presence_timers[face_id]
            
            # If seen for more than 2 seconds, mark attendance
            if time_seen > 2.0 and face_id not in attendance_log:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                attendance_log[face_id] = timestamp
                print(f"✅ Attendance marked for {face_id} at {timestamp}")
                
                # Save to CSV immediately
                file_exists = os.path.isfile('attendance.csv')
                with open('attendance.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    if not file_exists:
                        writer.writerow(['Student ID', 'Timestamp']) # Header
                    writer.writerow([face_id, timestamp])

    # Show the video feed
    cv2.imshow('Attendance Camera', frame)

    # Press 'q' to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()