<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookie Creation</title>
</head>
<body>
    <%
        Cookie nameCookie = new Cookie("name", request.getParameter("name"));
        Cookie passCookie = new Cookie("password", request.getParameter("password"));

        Integer validity = Integer.valueOf(request.getParameter("passVailidity"));
        passCookie.setMaxAge(60 * 60 * validity);

        response.addCookie(nameCookie);
        response.addCookie(passCookie);
    %>
    <h1>Cookies Created!!</h1>
    <a href="readCookies.jsp">Read Cookies</a>
    <a href="deleteCookies.jsp">Delete Cookies</a>
</body>
</html> 
