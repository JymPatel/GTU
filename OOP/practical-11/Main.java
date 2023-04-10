import java.util.*;

public class Main {
    public static void print2DArray(int[][] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++)
                System.out.print(arr[i][j] + " ");
            System.out.println();
        }
    }

    public static void randomizeArray(int[][] arr) {
        Random r = new Random();

        for (int i = 0; i < arr.length; i++)
            for (int j = 0; j < arr[0].length; j++)
                arr[i][j] = (int) (r.nextInt(2));
    }

    public static void checkOddOnes(int[][] arr) {

        for (int loop = 0; loop < 2; loop++)
        {
            if (loop == 0) {
                System.out.print("rows having odd number of 1s are: ");
            }
            else {
                System.out.print("columns having odd number of 1s are: ");
            }
            for (int i = 0; i < arr.length; i++) {
                int rowNumber = i + 1;
                int sum = 0;
                for (int j = 0; j < arr.length; j++) {
                    if (loop == 0) sum += arr[i][j];
                    else sum += arr[j][i];
                }
                if (sum % 2 != 0) System.out.print(rowNumber + " ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        int[][] twoDArray = new int[6][6];
        randomizeArray(twoDArray);
        print2DArray(twoDArray);
        checkOddOnes(twoDArray);
    }
}