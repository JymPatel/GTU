import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        String plateNumber = "";
        for (int i = 0; i < 3; i++){
            char c = (char)((int)(Math.random() * 26)+ 'A');
            plateNumber += c;
        }
        for (int i = 0; i < 4; i++){
            int c = (int)(Math.random());
            plateNumber += c;
        }
        System.out.println("your plate number is: " + plateNumber);
    }
}