def get_even_elements(input_list):
    return [x for x in input_list if x % 2 == 0]

input_list = [4, 2, 4, 4, 5, 6, 7, 8, 9, 10]

even_elements = get_even_elements(input_list)

print(even_elements)