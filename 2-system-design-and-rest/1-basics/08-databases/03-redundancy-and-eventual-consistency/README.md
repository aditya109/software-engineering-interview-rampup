# Redundancy

Redundancy is duplication of critical data or services with the intention of increased reliability of the system.

**Use-case**: *High availability with no single point of failure.*

*Server failover*: Remove single points of failure and provide backups.

*Shared-nothing architecture:* 

- Each node can operate independently of one another.
- No central service managing state or orchestrating activities.
- New services can be added without special conditions or knowledge.
- No single point of failures.

# Eventual Consistency

![](https://github.com/aditya109/designs-for-software-designers/raw/main/assets/db.svg)

Read(x)1 operation = 600 (inconsistent at 11.05 am)    		⬇️<br/>
Read(x)2 operation = 500 (inconsistent at 11.05 am)            ⬇️ <br/>Read(x)1 operation = 600 (inconsistent at 11.20 am)            ⬇️ (*Convergence*) <br/>
Read(x)2 operation = 600  (inconsistent at 11.20 am)           ⬇️ *Eventual consistency*<br/>

| Eventual Consistency  | Strong Consistency |
| --------------------- | ------------------ |
| Lazy backup or update | Quick update       |
| Low consistency       | High consistency   |
| Low latency           | High latency       |

