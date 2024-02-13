<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Welcome Page</title>
</head>
<body>

<%
    // Retrieve parameters from the URL
    String linkName = request.getParameter("name");
    String city = request.getParameter("city");

    // Check if parameters are not null
    if (linkName != null && city != null) {
%>

    <h2>Link Name: <%= linkName %></h2>
    <h2>City: <%= city %></h2>

<%
    } else {
%>

    <h2>Parameters not provided.</h2>

<%
    }
%>

</body>
</html>
