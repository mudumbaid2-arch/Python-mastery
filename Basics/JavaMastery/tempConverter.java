import java.util.Scanner;
public class tempConverter {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        while(true){
            String option1 = " option 1 is convert temp from celcius to farenheit(type 1 if you wanna choose this)";
            System.out.println(option1);
            String option2 = "option 2: convert temp from farenheit to celcius (type 2 if you wanna choose this)";
            System.out.println(option2);
            String option3 = "option 3:if you wish to quit this program type 0";
            System.out.println(option3);
            int chooseOption = scanner.nextInt();
            if(chooseOption==1){
                System.out.println("enter the temperature here (in celcius)");
                double temp1 = scanner.nextDouble();
                temp1 = temp1*9/5+32;
                System.out.printf("you temeperature is now %.3f\n degrees farenheight", temp1);
                break;
            }
            else if (chooseOption==2){
                System.out.println("enter the temperature here (in farenheight)");
                double temp2 = scanner.nextDouble();
                temp2 = (temp2-32)*5/9;
                System.out.printf("you temeperature is now %.3f\n degrees celsius", temp2);
                break;
            }
            else if(chooseOption==0){
                break;
            }
            else{
                System.out.println("you have entered an invalid option please try again ");
            }

        }
        scanner.close();
    }
}
