import psycopg2
import csv

def delete(conn,cursor):
    print('Введите ID контакта')
    x=input()
    sql_delete_query = """Delete from contacts where user_id = %s"""
    cursor.execute(sql_delete_query, (x,))
    conn.commit()
    count = cursor.rowcount
    print(count, "Удаление произошло успешно")

def update(conn,cursor):
    print('Введите ID контакта, который хотите обновить')
    x=int(input())

    print('что вы хотите обновить?')

    print('имя,фамилию,номер')
    y=input()

    print('введите на что хотите изменить')
    z=input()

    if y=='имя':
        sql_update_query = """Update contacts set first_name = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    elif y=='фамилие':
        sql_update_query = """Update contacts set last_name = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    else:
        sql_update_query = """Update contacts set phone_number = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    print('УСПЕШНО!')

def show(cursor):
    print('Напишите что вы хотите вывести')
    print('1:ID')
    print('2:first_name')
    print('3:all')
    
    k=int(input())
    cursor.execute('SELECT * FROM contacts LIMIT 10')
    if k == 1:
        records = cursor.fetchall()
        for row in records:
            print(row[0])
    elif k == 2:
        records = cursor.fetchall()
        for row in records:
            print(row[1])
    else:
        records = cursor.fetchall()
        for row in records:
            print(row)


def add(conn,cursor):
    print('Введите через пробел ID, имя, фамилию и номер телефона пользователя')
    z=input().split()
    postgres_insert_query = """ INSERT INTO contacts (user_id,last_name,first_name,phone_number) VALUES (%s,%s,%s,%s)"""
    record_to_insert = (z[0], z[1], z[2], z[3])

    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()

    print( "УСПЕШНО!")

def csv_(conn,cursor):
    print("Введите путь до файла")
    path=str(input())
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            postgres_insert_query = """ INSERT INTO contacts (user_id,last_name,first_name,phone_number) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (i[0], i[1], i[2], i[3])
            cursor.execute(postgres_insert_query, record_to_insert)
            conn.commit()

try:
    conn = psycopg2.connect(dbname="madara",  user="madara",  password="123", host="localhost")
    cursor = conn.cursor()
    print('Выберите что вы хотите сделать:')
    print('1:Добавить контакт')
    print('2:Удалить контакт')
    print('3:Показать контакты')
    print('4:Обновить контакт')
    print('5:csv')
    choose=input()
    if choose == '2':
        delete(conn,cursor)
    elif choose == '1':
        add(conn,cursor)
    elif choose=='3':
        show(cursor)
    elif choose=='4':
        update(conn,cursor)
    elif choose=='5':
        csv_(conn,cursor)

except psycopg2.Error as e:
    print('fail')


