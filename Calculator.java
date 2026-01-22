public class Calculator {
    public static double add(double a, double b) { return a + b; }
    public static double subtract(double a, double b) { return a - b; }
    public static double multiply(double a, double b) { return a * b; }

    // Bug parity fix: explicitly throw on divide-by-zero to mirror Python error
    public static double divide(double a, double b) {
        if (b == 0.0) {
            throw new ArithmeticException("division by zero");
        }
        return a / b;
    }

    private static boolean isInteger(double x) {
        double r = Math.rint(x);
        return Math.abs(x - r) < 1e-10;
    }

    // Real-number semantics: disallow negative base with non-integer exponent
    public static double power(double a, double b) {
        if (a < 0 && !isInteger(b)) {
            throw new IllegalArgumentException("negative base with non-integer exponent has no real result");
        }
        return Math.pow(a, b);
    }

    public static double calculate(String operation, double num1, double num2) {
        switch (operation) {
            case "add":      return add(num1, num2);
            case "subtract": return subtract(num1, num2);
            case "multiply": return multiply(num1, num2);
            case "divide":   return divide(num1, num2);
            case "power":    return power(num1, num2);
            default:
                throw new IllegalArgumentException("Unknown operation: " + operation);
        }
    }
}
