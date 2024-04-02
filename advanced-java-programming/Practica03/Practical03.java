package Practica03;
import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.sql.*;

@WebServlet("/InsertDataServlet")
public class InsertDataServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String enrolment = request.getParameter("enrolment");
        String studentName = request.getParameter("student_name");
        String branch = request.getParameter("branch");
        String year = request.getParameter("year");
        
        Connection con = null;
        PreparedStatement ps = null;
        
        try {
            // Load the Access JDBC driver
            Class.forName("net.ucanaccess.jdbc.UcanaccessDriver");
            
            // Establish the connection
            con = DriverManager.getConnection("jdbc:ucanaccess://path/to/your/access/database.accdb");
            
            // Prepare the statement
            String query = "INSERT INTO Student (ENROLMENT, STUDENT_NAME, BRANCH, YEAR) VALUES (?, ?, ?, ?)";
            ps = con.prepareStatement(query);
            
            // Set the parameters
            ps.setString(1, enrolment);
            ps.setString(2, studentName);
            ps.setString(3, branch);
            ps.setString(4, year);
            
            // Execute the update
            ps.executeUpdate();
            
            // Close resources
            ps.close();
            con.close();
            
            // Redirect to a success page
            response.sendRedirect("success.html");
        } catch (Exception e) {
            e.printStackTrace();
            // Redirect to an error page
            response.sendRedirect("error.html");
        }
    }
}
