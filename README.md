# OCR_READER

이 프로젝트는 다양한 OCR(Optical Character Recognition) 모델을 설치하고 테스트하여 성능을 비교하고, PaddleOCR의 파인튜닝을 수행하며, Streamlit을 활용한 간단한 OCR 테스트가 가능한 UI를 구현하였습니다.

## 프로젝트 구성

1. **OCR 모델 설치 및 테스트**

   - Tesseract OCR, EasyOCR, PaddleOCR 등의 OCR 모델을 설치하고 기본적인 테스트를 수행하였습니다.

2. **OCR 모델 성능 비교**

   - 각 모델의 인식 정확도, 처리 속도 등을 비교하여 최적의 모델을 선정하였습니다.

3. **PaddleOCR 파인튜닝**

   - 선정된 PaddleOCR 모델을 특정 데이터셋에 맞게 파인튜닝하여 성능을 향상시켰습니다.

4. **Streamlit을 활용한 OCR 실험 화면 구현**
   - Streamlit을 사용하여 OCR 실험 인터페이스를 개발하였습니다.

## 설치 및 실행 방법

1. **필요한 라이브러리 설치**

   ```bash
   pip install -r requirements.txt

   ```

2. **Streamlit 애플리케이션 실행**
   ```bash
   streamlit run app.py
   ```

## 파일 구조

├── app.py # Streamlit 애플리케이션 메인 파일
├── requirements.txt # 필요한 라이브러리 목록
├── models/ # OCR 모델 관련 파일
├── data/ # 테스트 데이터셋
└── README.md # 프로젝트 설명서
