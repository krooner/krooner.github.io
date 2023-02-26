---
layout: post
title:  "실시간 비디오 분석"
parent: Paper
grand_parent: Study
nav_order: 2
permalink: /docs/study/paper/realtime-va
date:   2020-02-15 16:00:00 +0900
---
# Real-time Video Analytics
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## 논문
---
G. Ananthanarayanan et al., ["Real-Time Video Analytics: The Killer App for Edge Computing,"] in Computer, vol. 50, no. 10, pp. 58-67, 2017, doi: 10.1109/MC.2017.3641638.

["Real-Time Video Analytics: The Killer App for Edge Computing,"]: https://ieeexplore.ieee.org/abstract/document/8057318

## Real-time Video Analytics란
---
a camera installed for every 29 people, mature markets for every 8 people

number of camera increases 20% year over year for 5 years

video analytics: traffic control, surveillance, security, consumer applications for real-time decisions

**geographically distributed architecture** of public clouds, private clusters, and edges that extend down to the cameras is the only approach that can meet the strict real-time requirements of large-scale video analytics, which must address latency, bandwidth, and provisioning challenges.

- Apps require very low latency when processing to interact with humans and actuate some other system
- high-definition video requires large bandwidth, streaming video feeds directly to the cloud unfeasible.
- using compute capacities available on the camera itself allows lower provisioning in the cloud
- video processing's high compute cost

→ high data volume, compute demands, latency make camera the most challenging things in IoT

real-time video analytics system with low resource costs that produces high-accuracy outputs

## Video analytics applications
---
Apps from surveillance and self-driving cars to personal digital assistants and drone cam.

SOTA; deploy expensive custom solutions with a hard-coded set of video analytics, not take advantage of the geo-distributed edge infrastructure.

geo-distributed architecture is best suited to the low response times and high bandwidth requirement.

* Vision Zero for traffic:
eliminate traffic-related deaths by analyzing video from cameras for traffic safety and planning.

* Self-driving and smart cars:
video usage from multiple onboard cameras for a self-driving car to make low-latency driving decisions, ability to fuse multiple video feeds and quickly analyze them.

output from traffic camera analytics can trigger decisions in cars

* Personal digital assistants:
Digital assistants can be incorporated into smart mobile devices or standalone HW. interact with facial recognition, gesture identification. video processing and analytics have to continuously execute with low latency, either locally on the device or with assistance from the remote cloud.

* Surveillance and security
Enterprise and government surveillance

law enforcement officers use body-worn cameras → help identify suspicious license plate or people and alert officer to call for backup and support.

Also, home surveillance cameras that identify motion and people. drone camera will also aid

* Augmented reality

analytics cannot be performed directly inside the headset

→ offload to a nearby edge computer or to the cloud.

## Infrastructure design and Characteristics
---
- geo-distribution: to ensure analytics functionality across cameras, edges, clusters, clouds
- multitenancy: to capture and handle queries per camera and queries across multiple cameras
- HW heterogeneity: to flexibly manage a mix of processing capacities and network

including edge clusters and private clusters with heterogeneous HW to decode video, detect objects and perform other video analytics tasks.

Edge devices include the cameras or processing units placed close to the cameras

network connecting the cameras, edges, private clusters, and the public cloud is a critical resource.

uplink bandwidths btw the private clusters and the cloud are not sufficient for streaming a large number of high-resolution videos to the cloud.

deployment vary from having

- all the analytics in the cloud(for small deployments of cameras)
- all the analytics in private clusters(insufficient bandwidths to the cloud or privacy reasons)
- a hybrid of edge/private clusters and the cloud(the most widely used setup, perhaps after denaturing the videos to maintain privacy)
- all the analytics on the edge

## Rocket: Video analytics software stack
---
*video pipeline optimizer*

- converts high-level video queries to video-processing pipelines composed of many vision modules
- each module implements predefined interfaces to receive and process events and then sends its results downstream
- estimates the query's resource-accuracy profile
- computes the total resource cost and accuracy of the query
- invokes crowd-sourcing to obtain the labeled data required to compute accuracy.
- the pipeline and its generated profile are submitted to the resource manager

*resource manager*

- responsible for all currently executing query pipelines and their access to all resources
- determines the best configuration of each query and the placement of components
- allocates resources for each vision module
- merges common modules across pipelines processing the same video stream.

*geo-distributed executor*

- pipelines execute through geo-distributed executor, which runs across all the cluster.
- camera manager
- adjusts resolution, frame rate, and quality of the video in each camera
- virtualize across multiple query pipelines accessing the camera
- GPU manager
- execution of DNNs on GPUs is made dramatically more efficient by running a DNN execution service on each machine handles all DNN requests on the GPU.
- video storage
- faster cataloging and video retrieval

## Resource-accuracy profiles for scheduling

Video analytics; very high resource demands 

tracking objects but processing cost and data transfer is expensive, to reduce them, *approximation*

resource-accuracy relationship

vision algorithms' parameters: frame resolution, sampling, internal parameters, contain DNN model.

video stream frame processing in high resolution: high accuracy, high resource demand

parameter configuration → determine output accuracy, resource demand

