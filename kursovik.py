import sqlite3
connection = sqlite3.connect('приемная_коммиссия.db') #для создания базы данных. Будет создан объект подключения.
cursor = connection.cursor() #Чтобы создать таблицу в базе данных, нам нужно использовать объект курсора
#print("Подключен к SQLite")
cursor.execute('''DROP TABLE IF EXISTS Список_абитуриентов''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Список_абитуриентов(
                      регистрационный_номер INTEGER primary key, 
                      фамилия TEXT,
                      имя TEXT,
                      отчество TEXT, 
                      дата_рождения DATE, 
                      город TEXT,
                      название TEXT,
                      номер TEXT,
                      дата_окончания DATE,
                      достижения BOOL,
                      город_проживания TEXT,
                      улица TEXT,
                      номер_дома TEXT,
                      телефон_для_связи TEXT,
                      выбранная_специальность TEXT)''')
#введем данные в таблицу абитуриент (фио и тд)
#cursor.execute('''INSERT INTO Список_абитуриентов (регистрационный_номер, фамилия_имя_отчество, дата_рождения, оконченное_среднее_учебное_заведение_название_номер_город, дата_окончания, наличие_красного_диплома_или_олотой_серебряной_медали, адрес_город_улица_номер_дома_телефон, выбранная_специальность)
#VALUES (1, 'Иванов Иван Иванович', '2000-01-01', 'название заведения', '2023-01-01', 'true', 'адрес', 'инженер')''') #значения в ковычки
#resultset = cursor.execute(''' SELECT * FROM Список_абитуриентов''')
#print(resultset.fetchall()) #получить из результата таблицу абитуриент

cursor.execute('''DROP TABLE IF EXISTS Справочник_специальностей''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Справочник_специальностей(
              номер_специальности INTEGER primary key, 
              название_специальности TEXT)''')
#введем данные в таблицу со специальностями
#cursor.execute('''INSERT INTO Справочник_специальностей (номер_специальности, название_специальности)
#VALUES ('11', 'инженер')''') #значения в ковычки
#resultset = cursor.execute(''' SELECT * FROM Справочник_специальностей''')
#print(resultset.fetchall()) #получить из результата специальностями

cursor.execute('''DROP TABLE IF EXISTS Список_предметов''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Список_предметов(
              номер_предмета INTEGER, 
              название_предмета TEXT)''')

#введем данные в таблицу Список_предметов
#cursor.execute('''INSERT INTO Список_предметов (номер_предмета, название_предмета)
#VALUES (1, 'математика')''') #значения в ковычки
#resultset = cursor.execute(''' SELECT * FROM Список_предметов''')
#print(resultset.fetchall()) #получить из результата
connection.commit()
#result = int(input("введите 1 чтоб записать абитурианта, 2 - вывести список абитуриентов"))

connection.close()
#УКОРОТИТЬ НАЗВАНИЯ
#print("Соединение с SQLite закрыто")
# a = input('введите ФИО')
#spisokStudentov = {}
#spisokStudentov.append(a)
#extend
#print(spisokStudentov)


