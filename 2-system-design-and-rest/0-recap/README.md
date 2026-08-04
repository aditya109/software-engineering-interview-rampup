# System Design Architecture Notes

## System Overview

```sh
                    ┌─────────────────────┐
                    │   User Browser      │
                    └──────────┬──────────┘
                               │
                    www.mysite.com
                               │
                    ┌──────────▼──────────┐
                    │  api.mysite.com     │
                    │  (DNS Resolution)   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   IP Address        │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Web Server        │
                    │   (R/W/D)           │
                    │   Return Data       │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
        ┌───────▼────────┐          ┌────────▼────────┐
        │ Traditional    │          │ Non-Traditional │
        │ RDBMS          │          │ DBMS            │
        └────────────────┘          └─────────────────┘
```

## Database Types

### Relational (Traditional RDBMS)

- SQL-based databases
- Supports JOIN operations

### Non-Relational (NoSQL)

**⚠️ Important Note:** Join operations are generally NOT supported in NoSQL

#### NoSQL Data Models

- **Key-Value**: Simple, fast lookups
- **Document**: JSON, XML, YAML formats
- **Graph**: Relationship-based data
- **Column**: Wide-column storage

---

## When to Use NoSQL?

Use NoSQL if:

1. **Need for super-low latency**
   - Requires minimal response time
   - High-speed data access required

2. **Data is unstructured** or you do not have any relational data
   - No strict schema requirements
   - Flexible data structure

3. **Need only for deserialization of data** (JSON, XML, YAML)
   - Simple data format conversion
   - No complex queries needed

4. **Need to store massive amount of data**
   - Scales horizontally easily
   - High data volume capacity

---

## Scaling Strategies

### Horizontal Scaling

```sh
┌─────────┐     ┌─────────┐     ┌─────────┐
│ Server1 │     │ Server2 │     │ Server3 │
└─────────┘     └─────────┘     └─────────┘
    ▲               ▲               ▲
    └───────────────┴───────────────┘
         Load Balancer
```

**Advantages:**

- No hardware limits (can add ∞ servers)
- Built-in failover and redundancy

---

### Vertical Scaling

```sh
┌─────────────────────────────┐
│      Single Server          │
│  (Increased CPU, Memory)    │
└─────────────────────────────┘
```

**Limitations:**

1. **Hard limit of hardware**
   - Cannot add infinite CPU and memory to a single server
   - Physical constraints

2. **No failover and redundancy**
   - Single point of failure
   - Downtime if server goes down

---

## Key Takeaways

- **Choose NoSQL** for high-volume, unstructured, low-latency requirements
- **Horizontal scaling** is preferred for reliability and unlimited growth
- **Vertical scaling** has inherent limitations and should be avoided as the primary strategy
