from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    def pay(selfself,amount):
        pass
class UPI(PaymentMethod):
    def pay(self,amount):
        print(f"paid: {amount} via UPI")
upi=UPI()
upi.pay(100)


