import java.util.Scanner;

public class input {
    public static void main(String[] args) {
        System.out.println("i am him");
        Scanner scanner = new Scanner(System.in); // this tells the imported module that we are now able to accept input
        System.out.print("what is your name ?: ");
        String name = scanner.nextLine(); // to accept strings
        System.out.println("hello" + " " + name + ", " + "my name is jack");
        System.out.print("enter your age: ");
        int age = scanner.nextInt(); // too accept integers
        System.out.println("you are " + " " + age + " years old");
        System.out.print("Enter your gpa: ");
        double gpa = scanner.nextDouble(); // accepts floats
        System.out.println("you gpa is " + gpa);
        System.out.println("Are you a student:?");
        boolean isStudent = scanner.nextBoolean(); // accepts booleans
        System.out.println(isStudent);
        if (gpa > 2.5) { // conditionals just like python
            System.out.println("congrats you are eligible for enrolement here ");
        } else {
            System.out.println("you do not have a high enough grade to be a student here sorry");

        }

        // calculate area of a rectangle
        System.out.print("Enter the width here: ");
        double width = scanner.nextDouble();
        System.out.print("enter the length here: ");
        double length = scanner.nextDouble();
        System.out.println("this area is " + length * width + " cm^2");
        scanner.nextLine();

        // mad libs game

        System.out.println("Enter a adjective");
        String adj1 = scanner.nextLine();
        System.out.println("Enter a noun");
        String noun1 = scanner.nextLine();
        System.out.println("Enter a adjective");
        String adj2 = scanner.nextLine();
        System.out.println("Enter a adjective");
        String adj3 = scanner.nextLine();
        System.out.println("Enter a noun");
        String noun2 = scanner.nextLine();
        System.out.println("today i went to a " + adj1 + " zoo");
        System.out.println("there i saw a " + noun1);
        System.out.println("it was really " + adj2 + "and " + adj3);
        System.out.println(" i went back many time to visit " + noun2);
        scanner.close();

    }

}
