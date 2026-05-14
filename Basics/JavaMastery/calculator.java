import java.util.Scanner;

public class calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        calcLoop: while (true) {
            System.out.println("Enter a number:");
            double num1 = scanner.nextDouble();
            
            System.out.println("Enter another number:");
            double num2 = scanner.nextDouble();
            
            System.out.println("Choose an arithmetic operator (+, -, *, /, ^) or 0 to exit:");
            // FIX 1: Use .next() to ignore the leftover newline character
            String operator = scanner.next(); 
            
            double resultAdd = num1 + num2;
            double resultSub = num1 - num2;
            double resultMulti = num1 * num2;
            double resultDivi = num1 / num2;
            double resultPow = Math.pow(num1, num2);
            
            switch (operator) {
                case "+" -> System.out.println("Result: " + resultAdd);
                case "-" -> System.out.println("Result: " + resultSub);
                case "*" -> System.out.println("Result: " + resultMulti);
                case "/" -> System.out.println("Result: " + resultDivi);
                case "^" -> System.out.println("Result: " + resultPow);
                case "0" -> {
                    System.out.println("Exiting calculator...");
                    break calcLoop; 
                }
                // FIX 3: Re-add default case to catch typos
                default -> System.out.println("Invalid operator selected. Try again."); 
            }
            
            System.out.println(); // Prints a blank line for clean spacing before the next loop
            
        } // Loop ends here
        
        // FIX 2: Move scanner.close() OUTSIDE the while loop
        scanner.close(); 
        System.out.println("Program finished.");
    }
}
