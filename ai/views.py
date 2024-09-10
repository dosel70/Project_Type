import os

import joblib
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from sklearn.preprocessing import StandardScaler

# Django 프로젝트의 BASE_DIR에서 모델 파일 경로 설정
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ai/portpolio1.pkl')

# joblib으로 모델 로드
model = joblib.load(MODEL_PATH)



# 숫자인지 확인하는 함수
def is_number(value):
    try:
        float(value)  # 숫자 여부를 float으로 체크
        return True
    except ValueError:
        return False

# 정수인지 확인하는 함수
def is_integer(value):
    try:
        int(value)  # 정수 여부를 int로 체크
        return True
    except ValueError:
        return False

class AiMainView(View):
    def get(self, request):
        print("AI 들어옴")
        return render(request, 'manufact/manufact.html')

class ManufactView(View):
    def get(self, request):
        print("ManufactView 들어옴")
        return render(request, 'manufact/manufactSub.html')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 모델 로드
        self.model = joblib.load(MODEL_PATH)

    def post(self, request):
        data = request.POST
        tem_x_press = data.get('tem_x_press', '').strip()
        conversion_index = data.get('conversion_index', '').strip()

        # 입력 값이 숫자인지 확인
        if not is_number(tem_x_press):
            return JsonResponse({'error': 'Temperature x Pressure 값에 숫자를 입력해주세요.'})

        if not is_number(conversion_index):
            return JsonResponse({'error': 'Material Conversion Index 값에 숫자를 입력해주세요.'})

        try:
            Temperature_x_Pressure = float(tem_x_press)
            Material_Transformation_Metric = float(conversion_index)

            # 모델 예측
            features = [[Temperature_x_Pressure, Material_Transformation_Metric]]
            Quality_Rating = self.model.predict(features)[0]

            # 예측 결과를 세션에 저장
            request.session['quality_score'] = Quality_Rating

            # ManufactResultView로 리다이렉트
            return redirect('ai:manufact-result')  # URL 패턴 이름

        except ValueError as e:
            return JsonResponse({'error': f'입력값을 처리하는 데 오류가 발생했습니다: {str(e)}'})

class ManufactResultView(View) :
    def get(self, request):
        # 세션에서 예측 점수 가져오기
        quality_score = request.session.get('quality_score', 0)  # 기본값을 0으로 설정
        if quality_score <= 0.39363 and quality_score > 0.37449:
            score = "좋음"
        elif quality_score <= 0.37449 and quality_score > 0.35185 :
            score = "평균"
        else :
            score = "나쁨"

        # 템플릿에 점수 전달
        return render(request, 'manufact/manufactResult.html', {'quality_score': quality_score, 'score': score})

class AlzhimeraView(View):
    def get(self, request):
        return render(request, 'alzhimer/alz.html')