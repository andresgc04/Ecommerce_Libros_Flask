from werkzeug.security import check_password_hash

from .entities.Users import Users

class ModelUser():

    @classmethod
    def login(self, connection, user, pymysql):
        try:
            connection_db = connection

            with connection_db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""SELECT USERID, USER_NAME, PASSWORD 
                                    FROM USERS WHERE USER_NAME = '{0}'""".format(user.user_name)
                              )

                user_data = cursor.fetchone()

                password_match = check_password_hash(user_data['PASSWORD'], user.password)

                if password_match:
                    user_loged = Users(user_data['USERID'], user_data['USER_NAME'], None, None)
                    
                    return user_loged
                else:
                    return None
                
        except Exception as ex:
            raise Exception(ex)