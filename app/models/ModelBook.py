from .entities.Authors import Authors
from .entities.Books import Books


class ModelBook():

    @classmethod
    def list_books(self, connection, pymysql):
        try:
            connection_db = connection

            with connection_db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute('''SELECT books.ISBN, books.TITLE, books.YEAR_EDITION, books.PRICE,
                                         authors.LAST_NAMES, authors.NAMES
                                    FROM BOOKS books INNER JOIN AUTHORS authors 
                                      ON books.authorID = authors.authorID
                                ORDER BY books.TITLE ASC''')
                books_data = cursor.fetchall()
                books = []

                for row_books in books_data:
                    author = Authors(
                        0, row_books['LAST_NAMES'], row_books['NAMES'])
                    book = Books(row_books['ISBN'], row_books['TITLE'],
                                 author, row_books['YEAR_EDITION'], row_books['PRICE'])

                    books.append(book)

                return books

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def list_sold_books(self, connection, pymysql):
        try:
            connection_db = connection

            with connection_db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute('''
                                  SELECT purchasing.book_isbn, books.title, books.price,
                                         COUNT(purchasing.book_isbn) AS units_sold
                                    FROM PURCHASING purchasing
                              INNER JOIN BOOKS books
                                      ON purchasing.book_isbn = books.isbn
                                GROUP BY purchasing.book_isbn
                                ORDER BY 4 desc, 2 asc
                                ''')

                books_sold_data = cursor.fetchall()

                books_sold = []

                for row_books_sold in books_sold_data:
                    books = Books(row_books_sold['book_isbn'], row_books_sold['title'], None, None, row_books_sold['price'])
                    books.units_sold = int(row_books_sold['units_sold'])

                    books_sold.append(books)
                
                return books_sold
                
        except Exception as ex:
            raise Exception(ex)
