import java.util.Random;

// rolling dice program
public class randomNumbers {

    public static void main(String[] args) {
        Random random = new Random();
        int number1;
        int number2;
        int number3;
        number1 = random.nextInt(1, 7); // generates a random input with any data type ( int, double , boolean )
        System.out.println(number1); // (1,7) are the bounds of which the random number is beeing
        number2 = random.nextInt(1, 7); // is beeing picked from the last number is exclusive
        System.out.println(number2);
        number3 = random.nextInt(1, 7);
        System.out.println(number3);

    }

}
