# 오늘의 파이썬
[Reference](https://dacon.io/competitions/open/235698/overview/description)

## 결측치 보간법과 랜덤포레스트로 따릉이 데이터 예측하기
---
### 전처리 (Data Preprocessing)
1. `df.fillna({col_name: df[col_name].mean()}, inplace=True)` - `col_name` 피쳐의 결측치를 평균값으로 대체
2. `df.interpolate(inplace=True)` - 데이터 결측치를 보간법으로 대체
    - 보간: **이전 행** 피쳐와 **다음 행** 피쳐의 "평균"
    - 시계열 데이터의 경우 Row 순서가 시간 순서이므로 보간법은 합리적인 대체 방법일 수 있다.

### 모델링 (Modeling)
(머신러닝) 모델을 훈련시키고, 훈련된 모델로 예측하는 단계

#### 랜덤 포레스트 (Random Forest)
여러 개의 의사결정나무를 만들고, 이들의 평균을 내어 예측 성능을 높이는 **앙상블 (Ensemble)** 기법
1. 주어진 하나의 데이터로부터 여러 개의 랜덤 데이터셋을 추출한다.
2. 각 랜덤 데이터셋을 각 모델에 적용하여 학습시킨다.

1. `from sklearn.ensemble import RandomForestRegressor` - `scikit-learn` 라이브러리 활용하기
2. `model = RandomForestRegressor(criterion='mse')` - 평가 척도를 `MSE`로 설정하여 모델 선언
    - MSE (Mean Squared Error)
    - RMSE (Root Mean Squared Error)
3. `model.fit(X_train, Y_train)` - 모델 학습

### 튜닝 (Tuning)
#### 불필요 피쳐 제거
1. `model.feature_importances_`: 학습된 모델이 예측 변수를 결정할 때 각 피쳐의 중요도
    - 중요도가 낮은 피쳐는 제거하는 것이 모델의 성능을 향상시킬 수 있음
2. `X_train = train.drop(['count', 'id', 'hour_bef_pm2.5'], axis=1)`
    - `id`: 예측에 의미 없는 피쳐
    - `hour_bef_pm2.5`: 미세먼지 농도

#### 하이퍼파라미터 튜닝 (Hyper-parameter Tuning)
의사결정나무의 **정지 규칙 (Stopping criteria) 값**을 조절하여 최대 성능을 만드는 방식
1. 최대 깊이 `max_depth`
    - 루트 노드로부터 내려갈 수 있는 최대 깊이로, 작게 값을 설정할수록 트리가 작아진다.
2. 최소 노드 크기 `min_samples_split`
    - 노드를 분할하기 위한 최소 데이터 수로, 작게 값을 설정할수록 트리는 커진다.
3. 최소 향상도 `min_impurity_decrease`
    - 노드를 분할하기 위한 최소 향상도로, 작게 값을 설정할수록 트리는 커진다.
4. 비용 복잡도 `cost-complexity`
    - 트리의 확장에 대해 페널티를 부여하여, 불순도와 트리 확장의 복잡도 계산

#### Grid Search
주어진 파라미터 리스트의 조합에 대해 완전 탐색 (Exhaustive Search)를 적용하여 가능한 모든 경우의 수 중 최적 조합을 찾는다.

시간이 매우 오래 걸릴 수 있다.

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

train.interpolate(inplace = True)
test.fillna(0, inplace = True)

X_train = train.drop(['count', 'id', 'hour_bef_pm2.5'], axis=1)
Y_train = train['count']
test = test.drop(['id', 'hour_bef_pm2.5'], axis=1)

model = RandomForestRegressor(
    criterion = 'squared_error', random_state = 2020
)

params = {
    'n_estimators': [200, 300, 500],
    'max_features': [5, 6, 8],
    'min_samples_leaf': [1, 3, 5]
}

greedy_cv = GridSearchCV(
    model, param_grid = params, cv = 3, n_jobs = -1
)
greedy_cv.fit(X_train, Y_train)

pred = greedy_cv.predict(test)

```

