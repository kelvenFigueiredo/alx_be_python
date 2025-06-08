#function that performs basic arithmetic operations
def perform_operation(num1:float, num2:float, operation:str):
        match operation:
                case "add":
                    result = num1 + num2
                    return result
                case "subtract":
                    result = num1 - num2
                    return result
                case "multiply":
                    result = num1 * num2
                    return result
                case "divide":
                    if num2 != 0:
                        result = num1 / num2
                        return result
                    else:
                        return "Cannot divide by zero."
                case _: 
                    print("Invalid operator.")