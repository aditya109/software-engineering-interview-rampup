## Table of Contents

- [Caching](#caching)
  - [Definition](#definition)
  - [Why use Caching ?](#why-use-caching--)
  - [Setting Up Explanation](#setting-up-explanation)
  - [Solution to increased cache miss of request layer expansion](#solution-to-increased-cache-miss-of-request-layer-expansion)
    - [Distributed cache](#distributed-cache)
    - [Global cache](#global-cache)
  - [Content Distributed Network (CDN)](#content-distributed-network--cdn-)
  - [Cache Invalidation](#cache-invalidation)
    - [Write-through-cache](#write-through-cache)
    - [Write-around-cache](#write-around-cache)
    - [Write-back-cache](#write-back-cache)
  - [Cache Eviction Policies](#cache-eviction-policies)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Caching

## Definition

Caching is the process of storing copies of files in a cache, or temporary storage location, so that they can be accessed more quickly.

Essentially, a cache is any temporary storage location for copies of files or data.

Web browsers cache HTML files, JavaScript and images in order to load websites more quickly, while DNS servers cache DNS records for faster lookups and CDN servers cache content to reduce latency.

## Why use Caching ?

The reason we use Caching -

- Taking advantage of the locality of reference principle _"Recently requested data is likely to be requested again"._

Caching exists at all levels in architecture, but often found at the level nearest to the frontend.

## Setting Up Explanation

**Application Server Cache**

1. Cache placed on a request layer node.
2. When a request layer node is expanded to many nodes.
   - Load balancers randomly distributes requests across the nodes.
   - The same request can go to different nodes.
   - Increase cache miss
     - Distributed cache (solution).
     - Global cache.

## Solution to increased cache miss of request layer expansion

### Distributed cache

- Each request layer node owns part of cache data.
- Entire cache is divided up using a consistent hash function.

_PROS_

Cache space can be increased easily by adding more nodes to the request pool.

_CONS_

A missing node leads to fractional cache loss.

### Global cache

A server or file store that is faster than original store, and accessible by all request layer nodes.

**_Common forms_**

1. **Cache server handles cache miss**
   - Used by most applications
2. **Request nodes handle cache miss**
   - Have a large percentage of hot data set in the cache.
   - An architecture where the files stored in the cache are static and shouldn't be evicted.
   - Application logic understands the eviction strategy or hotspots better than the cache.

## Content Distributed Network (CDN)

For sites, serving large amounts of static media usually follow the given process.

**For such a large system,**

1. A request first asks the CDN for a piece of static media.
2. CDN servers that contents if it has it locally available.
3. If content isn't available , CDN will query backend servers for the file, cache it locally and serve it to the requesting user.

**For not a CDN-large system,**

1. Serving static media off a separate subdomain using a lightweight HTTP server.
2. Cutover DNS from this subdomain to a CDN later.

## Cache Invalidation

Keep cache coherent with the source of truth. Invalidate cache which source of truth has changed.

### Write-through-cache

Data is written into the cache and permanent storage at same time.

| PROS                                                   | CONS                          |
| ------------------------------------------------------ | ----------------------------- |
| Fast retrieval.                                        | High latency.                 |
| Complete data consistency robust to system disruption. | Latency for write operations. |

### Write-around-cache

Data is written to permanent storage, not cache.

| PROS                                      | CONS                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------ |
| Reduces the cache that is no longer used. | Query for recently written data creates a cache miss and higher latency. |

### Write-back-cache

Data is written only to cache; later on to permanent storage.

| PROS                                             | CONS                                            |
| ------------------------------------------------ | ----------------------------------------------- |
| Low latency.                                     | Risk of data loss in ease of system disruption. |
| High throughout for write-intensive application. |                                                 |

## Cache Eviction Policies

- FIFO (**F**irst-**I**n-**F**irst-**O**ut)
- LIFO (**L**ast-**I**n-**F**irst-**O**ut)
- LRU (**L**east **R**ecently **U**sed)
- MRU (**M**ost **R**ecently **U**sed)
- LFU (**L**east **F**requently **U**sed)
- RR (**R**ound **R**obin)
