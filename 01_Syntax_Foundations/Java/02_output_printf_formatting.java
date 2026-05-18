import java.util.Scanner;

public class printf {
    public static void main(String[] args) {
        // printf used to insert variables , round doubles etc etc
        String name = "Jack";
        int age = 20;
        char firstLetter = 'J';
        double height = 180;
        System.out.printf("hello %s\n", name); // % means you can now input direct vriables
        System.out.printf("i am %d\n ", age, " years old"); // you must define the datatype of the variable you are
                                                            // placing
        System.out.printf("the first letter of my name is %c\n", firstLetter); // s=strng , d=int,f = double and char=c
        System.out.printf("you are %.2f centimeters tall\n ", height);
        System.out.printf("hi my name is %s and i am %d years old\n ", name, age); // can input multiple values

        // compund interest calculator
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter rate of interest here: ");
        double rateofInterest = scanner.nextDouble();
        System.out.println("Enter number of years you will be compunding this amount");
        int numofYears = scanner.nextInt();
        System.out.println(" Enter your intial value of investement");
        double initValue = scanner.nextDouble();
        System.out.println("Enter the nuber of times the amount will be compunded yearly");
        double numofTimes = scanner.nextDouble();
        double result = Math.pow(1 + rateofInterest / 100, numofYears * numofTimes) * initValue;
        System.out.printf("your final amount after compounding for %d years at a  %f interest is $%.2f\n", numofYears,
                rateofInterest, result);

        scanner.close();

    }

}
