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
