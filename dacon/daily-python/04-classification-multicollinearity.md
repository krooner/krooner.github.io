# 오늘의 파이썬
[Reference](https://dacon.io/competitions/open/235698/overview/description)

## 교차검증과 앙상블 모델을 활용한 와인 품질 분류하기
---
### EDA using `seaborn`
#### Pairplot
2차원 이상의 데이터에 들어 있는 모든 피쳐 간의 상관관계를 얻는다. Grid 형태로 각 조합에 대한 히스토그램과 분포도를 그린다.

```python
import seaborn as sns
import pandas as pd

train = pd.read_csv("data/train.csv")

data = train.loc[:, 'fixed acidity' : 'chlorides']
sns.pairplot(data)
```

#### Distplot
데이터의 히스토그램을 그려주는 함수로, 수치형 데이터의 분포를 정확히 표현한다. 변수를 여러 개의 bin으로 나눈 뒤 bin 당 관측 수를 막대 그래프로 표현한다.

```python
data = train['fixed acidity']
sns.distplot(data, bins = 100)
```

#### Multi-collinearity (다중공선성)
상관관계가 높은 독립변수들이 동시에 모델에 포함될 때 발생한다. 두 변수가 완벽한 Multi-collinearity를 갖는다면, 사실상 동일한 변수를 두 번 넣은 것이므로 모델이 결과값을 추론하는데 방해가 된다.

예 - 매출에 대한 피쳐들
- 매출을 설명하는 `TV`의 변동성
- 매출을 설명하는 `Radio`의 변동성
- 매출을 설명하는 `Newspaper`의 변동성

각 피쳐의 변동성이 중복되게 되고 (Multi-collinearity), 잘못된 변수 해석과 예측 정확도 하락을 야기한다.

**확인 방법**
1. Heatmap
2. Scatterplot
3. VIF (Variance Inflation Factors, 분산 팽창 요인)

#### Heatmap
두 개의 카테고리 변수에 대한 반응 변수의 크기를 색깔 변화로 표현한 것으로, 변수별 상관관계를 확인할 때 주로 사용된다.

`.corr()` 함수는 데이터에 포함된 변수 간 상관도를 출력하는 함수이다.

```python
data = train.corr()
sns.heatmap(data)
```

#### Scatterplot
두 개의 연속형 변수에 대한 관계를 파악하는데 유용하게 사용된다.

```python
x_data = train['residual sugar']
y_data = train['density']

sns.scatterplot(x_data, y_data)
```

#### VIF (Variance Inflation Factors)
분산팽창요인은 변수 간의 Multicollinearity를 진단하는 수치이며 [1, infinity)의 범위를 갖는다. 통계학에서는 VIF가 10 이상인 경우 다중공선성을 갖는 것으로 판단한다.

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

train.drop('type', inplace = True, axis = 1)

vlist = []
train_values = train.values

for i in range(len(train.columns)):
    vlist.append(
        vif(train_values, i)
    )

vdf = pd.DataFrame()
vdf['columns'] = train.columns
vdf['VIF'] = vlist
```

### 전처리 - Remove Multicollinearity 
#### 변수 정규화
수치형 데이터를 `Min Max Scaling`이나 `Z-score Scaling` 등으로 정규화 시킨다.

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
from sklearn.preprocessing import MinMaxScaler

vdf = pd.DataFrame()
vdf["VIF factor"] = [
    vif(train.values, i) for i in range(train.shape[1])
]
vdf["Features"] = train.columns

scaler = MinMaxScaler()
scaler.fit(train)
train_scale = scaler.transform(train)

new_train = pd.DataFrame(train_scale)
new_train.columns = train.columns

vdf_scale = pd.DataFrame()
vdf_scale["VIF factor"] = [
    vif(new_train.values, i) for i in range(new_train.shape[1])
]
vdf_scale["Features"] = new_train.columns
```

#### 변수 제거
종속 변수인 `quality` 피쳐를 제외한, VIF 값이 10 이상인 변수를 제거한다.

```python
new_train = train.drop(['fixed acidity', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'], axis=1)

newdf = pd.DataFrame(new_train)
newdf.columns = new_train.columns

vdf_drop = pd.DataFrame()
vdf_drp[["VIF factor"] = [
    vif(new_train.values, i) for i in range(new_train.shape[1])
]
vdf_drop["Features"] = new_train.columns
```

#### PCA (Principal Component Analysis, 주성분 분석
여러 변수 간에 존재하는 상관관계를 이용하여, 이를 대표하는 주성분을 추출하는 차원 축소 기법. 

**차원 축소**: 많은 피쳐로 구성된 다차원 데이터셋의 차원을 축소하여 새로운 차원의 데이터셋을 생성하는 것이다. 3차원 이하의 차원 축소를 통해 압축된 데이터를 시각화할 수 있고, 학습 데이터 크기가 감소하여 학습 데이터 처리 능력도 향상된다.
1. Feature Selection: 특정 피쳐에 종속성이 강한, 불필요한 피쳐를 제거하여 데이터 특징을 잘 나타내는 주요 피쳐만 선택한다.
2. Feature Extraction: 기존 피쳐를 저차원의 다른 공간으로 매핑하여 추출하며, 기존 피쳐와는 완전히 다른 값이 된다.

**차원 증가의 문제점**
1. 데이터 포인트 간의 거리가 멀어져 Sparse한 구조를 갖게 되고, 이러한 경우 상대적으로 적은 차원에서 학습된 모델보다 예측 신뢰도가 낮을 수 있다.
2. 대다수의 피쳐 간의 상관관계가 높을 가능성이 크고, 결국 Multicollinearity 문제로 예측 성능이 떨어진다. 
3. 피쳐가 너무 많아 시각화 또한 어렵다.

PCA
1. 기존 데이터 정보 유실을 최소화하기 위해 가장 높은 분산을 가지는 데이터 축을 찾는다.
2. 새로운 축으로 데이터를 투영한다.
3. 새로운 기준으로 데이터를 표현한다.
4. 새로운 축에 직각이 되는 축을 두 번째 축으로 삼는다.
5. 두 번째 축에 직각이 되는 축을 세 번쨰 축으로 삼는다.

즉, 축의 갯수만큼을 차원으로 갖는 데이터로 원본 데이터가 축소된다.

```python
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import pandas as pd

iris = load_iris()

df = pd.DataFrame(iris.data)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df['target'] = iris.target

df_features = df[['sepal_length','sepal_width','petal_length','petal_width']]
df_scaler = MinMaxScaler().fit_transform(df_features)

pca = PCA(n_components = 2)
pca.fit(df_scaler)

df_pca = pca.transform(df_scaler)
df_pca = pd.DataFrame(df_pca)
df_pca.columns = ['PCA_1', 'PCA_2']
df_pca['target'] = df.target
```

#### 연속형 변수 변환
머신러닝 모델링 과정에서, 제한된 변수로 성능을 향상시키는 건 한계가 존재한다.
1. 어떻게 데이터를 증강시킬 것인가?
    - 정형 데이터의 경우 데이터 증강은 제한적이다
2. **어떤 파생 변수를 추가할 것인가?**
    - 연속형 변수를 범주형 변수로 변환할 수 있다

**수치 범위 구간을 직접 지정하기**: pH 피쳐를 카테고리 변수로 변환하기

```python
def function(x):
  if x < 1:
    return "lowest"
  elif 1<= x < 2:
    return "low"
  elif 2<= x < 3:
    return "normal"
  else:
    return "high"

train['pH'] = train['pH'].apply(function)
```

단점 - 여러 변수에 한번에 적용하기 어렵고, 각 변수에 적합한 범위를 설정하려면 많은 시간이 소요된다.

**Pandas의 `.cut()` 함수로 레이블링 하기**: 학습 데이터의 `alcohol` 변수를 구간이 5개인 범주형 변수로 변환하기

```python
train['alcohol'] = pd.cut(
    train.alcohol, 5, labels = False
)
```

**`Polynomial Features`로 파생 변수 생성 및 모델 학습**

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# 범주형 변수, Index 제거
train.drop(['type', 'index'], axis = 1,inplace = True)
test.drop(['type', 'index'], axis = 1,inplace = True)

poly_features = PolynomialFeatures(degree = 2)
df = train.drop('quality', axis = 1)
df_poly = poly_features.fit_transform(df) 
df_poly = pd.DataFrame(df_poly)

model = DecisionTreeClassifier()
model.fit(df_poly,train['quality'])

poly_features = PolynomialFeatures(degree = 2) 
test_poly = poly_features.fit_transform(test) 
test_poly = pd.DataFrame(test_poly) 

pred = model.predict(test_poly)
```





