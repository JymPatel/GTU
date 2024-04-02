<!DOCTYPE html>
<html>
<head>
    <title>Employee Details Form</title>
</head>
<body>
    <h2>Employee Details Form</h2>
    <form action="../src/java/InsertDataServlet" method="post">
        <label for="emp_id">Employee ID:</label>
        <input type="text" id="emp_id" name="emp_id"><br><br>
        
        <label for="emp_name">Employee Name:</label>
        <input type="text" id="emp_name" name="emp_name"><br><br>
        
        <label for="dept">Department:</label>
        <input type="text" id="dept" name="dept"><br><br>
        
        <label for="city">City:</label>
        <input type="text" id="city" name="city"><br><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
