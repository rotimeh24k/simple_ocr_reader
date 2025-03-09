import easyocr
from PIL import Image 

def perform_ocr_easyocr(image, lang_list=['ko']):
    try:
        reader = easyocr.Reader(lang_list) # EasyOCR Reader 객체 생성 (언어 설정)
        result = reader.readtext(image) # 이미지에서 텍스트 인식

        recognized_text = ""
        for detection in result: # 인식 결과 처리
            text = detection[1] # 인식된 텍스트 추출
            recognized_text += text + "\n" # 줄바꿈 문자와 함께 텍스트 추가

        return recognized_text

    except Exception as e:
        print(f"EasyOCR 오류 발생: {e}") # 오류 메시지 출력 (필요에 따라 로깅 또는 다른 오류 처리 방식 적용)
        return None # 오류 발생 시 None 반환