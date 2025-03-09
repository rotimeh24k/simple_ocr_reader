import pytesseract
from PIL import Image
import cv2
import numpy as np

def perform_ocr_tesseract(image):
    try:
        # 2. pytesseract를 사용하여 OCR 수행
        recognized_text = pytesseract.image_to_string(image, lang='kor+eng') # 한국어와 영어 인식 설정

        return recognized_text

    except Exception as e:
        print(f"TesseractOCR 오류 발생: {e}")
        return None