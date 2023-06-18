---
layout: post
title:  "Edge Computing이란"
parent: Paper
grand_parent: Study
nav_order: 1
permalink: /docs/study/paper/edge-computing
date:   2020-02-10 16:00:00 +0900
---
# The Emergence of Edge Computing
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## 논문
---
M. Satyanarayanan, ["The Emergence of Edge Computing,"] in Computer, vol. 50, no. 1, pp. 30-39, Jan. 2017, doi: 10.1109/MC.2017.9.

["The Emergence of Edge Computing,"]: https://ieeexplore.ieee.org/abstract/document/7807196

## 배경
---
클라우드 컴퓨팅: 컴퓨팅 파워를 지구상의 여러 대규모 데이터 센터로 통합함
- 규모의 경제: 시스템 관리 및 운영 비용 감축
- 자본 지출을 줄임: 대규모 서비스 제공자의 자원을 소비함

엣지 컴퓨팅: 분산된 컴퓨팅
- 상당 부분의 컴퓨팅 및 저장 리소스를 모바일 기기 또는 센서와 가까이 위치한 `인터넷의 엣지`에 위치시킴

industry investment and research interest in edge computing have grown.

content delivery network(CDN): use nodes at the edge near user to prefetch and cache web content

nodes also perform content customization, adding location-relevant advertising, valuable for saving bandwidth from caching

Edge computing generalizes and extends the CDN concept by leveraging cloud computing infra.

the proximity of cloudlets, cloudlet can run arbitrary code just as in cloud computing.

cyber foraging: amplification of a mobile device's computing capabilities by leveraging nearby infrastructure.

large average separation btw a mobile device and its optimal cloud datacenter.

- avg roundtrip time
- the latency of a wireless first hop
- the variance inherent in a multihop network

→ reliance on a cloud datacenter is not advisable, tight control of latency

conceptual foundation for edge computing, two-level architecture

first level: cloud infrastructure

second level: cloudlets with state cached from the first level

→ persistent caching simplifies the management of cloudlets

→ cloudlet can be expanded to a multilevel cloudlet hierarchy

→ fog computing: decentralization for IoT infrastructure scalability

## Why proximity matters
---
logical network proximity: low latency, low jitter, high bandwidth

physical proximity affects

- end-to-end latency
- economically viable bandwidth
- establishment of trust
- survivability

multihop networking → economic limit on both latency and bandwidth

each hop introduces queuing and routing delay, as well as buffer bloat.

the proximity of cloudlets helps

- Highly responsive cloud services
    - physical proximity → low end-to-end latency, high bandwidth, low jitter to services
    - valuable for offloading computation to the cloudlet
- Scalability via edge analytics
    - raw data is analyzed on cloudlets → bandwidth demand decreasing
    - extracted data and metadata must be transmitted to the cloud
- Privacy-policy enforcement
    - cloudlet can enforce the privacy policies of its owner prior to release of the data to cloud
- Masking cloud outages
    - cloud service unavailable due to network failure, cloud failure, denial-of-service attack → fallback service on a nearby cloudlet can mask the failure.

## Highly responsive cloud services
---
Humans are acutely sensitive to delays

- face recognition: 370-620ms
- speech recognition: 300-450ms

end-to-end latency of a few tens of milliseconds is a safe but achievable goal.

(figure 1) the importance of cloudlets for low-latency offload services

the ideal is best approximated by a cloudlet

worsening response-time curves corresponding to more distant AWS

response time ↑ →  per-operation energy consumption on the mobile device ↑

Mobile only case: no offloading is performed and the CV code is run on the mobile device

→ avoiding energy and performance cost of WiFi communication, but slower than using cloudlet

→ offloading is clearly important

Cloudlets: energy-rich high-end computing within one wireless hop of mobile devices, computation-intensive and latency-sensitive.

cognitive assistance applications

- first phase: the sensor inputs are analyzed to extract a symbolic representation of task

idealized representation and excluding all irrelevant detail, tolerant of variability (analog to digital)

- second phase: comparing symbolic representation with expected task state generates user guidance

## Scalability through edge analytics
---
cloudlet can also reduce ingress bandwidth into the cloud

e.g. many colocated users are transmitting video to the cloud for content analysis

→ too much cumulative data rate

**GigaSight** framework, video from a mobile device only travels as far as a nearby cloudlet.

cloudlet runs CV analytics in near realtime and sends the results with metadata to the cloud.

→ reduce ingress bandwidth into the cloud

→ data in the cloud guides deeper and more customized searches of the content of video segment

video camera, modern aircraft, automobile

whether cloudlets should be in automobiles or part of the telco infra.

multiplayer video game (vehicle's cloudlet): real-time analytics to alert

collaborative real-time avoidance of road hazards (telco cloudlet)

## Privacy policy enforcement
---
growing concerns over data privacy arising from IoT system overcentralization

reluctant to release raw sensor data to an IoT data hub → desire finer-grain control over release

Today's IoT architecture: impossible to make fine-grain control.

Nigel Davies proposes an IoT privacy architecture leveraging a cloudlet within a sensor owner's trust domain.

privacy mediators on cloudlet to perform denaturing and privacy-policy enforcement on sensor stream.

→ cloudlet provides the foundation for a scalable and secure privacy solution.

full-fidelity sensor data can be archived on a cloudlet for a finite duration

## Masking cloud outages
---
cloud dependency grows, vulnerability to cloud outages grows

convergence of mobile and cloud computing → cloud is easily accessible at all times

hostile environment

- a theater of military operations
- geographical region where recovery is under way
- developing country with weak networking infrastructure
- Internet that has temporarily become a hostile environment because it is under cyber attack.

cloudlet can alleviate cloud outages

physical proximity → survivability of cloudlet, closer to associated mobile devices

It opens the door: a fallback service on a cloudlet can temporarily mask cloud inaccessibility.

during failures, cloudlet can serve as a proxy for the cloud and perform its critical services

# The road ahead
---
- technical side
    - unknowns pertaining to the SW mechanisms and algorithms for control and cloudlet sharing in distributed computing
    - dispersion inherent in edge computing raises the complexity of management → developing innovative technical solutions to reduce this complexity
    - development of mechanisms to compensate for the weaker perimeter security of cloudlet
    - development of tamper-resistant and tamper-evident enclosures, remote surveillance, etc
- nontechnical side
    - viable business models for deploying cloudlets
    - bootstrapping problem

the emergence of edge computing coincides with three important trends

1. software-defined networking(SDN) and the associated concept of network function virtualization(NFV)
2. ultra-low-latency wireless networks
3. improvement in the computing capabilities of mobile devices

→ sweet spot for edge computing: infrastructure that amplify the capabilities of proximate mobile devices and sensors.