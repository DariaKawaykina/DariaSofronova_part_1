# TODO Напишите функцию find_common_participants

def find_common_participants(first_str, second_str, delimiter = ","):
    first_list = first_str.split(delimiter)
    second_list = second_str.split(delimiter)
    intersection_participants = list(set(first_list).intersection(second_list))
    intersection_participants.sort()
    return intersection_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,"|"))
