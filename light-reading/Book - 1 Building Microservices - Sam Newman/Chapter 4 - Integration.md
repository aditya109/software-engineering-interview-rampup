# Table of Contents

- [Integration](#integration)
  * [Looking for the Ideal Integration Technology](#looking-for-the-ideal-integration-technology)
    + [Avoid Breaking Changes](#avoid-breaking-changes)
    + [Keep Your APIs Technology Agnostic](#keep-your-apis-technology-agnostic)
    + [Make Your Service Simple for Consumers](#make-your-service-simple-for-consumers)
    + [Hide Internal Implementation Detail](#hide-internal-implementation-detail)
  * [Interfacing with Customers](#interfacing-with-customers)
  * [The Shared Database](#the-shared-database)
  * [Synchronous Versus Asynchronous](#synchronous-versus-asynchronous)
  * [Orchestration Versus Choreography](#orchestration-versus-choreography)
  * [Remote Procedural Calls](#remote-procedural-calls)
    + [Technology Coupling](#technology-coupling)
    + [Local Calls Are Not Like Remote Calls](#local-calls-are-not-like-remote-calls)
    + [Brittleness](#brittleness)
    + [Is RPC terrible ?](#is-rpc-terrible--)
  * [REST](#rest)
    + [REST and HTTP](#rest-and-http)
    + [Hypermedia As the engine of Application State](#hypermedia-as-the-engine-of-application-state)
    + [JSON, XML or Something Else ?](#json--xml-or-something-else--)
    + [Beware too Much Convenience](#beware-too-much-convenience)
    + [Downsides to REST Over HTTP](#downsides-to-rest-over-http)
  * [Implementing Asynchronous Event-Based Collaboration](#implementing-asynchronous-event-based-collaboration)
    + [Technology Choices](#technology-choices)
    + [Complexities of Asynchronous Architectures](#complexities-of-asynchronous-architectures)
  * [Services as State Machines](#services-as-state-machines)
  * [Reactive Extensions](#reactive-extensions)
  * [DRY and the Perils of Code Reuse in a Microservice World](#dry-and-the-perils-of-code-reuse-in-a-microservice-world)
    + [Client Libraries](#client-libraries)
  * [Access By Reference](#access-by-reference)
  * [Versioning](#versioning)
    + [Defer It for as long as Possible](#defer-it-for-as-long-as-possible)
    + [Catch Breaking Changes Early](#catch-breaking-changes-early)
    + [Use Semantic Versioning](#use-semantic-versioning)
    + [Coexist Different Versioning](#coexist-different-versioning)
    + [Use Multiple Concurrent Service Versions](#use-multiple-concurrent-service-versions)
  * [User Interfaces](#user-interfaces)
    + [Toward Digital](#toward-digital)
    + [Constraints](#constraints)
    + [API Composition](#api-composition)
    + [UI Fragment Composition](#ui-fragment-composition)
    + [Backend for Frontends](#backend-for-frontends)
    + [A Hybrid Approach](#a-hybrid-approach)
  * [Integrating with Third-Party Software](#integrating-with-third-party-software)
    + [Lack of Control](#lack-of-control)
    + [Customization](#customization)
    + [Integration Spaghetti](#integration-spaghetti)
    + [On Your Own Terms](#on-your-own-terms)
      - [Example: CMS as a Service](#example--cms-as-a-service)
      - [Example: The multirole CRM system](#example--the-multirole-crm-system)
    + [The Strangler Pattern](#the-strangler-pattern)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Integration

## Looking for the Ideal Integration Technology

### Avoid Breaking Changes

### Keep Your APIs Technology Agnostic

### Make Your Service Simple for Consumers

### Hide Internal Implementation Detail

## Interfacing with Customers

## The Shared Database

## Synchronous Versus Asynchronous

## Orchestration Versus Choreography

## Remote Procedural Calls

### Technology Coupling

### Local Calls Are Not Like Remote Calls

### Brittleness

### Is RPC terrible ?

## REST

### REST and HTTP

### Hypermedia As the engine of Application State

### JSON, XML or Something Else ?

### Beware too Much Convenience

### Downsides to REST Over HTTP

## Implementing Asynchronous Event-Based Collaboration

### Technology Choices

### Complexities of Asynchronous Architectures

## Services as State Machines

## Reactive Extensions

## DRY and the Perils of Code Reuse in a Microservice World

### Client Libraries

## Access By Reference

## Versioning

### Defer It for as long as Possible

### Catch Breaking Changes Early

### Use Semantic Versioning

### Coexist Different Versioning

### Use Multiple Concurrent Service Versions

## User Interfaces

### Toward Digital

### Constraints

### API Composition

### UI Fragment Composition

### Backend for Frontends

### A Hybrid Approach

## Integrating with Third-Party Software

### Lack of Control

### Customization

### Integration Spaghetti

### On Your Own Terms

#### Example: CMS as a Service

#### Example: The multirole CRM system

### The Strangler Pattern