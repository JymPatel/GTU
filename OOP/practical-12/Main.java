import java.util.Random;


public class Main {
    public static void main(String[] args) {
        Random random = new Random(1000);
        for (int i = 0; i < 100; i++){
            int num = 50;
            while (num > 49) {
                num = random.nextInt(48) + 1;
            }
            System.out.print(num + " ");
        }
    }
}