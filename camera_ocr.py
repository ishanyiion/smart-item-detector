import cv2
from paddleocr import PaddleOCR

print("Loading OCR model...")
ocr = PaddleOCR(lang="en")
print("OCR Ready")

cap = cv2.VideoCapture(0)

last_text = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = ocr.predict(img)

    if result:
        for page in result:
            texts = page["rec_texts"]
            boxes = page["rec_boxes"]

            for text, box in zip(texts, boxes):
                x1, y1, x2, y2 = box

                # Draw box
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

                # Draw text
                cv2.putText(frame, text, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

                # Print new detected product
                if text != last_text:
                    print("Detected:", text)
                    last_text = text

    cv2.imshow("Live OCR", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
