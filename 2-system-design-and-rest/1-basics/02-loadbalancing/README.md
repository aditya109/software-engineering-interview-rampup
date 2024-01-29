## Table of Contents

- [Load Balancing](#load-balancing)
  * [Definition and Benefits](#definition-and-benefits)
  * [Dealing with Redundancy in Load Balancers](#dealing-with-redundancy-in-load-balancers)
  * [Load Balancing Algorithms](#load-balancing-algorithms)
    + [Least Connection Method](#least-connection-method)
    + [Least Response Time Method](#least-response-time-method)
    + [Least Bandwidth Method](#least-bandwidth-method)
    + [Round Robin Method](#round-robin-method)
    + [Weighted Round Robin](#weighted-round-robin)
    + [IP Hash](#ip-hash)
    + [Consistent Hashing](#consistent-hashing)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Load Balancing

### Definition

The process of balancing load evenly on *N* servers is **Load Balancing**.

A properly implemented **load balancer** helps in the following ways:

1. It helps spread traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases.
2. Keeps tract of statuses of all the resources while distributing requests.
3. Avoids re-routing requests to a server which has the following issues:
   - elevated rate of errors,
   - non-responsiveness, and;
   - request overload.
4. Prevents single point of failure and increases, availability and responsiveness.

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/lbrole.svg)

The following diagram explains where are all the places where Load Balancers, can be placed to utilize full scalability and reliability.  

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/lbpresence.svg)

### Benefits of load balancing

A properly implemented load balancing system can have the following benefits:

1. Enhances User Experience, since continuous load distribution in turn provides *uninterrupted service*.
2. Service providers experience *less downtime* and *higher throughout*.
3. Predictive analytics to *determine bottlenecks* before they happen.
4. System admins experience *fewer failed or stressed components*.

## Dealing with Redundancy in Load Balancers

Load balancer can be a single point of failure; second load balancer can be connected to form a cluster.

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/lbredundacy.svg)

Ideally, increase in capacity linearly with servers' addition.

![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/lbcapacity.svg)

#### Types of Load Balancers

1. **Smart Client:** Adding loadbalancer functionality into your client. The setup process is really difficult.
   ![](https://raw.githubusercontent.com/aditya109/system-design/main/assets/smartclient.svg)
2. **Hardware Loadbalancer:** Dedicated Hardware for LoadBalancer. The setup process is difficult and is very expensive. For example, *Citrix NetScaler*.
3. **Software Loadbalancer:** Runs locally on each of these servers and loadbalancer services has a bound port. For example, *HAProxy*, *NginX*, etc.


## Load Balancing Algorithms

***Health check***: Attempts to connect to backend servers to ensure that server is listening; on health check failure, server is automatically removed from pool, till health check is green again.

| Algorithm                  | Explanation                                                  |
| -------------------------- | ------------------------------------------------------------ |
| Least Connection Method    | Server with fewest active connections; large number of persistent client connections. |
| Least Response Time Method | Server with fewest active connections and lowest average response time. |
| Least Bandwidth Method     | Server serving least amount of traffic in Mbps.              |
| Round Robin Method         | Servers of equal specialization (processing power) and not many persistent connections; RR of server list. |
| Weighted Round Robin       | RR of weighted processing capacities server list.            |
| IP Hash                    | Hash IP                                                      |
| Consistent Hashing         | Click [here](#consistent-hashing).                           |

### Consistent Hashing

Concept of balancing load evenly on *N servers* is **load balancing**.

###### **Problem**

Let's say we have a hash function **Φ**, which distributes load amongst our N servers connected in a cyclic manner S<sub>0</sub> => S<sub>1</sub> => S<sub>2</sub> => S<sub>3</sub> => S<sub>0</sub>, and we have *R* requests in-flow, each having random unique IDs, *i<sup>th</sup>* request getting mapped to *R<sub>i</sub>* ID.

So, a request *R<sub>i</sub>* on being hashed through, i.e., **Φ**(R<sub>i</sub>) gets mapped to a server *S<sub>j</sub>*.

Hence, load on j<sup>th</sup> server ~ `R/N` and load factor ~ `1/N`. 

###### Graph for load distribution and load shift

Let's assume *N* = 4 initially, so the load distribution amongst servers is `25%`.

Now, again with increased requests, we can increase the number of servers. Let's say we increase the number of servers by `1`, making the arrangement S<sub>0</sub> => S<sub>1</sub> => S<sub>2</sub> => S<sub>3</sub> => S<sub>4</sub> => S<sub>0</sub>.

Note, the delta shift in load distribution.

Initially, the server S<sub>0</sub> had load of `25%`. 
But now, since a new server was added, the load distribution of all servers will be forced to `20%`. The problem is `5%` load is reduced from S<sub>0</sub> and added to S<sub>1</sub>.

Now, for the server S<sub>1</sub> which also initially had a load of `25%`, `5%` new load will be added to it, while `10%` old load will be reduced from it, making it `20%` resultant.

Similarly, for S<sub>2</sub> again initially having a load of `25%`, `10%` new load will be added to it, while `15%` old load will be removed, and carried forward to the next server, similarly for S<sub>3</sub>, new load of `15%` will be added, and old load of `20%` will be removed, to make way for server S<sub>4</sub>.

Be it new load addition or old load removal, every move is counted as **𐤃 shift in load distribution**, making it total 
`+5% + (+5%+10%) + (+10%+15%) + (+15%+20%) + 20% = 100%`.

Truth is request IDs are rarely random, so **Φ**(R<sub>i</sub>) is going to be same for frequent number of times. 

So each time a server is added **𐤃 shift in load distribution** of `100%` is observed, which might not sound as bad, but imagine, each request mapping removal results entails removal of cached data, IP entries, request logs, etc. 

>  As **𐤃 shift in load distribution** increases, data in server cache goes to s**t.

###### Construction of this skewed load

On implementing just one hash function **Φ<sub>1</sub>**, the range of requests r<sub>0</sub>, r<sub>1</sub>, r<sub>2</sub>, r<sub>3</sub>, r<sub>4</sub>, ….. and r<sub>m</sub> gets mapped to respective servers S<sub>0</sub>, S<sub>1</sub>, S<sub>2</sub> and S<sub>3</sub>. 

If even of the servers fails, since load suddenly increases on the next server in RR.

###### Solution to this skewed load architecture

We implement not just one, but multiple hash functions  **Φ<sub>2</sub>**,  **Φ<sub>3</sub>**, etc. Now, we have multiple server mappings. Now even if one of the server fails, multiple servers re-distribute the load amongst themselves. This is called **Consistent hashing**.













































