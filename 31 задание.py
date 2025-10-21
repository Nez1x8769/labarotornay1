def get_keys_and_values():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    city = input("Введите город: ")
    info_dict = {"name": name, "age": age, "city": city}   
    print("Ключи:", info_dict.keys())
    print("Значения:", info_dict.values())
get_keys_and_values()
