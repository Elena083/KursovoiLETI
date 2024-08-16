import sqlite3
connection = sqlite3.connect('Список_абитуриентов.db') #для создания базы данных. Будет создан объект подключения.
cursor = connection.cursor() #Чтобы создать таблицу в базе данных, нам нужно использовать объект курсора
cursor.execute('''CREATE TABLE IF NOT EXISTS Список_абитуриентов
              (Title TEXT, Director TEXT, Year INT)''')

connection.commit()
connection.close()
# a = input('введите ФИО')
#spisokStudentov = {}
#spisokStudentov.append(a)
#extend
#print(spisokStudentov)


