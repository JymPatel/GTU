<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Creation</title>
</head>
<body>
    <%
        Cookie[] cookies = null;
        cookies = request.getCookies();
        out.print("Cookies Found: <br />");
        for (Cookie cookie: cookies) {
               out.print("Name : " + cookie.getName( ) + ",  ");
               out.print("Value: " + cookie.getValue( )+" <br/>");
            }
    %>
    <a href="deleteCookies.jsp">Delete Cookies</a>
</body>
</html> 
