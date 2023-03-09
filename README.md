
<h1>Book API</h1>
<p>This is a simple REST API for managing books. It provides basic CRUD (Create, Read, Update, Delete) operations for books.</p>
<h2>Getting started</h2>
<p>To use the API, simply run the main.py file to start the server at http://localhost:8000.</p>

<h2>Available Endpoints</h2>
<ul>
  <li>GET /books - Get a list of all books.</li>
  <li>GET /books/{id} - Get details of a specific book by ID.</li>
  <li>POST /books - Create a new book.</li>
  <li>PUT /books/{id} - Update an existing book by ID.</li>
  <li>DELETE /books/{id} - Delete an existing book by ID.</li>
</ul>

<h2>API Usage</h2>

<h3>GET /books</h3>
<p>To get a list of all books, send a GET request to /books. The API will return a JSON response containing an array of book objects.</p>

<h3>GET /books/{id}</h3>
<p>To get details of a specific book, send a GET request to /books/{id}, where {id} is the ID of the book you want to retrieve. If the book exists, the API will return a JSON response containing the book object. If the book does not exist, the API will return a 404 error.</p>

<h3>POST /books</h3>
<p>To create a new book, send a POST request to /books with the following parameters:</p>
<ul>
  <li>title (required) - The title of the book.</li>
  <li>genre (optional) - The genre of the book.</li>
  <li>author (optional) - The author of the book.</li>
  <li>price (optional) - The price of the book.</li>
</ul>
<p>The API will return a JSON response containing the ID of the newly created book.</p>

<h3>PUT /books/{id}</h3>
<p>To update an existing book, send a PUT request to /books/{id}, where {id} is the ID of the book you want to update. The request should contain the following parameters:</p>
<ul>
  <li>title (optional) - The updated title of the book.</li>
  <li>genre (optional) - The updated genre of the book.</li>
  <li>author (optional) - The updated author of the book.</li>
  <li>price (optional) - The updated price of the book.</li>
</ul>
<p>If the book exists, the API will update the book with the new values and return a JSON response containing a success message. If the book does not exist, the API will return a 404 error.</p>

<h3>DELETE /books/{id}</h3>
<p>To delete an existing book, send a DELETE request to /books/{id}, where {id} is the ID of the book you want to delete. If the book exists, the API will delete the book and return a JSON response containing a success message. If the book does not exist,
