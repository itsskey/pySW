# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, sep_=','):

    first = first.split(sep_)
    array_of_people = []
    for i in first:
        if second.find(i) != -1:
            array_of_people.append(i)
    return array_of_people


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

answer = find_common_participants(participants_first_group, participants_second_group, '|')
answer.sort()
print(answer)
# TODO Провеьте работу функции с разделителем отличным от запятой