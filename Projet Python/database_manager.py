import sqlite3


def connect():
    try:
        sqliteConnection = sqlite3.connect('accounts.db')
        return sqliteConnection
    except (Exception, sqlite3.Error) as error:
        print('There was an error trying to connect to the DB, the error message is as follows: ', error)


def store_passwords(givenpassword, givenemail, givenuser, givenurl, givenname):
    try:
        conn = connect()
        cursor = conn.cursor()
        print("Successfully Connected to DB\n")

        sql_insert_query = "insert into accounts(password, email, username, url, app_name) VALUES( ?, ?, ?, ?, ?)"
        query_variables = (givenpassword, givenemail, givenuser, givenurl, givenname)
        cursor.execute(sql_insert_query, query_variables)

        conn.commit()
        print("Data inserted successfully into DB ")
        cursor.close()

    except (Exception, sqlite3.Error) as error:
        print("Failed to insert data into DB, the error message is as follows: ", error)
    finally:
        if (conn):
            conn.close()
            print("Successfully close DB\n")


def retrieve_app_password(app_name):
    try:
        conn = connect()
        cursor = conn.cursor()

        sql_select_query = "SELECT password FROM accounts WHERE app_name = ?"
        query_variables = (app_name,)
        cursor.execute(sql_select_query, query_variables)

        conn.commit()
        result = cursor.fetchall()

        print('Your password is: ', result[0][0])

    except (Exception, sqlite3.Error) as error:
        print("Failed to fetching data from DB, the error message is as follows: ", error)
    finally:
        if (conn):
            conn.close()


def retrieve_password_for_account(user_email):
    data = ('Password = ', 'Email = ', 'Username = ', 'url = ', 'nickname = ')
    try:
        conn = connect()
        cursor = conn.cursor()

        sql_select_query = "SELECT password, email, username, url, app_name, id FROM accounts WHERE email = ?"
        query_variables = (user_email,)
        cursor.execute(sql_select_query, query_variables)

        conn.commit()
        result = cursor.fetchall()

        print('_' * 50)
        print('SEARCH RESULT:')
        print('_' * 50)
        x = 1
        for rows in result:
            print('#' * 60)
            print(' ' * 25 + 'Account #', x)
            print('')
            for i in range(0, len(rows) - 1):
                print(' ' * 20 + data[i] + rows[i])
            x += 1
            print('#' * 60)
            print('')
        print('')
        print('_' * 30)

    except (Exception, sqlite3.Error) as error:
        print("Failed to fetching data from DB, the error message is as follows: ", error)
    finally:
        if (conn):
            conn.close()


def verify_app_name(app_name):
    try:
        conn = connect()
        cursor = conn.cursor()

        sql_select_query = "SELECT app_name FROM accounts WHERE app_name = ?"
        query_variables = (app_name,)
        cursor.execute(sql_select_query, query_variables)

        conn.commit()
        result = cursor.fetchall()

        if app_name in result[0][0]:
            return True

        else:
            return False
    except (Exception, sqlite3.Error) as error:
        print(" beep Failed to fetching data from DB, the error message is as follows: ", error)
    finally:
        if (conn):
            conn.close()

# find_users('saskia@mail')
# find_password('FACEBOOK')
