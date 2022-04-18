---
title: "Language and Vision"
layout: post
parent: Introduction to AI
grand_parent: Coursework
nav_order: 10
date:   2022-04-18 23:01:00 +0900
---
# Language and Vision
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Modeling language
---
1. 문장 생성: Sentence generation
    - $f_{\theta} \rightarrow$ `I'm very hungry at the end of every class`
2. 텍스트 요약: Text summarization
    - English sentence $\rightarrow f_{\theta} \rightarrow$ French sentence
3. 기계 번역: Machine translation
    - Document $\rightarrow f_{\theta} \rightarrow$ Summary

$\therefore$ 문장은 discrete symbol의 시퀀스이다.

|A|Man|is|holding|a|bat|
|---|---|---|---|---|---|
|[00001000]|[01000000]|[00000010]|[00000100]|[00001000]|[10000000]|
|$x_0$|$x_1$|$x_2$|$x_3$|$x_4$|$x_5$|

One-hot encoding of discrete symbol (tokenization)