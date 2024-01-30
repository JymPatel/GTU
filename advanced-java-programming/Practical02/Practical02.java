package Practical02;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Practical02 {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306",
                    "root", "");

            Statement statement = con.createStatement();
            String query = "CREATE DATABASE diet";

            statement.execute(query);
            // int i = statement.executeUpdate(query);
            // System.out.println("total no. of rows updated=" + i);

            statement.close();
            con.close();
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }

}
