#Calcultor
from art import logo
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def sub(n1, n2):
  return n1 - n2

#Multiply
def mul(n1, n2):
  return n1*n2

#Divide
def div(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}
def calculator():
  """
  Returns the calculated value of given inputs.
  """
  print(logo)
  num1 = float(input("What is the first number?: "))
  for operator in operation:
     print(operator)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    check = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
    if check == "y":
      should_continue = True
      answer = num1
    else:
      print("Thank You for using the Calculator. Let's start over!!")
      calculator()
    
calculator()
                         


