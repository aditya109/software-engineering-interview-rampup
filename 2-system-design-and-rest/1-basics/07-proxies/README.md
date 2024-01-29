# Proxies

A proxy server is an intermediate piece of hardware or software sitting between client and backend server, which has the capability to do the following:

1. Filter requests
2. Log requests
3. Transform requests (encrypt, compress, etc.,)
4. Cache
5. Batch requests
   - *Collapsed forwarding*: Enable multiple requests for the same URL to be processed as one request to the backend server. Collapse requests for data that is spatially close together in the storage to minimize the reads.