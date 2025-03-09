from paddleocr import PaddleOCR
from PIL import Image

def perform_ocr_paddleocr(image):
    try:
        ocr = PaddleOCR(use_angle_cls=True, lang='korean') #객체 생성
        result = ocr.ocr(image, cls=True)

        recognized_text = ""
        for line in result:
            for word_info in line:
                text, confidence = word_info[1]
                recognized_text += text + "\n"

        return recognized_text

    except Exception as e:
        print(f"paddleocr 오류 발생: {e}") # 오류 메시지 출력 (필요에 따라 로깅 또는 다른 오류 처리 방식 적용)
        return None # 오류 발생 시 None 반환