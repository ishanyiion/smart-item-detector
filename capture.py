import cv2
import os

name = input("Enter product name: ").strip().lower()

folder = f"dataset/images/{name}"
os.makedirs(folder, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

print("Press SPACE to capture, ESC to quit")

while True:
    ret, frame = cap.read()
    cv2.imshow("Capture Product", frame)

    key = cv2.waitKey(1)

    if key == 27:   # ESC
        break

    if key == 32:   # SPACE
        count += 1
        path = f"{folder}/{name}_{count}.jpg"
        cv2.imwrite(path, frame)
        print("Saved:", path)

cap.release()
cv2.destroyAllWindows()
