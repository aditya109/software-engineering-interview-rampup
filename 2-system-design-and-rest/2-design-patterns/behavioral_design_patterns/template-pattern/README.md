# Template Pattern
## What is it ?

It defines the skeleton of an algorithm in the super-class but lets sub-classes override specific steps of the algorithm without changing its structure.
### Basic Structure

<image src="https://github.com/aditya109/software-engineering-interview-rampup/blob/main/2-system-design-and-rest/2-design-patterns/assets/template-pattern.png?raw=true"/>
### Example

```go
package main  
  
import (  
    "fmt"  
    "log")  
  
type IOtp interface {  
    genRandomOTP(int) string  
    saveOTPCache(string)  
    getMessage(string) string  
    sendNotification(string) error  
}  
  
type Otp struct {  
    iOtp IOtp  
}  
  
func (o *Otp) genAndSendOTP(otpLength int) error {  
    otp := o.iOtp.genRandomOTP(otpLength)  
    o.iOtp.saveOTPCache(otp)  
    message := o.iOtp.getMessage(otp)  
    return o.iOtp.sendNotification(message)  
}  
  
type Sms struct {  
    Otp  
}  
  
func (s *Sms) genRandomOTP(otpLength int) string {  
    randomOTP := "1234"  
    fmt.Printf("SMS: generating random OTP %s\n", randomOTP)  
    return randomOTP  
}  
  
func (s *Sms) saveOTPCache(otp string) {  
    fmt.Printf("SMS: saving OTP %s to cache\n", otp)  
}  
  
func (s *Sms) getMessage(otp string) string {  
    return "SMS OTP for login is " + otp  
}  
  
func (s *Sms) sendNotification(message string) error {  
    fmt.Printf("SMS: sending sms: %s\n", message)  
    return nil  
}  
  
type Email struct {  
    Otp  
}  
  
func (e *Email) genRandomOTP(otpLength int) string {  
    randomOTP := "1234"  
    fmt.Printf("Email: generating random OTP %s\n", randomOTP)  
    return randomOTP  
}  
  
func (e *Email) saveOTPCache(otp string) {  
    fmt.Printf("Email: saving OTP %s to cache\n", otp)  
}  
  
func (e *Email) getMessage(otp string) string {  
    return "Email OTP for login is " + otp  
}  
  
func (e *Email) sendNotification(message string) error {  
    fmt.Printf("Email: sending sms: %s\n", message)  
    return nil  
}  
  
func main() {  
    smsOTP := &Sms{}  
    o := Otp{  
       iOtp: smsOTP,  
    }  
    err := o.genAndSendOTP(4)  
    if err != nil {  
       log.Fatal(err)  
    }  
  
    emailOTP := &Email{}  
    o = Otp{  
       iOtp: emailOTP,  
    }  
    err = o.genAndSendOTP(4)  
    if err != nil {  
       log.Fatal(err)  
    }  
}
```

### Where to apply ?
- When you want to let clients extend only particular steps of an algorithm, or its structure.
- When you have several classes that contain almost identical algorithms with some minor differences. As a result, you might need to modify all classes when the algorithm changes.

#### Pros
- You can let clients override only certain parts of a large algorithm, making them less affected by changes that happen to other parts of the algorithm. 
- You can pull the duplicate code into a superclass.

#### Cons
- Some clients may be limited by the provided skeleton of an algorithm. 
- You might violate the Liskov Substitution Principle by suppressing a default step implementation via a subclass. 
- Template methods tend to be harder to maintain the more steps they have.