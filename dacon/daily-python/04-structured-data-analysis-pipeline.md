# 오늘의 파이썬
[Reference](https://dacon.io/competitions/open/235698/overview/description)

## 정형 데이터 분석 파이프라인
---
### 탐색적 데이터 분석, EDA
처음 데이터를 수집하였을 때 다양한 각도에서 관찰하고 이해하는 과정. 데이터를 이해하고 파악해야 목적에 맞게 데이터를 정제하고, 새로운 인사이트를 도출할 수 있다.
- 라이브러리 및 파일 불러오기 `import, pd.read_csv()`
- 행/열 갯수 관찰하기 `df.shape`
- 데이터 확인하기 `df.head()`
- 결측치 유무 확인하기 `df.isnull().sum(), df.info()`
- 수치 데이터 특성 보기 `df.describe()`

### 데이터 전처리
분석 결과 및 인사이트와 모델 성능에 직접적인 영향을 미치는 데이터 분석 파이프라인에서 가장 중요한 과정.
- 결측치 다루기 `df.dropna(), df.fillna(), df.interpolate()`
- 이상치 다루기 `sns.boxplot(), IQR`
- 정규화 및 인코딩 `MinMaxScaler(), OneHotEncoder()`

### 머신러닝 모델링
모델을 정의하고 학습 데이터로 모델을 학습시키는 과정.

모델
- 트리 기반의 Decision Tree
- 앙상블 모델인 Random Forest, XGBoost, LGBM, Voting Classifier

검증
- K-fold
- Stratified K-Fold

### 모델 튜닝
모델에 존재하는 여러가지 파라미터의 최적값을 찾는 과정
- GridSearch, Bayesian Optimization