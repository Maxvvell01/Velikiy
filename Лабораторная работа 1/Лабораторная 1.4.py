users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict_1 = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}

dict_1["Общее количество"] = len(users)

unique_users = set(users)
dict_1["Уникальные посещения"] = len(unique_users)

print(dict_1)
