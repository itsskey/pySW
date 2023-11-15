# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, sep_=','):
    first = first.split(sep_)
    second = second.split(sep_)
    intersection_group = set(first).intersection(second)
    intersection_group = list(intersection_group)
    intersection_group.sort()
    return intersection_group

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
answer = find_common_participants(participants_first_group, participants_second_group, '|')
print(answer)
# TODO Провеьте работу функции с разделителем отличным от запятой
