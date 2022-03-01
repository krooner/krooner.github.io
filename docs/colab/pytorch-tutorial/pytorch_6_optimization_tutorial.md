---
layout: post
title:  "최적화 (Optimization)"
parent: Pytorch Basics
grand_parent: ML/DL Practice
nav_order: 7
date:   2022-02-28 19:52:00 +0900
---
# Optimization
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

```python
%matplotlib inline
```

## 모델 매개변수 최적화하기
---
데이터에 매개변수를 최적화하여 모델을 학습하고, 검증하고, 테스트할 차례입니다.

모델을 학습하는 과정은 반복적인 과정을 거칩니다; 
- (*에폭(epoch)* 이라고 부르는) 각 반복 단계에서 모델은 출력을 추측하고,
- 추측과 정답 사이의 오류 (*손실(loss)*)를 계산하고, 
- 매개변수에 대한 오류의 도함수(derivative)를 수집한 뒤, 경사하강법을 사용하여 이 파라매터들을 **최적화(optimize)** 합니다.

이 과정에 대한 자세한 설명은 [3Blue1Brown의 역전파](https://www.youtube.com/watch?v=tIeHLnjs5U8) 영상을 참고하세요.

### 기본(Pre-requisite) 코드
이전 장 `Dataset과 DataLoader`와 `신경망 모델 구성하기` 에서 코드를 가져왔습니다.

```python
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

train_dataloader = DataLoader(training_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork()
```

    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz
    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz to data/FashionMNIST/raw/train-images-idx3-ubyte.gz



      0%|          | 0/26421880 [00:00<?, ?it/s]


    Extracting data/FashionMNIST/raw/train-images-idx3-ubyte.gz to data/FashionMNIST/raw
    
    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz
    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw/train-labels-idx1-ubyte.gz



      0%|          | 0/29515 [00:00<?, ?it/s]


    Extracting data/FashionMNIST/raw/train-labels-idx1-ubyte.gz to data/FashionMNIST/raw
    
    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz
    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz



      0%|          | 0/4422102 [00:00<?, ?it/s]


    Extracting data/FashionMNIST/raw/t10k-images-idx3-ubyte.gz to data/FashionMNIST/raw
    
    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz
    Downloading http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz



      0%|          | 0/5148 [00:00<?, ?it/s]


    Extracting data/FashionMNIST/raw/t10k-labels-idx1-ubyte.gz to data/FashionMNIST/raw
    


## 하이퍼 파라매터(Hyperparameter)
---
하이퍼파라매터(Hyperparameter)는 모델 최적화 과정을 제어할 수 있는 조절 가능한 매개변수입니다.
- 서로 다른 하이퍼파라매터 값은 모델 학습과 수렴율(convergence rate)에 영향을 미칠 수 있습니다.
- 하이퍼파라매터 튜닝(tuning)에 대해 [더 알아보기](https://tutorials.pytorch.kr/beginner/hyperparameter_tuning_tutorial.html)

학습 시에는 다음과 같은 하이퍼파라매터를 정의합니다:
 - **에폭(epoch) 수** - 데이터셋을 반복하는 횟수
 - **배치 크기(batch size)** - 매개변수가 갱신되기 전 신경망을 통해 전파된 데이터 샘플의 수
 - **학습률(learning rate)** - 각 배치/에폭에서 모델의 매개변수를 조절하는 비율. 값이 작을수록 학습 속도가 느려지고, 값이 크면 학습 중 예측할 수 없는 동작이 발생할 수 있습니다.


```python
learning_rate = 1e-3
batch_size = 64
epochs = 5
```

## 최적화 단계(Optimization Loop)
---
하이퍼파라매터를 설정한 뒤에는 최적화 단계를 통해 모델을 학습하고 최적화할 수 있습니다.

최적화 단계의 각 반복(iteration)을 **에폭** 이라고 부릅니다. 하나의 에폭은 다음 두 부분으로 구성됩니다:
 - **학습 단계(train loop)** - 학습용 데이터셋을 반복(iterate)하고 최적의 매개변수로 수렴합니다.
 - **검증/테스트 단계(validation/test loop)** - 모델 성능이 개선되고 있는지를 확인하기 위해 테스트 데이터셋을 반복(iterate)합니다.

학습 단계(training loop)에서 일어나는 몇 가지 개념들을 간략히 살펴보겠습니다.

### 손실 함수(loss function)
학습용 데이터를 제공하면, 학습되지 않은 신경망은 정답을 제공하지 않을 확률이 높습니다. 

손실 함수는 획득한 결과와 실제 값 사이의 틀린 정도(degree of dissimilarity)를 측정하며, 학습 중에 이 값을 최소화하려고 합니다.

주어진 데이터 샘플을 입력으로 계산한 예측과 정답(label)을 비교하여 손실(loss)을 계산합니다.

일반적인 손실함수에는 
- 회귀 문제(regression task)에 사용하는 [nn.MSELoss](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html#torch.nn.MSELoss) - 평균 제곱 오차(MSE; Mean Square Error)나 
- 분류(classification)에 사용하는 [nn.NLLLoss](https://pytorch.org/docs/stable/generated/torch.nn.NLLLoss.html#torch.nn.NLLLoss) - 음의 로그 우도(Negative Log Likelihood)
- ``nn.LogSoftmax`` 와 ``nn.NLLLoss``를 합친 [nn.CrossEntropyLoss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) 

모델의 출력 로짓(logit)을 ``nn.CrossEntropyLoss`` 에 전달하여 로짓(logit)을 정규화하고 예측 오류를 계산합니다.




```python
# 손실 함수를 초기화합니다.
loss_fn = nn.CrossEntropyLoss()
```

### 옵티마이저(Optimizer)
최적화는 각 학습 단계에서 모델의 오류를 줄이기 위해 모델 매개변수를 조정하는 과정입니다.

**최적화 알고리즘** 은 이 과정이 수행되는 방식(여기에서는 확률적 경사하강법(SGD;Stochastic Gradient Descent))을 정의합니다.

모든 최적화 절차(logic)는 ``optimizer`` 객체에 캡슐화(encapsulate)됩니다. 

PyTorch에는 ADAM이나 RMSProp과 같은 다른 종류의 모델과 데이터에서 더 잘 동작하는 [다양한 옵티마이저](https://pytorch.org/docs/stable/optim.html) 가 있습니다.

학습하려는 모델의 매개변수와 학습률(learning rate) 하이퍼파라매터를 등록하여 옵티마이저를 초기화합니다.




```python
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
```

학습 단계(loop)에서 최적화는 세 단계로 이뤄집니다:
1. ``optimizer.zero_grad()`` 를 호출하여 모델 매개변수의 변화도를 재설정합니다. 
  - 기본적으로 변화도는 더해지기(add up) 때문에 중복 계산을 막기 위해 반복할 때마다 명시적으로 0으로 설정합니다.
2. ``loss.backwards()`` 를 호출하여 예측 손실(prediction loss)을 역전파합니다. 
  - PyTorch는 각 매개변수에 대한 손실의 변화도를 저장합니다.
3. 변화도를 계산한 뒤에는 ``optimizer.step()`` 을 호출하여 역전파 단계에서 수집된 변화도로 매개변수를 조정합니다.



## 전체 구현
---
최적화 코드를 반복하여 수행하는 ``train_loop`` 와 

테스트 데이터로 모델의 성능을 측정하는 ``test_loop`` 를 정의하였습니다.


```python
def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
```

손실 함수와 옵티마이저를 초기화하고 ``train_loop`` 와 ``test_loop`` 에 전달합니다.

모델의 성능 향상을 알아보기 위해 자유롭게 에폭(epoch) 수를 증가시켜 볼 수 있습니다.




```python
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

epochs = 10
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")
```

    Epoch 1
    -------------------------------
    loss: 2.299818  [    0/60000]
    loss: 2.301200  [ 6400/60000]
    loss: 2.279417  [12800/60000]
    loss: 2.282822  [19200/60000]
    loss: 2.249819  [25600/60000]
    loss: 2.222014  [32000/60000]
    loss: 2.234944  [38400/60000]
    loss: 2.200947  [44800/60000]
    loss: 2.193802  [51200/60000]
    loss: 2.170050  [57600/60000]
    Test Error: 
     Accuracy: 39.4%, Avg loss: 2.164883 
    
    Epoch 2
    -------------------------------
    loss: 2.163385  [    0/60000]
    loss: 2.168315  [ 6400/60000]
    loss: 2.111036  [12800/60000]
    loss: 2.133869  [19200/60000]
    loss: 2.079017  [25600/60000]
    loss: 2.020911  [32000/60000]
    loss: 2.053516  [38400/60000]
    loss: 1.979324  [44800/60000]
    loss: 1.972612  [51200/60000]
    loss: 1.912487  [57600/60000]
    Test Error: 
     Accuracy: 55.6%, Avg loss: 1.907819 
    
    Epoch 3
    -------------------------------
    loss: 1.929526  [    0/60000]
    loss: 1.913931  [ 6400/60000]
    loss: 1.795278  [12800/60000]
    loss: 1.840527  [19200/60000]
    loss: 1.730337  [25600/60000]
    loss: 1.680813  [32000/60000]
    loss: 1.706084  [38400/60000]
    loss: 1.607633  [44800/60000]
    loss: 1.622599  [51200/60000]
    loss: 1.527825  [57600/60000]
    Test Error: 
     Accuracy: 60.9%, Avg loss: 1.537263 
    
    Epoch 4
    -------------------------------
    loss: 1.594651  [    0/60000]
    loss: 1.566571  [ 6400/60000]
    loss: 1.412425  [12800/60000]
    loss: 1.491551  [19200/60000]
    loss: 1.374017  [25600/60000]
    loss: 1.363599  [32000/60000]
    loss: 1.384933  [38400/60000]
    loss: 1.302045  [44800/60000]
    loss: 1.335862  [51200/60000]
    loss: 1.244951  [57600/60000]
    Test Error: 
     Accuracy: 63.5%, Avg loss: 1.263438 
    
    Epoch 5
    -------------------------------
    loss: 1.332675  [    0/60000]
    loss: 1.318068  [ 6400/60000]
    loss: 1.151137  [12800/60000]
    loss: 1.261432  [19200/60000]
    loss: 1.145367  [25600/60000]
    loss: 1.160078  [32000/60000]
    loss: 1.186256  [38400/60000]
    loss: 1.114341  [44800/60000]
    loss: 1.156490  [51200/60000]
    loss: 1.079363  [57600/60000]
    Test Error: 
     Accuracy: 64.9%, Avg loss: 1.094073 
    
    Epoch 6
    -------------------------------
    loss: 1.157225  [    0/60000]
    loss: 1.161668  [ 6400/60000]
    loss: 0.981594  [12800/60000]
    loss: 1.117426  [19200/60000]
    loss: 1.002845  [25600/60000]
    loss: 1.023665  [32000/60000]
    loss: 1.061346  [38400/60000]
    loss: 0.996515  [44800/60000]
    loss: 1.039788  [51200/60000]
    loss: 0.975127  [57600/60000]
    Test Error: 
     Accuracy: 65.6%, Avg loss: 0.984933 
    
    Epoch 7
    -------------------------------
    loss: 1.035444  [    0/60000]
    loss: 1.060718  [ 6400/60000]
    loss: 0.866529  [12800/60000]
    loss: 1.021808  [19200/60000]
    loss: 0.912228  [25600/60000]
    loss: 0.927976  [32000/60000]
    loss: 0.979231  [38400/60000]
    loss: 0.921845  [44800/60000]
    loss: 0.960259  [51200/60000]
    loss: 0.904867  [57600/60000]
    Test Error: 
     Accuracy: 66.7%, Avg loss: 0.911210 
    
    Epoch 8
    -------------------------------
    loss: 0.947530  [    0/60000]
    loss: 0.991618  [ 6400/60000]
    loss: 0.785201  [12800/60000]
    loss: 0.955135  [19200/60000]
    loss: 0.851687  [25600/60000]
    loss: 0.858648  [32000/60000]
    loss: 0.921838  [38400/60000]
    loss: 0.873515  [44800/60000]
    loss: 0.903661  [51200/60000]
    loss: 0.854760  [57600/60000]
    Test Error: 
     Accuracy: 67.7%, Avg loss: 0.858776 
    
    Epoch 9
    -------------------------------
    loss: 0.881072  [    0/60000]
    loss: 0.940895  [ 6400/60000]
    loss: 0.724796  [12800/60000]
    loss: 0.906396  [19200/60000]
    loss: 0.808179  [25600/60000]
    loss: 0.806612  [32000/60000]
    loss: 0.878994  [38400/60000]
    loss: 0.840759  [44800/60000]
    loss: 0.861594  [51200/60000]
    loss: 0.816741  [57600/60000]
    Test Error: 
     Accuracy: 69.0%, Avg loss: 0.819293 
    
    Epoch 10
    -------------------------------
    loss: 0.828260  [    0/60000]
    loss: 0.901086  [ 6400/60000]
    loss: 0.677827  [12800/60000]
    loss: 0.869159  [19200/60000]
    loss: 0.775017  [25600/60000]
    loss: 0.766413  [32000/60000]
    loss: 0.844869  [38400/60000]
    loss: 0.817015  [44800/60000]
    loss: 0.828802  [51200/60000]
    loss: 0.786272  [57600/60000]
    Test Error: 
     Accuracy: 70.1%, Avg loss: 0.787963 
    
    Done!


## 더 읽어보기
---
1. [Loss Functions](https://pytorch.org/docs/stable/nn.html#loss-functions)
2. [torch.optim](https://pytorch.org/docs/stable/optim.html)
3. [Warmstart Training a Model](https://tutorials.pytorch.kr/recipes/recipes/warmstarting_model_using_parameters_from_a_different_model.html)
