package factory_pattern

import (
	"fmt"
)

/*
Create a payment solution

Acceptance criteria
- to have a common method for every payment method called pay
- to be able to delegate the creation of payment methods to the factory
- to be able to add more payment methods to the library by just adding it to the factory method
*/

type PaymentMethod interface {
	Pay(amt float32) string
}

// our current implemented payment methods are described here
const (
	Cash      = 1
	DebitCard = 2
)

/*
CreatePayment() returns a pointer to a PaymentMethod object, or an error if method is not registered.
We used "new" operator to return the pointer but we could also used &Type{} although new makes it more readable for
newcomers could be confusing.
*/

func GetPaymentMethod(m int) (PaymentMethod, error) {
	switch m {
	case Cash:
		return new(CashPaymentMethod), nil
	case DebitCard:
		return new(DebitCardPaymentMethod), nil
	default:
		return nil, fmt.Errorf("payment method %d not recognized", m)
	}
}

type CashPaymentMethod struct{}
type DebitCardPaymentMethod struct{}

func (c *CashPaymentMethod) Pay(amt float32) string {
	return fmt.Sprintf("%0.2f paid using cash\n", amt)
}
func (c *DebitCardPaymentMethod) Pay(amt float32) string {
	return fmt.Sprintf("%0.2f paid using debit card\n", amt)
}
