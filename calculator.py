class Calculator:
  def __init__(self, a) -> None:
    self.result = a
  def addition(self, b=0):
    self.result = self.result + b
    return self.result
  def substraction(self, b=0):
    self.result = self.result-b
    return self.result
  def division(self, b=0):
    self.result = self.result/b
    return self.result
  def multiplication(self, b=0):
    self.result = self.result*b
    return self.result
  def sqr(self):
    self.result=self.result**2
    return self.result
    
  def delete_result(self):
    self.result = 0
one_and_two = Calculator(2)
print(one_and_two.sqr())
print(one_and_two.addition(2))
print(one_and_two.substraction(2))
one_and_two.delete_result()

print(one_and_two.addition(1))

print(one_and_two.multiplication(1))
print(one_and_two.division(1))