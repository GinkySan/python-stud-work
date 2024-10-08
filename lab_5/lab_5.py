def insert_text_at_line(file_path, text, line_number):

    if line_number < 1:
        raise ValueError("Номер строки должен быть положительным целым числом.")

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if line_number > len(lines) + 1:
        raise ValueError("Номер строки превышает количество строк в файле.")

    lines.insert(line_number - 1, text + '\n')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


file_path = 'example.txt'
text_to_insert = 'привет'
line_to_insert = 3

insert_text_at_line(file_path, text_to_insert, line_to_insert)