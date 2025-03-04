import logging
from utils.validator import is_valid_expression
from utils.calculator import calculate


LOG_FILE = "logs/app.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    print("Welcome to the Mathematical Expression Validator and Calculator")
    
    while True:
        expression = input("Enter a expression (or 'exit' to quit): ").strip()

        if expression.lower() == "exit":
            print("Goodbye!")
            logging.info("Exiting program.")
            break

        if is_valid_expression(expression):
            logging.info(f"Valid exp: {expression}")
            result = calculate(expression)
            if result is not None:
                print(f"Result: {result}")
                logging.info(f"Result  is {result}")
        else:
            print("Invalid expression.")
            logging.error(f"Invalid expression: {expression}")

if __name__ == "__main__":
    main()
