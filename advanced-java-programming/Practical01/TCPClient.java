package Practical01;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.InetAddress;
import java.net.Socket;

public class TCPClient {
    public static void main(String[] args) {
        String message = "Hello, Server!";
        DataInputStream dataInputStream = new DataInputStream(System.in);
        try {
            Socket socket = new Socket(InetAddress.getByName("localhost"), 8000);

            OutputStream outputStream = socket.getOutputStream();
            PrintStream printStream = new PrintStream(outputStream);

            while (!message.equals("Over and Out!")) {
                message = dataInputStream.readLine();
                printStream.println(message);
            }
            printStream.close();
            socket.close();
        } catch (IOException unknownHostException) {
            unknownHostException.printStackTrace();
        }
    }
}
