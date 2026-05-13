

public class App {
    public static void main(String[] args) {
        String name = "Jack";
        System.out.println(name);
        int length = name.length();
        System.out.println(length);
        char letter = name.charAt(1); // reutrn the character existing at a specific index location
        System.out.println(letter);
        int index = name.indexOf("C"); // locates the index each character exists at
        System.out.println(index);
        int lastIndex = name.lastIndexOf("o"); // locates the last index a character is located at
        System.out.println(lastIndex);
        name = name.toUpperCase(); //makes whole string UPPERCASE
        System.out.println(name);
        name = name.toLowerCase();
        name = name.replace("o","e"); //replace(x,y) means replace x with y
        System.out.println(name);
        System.out.println(name.isEmpty()); // returns bolean
        if(name.isEmpty()){
            System.out.println("you name is empty");
        
        }
        else{
            System.out.println("hello " +" "+name);

        }
        if(name.contains(" ")){
            System.out.println(" you have a space in your name");

        }
        else{
            System.out.println("You dont have a space in your name");
        }

        if(name.equals("password")){
            //equals checks too see if a string is the same as another char by char
            System.out.println("your name cant be your password");
        }
        else{
             System.out.println("hello" + " "+ name);
        }
        //.substring() used to extract a portion of the substring 
        // .substring(start,end)
        String email ="123@hotmail.org";
        String username = email.substring(0,6);
        String domain = email.substring(4); //if no end index is defined itll print everything after the starting index
        System.out.printf("my domain is %s\n" ,domain);
        System.out.printf("my username is %s\n" ,username);
        


    
    
    
    
    
    
    
    
    
    
    
    }

}

        

        




        
        


    
