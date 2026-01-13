from paddleocr import PaddleOCR

print("Starting OCR...")

ocr = PaddleOCR(lang="en")

print("Model Loaded")

result = ocr.predict("test (10).jpeg")   # or test.jpg

for page in result:
    texts = page["rec_texts"]
    scores = page["rec_scores"]

    print("\nDetected Text:")
    for t, s in zip(texts, scores):
        print(f"{t}  ({s:.2f})")
