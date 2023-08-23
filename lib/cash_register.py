#!/usr/bin/env python3
class CashRegister:
  def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []

  def add_item(self, item, price, quantity=1):
        self.items.append(item)
        self.prices.append(price)
        self.quantities.append(quantity)
  def calculate_total(self):
        total = sum(price * quantity for price, quantity in zip(self.prices, self.quantities))
        return total

  def apply_discount(self, discount_percentage):
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        
        discount = self.calculate_total() * (discount_percentage / 100)
        return self.calculate_total() - discount
  
  def void_last_transaction(self):
        if self.items:
            self.items.pop()
            self.prices.pop()
            self.quantities.pop()
        else:
            print("No items to void")
