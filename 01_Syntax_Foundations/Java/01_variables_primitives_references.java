public class Main {
    public static void main(String[] args) {
        // first Java Program!!!
        System.out.println("Hello world"); // println outputs each input on a new line unline normal print
        System.out.println("i love pasta!");
        System.out.println("I play basketball");

        /*
         * Variables is a container that stores values
         * 2 types
         * Primitive - int boolean char double , stored directly in the momery(stack)
         * reference - string array object , memory adress sotred directly in the heap
         */
        int age = 30;
        System.out.println("i am " + age + " " + "years old "); // placing a variable in between a str output
        double pi = 2.345678; // " " = space in a print statement
        System.out.println("my favorite pie is " + pi);
        boolean isRunning = true;
        System.out.println(isRunning);
        char Alphabet = 'A';
        System.out.println(Alphabet);
        String name = "jack";
        System.out.println("my name is " + name);
        double age1 = 23; // can store integers as doubles but not the other way around
        System.out.println(age1);
        String email = "123fake@gmail.com"; // string can contain numbers as well all are treated a characters
        System.out.println("my email is " + email);

    }

}