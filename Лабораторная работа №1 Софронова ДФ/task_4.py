users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
visit_statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
visit_statistics["Общее количество"] = len(users)
visit_statistics["Уникальные посещения"] = len(set(users))
print(visit_statistics)
