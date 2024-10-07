def find_middle_elements(list1, list2):

    if len(list1) != 3 or len(list2) != 3:
        raise ValueError("Оба списка должны содержать по три элемента")

    middle1 = list1[1]
    middle2 = list2[1]

    return [middle1, middle2]

list1 = [7, 3, 4]
list2 = [5, 2, 1]

result = find_middle_elements(list1, list2)

print(result)