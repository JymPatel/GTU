package Practical1;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPClient {
    public static void main(String[] args) {
        try {
            String message = "Hello, World!";
            
            DatagramSocket datagramSocket = new DatagramSocket();
            DatagramPacket datagramPacket = new DatagramPacket(message.getBytes(), message.getBytes().length, InetAddress.getByName("localhost"), 8001);
            datagramSocket.send(datagramPacket);
            datagramSocket.close();
        }
        catch (Exception exception) {
            exception.printStackTrace();
        }
    }
}
