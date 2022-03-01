---
layout: post
title:  "모델 저장 및 불러오기 (Save and load model)"
parent: Pytorch Basics
grand_parent: ML/DL Practice
nav_order: 8
date:   2022-02-28 19:58:00 +0900
---
# Save and Load Model
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

## 모델 저장하고 불러오기
---
이번 장에서는 저장하기나 불러오기를 통해 
- 모델의 상태를 유지(persist)하고 
- 모델의 예측을 실행하는 방법을 알아보겠습니다.

```python
import torch
import torchvision.models as models
```

## 모델 가중치 저장하고 불러오기
---
PyTorch 모델은 학습한 매개변수를 ``state_dict`` 라고 불리는 내부 상태 사전(internal state dictionary)에 저장합니다.

이 상태 값들은 ``torch.save`` 메소드를 사용하여 저장(persist)할 수 있습니다:




```python
model = models.vgg16(pretrained=True)
torch.save(model.state_dict(), 'model_weights.pth')
```

    Downloading: "https://download.pytorch.org/models/vgg16-397923af.pth" to /root/.cache/torch/hub/checkpoints/vgg16-397923af.pth



      0%|          | 0.00/528M [00:00<?, ?B/s]


모델 가중치를 불러오기 위해서는, 
1. 먼저 동일한 모델의 인스턴스(instance)를 생성한 다음에
2. ``load_state_dict()`` 메소드를 사용하여 매개변수들을 불러옵니다.




```python
model = models.vgg16() # 기본 가중치를 불러오지 않으므로 pretrained=True를 지정하지 않습니다.
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()
```




    VGG(
      (features): Sequential(
        (0): Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (1): ReLU(inplace=True)
        (2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (3): ReLU(inplace=True)
        (4): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
        (5): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (6): ReLU(inplace=True)
        (7): Conv2d(128, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (8): ReLU(inplace=True)
        (9): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
        (10): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (11): ReLU(inplace=True)
        (12): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (13): ReLU(inplace=True)
        (14): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (15): ReLU(inplace=True)
        (16): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
        (17): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (18): ReLU(inplace=True)
        (19): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (20): ReLU(inplace=True)
        (21): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (22): ReLU(inplace=True)
        (23): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
        (24): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (25): ReLU(inplace=True)
        (26): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (27): ReLU(inplace=True)
        (28): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        (29): ReLU(inplace=True)
        (30): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
      )
      (avgpool): AdaptiveAvgPool2d(output_size=(7, 7))
      (classifier): Sequential(
        (0): Linear(in_features=25088, out_features=4096, bias=True)
        (1): ReLU(inplace=True)
        (2): Dropout(p=0.5, inplace=False)
        (3): Linear(in_features=4096, out_features=4096, bias=True)
        (4): ReLU(inplace=True)
        (5): Dropout(p=0.5, inplace=False)
        (6): Linear(in_features=4096, out_features=1000, bias=True)
      )
    )



추론(inference)을 하기 전에 ``model.eval()`` 메소드를 호출하여 

드롭아웃(dropout)과 배치 정규화(batch normalization)를 평가 모드(evaluation mode)로 설정해야 합니다. 

그렇지 않으면 일관성 없는 추론 결과가 생성됩니다.



## 모델의 형태를 포함하여 저장하고 불러오기
---
모델의 가중치를 불러올 때, 신경망의 구조를 정의하기 위해 모델 클래스를 먼저 생성(instantiate)해야 했습니다.

이 클래스의 구조를 모델과 함께 저장하고 싶으면, (``model.state_dict()`` 가 아닌) ``model`` 을 저장 함수에 전달합니다:




```python
torch.save(model, 'model.pth')
```

다음과 같이 모델을 불러올 수 있습니다:




```python
model = torch.load('model.pth')
```

이 접근 방식은 Python [pickle](https://docs.python.org/3/library/pickle.html) 모듈을 사용하여 모델을 직렬화(serialize)하므로, 모델을 불러올 때 실제 클래스 정의(definition)를 적용(rely on)합니다.