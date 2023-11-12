def find_common_participants(first_group, second_group, divide_=","):
    same = set(first_group.split(divide_)).intersection(set(second_group.split(divide_)))
    result = list(same)
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, divide_="|"))
