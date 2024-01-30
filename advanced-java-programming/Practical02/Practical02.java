package Practical02;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;


public class Practical02 {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.jdbc.Driver");

Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/GTU",

"root","root");

Statement stmt=con.createStatement();

String query="update diet set Name='abc601' where Enr_no=601";

int i=stmt.executeUpdate(query);

System.out.println("total no. of rows updated="+i);

stmt.close();

con.close();
        }
        catch (Exception exception) {
            exception.printStackTrace();
        }
    }

}
