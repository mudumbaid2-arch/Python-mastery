import java.util.Scanner;

public class Excercises {
    public static void main(String[] args) {
        // shopping cart program
        Scanner scanner = new Scanner(System.in);

        System.out.print("What item would you like to purchase?: ");
        String items = scanner.nextLine();

        System.out.print("What is the price for each item?: ");
        double price = scanner.nextDouble();
        System.out.print("how many items will u you be purchasing today ");
        int quantity = scanner.nextInt();
        double totalAmount = quantity * price;
        System.out.println("The item you chose is " + items);
        System.out.println("The price for each " + items + " is " + price);
        System.out.println("you have purchased " + " " + quantity + " " + items);
        System.out.println("your bill costs" + " $" + totalAmount);

        scanner.close();

    }

}
