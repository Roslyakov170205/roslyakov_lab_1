from task_1 import Table, Tree, SocialMediaProfile  # Импорт классов, созданных ранее

if __name__ == "__main__":
    # Инстанцировать все описанные классы, создав три объекта
    table = Table("дерево", 4, 1.5)
    tree = Tree("дуб", 10, 5.0)
    profile = SocialMediaProfile("user123", 100, 5)

    try:
        # Вызвать метод с некорректными аргументами (resize_table)
        table.resize_table(-1)
    except ValueError as error:
        print(f"Ошибка: {error}")

    try:
        # Вызвать метод с некорректными аргументами (grow)
        tree.grow(-5)
    except ValueError as error:
        print(f"Ошибка: {error}")

    try:
        # Вызвать метод с некорректными аргументами (follow)
        profile.follow(-10)
    except ValueError as error:
        print(f"Ошибка: {error}")


