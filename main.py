"""Entry point for Desktop Calculator"

import sys
from calculator import CalculatorApp

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"\nRunning tests: {sys.argv[1:]}")
        import pytest
        pytest.main(sys.argv[1:])
    else:
        app = CalculatorApp()
        app.run()"