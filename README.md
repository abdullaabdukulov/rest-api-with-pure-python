<h1>Book API</h1>
<p>This is a simple RESTful API for managing books. The API is built using Python and the HTTP server is provided by the 'http.server' library.</p>
<h2>Installation</h2>
<p>To run the API, you need to have Python 3.7 or later installed on your system.</p>
<ol>
<li>Clone this repository:<br>


```bash
git clone https://github.com/abdullaabdukulov/rest-api-with-pure-python.git
```


</li>
<li>Change directory to the project folder:<br>

```bash
cd book-api
```

</li>
</ol>
<h2>Usage</h2>
<p>To start the server, run the following command:</p>

```python
python main.py
```

<p>The server will start running on 'http://localhost:8000'.</p>

<h2>API Endpoints<h2>
<h3>GET /books<h3>
<p1>Returns a list of all books in the database.</p1>
<p1>Example response:</p1>
```json
[
    {
        "id": 1,
        "title": "The Great Gatsby",
        "genre": "Fiction",
        "author": "F. Scott Fitzgerald",
        "price": 9.99
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "genre": "Fiction",
        "author": "Harper Lee",
        "price": 7.99
    },
    ...
]
```
<h3>GET /books/{id}</h3>
<p>Returns the details of a single book.</p>
<p>Example response:</p>

```json
{
    "id": 1,
    "title": "The Great Gatsby",
    "genre": "Fiction",
    "author": "F. Scott Fitzgerald",
    "price": 9.99
}
```

<h3>POST /books </h3>
<p>Adds a new book to the database.</p>

```json
{
    "title": "1984",
    "genre": "Science Fiction",
    "author": "George Orwell",
    "price": 6.99
}
```

<p>Example response:</p>

```json
{
    "id": "8f7062ee-be3d-11ed-a7a6-28ec950a7752"
}
```
<h1>PUT /books/{id}</h1>
<p>Updates the details of a single book.</p>
<p>Example request body:</p>

```json
{
    "title": "The Great Gatsby",
    "genre": "Literary Fiction",
    "author": "F. Scott Fitzgerald",
    "price": 11.99
}
```
<p>Example response:</p>

```json
{
    "id": "8f7062ee-be3d-11ed-a7a6-28ec950a7752"
}
```

<h2>DELETE /books/{id}</h2>
<p>Deletes a single book from the database.</p>
<p>Example response:</p>

```http request
HTTP/1.1 204 No Content
```

<h2>License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>