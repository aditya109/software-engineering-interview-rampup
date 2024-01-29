# Table of Contents

- [Introduction](#introduction)
  * [How to attempt a System Design Question ?](#how-to-attempt-a-system-design-question--)
  * [Five Things to Look Out for in a Good System Design](#five-things-to-look-out-for-in-a-good-system-design)
  * [Horizontal vs Vertical Scaling of Systems](#horizontal-vs-vertical-scaling-of-systems)
  * [The Pizza Parlor Analogy](#the-pizza-parlor-analogy)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Introduction

## How to attempt a System Design Question ?

***1. Scope the Problem***

- DO NOT make assumptions.
- Ask clarifying questions to understand the constraints and use cases.
  - *REQUIREMENTS CLARIFICATION*
  - *SYSTEM INTERFACE DEFINITION*

***2. Sketch up Abstract Design***

- Building blocks of the system and relationships between them.
  - *BACK OF ENVELOPE ESTIMATION*
  - *DEFINING DATA MODEL*
  - *HIGH LEVEL DESIGN*

***3. Identify and address the bottlenecks***

- Use fundamental principles of scalable system design
  - *DETAILED DESIGN*
  - *IDENTIFYING AND RESOLVING BOTTLENECKS*

## Five Things to Look Out for in a Good System Design

- **S**CALABILITY
- **R**ELIABILITY
- **A**VAILABILITY
- **E**FFICIENCY
- **S**ERVICEABILITY

## Horizontal vs Vertical Scaling of Systems

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/horizontalvertical.svg?token=AFH4ROYRJFHGWZQLOR243PTABZJSS)

**Vertical Scaling of Systems**

In vertical scaling of systems, the processing power of the system is increased by putting in better and expensive parts, or in the words of Gaurav Sen, *"you throw more money at the system"*.

Characteristics to this approach:

- There is a limit, up to which hardware can be scaled.
- Increasing the computing power of the system, makes way for a single point of failure.
- Consistency and resiliency is increased.
- Since there is just IPC, network latency within system is reduced.

**Horizontal Scaling of Systems**

In horizontal scaling of systems, central system is distributed among a bench of systems with similar processing capacity.

Characteristics to this approach:

- There is inevitable need for load balancing.
- Network Calls or RPCs are quite frequent.
- Requires data consistency proportional to users.

## The Pizza Parlor Analogy

**Goal:** You have to make a Pizza Parlor and deal with all the difficulties and make the business scalable.

**Process:**

Initial Setup: We have 1 store and 1 chef to handle all the customer requests.

***————–Customer Base Increment————–***

To deal with it, we pay the chef more (*Vertical Scaling*). The prep work can be done before hand during off-hours to make more time and reduce efforts in order prepping (*Preprocessing and Cronjobs*)

***————–Customer Base Increment + Chef is sick————–***

We can't keep pay the chef to get better. (*Limit of vertical scaling*, *Single point of failure*) 
We hire a backup chef to fill in the days when our main chef is absent. (*Dealing with resilience*) 

***————–Customer Base Increment————–***

We make our backup chef permanent. (*Horizontal Scaling*)

***————–Latency Issues————–***

We make teams working under multiple chefs, each having there own speciality. (*Microservices*)

***————–Localized Natural Disaster————–***

We open shops in multiple places all throughout the customer region so that we can keep serving customer requests even though one or more shop is hit and goes under. (*Distributed system or Partitioning, Dealing with fault tolerance*)

***————–Continuous Customer Base Increment————–*** 

We implement order stations which take orders and distribute the customer requests among the Pizza station, taking into account various parameters like workload on the stations, delivery destination location from the stations, etc. (*Load Balancing*)

We start to decouple the main system into independent functionalities, working on their own. For example, we open up Delivery Stations to deliver orders to customer quicker, etc. (*Decoupling*)

Now, it is also important to monitor and logs every event which takes place in the Pizza Parlor, so that error made can be tracked down. (*Logging and Monitoring*)



