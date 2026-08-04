# Table of Contents

- [What Makes a Good Service?](#what-makes-a-good-service-)
  * [Loose Coupling](#loose-coupling)
  * [High Cohesion](#high-cohesion)
- [The Bounded Context](#the-bounded-context)
  * [Shared and Hidden Models](#shared-and-hidden-models)
  * [Modules and Services](#modules-and-services)
  * [Premature Decomposition](#premature-decomposition)
- [Business Capabilities](#business-capabilities)
- [Turtles All the Way Down](#turtles-all-the-way-down)
- [Communication in terms of Business Concepts](#communication-in-terms-of-business-concepts)
- [The Technical Boundary](#the-technical-boundary)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# What Makes a Good Service?

## Loose Coupling

When services are loosely coupled, a change to one service should not require a change to another.

A loosely coupled service knows as little as it needs to about the services with which it collaborates.

This also means we probably want to **limit the number of different types of calls from one service to another**, because the potential performance problem, *chatty communication can lead to tight coupling*.

## High Cohesion

We want related behavior to sit together, and unrelated behavior to sit everywhere.

**Making changes in lots of different places is slower**, and **deploying lots of services at once is risky** - both of which we want to avoid.

So we want to find boundaries within our problem domain that help ensure that related behavior is in one place, and that communicate with other boundaries as loosely as possible.

# The Bounded Context

The idea is that any given domain consists of multiple bounded contexts, and residing within each are *things that do not need to be communicated outside* as well as *things that are shared externally with other bounded contexts*. Each bounded context has an explicit interface, where it decides what models to share with other contexts.

OR,

A specific responsibility enforced by explicit boundaries. If you want information from a bounded context, or want to make requests of functionality within a bounded context, you communicate with its explicit boundary using models.

> *Cells can exist because their membranes define what is in and out and determine what can pass.* 

## Shared and Hidden Models

![shared model](https://raw.githubusercontent.com/aditya109/microservices-light-reading/master/Book%20-%201%20Building%20Microservices%20-%20Sam%20Newman/assets/sharedmodel.svg)

On a side mote, we may encounter models with the same nature that have very different meanings in different contexts too. 

For example, we might have the concept of a return, which represents a customer sending something back. Within the context of the customer, a return is all about printing a shipping label, dispatching a package, and waiting for a refund.
For the warehouse, this could represent a package that is about to arrive, and a stock item that needs to be restocked. 

It follows that within the warehouse we store additional information associated with the return that relates to the tasks to be carried out; for example, we may generate a restock request. The shared model of the return becomes associated with different processes and supporting entities within each bounded context, but that is very much an internal concern within the context itself.

## Modules and Services

By thinking clearly about what models should be shared, and not sharing our internal representations, we avoid one of the potential pitfalls that can result in tight coupling.
We also have identified a boundary within our domain where all like-minded business capabilities should live, giving us the high cohesion we want.
These bounded contexts, then, lend themselves extremely well to being compositional boundaries.

When you're starting out on a new codebase, this probably a good place to begin. So once you have found your bounded contexts in your domain, make sure they are modeled within your codebase as modules, with shared and hidden models. These modular boundaries then become excellent candidates for microservices.

> When starting out, however keep a new system on the more monolithic side; getting service boundaries wrong can be costly, so waiting for things to stabilize as you get to grips with a new domain is sensible.

## Premature Decomposition

Prematurely decomposing a system into microservices can be costly, especially if you are new to the domain.

# Business Capabilities

When you start to think about the bounded contexts that exists in your organization, you should be thinking not in terms of dat that is shared, but about the capabilities those contexts provide the rest of the domain.

So ask first, "What does this context do ?", and then "So what data does it need to do that ?"

When modeled as services, these capabilities become the key operations that will be exposed over the wire to other collaborators.

# Turtles All the Way Down

At the start, you will probably identify a number of of coarse-grained bounded contexts. But these bounded contexts can in turn contain further bounded contexts.

When considering the boundaries of your microservices, first think in terms of the larger, coarse-grained contexts, and then subdivide along these nested contexts when you're looking for the benefits of splitting out these seams.

# Communication in terms of Business Concepts

If our systems are decomposed along the bounded contexts that represent our domain, the changes we want are more likely to be isolated to one, single microservice boundary. This reduces the number of places we need to make a change, and allows us to deploy that change quickly.

