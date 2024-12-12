from deepface import DeepFace 

def detect_emotion(face_image):
    try:
        # Analyze emotion from the given face image
        result = DeepFace.analyze(face_image, actions=['emotion'], enforce_detection=False)
        
        # Extract the dominant emotion from the result
        dominant_emotion = result[0]['dominant_emotion']  # Since result is a list
        return dominant_emotion
    except Exception as e:
        # Catch any exception and print it
        print(f"Error detecting emotion: {e}")
        return "Unknown"
