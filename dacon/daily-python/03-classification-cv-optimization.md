# 오늘의 파이썬
[Reference](https://dacon.io/competitions/open/235698/overview/description)

## 교차검증과 랜덤 포레스트를 활용한 와인 품질 분류하기
---
### EDA - Exploratory Data Analysis
**DataFrame 통계 정보**
```python
import pandas as pd

df = pd.read_csv({url}) # 데이터 불러오기
df.info() # 데이터의 피쳐 수 및 이름, 결측치, 데이터 타입 정보
df.shape # 데이터의 행 및 열 갯수
df.head(N) # 데이터의 상위 N개 Row 정보를 출력
df.isnull.sum() # 데이터 결측치 수
df.describe() # 데이터의 다양한 통계량을 요약
```

**데이터 시각화 라이브러리 호출**

```python
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline # Jupyter notebook에서 결과를 출력하도록 설정

import warnings 
warnings.filterwarnings('ignore') # 오류가 아닌 경고 메시지 생략하기
```

**`seaborn, matplotlib`을 활용한 시각화**
```python
train = pd.read_csv("data/train.csv")
train_copy = train.copy()

sns.distplot(train_copy['quality'], kde = False, bins = 10) # 데이터의 품질 피쳐 시각화
plt.axis([0, 10, 0, 2500]) # 축 범위: X 최소, X 최대, Y 최소, Y 최대
plt.title("Wine Quality") # 그래프 제목 설정
plt.show()
```

### 전처리 - Data Preprocessing
#### 이상치 (Outlier) 탐지 및 제거
일반적인 데이터 패턴과 매우 다른 Outlier는 모델의 성능을 떨어뜨린다.

IQR (Inter-quantile range), 사분위 값의 편차를 활용하기 위해 boxplot으로 시각화한다.

```python
import pandas as pd
import numpy as np

train = pd.read_csv("data/train.csv")

sns.boxplot(data = train['fixed acidity']) # 데이터 시각화

quantile_25 = np.quantile(train['fixed acidity'], .25) # 25분위 데이터
quantile_75 = np.quantile(train['fixed acidity'], .75) # 75분위 데이터
IQR = quantile_75 - quantile_25 # 25분위와 75분위 사이 데이터
minimum = quantile_25 - 1.5*IQR
maximum = quantile_75 + 1.5*IQR

train_iqr = train[(minimum < train['fixed acidity']) & (train['fixed acidity'] < maximum)]
```

#### 수치형 데이터 정규화
의사결정나무, 랜덤포레스트 등 `트리 기반 모델`은 대소 비교를 통해 구분하므로 숫자 단위에 영향을 덜 받는다.

Logistic Regression, Lasso 등 `평활 함수 모델`은 숫자의 크기 및 단위에 영향을 많이 받으므로, **수치형 데이터 정규화** 과정에 필요하다.

**Min Max Scaling** - 가장 작은 값은 0, 가장 큰 값은 1로 만들어주는 방법

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler() # scaler를 선언한다.
scaler.fit(train[['fixed acidity']]) # scaler를 해당 피쳐에 대해 학습시킨다.

train['Scaled fixed acidity'] = scaler.transform(train['fixed acidity']) # 데이터 정규화가 적용된 결과를 새로운 피쳐로 지정한다.
```

#### One-hot Encoding
컴퓨터는 문자로 된 데이터를 학습할 수 없다.

카테고리 데이터에 대해 해당 카테고리에 (1, Hot)을 부여하고 나머지에는 (0, Cold)를 부여하여 문자 피쳐를 인코딩한다.

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder() # 인코더 선언
encoder.fit(train[['type']]) # 인코더를 type 피쳐에 대해 학습시킴
onehot = encoder.transform(train[['type']]) # 학습된 인코더로 type 피쳐를 변환함
onehot = pd.DataFrame(onehot.toarray()) # array로 형태로 바꾸고 DataFrame 형태로 만듬
onehot.columns = encoder.get_feature_names()
onehot = pd.concat([train, onehot], axis = 1)

train = train.drop(['type'], axis = 1)
```

### 모델링
#### 랜덤 포레스트 (Random Forest)

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

model = RandomForestClassifier()
X_train = train.drop(['quality'])
Y_train = train['quality']

model.fit(X_train, Y_train)
```

#### 교차 검증 (Cross-Validation)
**Hold-out**: 주어진 데이터를 `train_data`와 `valid_data`로 나눈 작업으로, 보통 `(train, valid)`를 8:2, 7:3 비율로 설정

그러나, `valid_data`는 모델이 학습하지 못하고 예측 용도로만 사용된다 (데이터 낭비)

**K-Fold**: 모든 데이터를 최소한 한 번씩 다 학습하도록, `valid_data`를 서로 겹치지 않게 나눈 N개의 데이터셋으로 적용하는 방식

```python
from sklearn.model_selection import KFold

kf = KFold(n_splits = 5, shuffle = True, random_state = 0)

for train_idx, valid_idx in kf_split(train):
    train_data = train.iloc[train_idx]
    valid_data = train.iloc[valid_idx]
```

#### Hyper-parameter Tuning

||GridSearch|RandomSearch|Bayesian Optimization|
|---|---|---|---|
|**방식**|탐색 값을 지정하고, 모든 조합을 바탕으로 최고점을 찾는다.|탐색 범위를 지정하고, 랜덤으로 조합을 만들어 최고점을 찾는다.|범위를 지정하고, Random하게 R번 탐색 후 B번 만큼 최적값을 찾는다.|
|**장점**|원하는 범위를 정확히 비교 및 분석할 수 있다.|시간이 비교적 빠르고 성능이 더 좋게 나올 수 있다.|시간이 덜 걸리며 `최적값`을 찾아갈 수 있고 신뢰할 수 있는 결과를 얻는다.|
|**단점**|시간이 오래 걸린다. 최고 성능이 아닐 가능성이 높다. 검색일뿐, 탐색은 아니다.|성능이 낮아질 때도 있다. 설정 범위가 너무 넓으면 일반화되지 않는다. `seed`를 고정하지 않으면 할 때마다 결과가 다르다.|Random하게 선택한 결과에 따라 시간과 결과가 크게 변화할 수 있다.|

기존 하이퍼파라미터 튜닝 방식 (GridSearch, RandomSearch)의 문제점은 **최적값을 찾아갈 수 없다**는 것이다.

Bayesian Optimization은 **Gaussian Process라는 통계학 기반 모델**로, 여러 개의 하이퍼파라미터에 대해 **Aquisition Function을 적용**하여 가장 큰 값이 나올 확률이 높은 지점을 선택한다.
1. 변경할 하이퍼파라미터의 범위를 설정한다.
2. 범위 내 하이퍼파라미터 값을 랜덤하게 가져온다.
3. 첫 R번 동안 Random하게 값을 꺼내서 성능을 확인한다.
4. 이후 B번 동안은 Bayesian Optimization을 통해 최적값을 찾는다.

```python
!pip install bayesian-optimization
from bayes_opt import BayesianOptimization

X = train.drop(['index', 'quality'])
y = train['quality']

rf_parameter_bounds = {
    'max_depth': (1, 3),
    'n_estimators': (30, 100)
}

def rf_bound(max_depth, n_estimators):
    rf_params = {
        'max_depth': int(round(max_depth)),
        'n_estimators': int(round(n_estimators))
    }
    rf = RandomForestClassifier(**rf_params)

    X_train, X_valid, y_train, y_valid = \
        train_test_split(X, y, test_size = .2)

    rf.fit(X_train, y_train)
    score = accuracy_score(y_valid, rf.predict(X_valid))
    
    return score

borf = BayesianOptimization(
    f = rf_bo, pbounds = rf_parameter_bounds, random_state = 0
)
borf.maximize(init_points = 5, n_iter = 5)

max_params = borf.max['params']
max_params['max_params'] = int(max_params['max_depth'])
max_params['n_estimators'] = int(max_params['n_estimators'])

borf_tuned = RandomForestClassifier(**max_params)
```






