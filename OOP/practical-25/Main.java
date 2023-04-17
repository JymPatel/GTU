import java.io.*;


public class Main {
    public static void main(String[] args) {
        // get file
        File file = new File("words.txt");

        // check if file exists
        if (!file.exists()) {
            System.out.println("file " + file + " doesn't exists");
            return;
        }


        // read file in arr
        char[] arr = new char[1000];

        try {
            FileReader readFile = new FileReader("words.txt");
            readFile.read(arr);
            readFile.close();
        }
        catch (Exception e) {
            System.out.println(e);
        }

        // get all words
        
        // sort all words

        // print all words

        System.out.println(arr);
    }
}
