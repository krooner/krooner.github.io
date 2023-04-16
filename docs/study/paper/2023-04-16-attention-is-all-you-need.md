---
layout: post
title:  "Attention"
parent: Paper
grand_parent: Study
# nav_order: 2
permalink: /docs/study/paper/2023-04-16-attention-is-all-you-need
date:   2023-04-16 10:00:00 +0900
---
# Attention Is All You Need
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## Abstract

> The dominant sequence transduction models are based on complex __recurrent or convolutional neural networks that include an encoder and decoder through an attention mechanism.__

> the __Transformer, based solely on attention mechanisms,__ dispensing with ~~recurrence and convolutions~~ entirely. ... these models to be superior ... being more __parallelizable and requiring significantly less time to train.__

## Introduction

> Recurrent models ... inherently __sequential nature precludes parallelization within training examples__, which becomes __critical at longer sequence lengths, as memory constraints limit batching across examples.__

$h_{t}=f(h_{t-1}, x_{t})$
- $h_{t}$ = a hidden state of position $t$
- $x_{t}$ = the input for position $t$

> ___Attention mechanisms___ ... allowing modeling of dependencies _without regard to their distance in the input or output sequences._

> the Transformer, a model architecture eschewing recurrence and _instead relying entirely on an attention mechanism_ to __draw global dependencies between input and output.__

## Background

> _The goal of reducing sequential computation_ ... Extended Neural GPU, ByteNet, and ConvS2S, all of which use __convolutional neural networks as basic building block, computing hidden representation in parallel for all input and output positions.__ ... 

> __the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions__ ... linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions.

- ConvS2S $O(n)$
- ByteNet $O(\log{n})$

> In the Transformer this is reduced to __a constant number of operations__, albeit at the cost of reduced effective resolution due to __averaging attention-weighted positions__ ... Multi-Head Attention ...

- Transformer $O(1)$

> _Self-attention_ ... is an attention mechanism __relating different positions of a single sequence in order to compute a representation of the sequence.__

> ... the Transformer is the first transduction model __relying entirely on self-attention to compute representations of its input and output__ ...

## Model Architecture

> the _encoder_ maps __an input sequence of symbol representations__ $\textbf{x} = [x_{1}, x_{2}, ... x_{n}]$ to __a sequence of continuous representations__ $\textbf{z} = (z_{1}, z_{2}, ... z_{n})$.
- Encoder $ E: \textbf{x} \rightarrow \textbf{z}$

> Given $z$, the _decoder_ then generates __an output sequence of symbols__ $\textbf{y} = [y_{1}, y_{2}, ... y_{m}]$ one element at a time. At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.

- Decoder $ D: \textbf{z} \rightarrow \textbf{y}$

> the Transformer follows this overall architecture using __stacked self-attention and point-wise, fully connected layers for both the encoder and decoder__ ...


### Encoder $E$
> The encoder is composed to a stack of $N=6$ indentical layers. Each layer has __two sub-layers ... a multi-head self-attention mechanism, and ... a simple, position-wise fully connected feed-forward network.__

> We employ __a residual connection around each of the two sub-layers, followed by layer normalization.__ That is, the output of each sub-layer is $\text{LayerNorm}(x + \text{Sublayer}(x))$ ... to facilitate these residual connections, __all sub-layers in the model, as well as the embedding layers, produce outputs of dimension__ $d_{model}=512$.


- Stacked Encoder
- Each stack is composed of two sub-layers
    1. a multi-head self-attention mechanism
    2. a simple, position-wise fully connected $FFN$
- Each sub-layer contains a residual connection
- Hyper-parameter
    - The number of stacks in encoder $N=6$
    - The embedding and sub-layer dimension $d_{model} = 512$

### Decoder $D$

> The decoder is also composed of a stack of $N=6$ identical layers. In addition to the two sub-layers in each encoder layer, the decoder layer, inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack.

> We also __modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions.__ This masking, combined with the fact that the output embeddings are offset by one position, ensures that __the predictions for position $i$ can depend only on the known outputs at positions less than__ $i$.

- Stacked Decoder
- Each stack is composed of three sub-layers
    1. a multi-head self-attention mechanism
    2. a simple, position-wse fully connected $FFN$
    3. multl-head attention
- Modification of third sub-layer
    - the output embeddings are offset by one position
    - the predictions for certain position can depend only on the known outputs at previous ones of its position.

### Attention

