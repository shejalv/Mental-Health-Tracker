import cv2
from emotion_detector import detect_emotion
from database_handler import log_emotion
from tensorflow import keras


def main():
    # Load face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Detect emotion for the face
            emotion = detect_emotion(frame[y:y+h, x:x+w])
            print(f"Detected Emotion: {emotion}")

            # Log the emotion to the database
            log_emotion(emotion)

        cv2.imshow('Mental Health Tracker', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
