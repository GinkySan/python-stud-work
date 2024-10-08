import sqlite3

def update_table_with_data(table_name, data_list):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    for index, data in enumerate(data_list):
        record_id = index + 1

        placeholders = ', '.join([f'{column} = ?' for column in data.keys()])
        query = f"UPDATE {table_name} SET {placeholders} WHERE id = ?"

        cursor.execute(query, list(data.values()) + [record_id])

    conn.commit()
    conn.close()

# Пример использования
table_name = 'example_table'
data_list = [
    {'column1': '1', 'column2': '2'},
    {'column1': 'gg', 'column2': 'wp'},
]

update_table_with_data(table_name, data_list)