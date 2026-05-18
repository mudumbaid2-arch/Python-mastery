 import java.util.Scanner;
public class terneryOperator {
    public static void main(String[] args){
        //ternary operator a shortcut way to write an if else in 1 line of code

        //normal conditional
        int score=70;
        if (score>=50){
            System.out.println("PASS");
        }
        else{
            System.out.println("FAIL");

        }

        //using ternary operator 
        int score2 =30;
        String passorFail = (score2>=60) ? "Pass" : "Fail";     // coditional? if true one ouptut :if false a different output
        System.out.println(passorFail);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int number = scanner.nextInt();
        String evenorOdd =(number%2==0)? "Even" : "odd";
        System.out.println(evenorOdd);
        System.out.println("enter the time right now");
        int hours = scanner.nextInt();
        String AmorPm = (hours>12)? "PM" : "AM";
        System.out.print(AmorPm);
        


        
        
        
        
        
        scanner.close();

    }

}
