import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        // take filename from CLI
        String filepath = "";
        if (args.length > 0) {
            filepath = args[0];
        }
        System.out.println("using file " + filepath);

        // get file
        File file = new File(filepath);

        // check if file exists
        if (!file.exists()) {
            System.out.println("file " + file + " doesn't exists");
            return;
        }

        // read file using scanner
        ArrayList<String> arr=new ArrayList<String>();
        try {
            Scanner scanner = new Scanner(file);
            while (scanner.hasNext()) {
                String nextWord = scanner.next();
                boolean addWord = true;
                for (String word: arr) {
                    if (word == null) break;
                    else if (word.equals(nextWord)) {
                        addWord = false;
                        break;
                    }

                }
                if (addWord) arr.add(nextWord);
            }
            scanner.close();
        }
        catch (Exception e) {
            System.out.println(e);
        }


        // sort words
        Collections.sort(arr, Collections.reverseOrder());


        // print all words
        for (String word: arr){
            if (word != null)
            System.out.println(word);
        }
    }
}
