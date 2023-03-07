from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from models.books import Book


class BookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/books':
            books = Book.get_all()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(books).encode('utf-8'))
        elif self.path.startswith('/books/'):
            book_id = self.path.split('/')[-1]
            book = Book.get_by_id(book_id)
            if book:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(book).encode('utf-8'))
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/books':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            book_data = json.loads(post_data.decode())
            book = Book(
                id=book_data.get('id', False),
                title=book_data['title'],
                genre=book_data['genre'],
                author_id=book_data['author_id'],
                price=book_data['price'],
            )
            print(book_data)
            book.save()
            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'id': book.id}).encode())
        else:
            self.send_error(404)

    def do_PUT(self):
        if self.path == '/books/':
            book_id = self.path.split('/')[-1]
            book = Book.get_by_id(book_id)
            if book:
                content_length = int(self.headers['Content-Length'])
                put_data = self.rfile.read(content_length)
                put_data = json.loads(put_data.decode())
                book.title = put_data['title']
                book.genre = put_data['genre']
                book.author_id = put_data['author_id']
                book.price = put_data['price']
                book.save()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Location', f'/books/{book.id}')
                self.end_headers()
                self.wfile.write(json.dumps({'id': book.id}).encode('utf-8'))
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_DELETE(self):
        if self.path == '/books/':
            book_id = self.path.split('/')[-1]
            book = Book.get_by_id(book_id)
            if book:
                book.delete()
                self.send_response(204)
                self.end_headers()
            else:
                self.send_error(404)
        else:
            self.send_error(404)


def run(server_class=HTTPServer, handler_class=BookHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print(f'Stopping server on port {port}...')


if __name__ == '__main__':
    run()
