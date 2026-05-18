import java.util.Scanner;

public class Arithmetic_operators {
    public static void main(String[] args) {
        int x = 10;
        int y = 20;
        System.out.println(x + y); // addition
        System.out.println(x - y); // substraction
        System.out.println(x * y); // multiplication
        System.out.println(x / y); /*
                                    * division if you dividing integers java will return an int value only
                                    * if u divide in floats/double itll return float value
                                    */
        System.out.println(x % y); // returns remainder of a division

        // increment and decrement operators
        x++; // increase by 1
        System.out.println(x);
        x--; // decrease by 1
        System.out.println(x);
        // useful math operations in java
        System.out.println(Math.PI);
        System.out.println(Math.E);
        double a = Math.pow(2, 3); // .pow(x,y) = x^y
        System.out.println(a);
        System.out.println(Math.abs(-5)); // abs returns only positve values
        double b;
        b = Math.sqrt(9);
        b = Math.round(3.245867);
        b = Math.ceil(3.1456);
        b = Math.floor(3.1456);
        b = Math.max(1, 3);
        b = Math.min(1, 3);

        // pythogrean theorum
        Scanner scanner = new Scanner(System.in);
        System.out.println("enter a number: ");
        double c = scanner.nextDouble();
        System.out.println("enter a number: ");
        double d = scanner.nextDouble();
        double result = (Math.sqrt(Math.pow(c, 2) + Math.pow(d, 2)));
        System.out.println(result);
        // area of a circle
        System.out.println("Enter length of radius ");
        double radius = scanner.nextDouble();
        double area = radius * Math.PI * 2;
        System.out.println(area + "cm^2");
        // area and volume of a shpere
        System.out.println("Enter length of radius1 ");
        double radius1 = scanner.nextDouble();
        double surfaceArea = 4 * Math.PI * Math.pow(radius1, 2);
        double volume = 4 / 3 * Math.PI * Math.pow(radius1, 3);
        System.out.printf("the surface area of this sphere is: %.2fcm^2\n", surfaceArea);
        System.out.printf("the volume of this sphere is:%.2fcm^3\n ", volume);

        scanner.close();
    }

}
