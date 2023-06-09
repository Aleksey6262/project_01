# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

# Выполнение
# Создание таблицы Students
import sqlite3

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# sqlquery = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY
# );"""
# cursor.execute(sqlquery)
# connection.commit()
# connection.close()

# Вставка значений в таблицу Students
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', '1'),
# (202, 'Петр', '2'),
# (203, 'Анастасия', '3'),
# (204, 'Игорь', '4');"""
# cursor.execute(sqlquery)
# connection.commit()
# connection.close()

# Вывести по ID студента данные о школе и студенте.
def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(select_query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

def get_student_info(student_id):
  try:
    school_name = get_school_name(student_id - 200)
    connection = get_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM Students WHERE student_id = ?"
    cursor.execute(select_query,(student_id,))
    records = cursor.fetchall()
    close_connection(connection)
    for row in records:
      print ("ID Студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы", school_name, "\n")
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

x = int(input("Введи ID:"))

get_student_info(x)
