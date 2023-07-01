from .entities.Users import Users
from .entities.UsersTypes import UsersTypes


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

                if user_data != None:
                    password_match = Users.verify_password(
                        user_data['PASSWORD'], user.password)

                    if password_match:
                        user_loged = Users(
                            user_data['USERID'], user_data['USER_NAME'], None, None)

                        return user_loged
                    else:
                        return None
                else:
                    return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_by_id(self, connection, pymysql, user_id):
        try:
            connection_db = connection

            with connection_db.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""SELECT users.USERID, users.USER_NAME,
                                         usersTypes.USER_TYPEID, usersTypes.USER_TYPE_NAME
                                    FROM USERS users INNER JOIN USERS_TYPES usersTypes
                                      ON users.USER_TYPEID = usersTypes.USER_TYPEID
                                   WHERE users.USERID = {0}""".format(user_id)
                               )

                user_data = cursor.fetchone()

                user_type = UsersTypes(
                    user_data['USER_TYPEID'], user_data['USER_TYPE_NAME'])

                user_loged = Users(
                    user_data['USERID'], user_data['USER_NAME'], None, user_type)

                return user_loged

        except Exception as ex:
            raise Exception(ex)
