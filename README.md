# Products API

This is a basic Django application that will allow basic CRUD operations on a Products database.

A single product has the below properties:
- Title: the name of the product
- Description: an extended content description of the product
- Price: the current price for the product
- Inventory Quantity: how many units of the product are currently in stock
- Image File: (optional field) a link to an online image for the product


## Endpoints
<b>localhost:8000/api/products/</b>
- GET: a GET request to this endpoint will return a list of all products in the database and their details
- POST: a POST request to this endpoint will create a new product

<b>localhost:8000/api/products/<int: pk>/</b>
- GET: a GET request to this endpoint will return the details for the product matching the passed primary key
- PUT: a PUT requst to this endpoint will update the product matching the passed primary key to match the information in the request body
- DELETE: a DELETE request to this endpoint will delete the product matching the passed primay key from the database