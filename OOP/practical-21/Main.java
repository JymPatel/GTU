import java.io.*;
import java.math.MathContext;
import java.util.*;
import static java.lang.Math.*;

class Main {
    public static void main(String[] args) {
        // get file
        File file = new File("123.txt");

        // create file if it doesn't exits
        try {
            if (!file.exists()) file.createNewFile(); 
        }
        catch (Exception e) {
            System.out.println(e);
        }

        // get 150 words
        String one50Words = "";
        for (int i = 0; i < 150; i++){
            int temp = (int)(random() * 1000);
            one50Words += Integer.toString(temp) + '\n';
        }
        
        // write in file
        try {
            FileWriter outputFile = new FileWriter("123.txt");
            outputFile.write(one50Words);
            outputFile.close();
            System.out.println("written 150 words in 123.txt");
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }
}
