# REST API

REST is an acronym for REpresentational State Transfer and an architectural style for **distributed hypermedia systems**. *It is not a protocol or a standard.*

> A Web API (or Web Service) conforming to the REST architectural style is called a *REST API*.

## Guiding Principles of REST

The six guiding principles or constraints of the RESTful architecture are:

1. Uniform Interface - The following four constraints can achieve a uniform REST interface:
   - Identification of resources 
   - Manipulation of resources through representations
   - Self-descriptive messages - Resource representations shall be self-descriptive, (media type have no relation to resource methods)
   - Hypermedia as the engine of application state - The client should only have the initial URI of the application, the client application should dynamically drive all other resources and interactions with the use of hyperlinks.
2. Client-Server - This pattern enforces the separation of concerns (user interface concern and data storage concern).
3. Stateless - Each request from client to server must contain all of the information necessary to understand and complete the request. The server should be stateless, with the session state contained within the client application.
4. Cacheable - The response should implicitly or explicitly label itself as cacheable or non-cacheable. 
5. Layered System - Allows an architecture to be composed of hierarchical layers by constraining component behaviour, each component cannot see beyond the immediate layer they are interacting with.
6. Code on Demand (optional) - Allows client functionality to extend by downloading and executing code in the form of applets or scripts.

### Terminology

| Name                | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| Resource            | Abstraction of information in REST comprises data, metadata and hypermedia links that can help the clients transition to the next desired state. |
| Resource Identifier | URI patterns                                                 |
| Resource Methods    | GET, POST, DELETE, PUT, etc.                                 |
|                     |                                                              |

> **REST != HTTP**