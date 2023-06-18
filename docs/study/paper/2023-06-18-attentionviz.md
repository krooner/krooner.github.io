---
layout: post
title:  "AttentionViz"
parent: Paper
grand_parent: Study
# nav_order: 2
permalink: /docs/study/paper/2023-06-18-attentionviz
date:   2023-06-18 23:00:00 +0900
---
# A Global View of Transformer Attention
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction
Transformer 기반의 신경망 구조가 널리 활용되고 있지만, 내부 매커니즘에 대해서는 아직 Mysterious하므로 Transformer 모델에 대한 이해가 필요하다.

그 중에서도 __Self-attention 매커니즘__ 은 입력값 내 Element 간의 다양한 관계를 학습하고 활용하도록 한다. Transformer를 구성하는 다양한 Attention head가 어떻게 동작하는지를 시각화하고자 한다.

AttentionViz는 __Joint query-key embedding을 기반으로, Transformer 모델 내의 Attention 트렌드를 관찰할 수 있는 시각화 기술__ 이다.

## Transformer 모델에 대해
Transformer는 시퀀스 입력값을 처리하기 위해 고안된 신경망이다. Transformer는 __Embedding__ 이라는, 벡터 집합을 입력값으로 받는다; 텍스트의 경우 단어, 이미지의 경우 이미지 패치 (Patches of pixels)

모델 내에서는 일련의 Attention layer를 통하여 입력 벡터를 반복적으로 변환하고, 이 과정에서 Embedding 쌍들 간의 정보가 이동한다. __Attention__ 이라는 단어에서 알 수 있듯이 모든 Embedding이 동일하게 연관되어 있진 않으며, 특정 쌍은 더 강하게 상호작용한다 (Pay more attention to each other)

Embedding Pair 간에는 다양한 관계가 존재할 수 있다: 단어의 경우, 형용사-명사 관계 또는 주어-동사 관계 등. 다양한 관계를 포착하기 위해 Attention layer는 여러 개의 __Attention head__ 로 구성되어 있다. 각각은 서로 다른 Attention 및 정보 패턴을 담고 있다.

각 Attention head 내에서, __두 Embedding vector $x, y$에 대한 Attention__ $f(x, y)$ 는 Query vector $W_{Q}x$와 Key vector $W_{K}y$의 내적으로 결정된다: $f(x, y) = \frac{1}{\sqrt{d}}<W_{Q}x, W_{K}y>$ ($d$는 Key vector의 차원 수) Query vector와 Key vector 간의 내적 값이 클수록 최종 Attention 값은 더욱 커질 것이다.