# 오늘의 파이썬
[Reference](https://dacon.io/competitions/open/235698/overview/description)

## LGBM 모델로 청와대 청원 데이터 분류하기
---
### EDA

```python
import pandas as pd

# 데이터의 3번째 행까지 불러오기
train = pd.read_csv("data/train.csv", nrows = 3)
# 데이터의 2번째 행을 컬럼으로 지정하여 불러오기
train = pd.read_csv("data/train.csv", header = 1)
# 데이터에서 컬럼을 index로 지정하여 불러오기
train = pd.read_csv("data/train.csv", index_col = 'index')
# 데이터에서 결측치를 제외하고 불러오기
train = pd.read_csv("data/train.csv", na_filter = False)
# 데이터에서 뒤에서 5개의 행 제외하고 불러오기
train = pd.read_csv("data/train.csv", skipfooter = 5)
# 데이터의 인코딩 형식에 맞게 불러오기 - 'utf-8' 또는 'cp949'
train = pd.read_csv("data/train.csv", encoding = 'cp949')
# 데이터의 컬럼명을 지정해서 불러오기
train = pd.read_csv("data/train.csv", names = ['col_a', 'col_b', 'col_c'])
# 데이터 저장하기 - 인덱스 제외
train.to_csv("data/train.csv", index = False)
# 데이터에서 category 컬럼의 고유값 갯수 구하기
# index가 고유값, value로 count가 들어간 Series가 Output
train['category'].value_counts()
# 데이터 기본 정보 (행/열 크기, 컬럼 이름, 데이터 타입, 결측치)
train.info()
```

### 전처리
텍스트 데이터 전처리

#### Cleansing, Filtering
- Cleansing: 분석에 방해되는 불필요한 문자 및 기호 제거
- Filtering: 불필요한 단어나 큰 의미가 없는 단어를 Stopword로 설정 후 제거

```python
string = "123,456,789"
# 123456,789
print(string.replace(',', '', 1))
# 123456789 
print(string.replace(',' ,''))
# True
print('a'.isalpha())
# False
print('*'.isalnum())
# True
print('9'.isdecimal())
# \\n 문자열 제거
train['data'] = train['data'].apply(
    lambda x: str(x).replace('\\n', '')
)
```

#### Tokenization
형태소 분석을 통해 문장을 형태소 단위의 토큰으로 분리. 토큰이란 문법적으로 더 이상 나눌 수 없는 기본 요소

```python
!pip install konlpy
from konlpy.tag import Kkma, Komoran, Okt

okt = Okt()
kkm = Kkma()
kom = Komoran()

text = '마음에 꽂힌 칼한자루 보다 마음에 꽂힌 꽃한송이가 더 아파서 잠이 오지 않는다'

kom.pos(text) #[('마음', 'NNG'), ('에', 'JKB'), ('꽂히', 'VV'), ('ㄴ', 'ETM'), ('칼', 'NNG'), ('한자', 'NNP'), ('루', 'JKB'), ('보다', 'MAG'), ('마음', 'NNG'),('에', 'JKB'), ('꽂히', 'VV'), ('ㄴ', 'ETM'), ('꽃', 'NNG'), ('한송이', 'NNP'), ('가', 'JKS'), ('더', 'MAG'), ('아파서', 'NNP'), ('잠', 'NNG'), ('이', 'JKS'), ('오', 'VV'), ('지', 'EC'), ('않', 'VX'), ('는다', 'EC')]

kkm.pos(text) # [('마음', 'NNG'), ('에', 'JKM'), ('꽂히', 'VV'), ('ㄴ', 'ETD'), ('칼', 'NNG'), ('한자', 'NNG'), ('로', 'JKM'), ('보다', 'MAG'), ('마음', 'NNG'), ('에', 'JKM'), ('꽂히', 'VV'), ('ㄴ', 'ETD'), ('꽃', 'NNG'), ('한', 'MDN'), ('송이', 'NNG'), ('가', 'JKS'), ('더', 'MAG'), ('아프', 'VA'), ('아서', 'ECD'), ('잠', 'NNG'), ('이', 'JKS'), ('오', 'VV'), ('지', 'ECD'), ('않', 'VXV'), ('는', 'EPT'), ('다', 'EFN')]

okt.pos(text, norm = True, stem = True) #[('마음', 'Noun'), ('에', 'Josa'), ('꽂히다', 'Verb'), ('칼', 'Noun'), ('한', 'Determiner'), ('자루', 'Noun'), ('보다', 'Verb'), ('마음', 'Noun'), ('에', 'Josa'), ('꽂히다', 'Verb'), ('꽃', 'Noun'), ('한송이', 'Noun'), ('가', 'Josa'), ('더', 'Noun'), ('아프다', 'Adjective'), ('잠', 'Noun'), ('이', 'Josa'), ('오지', 'Noun'), ('않다', 'Verb')]

# 조사 제거하기
def func(text):
  okt_pos = okt.pos(str(text),norm=True, stem=True)
  new_word = ''

  for word, pos in okt_pos:
    if pos != 'Josa': 
      new_word += word
  
  return new_word

train['data'] = train['data'].apply(lambda x : func(x))
test['data'] = test['data'].apply(lambda x : func(x))
```

#### Stemming / Lemmatization
- Stemming: 단어로부터 어간을 추출하는 작업
- Lemmatization: 표제어 추출

#### BoW (Bag of Words)
머신러닝 모델은 텍스트를 벡터 값으로 변환하는 피쳐 벡터화 과정이 필요하다. BoW는 단어의 문맥 및 순서를 무시하고, 단어의 빈도 값을 부여하여 변수를 만드는 방법이다.
1. 문장에 있는, 중복 제거된 모든 단어에 고유의 인덱스를 부여한다.
2. 개별 문장에서 해당 단어가 나타나는 횟수를 각 단어에 표시한다.

- 장점: 문장에서 단어의 특징을 나타낼 수 있어 활용도가 높다.
- 단점: 문맥 의미를 완벽히 반영하지 못한다. Sparse Matrix로 인한 성능 감소

**CountVectorizer**

단어에 값을 부여할 때, 각 문장에서 해당 단어의 빈도 Count를 부여한다. 값이 높을수록 중요한 단어로 인식된다.

```python
from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()
vect.fit(train['data'])
train_x = vect.transform(train['data'])
test_x = vect.transform(test['data'])
```

**TF-IDF: Term Frequency-Inverse Document Frequency**

개별 문서에서 자주 등장하는 단어에는 높은 가중치를 주고, 모든 문서에서 자주 등장하는 단어에 대해서는 패널티를 주며 값을 부여한다.

예를 들어 5개의 문서가 있을 때 `딥러닝`이라는 단어는 모든 문서에 등장하고, `머신러닝`이라는 단어는 1번 문서에서만 빈번히 등장하는 경우 TF-IDF에서는 딥러닝은 낮게, 머신러닝은 높게 부여된다.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer()
vect.fit(train['data'])
train_x = vect.transform(train['data'])
test_x = vect.transform(test['data'])
```