package Practical1;

import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class UDPServer {
     public static void main(String[] args) {
        try {
            DatagramSocket datagramSocket = new DatagramSocket(8001);
            byte buffer[] = new byte[1024];
    
            DatagramPacket datagramPacket = new DatagramPacket(buffer, 1024);
            datagramSocket.receive(datagramPacket);
    
            String str = new String(datagramPacket.getData(), 0, datagramPacket.getLength());
            System.out.println(str);
    
            datagramSocket.close();
         }
         catch (Exception e) {
            e.printStackTrace();
         }
     }
}
