# 오늘의 파이썬
[Reference](https://dacon.io/competitions/open/235698/overview/description)

## 교차검증과 앙상블 모델을 활용한 와인 품질 분류하기
---
### Modeling
#### XGBoost (Extreme Gradient Boosting)
Gradient Boosting 알고리즘을 병렬 학습이 지원되도록 구현한 라이브러리이다. 
- Regression과 Classification 문제를 모두 지원한다.
- 병렬 처리로 기존 모델 대비 빠른 수행시간
- 성능과 자원 효율 향상
- 과적합 규제
- 결측치를 내부적으로 처리
- 다양한 옵션으로 Customizing할 수 있다
- Early Stoppping 기능


**Boosting** 성능이 높지 않은 여러 개의 모델을 조합해서 사용하는 앙상블 기법 중 하나
- 성능이 낮은 예측 모형들의 학습 에러에 가중치를 둔다.
- 순차적으로 다음 학습 모델에 반영하여 강한 예측 모형을 만든다.

```python
!pip install xgboost
from xgboost import XGBClassifier

train_one = pd.get_dummies(train)
test_one = pd.get_dummies(test)

model = XGBClassifier()

X = train_one.drop('quality', axis = 1)
y = train_one['quality']
model.fit(X,y)

pred = model.predict(test_one)
```

#### LGBM (Light Gradient Boosting Machine)
GBM (Gradient Boosting Machine)은 오답에 가중치를 경사하강법으로 더하면서 학습을 진행한다. XGBoost는 GBM의 단점을 보완하였지만 여전히 느린 속도를 보인다.

기존 Boosting 모델은 트리를 level-wise하게 확장하지만, LGBM은 leaf-wise하게 확장한다.
- 장점
    - 대용량 데이터 처리
    - 효율적인 메모리 사용
    - 빠른 속도
    - GPU 지원
- 단점
    - leaf-wise 방식으로 인해 과적합 가능성
    - 데이터의 양이 적을 경우 사용 자제

```python
!pip install lightgbm
from lightgbm import LGBMClassifier

train_one = pd.get_dummies(train)
test_one = pd.get_dummies(test)

model = LGBMClassifier()

X = train_one.drop('quality',axis= 1)
y = train_one['quality']
model.fit(X,y)

pred = model.predict(test_one)
```

#### Stratified K-fold
K-fold Cross Validation: 학습 데이터셋을 `학습 데이터`와 `검증 데이터`로 나눈 뒤, 반복해서 검증 및 평가하는 방식 

**문제점**
- Label의 비율이 일정하지 않게 데이터에 들어갈 수 있다.
- `0, 1, 2` 세 가지 레이블이 있을 때 `0, 1`만 가지고 있는 데이터가 발생할 수 있다.

Stratified K-fold는 레이블의 비율을 일정하게 유지한 상태에서 교차 검증을 수행할 수 있도록 한다.

```python
from lightgbm import LGBMClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

skf = StratifiedKFold(n_splits = 5)

train_one = pd.get_dummies(train)
test_one = pd.get_dummies(test)

X = train_one.drop('quality',axis = 1)
y = train_one['quality']

for train_idx, valid_idx in skf.split(X, y):
    train_data = train_one.iloc[train_idx]
    valid_data = train_one.iloc[valid_idx]

    model = LGBMClassifier()

    train_X = train_data.drop(['quality'], axis=1)
    train_y = train_data['quality']

    model.fit(train_X, train_y)

    valid_X = valid_data.drop('quality',axis = 1)
    valid_y = valid_data['quality']

    pred = model.predict(valid_X)


    print(f"{cnt}번째 모델 정확도: {accuracy_score(pred, valid_y)}")
    acc += accuracy_score(pred, valid_y)
    cnt += 1

print(f'모델 정확도 평균: {acc/5}')
```

#### Voting Classifier
여러 개의 모델을 결합하여 더 좋은 예측 결과를 도출하는 앙상블 기법
- Hard voting (Majority voting): 각 모델의 예측을 모아 다수결 투표로 최종 예측 결과를 선정
- Soft voting (Probability voting): 각 모델의 예측 결과값의 확률을 합산하여 최종 예측 결과를 선정
    - 높은 확률값을 반환하는 모델의 비중을 고려할 수 있어 Hard voting보다 성능이 더 좋은 편이다.

```python
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

LGBM = LGBMClassifier()
XGB = XGBClassifier()
RF = RandomForestClassifier()

train_one = pd.get_dummies(train)
test_one = pd.get_dummies(test)

X = train_one.drop('quality', axis = 1)
y = train_one['quality']

VC = VotingClassifier(estimators = [
    ('rf', RF), ('xgb', XGB), ('lgbm', LGBM)
], voting = 'soft')
VC.fit(X,y)

pred = VC.predict(test_one)
```

### Tuning
#### Bayesian Optimization
사전 지식(실험 결과)을 반영해가며 하이퍼파라미터를 탐색한다. 현재까지 얻은 모델 파라미터와 추가적인 실험 정보를 통해, 데이터가 주어졌을 때 모델 성능이 가장 좋을 확률이 높은 파라미터를 찾는다.

```python
!pip install bayesian-optimization
from bayes_opt import BayesianOptimization
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import accuracy_score

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# Scaling
# Encoding

X = train.drop(columns = ['index', 'quality'])
y = train['quality']

rf_parameter_bounds = {
    'max_depth' : (1, 3),
    'n_estimators' : (30, 100)
}

def rf_bo(max_depth, n_estimators):
    rf_params = {
        'max_depth': int(round(max_depth)),
        'n_estimators': int(round(n_estimators))      
    }
    rf = RandomForestClassifier(**rf_params)

    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size = .2)

    rf.fit(X_train,y_train)
    score = accuracy_score(y_valid, rf.predict(X_valid))

    return score

BO_rf = BayesianOptimization(f = rf_bo, pbounds = rf_parameter_bounds, random_state = 0)
BO_rf.maximize(init_points = 5, n_iter = 5)

BO_rf_tuned = RandomForestClassifier(**max_params)
```

#### XGBoost Tuning
```python
from xgboost import XGBClassifier

# Scaling and Encoding

xgb_parameter_bounds = {
    'gamma': (0, 10),
    'max_depth': (1, 3),
    'subsample': (.5, 1)
}

def xgb_bo(gamma,max_depth, subsample):
    xgb_params = {
        'gamma' : int(round(gamma)),
        'max_depth' : int(round(max_depth)),
        'subsample' : int(round(subsample)),      
    }
    xgb = XGBClassifier(**xgb_params)

    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size = .2)

    xgb.fit(X_train, y_train)
    score = accuracy_score(y_valid, xgb.predict(X_valid))

    return score

BO_xgb = BayesianOptimization(f = xgb_bo, pbounds = xgb_parameter_bounds, random_state = 0)
BO_xgb.maximize(init_points = 5, n_iter = 5)

xgb_tune = XGBClassifier(gamma = 4.376, max_depth = 3, subsample = 0.9818)
xgb_tune.fit(X, y)
pred = xgb_tune.predict(test.drop(columns = ['index']))
```

#### LGBM Tuning
```python
from lightgbm import LGBMClassifier

lgbm_parameter_bounds = {
    'n_estimators' : (30, 100),
    'max_depth' : (1, 3),
    'subsample' : (0.5, 1)
}

def lgbm_bo(n_estimators,max_depth, subsample):
    lgbm_params = {
        'n_estimators' : int(round(n_estimators)),
        'max_depth' : int(round(max_depth)),
        'subsample' : int(round(subsample))    
    }
    lgbm = LGBMClassifier(**lgbm_params)

    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size = .2)

    lgbm.fit(X_train, y_train)
    score = accuracy_score(y_valid, lgbm.predict(X_valid))

    return score

BO_lgbm = BayesianOptimization(f = lgbm_bo, pbounds = lgbm_parameter_bounds, random_state = 0)
BO_lgbm.maximize(init_points = 5, n_iter = 5)

lgbm_tune = LGBMClassifier(n_estimators = 43, max_depth = 3, subsample = 1)
lgbm_tune.fit(X, y)
pred = lgbm_tune.predict(test.drop(columns = ['index']))
```

#### Voting Classifier
```python
LGBM = LGBMClassifier(max_depth = 2.09,n_estimators = 60, subsample = 0.8229)
XGB = XGBClassifier(gamma =  4.376, max_depth = 2.784, subsample = 0.9818)
RF = RandomForestClassifier(max_depth = 3.0, n_estimators = 35.31)

# VotingClassifier 정의
VC = VotingClassifier(estimators=[('rf', RF),('xgb', XGB),('lgbm', LGBM)], voting = 'soft')

X = train_one.drop('quality',axis= 1)
y = train_one['quality']
VC.fit(X,y)

pred = VC.predict(test_one)
```