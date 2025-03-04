import math
import logging

LOG_FILE = "logs/app.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate(expression:str)->float:
    
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return float(result)
    except ZeroDivisionError:
        print("Error:division by zero not allowed")
        logging.warning("Error:division by zero not allowed")
    except Exception as e:
        print(f"Error: Invalid expression ({e})e")
        logging.warning("Error:division by zero not allowed")