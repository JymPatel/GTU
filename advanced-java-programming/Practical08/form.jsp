<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        
        .item {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
        
        button {
            background-color: #4caf50;
            color: white;
            padding: 8px 12px;
            border: none;
            cursor: pointer;
        }
        
        button:hover {
            background-color: #45a049;
        }
        
        #myCartBtn {
            float: right;
            margin: 10px;
        }
    </style>
</head>

<body>

    <div class="item">
        <h2>HP Pavilion x360</h2>
        <p>2-in-1 Laptop - Intel Core i5, 8GB RAM, 256GB SSD</p>
        <p>Price: $899.99</p>
        <button onclick="addToCart(1)">Add to Cart</button>
    </div>

    <div class="item">
        <h2>Dell XPS 13</h2>
        <p>Ultra-Thin Laptop - Intel Core i7, 16GB RAM, 512GB SSD</p>
        <p>Price: $1499.99</p>
        <button onclick="addToCart(2)">Add to Cart</button>
    </div>

    <div class="item">
        <h2>Lenovo ThinkPad X1 Carbon</h2>
        <p>Business Laptop - Intel Core i7, 16GB RAM, 1TB SSD</p>
        <p>Price: $1799.50</p>
        <button onclick="addToCart(3)">Add to Cart</button>
    </div>

    <button id="myCartBtn" onclick="viewCart()">My Cart</button>

    <script>
        function addToCart(itemId) {
            alert('Item ' + itemId + ' added to cart!');
            // You can implement additional logic here to handle the cart functionality
        }

        function viewCart() {
            alert('View Cart functionality will be implemented here.');
            // You can implement the logic to navigate to the cart page or display the cart details
        }
    </script>

</body>

</html>