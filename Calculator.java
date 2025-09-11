public final class Calculator {
    private Calculator() {}

    public static double add(double a, double b) {
        return a + b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        // Handle division by zero explicitly
        if (b == 0.0) {
            throw new IllegalArgumentException("Division by zero");
        }
        return a / b;
    }

    public static double power(double a, double b) {
        // Reject negative base with non-integer exponent (no real result)
        if (a < 0 && !isInteger(b)) {
            throw new IllegalArgumentException(
                "Negative base with non-integer exponent has no real-valued result"
            );
        }
        return Math.pow(a, b);
    }

    public static double calculate(String operation, double num1, double num2) {
        if (operation == null) {
            throw new IllegalArgumentException("Operation cannot be null");
        }
        switch (operation) {
            case "add":
                return add(num1, num2);
            case "subtract":
                return subtract(num1, num2);
            case "multiply":
                return multiply(num1, num2);
            case "divide":
                return divide(num1, num2);
            case "power":
                return power(num1, num2);
            default:
                throw new IllegalArgumentException("Unknown operation: " + operation);
        }
    }

    private static boolean isInteger(double x) {
        // Tolerant check for integer-valued double
        return Math.abs(x - Math.rint(x)) < 1e-10;
    }
}
