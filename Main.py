items = {"Бочка": [], "Контейнер": []}

while True:
    try:
        amount = int(input("Введіть кількість товару: "))
        item_type = input("Введіть тип товару: ")

        if item_type in items:
            items[item_type].append(amount)
            print(f"{amount} додано в {item_type}.")
        else:
            add_type = input(f"Додати '{item_type}' до списку?: ")
            if add_type == "Так":
                items[item_type] = [amount]
                print(f"Тип '{item_type}' додано до списку")
            else:
                print("Тип товару не додано")
    except:
        print("Сталася помилка")