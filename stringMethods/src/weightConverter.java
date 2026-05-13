import java.util.Scanner;
public class weightConverter{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        
        
        while (true){
            System.out.println("option 1 :converting lbs to kgs");
            System.out.println("option 2 :converting kgs to lbs");
            System.out.println("enter an option");
            int optionInput =scanner.nextInt();
        
            if(optionInput == 1){
                System.out.println("Enter your weight(in lbs): ");
                double weight1 = scanner.nextDouble();
                weight1 = weight1/2.205;
                System.out.printf("your weight is %.2fkgs",weight1);
                break;
            }
            else if(optionInput == 2){
                System.out.println("Enter your weight(in kgs): ");
                double weight2 = scanner.nextDouble();
                weight2 = weight2*2.205;
                System.out.printf("your weight is %.2flbs",weight2);
                break;
            }
            else if(optionInput==0){
                break;
            }
            else{
            System.out.println("you have picked an invalid choice please try again");

            }
        }

       


        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        scanner.close();

    }

    }