> An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility funciton of the query with the corresponding key.

- $Attention: Q, (K, V) \rightarrow Output$
- $Output = W\cdot V$
- $W = f(Q, K)$

#### Scaled Dot-Product Attention

> We call our particular attention "Scaled Dot-Product Attention". The input consists of queries and keys of dimension $d_{k}$, and values of dimension $d_{v}$. We compute __dot products of the query with all keys, divide each by $\sqrt{d_{k}}$, and apply a softmax function to obtain the weights on the values.__

$Attention(Q,K,V) = \text{softmax}(\frac{QK^{T}}{\sqrt{d_{k}}})V$

> ... We suspect that __for large values of $d_{k}$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients.__ To counteract this effect, we scale the dot products by $\frac{1}{\sqrt{d_{k}}}$.

#### Multi-Head Attention

> Instead of performing a single attention with $d_{model}$-dimensional keys, values and queries, we found it beneficial to __linearly project the queries, keys and values $h$ times with different, learned linear projections to $d_{k}, d_{k}$ and $d_{v}$ dimensions, respectively.__

> On each of these projected versions of queries, keys and values we then __perform the attention function in parallel, yielding $d_{v}$-dimensional output values.__ These are concatenated and once again projected, resulting in the final values. Multi-head attention allows the model to __jointly attend to information from different representation subspaces at different positions.__

$\text{MultiHead}(Q,K,V)=\text{Concat}(\text{head}_{1}, ..., \text{head}_{h})W^{O}$<br>
$\text{where } \text{head}_{i}=\text{Attention}(QW_{i}^{Q}, KW_{i}^{K}, VW_{i}^{V})$
- a weight of $Q$ w.r.t. head $i$ = $W_{i}^{Q} \in \textbf{R}^{d_{model}\times d_{k}}$
- a weight of $K$ w.r.t. head $i$ = $W_{i}^{K} \in \textbf{R}^{d_{model}\times d_{k}}$
- a weight of $V$ w.r.t. head $i$ = $W_{i}^{V} \in \textbf{R}^{d_{model}\times d_{v}}$

Hyper-parameters
- The number of parallel attention layers (heads) $h=8$
- $d_k = d_v = \frac{d_{model}}{h}=64$  
(Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.)

#### Applications of Attention

> _In "encoder-decoder" attention layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder._ This allows __every position in the decoder to attend over all positions in the input sequence.__

> _The encoder contains self-attention layers._ In a self-attention layer all of the keys, values and queries __come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.__

> Similarly, _self-attention layers in the decoder_ allow each position in the decoder to attend to all positions in the decoder up to and inclduing that position. __We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking-out (setting to $-\infin$) all values in the input of the softmax which correspond to illegal connections.__

### Position-wise FFN
> In addition to attention sub-layers, each of the layers in our encoder and encoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear trnasformations with a ReLU activation in between.

$\text{FFN}(x)=\max(0, xW_{1}+b_{1})W_{2}+b_{2}$
- two convolutions with kernel size 1
- $d_{model}=512, d_{ff}=2048$

### Embedding and Softmax
> we use learned embeddings to convert the input tokens and output tokens to vectors of dimension $d_{model}$. We also use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities.

### Positional Encoding
> in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add positional encodings to the input embeddings at the bottoms of the encoder and encoder stacks.

$PE_{(pos,2i)}=\sin{\frac{pos}{10000^{2i/d_{model}}}}$  
$PE_{(pos,2i+1)}=\cos{\frac{pos}{10000^{2i/d_{model}}}}$
- the position $pos$ and the dimension $i$

> We chose this function ...  it would allow the model to __easily learn to attend by relative positions, since for any fixed offset $k$, $PE_{pos+k}$ can be represented as a linear function of $PE_{pos}$.__ ... We chose the sinusoidal version because it may __allow the model to extrapolate to sequence lengths longer than the ones encountered during training.__

## Why Self-Attention
1. The _total computational complexity per layer_
2. The _amount of computation that can be parallelized_
3. The _path length between long-range dependencies in the network_
    > One key factor affecting the ability to __learn such dependencies is the length of the paths forward and backward signals have to traverse in the network.__ The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies.  
    > 
    > In terms of computational complexity, __self-attention layers are faster than recurrent layers when the sequence length $n$ is smaller than the representation dimensionality $d$, which is most often the case ...__ A single convolutional layer with kernel width $ k < n$ does not connect all pairs of input and output positions.