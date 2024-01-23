package Practical1;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {
    public static void main(String args[]) {
        try {
            ServerSocket serverSocket = new ServerSocket(8000);
            Socket socket = serverSocket.accept();

            DataInputStream inputStream = new DataInputStream(socket.getInputStream());
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

            System.out.println("Client Connected!");
            String inpuString = "";
            while (inpuString != "stop") {
                inpuString = bufferedReader.readLine();
                if (inpuString != null) {
                    System.out.println(inpuString);
                }
            }

            socket.close();
            serverSocket.close();
        } catch (IOException ioException) {
            ioException.printStackTrace();
        }
    }
}