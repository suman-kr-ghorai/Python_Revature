import math

def calculate(expression:str)->float:
    
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return float(result)
    except ZeroDivisionError:
        print("Error:division by zero not allowed")
    except Exception as e:
        print(f"Error: Invalid expression ({e})e")