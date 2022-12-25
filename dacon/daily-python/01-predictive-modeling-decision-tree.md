# 오늘의 파이썬
[Reference](https://dacon.io/competitions/open/235698/overview/description)

## 의사결정회귀나무로 따릉이 데이터 예측
---
### EDA (Exploratory Data Analysis)
**통계 그래픽과 여러 시각화 기법**을 이용하여 **데이터셋의 주요 특징을 요약**하는 데이터 분석 방식
1. `import pandas as pd` - 라이브러리 불러오기
2. `pd.read_csv(file_dir)` - 파일 불러오기
3. `df.shape()` - 데이터 행/열 갯수 관찰하기
4. `df.head()` - 데이터 확인하기
5. `df.isnull()` - 데이터 결측치 확인하기

### 전처리 (Data Preprocessing)
1. `df.info()` - 데이터 결측치 및 정보 확인하기
2. `df.dropna(), df.fillna(value)` - 데이터 결측치 삭제 및 대체

### 모델링 (Modeling)
(머신러닝) 모델을 훈련시키고, 훈련된 모델로 예측하는 단계

#### 의사결정나무 (Decision Tree)
의사결정 규칙과 그 결과를 트리 구조로 도식화한 의사 결정 지원 도구

EDA를 통해 각 Row는 Col (Feature)를 가지고 있다.
1. **하나의 피쳐**를 정한다.
2. 해당 피쳐의 **특정한 한 개의 값을 기준**으로 삼는다.
3. **기준 값으로 모든 Row를 두 개의 Node로 이진 분할**한다.
    - 이전 단계에서 `N`개의 값을 기준으로 삼는 경우 `N+1`진 분할
    - 대표적인 CART 의사결정 나무는 이진 분할
4. 파생된 두 개의 Node에 대해 **각각 1~3 과정을 반복**한다.

분류될 때는 ~~양쪽이 균등하도록 값을 결정~~ `한쪽 방향으로 쏠리도록` 해주는 특정 값을 찾는다.
1. `import sklearn; from sklearn.tree import DecisionTreeRegressor` - `scikit-learn` 라이브러리 활용하기
2. `model = DecisionTreeRegressor` - 모델 선언하기
3. `model.fit(X_train, Y_train)` - 학습 데이터로 모델 훈련하기
    - `X_train`는 예측에 사용되는 변수들
        - `X_train = train.drop(['count'], axis=1)`
    - `Y_train`는 예측 결과 변수
        - `Y_train = train['count']`
    
4. `prediction = model.predict(test)` - 평가 데이터로 학습된 모델의 예측 결과 출력
5. `submission_df.to_csv("submission.csv", index=False)` - 예측 결과를 csv 파일로 생성



