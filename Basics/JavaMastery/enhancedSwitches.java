import java.util.Scanner;
public class enhancedSwitches {
    public static void main(String[] args){
        //enhanced switches 
        // a way to replace many if else if blocks into a more organised manner 
        // javas version of a matchcase statement
        // instead of match case its switch case anthe
        Scanner scanner = new Scanner(System.in);
        String day = scanner.nextLine();
        switch(day){
            case "monday" -> System.out.println("this is a weekday");
            case "tuesday" -> System.out.println("this is a weekday");
            case "wednesday" -> System.out.println("this is a weekday");
            case "thursday" -> System.out.println("this is a weekday");
            case "friday" -> System.out.println("this is a weekday");
            case "saturday" -> System.out.println("this is a weekday");
            case "sunday" -> System.out.println("this is a weekday");
            default -> System.out.println("this day doesnt exist you fool");
        }
        // can comma sepearte the cases if they give same output
        
        
        
        scanner.close();
    }
}
