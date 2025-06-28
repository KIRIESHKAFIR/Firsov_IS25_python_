#Приложение ПАРИКМАХЕРСКАЯ для некоторой организации. БД должна
#содержать таблицу услуги со следующей структурой записи: ФИО мастера, ФИО клиента,
#пол, название стрижки, стоимость.
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Создаем соединение с SQLite базой данных """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Подключено к SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn):
    """ Создаем таблицу услуги"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS uslugi (
            фио_мастера TEXT NOT NULL,
            фио_клиента TEXT NOT NULL,
            пол TEXT NOT NULL,
            название_стрижки TEXT NOT NULL,
            стоимость REAL NOT NULL
        );
        """)
        print("Таблица 'uslugi' создана успешно")
    except Error as e:
        print(e)




def add_service(conn, ysluga):
    """ Добавляем новую услугу в таблицу """
    sql = ''' INSERT INTO uslugi(фио_мастера, фио_клиента, пол, название_стрижки, стоимость)
              VALUES(?,?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, ysluga)
    conn.commit()
    return cursor.lastrowid

def delete_service(conn, full_name):
    sql = ''' DELETE FROM uslugi WHERE фио_клиента = ? '''
    cursor = conn.cursor()
    cursor.execute(sql, (full_name,))
    conn.commit()
    return cursor.rowcount

def update_service(conn, full_name, full_name_master, gender, price, nazv_stich):
    """Обновление данных услуги по фио_клиента"""
    sql = ''' UPDATE uslugi 
              SET фио_мастера = ?, пол = ?, название_стрижки = ?, стоимость = ? 
              WHERE фио_клиента = ? '''
    cursor = conn.cursor()
    cursor.execute(sql, (full_name_master, gender,  nazv_stich, price, full_name))
    conn.commit()
    return cursor.rowcount



def search_services(conn, search_term=None, field=None):
    """ Поиск услуг по различным критериям """
    cursor = conn.cursor()
    
    if search_term and field:
        sql = f''' SELECT * FROM uslugi WHERE {field} LIKE ? '''
        cursor.execute(sql, (f'%{search_term}%',))
    else:
        sql = ''' SELECT * FROM uslugi '''
        cursor.execute(sql)
    
    return cursor.fetchall()

def main():
    database = "parikmaherskaya.db"
    
    # Создаем соединение с базой данных
    conn = create_connection(database)
    
    if conn is not None:
        # Создаем таблицу
        create_table(conn)
        
        # Пример добавления данных
        uslugi = [
            ("Иванова Анна Петровна", "Смирнов Алексей Владимирович", "М", "Бокс", 500.0),
            ("Петрова Елена Сергеевна", "Кузнецова Ольга Игоревна", "Ж", "Каре", 1200.0),
            ("Сидорова Мария Дмитриевна", "Волков Денис Олегович", "М", "Полубокс", 800.0),
            ("Полько Евгений Владимирови", "Бруно Авилио Глагуза", "М", "Налысо", 5.0),
            ("Петрова Елена Сергеевна", "Редгрейв Данте Спардович", "М", "ПиццаМен", 800000.0),
            ("Полько Евгений Владимирович", "Сволдигод Анно Мариевна", "Ж", "Каре", 200.0),
            ("Сидорова Мария Дмитриевна", "Спидвагон Роберт Эдуардович", "М", "Маллето", 20000.0),
            ("Иванова Анна Петровна", "Дио Брандо Танакович", "М", "Блондин", 1400.0),
            ("Петрова Елена Сергеевна", "Джотаро Куджо Токийский", "М", "Эрокез", 1300.0),
            ("Полько Евгений Владимирович", "Йегер Эрен Гришегорьевич", "М", "Мальвиновка", 5000.0),
        ]
        
        for ysluga in uslugi:
            add_service(conn, ysluga)
            print(f"Добавлена услуга: {ysluga}")
        
        new = [ ("Иванова Анна Петровна", "Астерикс Галльский", "М", "Воинский ирокез", 1500.0),
                ("Петрова Елена Сергеевна", "Обеликс Каменотес", "М", "Борода+стрижка", 2500.0),
                ("Сидорова Мария Дмитриевна", "Фея Динь-Динь", "Ж", "Волшебный каскад", 1800.0),
        ]
        
        for ysluga in new:
            add_service(conn, ysluga)
            print(f"Добавлена услуга: {ysluga}")
        
        kare_services = search_services(conn, 'Каре', 'название_стрижки')
        naliso_services = search_services(conn, 'Налысо', 'название_стрижки')
        malet_services = search_services(conn, 'Малет', 'название_стрижки')
        
        print('У них каре: \n', ' \n'.join(map(str, kare_services)))
        
        delete_service(conn, "Сволдигод Анно Мариевна")
        delete_service(conn, "Дио Брандо Танакович")
        delete_service(conn, "Йегер Эрен Гришегорьевич")
        
        update_service(conn, "Астерикс Галльский", "Петрова Елена Сергеевна", "М", 1000.0, "НЕ Воинский ирокез")
        update_service(conn, "Фея Динь-Динь", "Иванова Анна Петровна", "Ж", 1200.0, "НЕ Волшебный каскад")
        update_service(conn, "Редгрейв Данте Спардович", "Сидорова Мария Дмитриевна", "М", 1500.0, "НЕ ПиццаМен")
        # Закрываем соединение
        conn.close()
    else:
        print("Ошибка! Не удалось подключиться к базе данных.")

if __name__ == '__main__':
    main()