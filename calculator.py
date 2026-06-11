"""Core calculator logic for desktop calculator application."""

class Calculator:
    """Performs arithmetic operations with validation."""

    def __init__(self):
        self.operation_history = []

    def add(self, a, b):
        """Add two numbers."""
        self._validate_numeric(a, b)
        result = a + b
        self._log_operation(f"ADD: {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Subtract two numbers."""
        self._validate_numeric(a, b)
        result = a - b
        self._log_operation(f"SUBTRACT: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiply two numbers."""
        self._validate_numeric(a, b)
        result = a * b
        self._log_operation(f"MULTIPLY: {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Divide two numbers with zero handling."""
        self._validate_numeric(a, b)
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        # Note: Using integer division for exact results
        result = a / b
        self._log_operation(f"DIVIDE: {a} / {b} = {result}")
        return result

    def square(self, a):
        """Square a number."""
        self._validate_numeric(a, None)
        result = a ** 2
        self._log_operation(f"SQUARE: {a}² = {result}")
        return result

    def square_root(self, a):
        """Calculate square root of a number."""
        self._validate_numeric(a, None)
        if a < 0:
            raise ValueError("Square root of negative number is not allowed.")
        import math
        result = math.sqrt(a)
        self._log_operation(f"SQUARE_ROOT: √{a} = {result}")
        return result

    def power(self, a, b):
        """Raise a number to the power of another."""
        self._validate_numeric(a, b)
        result = a ** b
        self._log_operation(f"POWER: {a}^({b}) = {result}")
        return result

    def clear_history(self):
        """Clear operation history."""
        self.operation_history = []
        self._log_operation("HISTORY_CLEARED")

    def get_history(self):
        """Return operation history as list of strings."""
        return self.operation_history.copy()

    def _validate_numeric(self, *args):
        """Validate that provided arguments are numeric."""
        for arg in args:
            if not (isinstance(arg, (int, float))):
                raise ValueError(f"Invalid input: {arg}. Must be a number.")

    def _log_operation(self, operation_str):
        """Log operation to history with timestamp."""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operation_history.append(f"{timestamp} | {operation_str}")

    def display_history(self):
        """Display operation history."""
        return "\n".join(self.operation_history)


class CalculatorApp:
    """CLI interface for the calculator."""

    def __init__(self):
        self.calculator = Calculator()
        self.running = True

    def run(self):
        """Start the calculator application."""
        print("Welcome to Desktop Calculator!")
        print("Available commands: add, subtract, multiply, divide, square, sqrt, power, history, exit")

        while self.running:
            cmd = input("\nEnter command: ").strip().lower()
            try:
                if cmd in ["add", "a"]:
                    self._handle_operation(
                        lambda a, b: self.calculator.add(float(a), float(b)),
                        "addition"
                    )
                elif cmd in ["subtract", "sub", "s"]:
                    self._handle_operation(
                        lambda a, b: self.calculator.subtract(float(a), float(b)),
                        "subtraction"
                    )
                elif cmd in ["multiply", "mul", "x", "times", "t"]:
                    self._handle_operation(
                        lambda a, b: self.calculator.multiply(float(a), float(b)),
                        "multiplication"
                    )
                elif cmd in ["divide", "div", "/", "d"]:
                    self._handle_operation(
                        lambda a, b: self.calculator.divide(float(a), float(b)),
                        "division"
                    )
                elif cmd in ["square", "sq", "square_num", "nsq"]:
                    self._handle_single_operand(
                        lambda a: self.calculator.square(float(a)),
                        "square"
                    )
                elif cmd in ["sqrt", "square_root", "root"]:
                    self._handle_single_operand(
                        lambda a: self.calculator.square_root(float(a)),
                        "square root"
                    )
                elif cmd in ["power", "pow", "^", "exponent"]:
                    self._handle_double_operand()
                elif cmd in ["history", "h"]:
                    self._show_history()
                elif cmd in ["exit", "quit", "exit()", "q"]:
                    self.running = False
                    print("Exiting calculator. Goodbye!")
                elif cmd == "clear":
                    self.calculator.clear_history()
                    print("Operation history cleared.")
                else:
                    print("Unknown command. Try: add, subtract, multiply, divide, square, sqrt, power, history, exit")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def _handle_operation(self, operation_func, op_name):
        """Handle binary operations."""
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            result = operation_func(a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_double_operand(self):
        """Handle operations requiring two operands."""
        try:
            a = input("Enter base number: ")
            b = input("Enter exponent: ")
            result = self.calculator.power(float(a), float(b))
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_single_operand(self, operation_func, op_name):
        """Handle operations requiring single operand."""
        try:
            a = input("Enter number: ")
            result = operation_func(a)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    def _show_history(self):
        """Show operation history."""
        history = self.calculator.display_history()
        if not history:
            print("No operations performed yet.")
        else:
            print("\nOperation History:")
            print(history)


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()