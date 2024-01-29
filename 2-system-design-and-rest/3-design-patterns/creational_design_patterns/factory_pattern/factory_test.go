package factory_pattern

import (
	"strings"
	"testing"
)

func TestGetPaymentCash(t *testing.T) {
	payment, err := GetPaymentMethod(Cash)
	if err != nil {
		t.Fatal("a payment method of type 'Cash' must exist")
	}
	msg := payment.Pay(10.30)
	if !strings.Contains(msg, "paid using cash") {
		t.Error("the cash payment method message wasn't correct")
	}
	t.Log("LOG:", msg)
}

func TestGetPaymentMethodDebitCard(t *testing.T) {
	payment, err := GetPaymentMethod(DebitCard)
	if err != nil {
		t.Fatal("a payment method of type 'DebitCard' must exist")
	}
	msg := payment.Pay(22.30)
	if !strings.Contains(msg, "paid using debit card") {
		t.Error("the debit card payment method message wasn't correct")
	}
	t.Log("LOG:", msg)
}

func TestGetPaymentMethodNonExistent(t *testing.T) {
	_, err := GetPaymentMethod(3)
	if err == nil {
		t.Fatal("a payment method with ID 3 must return an error")
	}
	
	t.Log("LOG:", err)
}
