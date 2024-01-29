# C/AP Theorem

| Theme                 | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| **Consistency**       | Every read receives the most recent write or an error.       |
| **Availability**      | Every request receives a response that is not an error.      |
| **Partition Theorem** | System continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes. |

C/AP theorem implies, "*only in the presence of a network partition, one has to choose between consistency and availability.*"

