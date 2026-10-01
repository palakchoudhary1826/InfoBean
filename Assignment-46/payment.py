

from abc import ABC, abstractmethod


class Payment(ABC):
 def __init__(self,customer_name,order_id,order_amount):
    self.customer_name=customer_name
    self.order_id=order_id
    self.order_amount=order_amount
    @abstractmethod
    def validate_payment():
       pass

    def calculate_processing_fee():
        pass

    def authenticate_payment():
        pass

    def process_payment():
        pass

    def generate_receipt():
        pass


class UPIPayment(Payment):
    def __init__(self,customer_name,order_id,order_amount,upi_id,upi_pin):
        self.upi_id=upi_id
        self.upi_pin=upi_pin
        self.method="UPI"
        super().__init__(customer_name,order_id,order_amount)
    def validate_payment(self):
        return"Validating payment details.../n Payment details validated successfully."


    def calculate_processing_fee(self):
        self.processing=0
        self.processinf_fees=self.order_amount*self.processing/100
        self.total=self.processinf_fees

        

    def authenticate_payment(self):
        return"Authenticating payment.../nAuthentication successful."


    def process_payment(self):
        return"Processing payment.../nPayment processed successfully."

    def generate_receipt(self):
        print(f"""========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer_name}
Order ID            : {self.order_id}
Payment Method      : {self.method}

Order Amount        : Rs{self.order_amount}
Processing Fee      : Rs.{self.processinf_fees}
Final Amount        : Rs.{self.processinf_fees}

Validating payment details...
Payment details validated successfully.

Authenticating payment...
Authentication successful.

Processing payment...
Payment processed successfully.

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================""")


class CreditCardPayment(Payment):
    def validate_payment():
        pass

    def calculate_processing_fee():
        pass

    def authenticate_payment():
        pass

    def process_payment():
        pass

    def generate_receipt():
        pass


class DebitCardPayment(Payment):
    def validate_payment():
        pass

    def calculate_processing_fee():
        pass

    def authenticate_payment():
        pass

    def process_payment():
        pass

    def generate_receipt():
        pass


class NetBankingPayment(Payment):
    def validate_payment():
        pass

    def calculate_processing_fee():
        pass

    def authenticate_payment():
        pass

    def process_payment():
        pass

    def generate_receipt():
        pass


class WalletPayment(Payment):
    def validate_payment():
        pass

    def calculate_processing_fee():
        pass

    def authenticate_payment():
        pass

    def process_payment():
        pass

    def generate_receipt():
        pass

