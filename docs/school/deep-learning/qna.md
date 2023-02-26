---
title: "Q&A"
layout: post
parent: Deep Learning
grand_parent: School
nav_order: 99
date:   2022-03-29 13:41:00 +0900
---
# 딥러닝 인터뷰 문답
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

[Reference](https://www.cpuheater.com/deep-learning/deep-learning-interview-questions-and-answers)

### 딥러닝이란
1개 이상의 은닉층을 갖는 심층 인공 신경망을 활용하여 데이터로부터 학습하는 ML의 세부 분야

### 왜 Deep 모델이 Shallow 모델보다 성능이 좋은가
두 모델 모두 임의의 함수를 근사할 수 있으나 Deep Network는 연산량이나 파라미터 수에 있어 효율적이다. <br>
Deep Network는 more abstract한 deep representation을 학습한다.

### Cost function이란
신경망이 얼마나 잘 작동하는지를 나타내는 지표. 학습의 목표는 cost function을 최소화하는 파라미터를 찾는 것. <br>
예 - Mean Squared Error $MSE=\frac{1}{n}\sum_{i=0}^{n}(\hat{Y}_{i}-Y_{i})^2$

### Gradient descent란
Cost function을 최소화하는 파라미터 값을 학습하는 최적화 알고리즘. <br>
매 iteration마다 각 parameter에 대한 cost function의 gradient를 계산하고 파라미터를 update. <br>
$W=W-\alpha\frac{\delta}{\delta W}J(W)$
- $W$: parameter, $\alpha$: learning rate, $J$: cost function

### Backpropagation이란
multi-layer를 갖는 신경망에 사용되는 학습 알고리즘. <br>
신경망의 계산된 결과에서 발생한 error 정보를 신경망 내부 parameter로 전파하여 gradient를 계산
1. Forward-propagation으로 Output value 계산
  - $f(x)=\hat{y}$
2. Target value (실제 값)과 Output value 간 error의 derivative를 activation에 대하여 계산
  - $J(x;W) = y-\hat{y}$, $\frac{\delta J}{\delta g}$
3. Back-propagation을 통해 이전 layer의 derivative를 계산하고, 같은 방식으로 모든 hidden layer에 적용
4. Gradient descent (update weights)

### Stochastic, Batch, Mini-batch gradient descent
Stochastic (SGD): single training sample로 gradient를 계산하고 파라미터를 update <br>
Batch: 전체 training set에 대한 gradient를 계산하고 각 iteration마다 1번 수행 <br>
Mini-batch: 전체가 아닌 mini-batch에 대해서 수행
  - SGD 방식에 비하여 효율적인 연산
  - flat minima를 찾음으로써 generalization을 개선한다
  - Mini-batch에 대한 gradient 계산은 전체 training set에 대한 gradient에 근사하는 것 <br>
    $\rightarrow$ local minima에 갇히는 것을 방지하고 convergence를 개선한다

### One-hot encoding
Category feature를 numerical value로 encode할 때 쓰이는 방식
- $\{Red\}, \{Green\}$

|$Red$|$Green$|$Blue$|
|---|---|---|
|1|0|0|
|0|1|0|

### Data normalization
값을 rescaling하여 특정 범위에 맞추는 방식 (e.g. $\frac{X-\mu}{\sigma}$) <br>
$\rightarrow$ Backpropagation 과정에서 더 나은 convergence를 가능하게 함

### Weight initialization
Bad initialization - Network의 학습을 방해한다 <br> 
Good initialization - 빠른 convergence와 개선된 overall error를 얻을 수 있다
- 일반적으로, 0이 아니면서 너무 작지 않은 값으로 weight을 설정함
- Zero initialization을 하게 되면, 각 layer의 모든 neuron이 backpropagation 과정에서 모두 동일한 output과 gradient를 계산하게 된다.
- 즉, neuron간의 비대칭성이 없기 때문에 network에 대한 학습이 진행되지 않는다

$\therefore$ weight initialization 과정에 randomness가 추가되어야 한다.

### Activation function
신경망에 non-linearity 특성을 추가하여, 매우 복잡한 함수를 학습할 수 있게끔 한다. <br>
Activation function 없이 신경망은 input data에 대한 선형 결합 함수만 학습할 수 있다.
- Sigmoid (logistic function): binary classification에 주로 활용된다.
  - $g(x)=\frac{1}{1+e^{x}}$
- Softmax: multi-class에 대한 classification에 활용된다.
  - $softmax(x_i) = \frac{e^{x_i}}{\sum_{j}e^{x_j}}$
- ReLU (Rectified Linear Unit): gradient vanishing 문제가 없으며 빠르다.
  - $g(x) = \max(0, x)$

### Hyperparameter
model parameter와 달리 training 과정에서 학습되지 않는 parameter로, 학습 이전에 설정되는 값
- learning rate $\alpha$: 최적화 과정에서 얼마나 빠르게 weight을 update할 것인가
- epoch number: one epoch이란 전체 training set에 대하여 1번의 forward-pass와 backward-pass를 수행하는 것
- batch size: 1번의 fwd-pass, backward-pass가 수행될 때 사용되는 training example 수

### Model capacity
주어진 임의의 함수를 근사할 수 있는 능력으로, Model capacity가 크다는 것은 네트워크 내에 많은 정보를 저장할 수 있다는 것.

### Convolutional Neural Network (CNN)
Convolution layer는 kernels (=a set of filters)로 구성되며, <br>
각각의 filter가 input image를 sliding하며 filter 내 weight와 covered area 간의 dot-product 계산. <br>
학습 과정에서 network는 특정 feature를 감지할 수 있는 filter를 학습함.

### Autoencoder
Supervision 없이 데이터에 대한 representation을 학습하는 신경망으로, Input과 똑같은 Output을 만들도록 network를 학습시킨다. <br>
Internal representation은 input보다 작은 dimension을 가지므로, 데이터를 표현하는 효율적인 방법을 학습할 수 있다.
- encoder: input에서 internal representation을 학습한다
- latent space $z$: internal representation
- decoder: internal representation으로부터 output을 만든다

### Dropout
Regularization 방식으로 신경망의 overfitting을 방지한다. <br>
각 학습 단계마다 임의로 neuron을 drop-out (set to zero) 하여 다른 모델을 만든다 (모델들은 weight을 공유한다)

### Cross-entropy cost function
Classification에 활용되며 output layer에는 sigmoid나 softmax가 activation function으로 쓰일 수 있다.
- $C=-\frac{1}{n}\sum_{i=1}^{n}(y_i\log{\hat{y}_i}+(1-y_i)\log(1-\hat{y}_i))$

### Feedforward NN과 Recurrent NN의 차이
- Feedforward
  - Signal이 한 방향으로만 흘러감: input에서 output
  - Fixed-size
- Recurrent
  - $s_t = f(s_{t-1}, x_t)$
    - 현재 $t$의 state $s_t$는 이전 state $s_{t-1}$와 현재 input $x_t$의 함수
    - 이전까지 본 시퀀스의 history를 summarize한 것
  - 임의의 길이를 갖는 시퀀스 데이터에 적용 가능