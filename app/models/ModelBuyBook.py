from .entities.Purchasing import Purchasing
from .entities.Books import Books


class ModelBuyBook():

    @classmethod
    def register_book_purchase(self, connection, book_purchase, pymysql):
        try:
            connection_db = connection

            with connection_db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""INSERT INTO PURCHASING (UUID, BOOK_ISBN, USERID)
                                       VALUES(uuid(), '{0}', {1})""".format(book_purchase.book.isbn, book_purchase.user.id)
                               )

                connection_db.commit()

                return True

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def list_user_purchases(self, connection, pymysql, user):
        try:
            connection_db = connection

            with connection_db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                                  SELECT purchasing.date, books.isbn, books.title,
                                         books.price
                                    FROM PURCHASING purchasing
                              INNER JOIN BOOKS books 
                                 ON purchasing.book_isbn = books.isbn
                              WHERE purchasing.userID = {0}""".format(user.id)
                               )

                data = cursor.fetchall()

                books_purchased = []

                for row in data:
                    book = Books(row['isbn'], row['title'],
                                 None, None, row['price'])
                    purchasing = Purchasing(None, book, user, row['date'])

                    books_purchased.append(purchasing)
                
                return books_purchased

        except Exception as ex:
            raise Exception(ex)
