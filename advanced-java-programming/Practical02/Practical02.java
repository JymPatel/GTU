package Practical02;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Practical02 {
    public static void main(String[] args) {
        String query = "INSERT INTO comp31 VALUES (1, 2, 3)";
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/students",
                    "root", "");

            Statement statement = con.createStatement();

            // int i = statement.executeUpdate(query);
            // System.out.println("total no. of rows updated = " + i);

            int a = statement.executeUpdate(query);
            // statement.executeQuery(query);

                // System.out.println(resultSet);
                // System.out.println(resultSet.getString(1));
                // while (resultSet.next()) {
                //     System.out.println("hey");
                //     System.out.println(resultSet.getInt(5));
                // }
            // statement.close();
            con.close();
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }

}
