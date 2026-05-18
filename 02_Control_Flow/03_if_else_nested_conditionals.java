import java.util.Scanner;

public class conditionals {
    public static void main(String[] args) {
        /*
         * if statement is used to see if something holds true/fasle
         * then only you execute the next lines of code
         */
        Scanner scanner = new Scanner(System.in);
        System.out.print("enter your age: ");
        int age = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Enter you name ");
        String name = scanner.nextLine();
        System.out.println("Are you a student");
        boolean isStudent = scanner.nextBoolean();
        if (name.isEmpty()) {
            System.out.println("you didnt enter your name😡 ");
        } else {
            System.out.println("Hello" + name);
        }
        if (isStudent) {
            System.out.println("You are a student 👨‍🎓");
        } else {
            System.out.println("You arent a student");
        }

        if (age > 18 && age < 65) {
            System.out.println("You are a adult and hence eligible to vote🧑 ");
        } else if (age <= 0) {
            System.out.println("You dont exist ");
        } else if (age >= 65) {
            System.out.println("you are a seniour! 🧓");
        } else {
            System.out.println("You are still a child and you cant vote 👦🧒");

        }
        // nested conditionals

        double price = 9.99;

        System.out.println("Enter your age");
        int age1 = scanner.nextInt();
        System.out.println("Are you a Student");
        boolean isStudent1 = scanner.nextBoolean();

        if (isStudent1 == true) {
            System.out.printf(" you get a 20% discount %.2f$ ", 0.8 * price);
        }
        if (age1 > 65) {
            System.out.printf(
                    "You get a 30 percent discount on a account of beeing a student and a seniour and the new price is %.2f$",
                    0.7 * price);

        } else if (age1 > 65) {

            System.out
                    .printf("you are a seniour you get a discount of 20 percent and the price is %.2f$", price * 0.8);
        }

        else {
            System.out.printf("You get no discount and the price is %.2f$", price);
        } // REMEBER printf MEANS COMMA SEPERATOR NOT PLUS LIKE print/println

        scanner.close();

    }

}
