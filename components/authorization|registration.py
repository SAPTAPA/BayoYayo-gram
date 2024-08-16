import psycopg2
#authorization|registration sys
#authorization|registration sys
#authorization|registration sys
#authorization|registration sys
#authorization|registration sys


conn = psycopg2.connect(dbname="login", user="postgres", password="postgres", host="127.0.0.1")
cursor = conn.cursor()


def createAK(name,  password):
    cursor.execute("SELECT 1 FROM users WHERE name = %s", (name,))
    exists = cursor.fetchone() is not None
    conn.commit()

    if exists:
        print("There is already such a user.")
        cursor.close()
        conn.close()
        exit()
    else:
        cursor.execute('''INSERT INTO users (name,password) VALUES (%s, %s)''',(name, password))
        conn.commit()
        print("You have registered an account.")
        cursor.close()
        conn.close()


def Login(name, password):
    cursor.execute('''SELECT name, password FROM users WHERE name=%s AND password=%s''', (name, password))

    exists = cursor.fetchone() is not None
    conn.commit()
    if exists:
        print("success")
        cursor.close()
        conn.close()

        #if __name__ == __main_:
    else:
        print("login or password is incorrect.")
        cursor.close()
        conn.close()
        exit()
