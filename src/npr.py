class calculations():

  @staticmethod
  def types_math_operations(operation):
    if(operation == '+'):
      return 1

    if(operation == '-'):
      return 1

    if(operation == '*'):
      return 2

    if(operation == '/'):
      return 2

    if(operation == '^'):
      return 3

  @staticmethod
  def calculate(operation, n1, n2):
    if(operation == '+'):
      return n1 + n2

    if(operation == '-'):
      return n1 - n2

    if(operation == '*'):
      return n1 * n2

    if(operation == '/'):
      return n1 / n2

    if(operation == '^'):
      return pow(n1, n2)


  def convert_to_npr(this, equation):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    typeOperations = ['+', '-', '*', '/', '^']

    finalEquation = []
    operations = []

    previousElement = ''

    for element in equation:
      if(str(element) in numbers):
        previousElement = previousElement + element
      
      elif(str(element) in typeOperations):
        finalEquation.append(float(previousElement))
        previousElement = ''

        if(len(operations) == 0):
          operations.append(element)
        else:
          currentOperationValue = this.types_math_operations(element)
          previousOperation = operations[len(operations) - 1]
          previousOperationValue = this.types_math_operations(previousOperation)

          while(currentOperationValue <= previousOperationValue):
            previousOperation = operations.pop()
            finalEquation.append(previousOperation)

            if(len(operations) == 0):
              break

            previousOperation = operations[len(operations) - 1]
            previousOperationValue = this.types_math_operations(previousOperation) 

          operations.append(element)

    finalEquation.append(float(previousElement))

    while(len(operations) > 0):
      finalEquation.append(operations.pop())

    return finalEquation

  def resolve_npr(this, npr):
    numbers = []

    for element in npr:
      if(type(element) == type(1.0)):
        numbers.append(element)
      else:
        secondNumber = numbers.pop()
        primaryNumber = numbers.pop()
        result = this.calculate(element, primaryNumber, secondNumber)
        numbers.append(result)

    return numbers.pop()

