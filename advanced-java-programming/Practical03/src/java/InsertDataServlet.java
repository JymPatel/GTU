import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.sql.*;

@WebServlet("/InsertDataServlet")
public class InsertDataServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String empId = request.getParameter("emp_id");
        String empName = request.getParameter("emp_name");
        String dept = request.getParameter("dept");
        String city = request.getParameter("city");
        
        Connection con = null;
        PreparedStatement ps = null;
        
        try {
            // Load the JDBC driver
            Class.forName("com.mysql.jdbc.Driver");
            
            // Establish the connection
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/employees", "root", "");
            
            // Prepare the statement
            String query = "INSERT INTO employee_details (EMP_ID, EMP_NAME, DEPT, CITY) VALUES (?, ?, ?, ?)";
            ps = con.prepareStatement(query);
            
            // Set the parameters
            ps.setString(1, empId);
            ps.setString(2, empName);
            ps.setString(3, dept);
            ps.setString(4, city);
            
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
