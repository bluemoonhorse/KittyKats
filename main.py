from cats import ClassСat

cats = [
    {
        "name": "Барон",
        "sex": "мальчик",
        "age": 2,
    },
    {
        "name": "Сэм",
        "sex": "мальчик",
        "age": 2,
    }
]

i = 0
for cat in cats:
    i += 1
    cat_instance = ClassСat()
    cat_instance.get_from_dict(cat)
    print(f'Кот {i}: ', cat_instance.name, cat_instance.sex, cat_instance.age)


