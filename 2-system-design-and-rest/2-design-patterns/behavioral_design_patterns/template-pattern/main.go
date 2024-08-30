package main

import (
	"fmt"
	"log"
)

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