application-specific parameters abstraction to resource-accuracy profile

resource-accuracy profile generation is challenging:  no well-known analytical model to capture relationship

**generate the profile using a labeled dataset of g.t. for each video query pipeline for each camera.**

Rocket's resource optimizer selectively explores only the promising configurations and avoids wasting CPU cycles exploring configurations acc. that have really low acc. or high resource demand.

In profiling queries, a pipeline of vision modules caches the intermediate results of modules and avoids re-running them.

to avoid an explosion of cache space, it profiles configurations with overlapping modules so saving CPU cycles and caching.

In a multitenant cluster with many video queries, **scheduling for accuracy** rather than for fairness.

Rocket's resource optimizer schedules thousands of video queries according to their resource-accuracy profiles and their tolerance to delay in processing, time btw arrival and processing of the frames.

It uses model predictive control and preferentially allocates resources to queries that provide higher accuracy. It also decides on the placement of modules and whether to execute considering capacities of multiple resources.

It shows 80% better avg. query accuracy than fair scheduler and consumes 3.5-fold fewer CPU cycles for profile generation.

## **Efficient DNNs execution on GPUs**

simplest model:

App that sets up and executes the corresponding operations on the GPU by using memory allocation and matrix computation functions provided by a library.

Each invocation of the library leads to one or more distinct instances of computational kernels

→ inadequate in the common setting when several applications try to perform possibly distinct DNN computations on incoming video.

1. loading weight matrices corresponding to DNNs into GPU memory

→ heavyweight operation, very large model so they cannot all be preloaded into memory.

→ important to consider when to load or evict individual models

2. more efficient to execute models in batch mode, the same model is executed in parallel on several inputs, than it is to present a series of heterogeneous models for execution to the GPU.

→ many Apps share the models and inputs they execute, so beneficial to combine models across multiple App to reduce resource demand.

3. some models are too large to execute on the edge, so execute in cloud if latency permits.

we use these ways in a DNN execution services that runs on each machine with a GPU.

All DNN requests run against this service that reconciling these complexities across multiple Apps.

Approximate scheduling

for each DNN, apply a set of optimizations to produce DNN variants with differing acc. and resource use.

several optimization method

- replacing matrices with smaller factors
- limiting the number of bits used to represent model param.
- reducing the architectural complexity of models

new optimization, specialization

replacing large, slow models useful for classifying many classes with **much smaller, faster models that handle just the classes observed at runtime (<10 objects) → reduce requirements**

we use these ways to make a single "optimizing compiler" for DNNs.

- select appropriate DNN variant and its placement to optimize the acc, latency, and cost of the whole query pipeline

## Virtualizing steerable cameras

challenge in supporting multiple App queries concurrently: view and image requirements can differ!

Allowing queries to directly steer the cameras inevitably leads to conflicts.

Rocket's camera manager virtualizes the camera HW, thereby breaking the one-to-one binding btw camera and App query.

Our system is designed to provide each App query with the most recent view that meets requirement.

to know when to steer, our SW learns the movement patterns in its view and predicts when motion or change is likely to occur in each of the views it is managing.

→ our system captures up to 80% percent more events of interest compared to the system that allows App query to control camera directly.

## Application-level optimizations

reduce resource demand and tolerate high latencies of executing expensive DNN operations in the cloud

### Intelligent frame selection

most video streams have temporal redundancy among frames, making it possible to subsample them without losing accuracy.

→ a suite of context-aware and application-aware techniques to sample only a few key frames for processing without compromising the App's accuracy

core nugget: use easily computable "shallow-vision" features to decide whether a frame is worthy of "deep-vision" analysis.

- frame-differencing, extremely cheap way to discard frames that have not changed significantly
- blurriness and lighting, cheap quality metrics to decide if frame is of sufficiently quality to process
- App-level requirements, app-specific sampling both enhances and complements app-agnostic

### Intelligent feed selection

more cameras generate more video streams, which require more network bandwidth and computing resources in the cloud.

→ smart cameras, reducing the network and cloud computing demands while improving the accuracy of the video analytics system.

our system processes incoming video stream at each of the smart cameras and edge nodes to detect objects of interest.

only the most important frames from the different video streams are then uploaded to the cloud for further processing.

use the minimum amount of bandwidth while maximizing the number of query-specified objects delivered to the cloud.

frames from only the cameras that have video frames containing the greatest number of relevant objects to the user's query

suppress a large fraction of unrelated video data, reduce network utilization and increases the utility of the video analytics system

→ our analytics system can support a coverage area that is 5- and 200- fold larger than one that simply streams video from the camera to the cloud.

→ our system outperforms the default equal throughput allocation strategy by delivering up to 25% more objects relevant to a user's query.

### Delay-tolerance

real-time CV App can suffer from high frame processing delays.

processing → high latencies

when App receives results then it might be stale and object could move to different location.

**local object tracking to project the stale results obtained from a processed frame to the current frame.**

maintain an active cache that stores all subsequent frames from the frame that is selected for deep-vision processing

when the processed frame result comes back, run tracking from the processed frame, through the cached frames, to catch up with the current frame.

When newer objects appear in the processed frame, we start tracking them.

## Traffic video analytics