import cv2
import pytesseract

# If Tesseract not detected, uncomment below line and set path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

if __name__ == "__main__":
    path = input("Enter image path: ")
    result = extract_text(path)

    print("\nExtracted Text:\n")
    print(result)
