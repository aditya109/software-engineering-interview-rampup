# Proxy Design Pattern

# Composite Design Pattern

## What is it ?

Composite is a design pattern which lets you compose objects into tree structures and work with these structures as if they were individual objects.

It favors composition (HAS-A relationship) over inheritance (IS-A relationship).
It creates hierarchies and tree of objects.
Objects have different objects with their own fields and methods inside them.

### Basic Structure

<img src="../../assets/proxy-pattern.svg"></img>

### Example

<img src="../../assets/example-proxy-pattern.svg"></img>

```go
package main

import (
	"fmt"
	"net/http"
)

type Application struct{}

func (app *Application) ServeHTTP(url, method string) (int, string) {
	switch {
	case url == "/app/status" && method == http.MethodGet:
		return http.StatusOK, "Ok"
	case url == "/create/user" && method == http.MethodPost:
		return http.StatusCreated, "User Created"
	default:
		return http.StatusNotFound, "Not Found"
	}
}

type server interface {
	handleRequest(string, string) (int, string)
}

type Nginx struct {
	application       *Application
	maxAllowedRequest int
	rateLimiter       map[string]int
}

func newNginxServer() *Nginx {
	return &Nginx{
		application:       &Application{},
		maxAllowedRequest: 2,
		rateLimiter:       make(map[string]int),
	}
}

func (n *Nginx) handleRequest(url string, method string) (int, string) {
	allowed := n.checkRateLimiting(url)
	if !allowed {
		return http.StatusTooManyRequests, "Too many requests"
	}
	return n.application.ServeHTTP(url, method)
}

func (n *Nginx) checkRateLimiting(url string) bool {
	if n.rateLimiter[url] == 0 {
		n.rateLimiter[url] = 1
	}
	if n.rateLimiter[url] > n.maxAllowedRequest {
		return false
	}
	n.rateLimiter[url]++
	return true
}

func main() {
	nginxServer := newNginxServer()
	appStatusURL := "/app/status"
	createuserURL := "/create/user"

	httpCode, body := nginxServer.handleRequest(appStatusURL, "GET")
	fmt.Printf("\nUrl: %s\nHttpCode: %d\nBody: %s\n", appStatusURL, httpCode, body)

	httpCode, body = nginxServer.handleRequest(appStatusURL, "GET")
	fmt.Printf("\nUrl: %s\nHttpCode: %d\nBody: %s\n", appStatusURL, httpCode, body)

	httpCode, body = nginxServer.handleRequest(appStatusURL, "GET")
	fmt.Printf("\nUrl: %s\nHttpCode: %d\nBody: %s\n", appStatusURL, httpCode, body)

	httpCode, body = nginxServer.handleRequest(createuserURL, "POST")
	fmt.Printf("\nUrl: %s\nHttpCode: %d\nBody: %s\n", appStatusURL, httpCode, body)

	httpCode, body = nginxServer.handleRequest(createuserURL, "GET")
	fmt.Printf("\nUrl: %s\nHttpCode: %d\nBody: %s\n", appStatusURL, httpCode, body)
}
```

The output found:

```shell
Url: /app/status
HttpCode: 200
Body: Ok

Url: /app/status
HttpCode: 200
Body: Ok

Url: /app/status
HttpCode: 429
Body: Too many requests

Url: /app/status
HttpCode: 201
Body: User Created

Url: /app/status
HttpCode: 404
Body: Not Found
```


## When to apply ?

1. Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time.
2. Access control (protection proxy). This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).
3. Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.
4. Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.
5. Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.
6. Smart reference. This is when you need to be able to dismiss a heavyweight object once there are no clients that use it.

## Pros

1. You can control the service object without clients knowing about it. 
2. You can manage the lifecycle of the service object when clients don’t care about it.
3. The proxy works even if the service object isn’t ready or is not available.
4. Open/Closed Principle. You can introduce new proxies without changing the service or clients.

## Cons

1. The code may become more complicated since you need to introduce a lot of new classes.
2. The response from the service might get delayed.

