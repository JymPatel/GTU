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
        for (Cookie cookie: cookies) {
            cookie.setMaxAge(0);
            response.addCookie(cookie);
            }
    %>
    <h1>Deleted all Cookies!!</h1>
    <a href="readCookies.jsp">Read Cookies</a>
</body>
</html> 
