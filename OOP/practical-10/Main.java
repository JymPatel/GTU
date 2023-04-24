import java.util.*;

public class Main {
    public static int[] reverseArray(int [] arr){
        int []newArr = new int[10];
        for (int i = 0; i < 10; i++) {
            newArr[i] = arr[9 - i];
        }
        return newArr;
    };

    public static void main(String[] args) {
        int []arr = new int[10];

        Scanner scanner = new Scanner(System.in);
        System.out.println("enter 10 numbers: ");
        for (int i = 0; i < 10; i++){
            arr[i] = scanner.nextInt();
        }
        int []reversedArr = Main.reverseArray(arr);
        for (int i = 0; i < 10; i++) {
            System.out.print(reversedArr[i] + " ");
        }
        scanner.close();
    };
}