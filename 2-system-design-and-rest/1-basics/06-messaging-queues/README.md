# Messaging Queues

Queues are used to effectively manage requests in large-scale distributed system, in which different components of the system may need to work in an asynchronous way.

This is an abstraction between the client' request and the actual work performed to solve it.

They are implemented on the asynchronous communication protocol.
![](https://github.com/aditya109/designs-for-software-designers/raw/main/assets/smsq.svg)

The following is a typical implementation of a system without messaging queue.

![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/typicalsystemswithoutmq.svg)

The issue here is as requests increases more and more, the load on management system would increase, to the point where it would ultimately stop taking in requests as it would not have any resources to process the request. This is bad for business as it would cause customers to loose interest thereby declining popularity of the business. We wouldn't want that right ?

We would take implement the inherent idea behind producer-consumer problem using messaging queues.

The following is a simple implementation of the above.

 ![](https://raw.githubusercontent.com/aditya109/designs-for-software-designers/main/assets/asyncsystemwithmq.svg)

Now the brunt of the load is taken off by the messaging queues.

## Kafka - a scalable option

1. Kafka is fast and uses IO efficiently by batching and compressing records.
2. Kafka is used by decoupling data streams.
3. Kafka is used to stream data into data lakes, and RT analysis streams.

4. Kafka clusters retain all published records. If limit is not set, it keeps records until disk space runs out.



