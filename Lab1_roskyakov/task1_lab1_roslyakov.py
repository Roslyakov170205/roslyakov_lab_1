class Table:
    """
    Класс для описания объекта "Стол".

    Атрибуты:
        material (str): Материал стола (например, дерево, металл).
        legs (int): Количество ножек.
        length (float): Длина стола в метрах.
    """

    def __init__(self, material: str, legs: int, length: float):
        if legs <= 0:
            raise ValueError("Количество ножек должно быть больше 0.")
        if length <= 0:
            raise ValueError("Длина стола должна быть положительной.")

        self.material = material
        self.legs = legs
        self.length = length

    def change_material(self, new_material: str) -> None:
        """
        Изменить материал стола.

        Args:
            new_material (str): Новый материал.
        """
        self.material = new_material

    def resize_table(self, new_length: float) -> None:
        """
        Изменить длину стола.

        Args:
            new_length (float): Новая длина стола (в метрах).
        """
        if new_length <= 0:
            raise ValueError("Новая длина должна быть положительной.")
        self.length = new_length

    def get_info(self) -> str:
        """
        Получить информацию о столе.

        Returns:
            str: Строка с описанием стола.

        >>> table = Table("дерево", 4, 1.5)
        >>> table.get_info()
        'Стол из дерева, 4 ножки, длина 1.5 м.'
        """
        return f"Стол из {self.material}, {self.legs} ножки, длина {self.length} м."


class Tree:
    """
    Класс для описания дерева.

    Атрибуты:
        species (str): Вид дерева.
        age (int): Возраст дерева (в годах).
        height (float): Высота дерева (в метрах).
    """

    def __init__(self, species: str, age: int, height: float):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота должна быть положительной.")

        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int, growth_per_year: float = 0.5) -> None:
        """
        Увеличить возраст дерева и его высоту.

        Args:
            years (int): Количество лет, на которое увеличится возраст.
            growth_per_year (float, optional): Рост в метрах за один год. По умолчанию 0.5 м.
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным.")
        self.age += years
        self.height += years * growth_per_year

    def is_mature(self) -> bool:
        """
        Проверить, является ли дерево зрелым.

        Returns:
            bool: True, если дерево старше 50 лет, иначе False.

        >>> tree = Tree("дуб", 60, 15)
        >>> tree.is_mature()
        True
        """
        return self.age > 50

    def get_description(self) -> str:
        """
        Получить описание дерева.

        Returns:
            str: Описание дерева.
        """
        return f"{self.species.capitalize()}, возраст: {self.age} лет, высота: {self.height:.2f} м."


class SocialMediaProfile:
    """
    Класс для описания профиля в социальной сети.

    Атрибуты:
        username (str): Имя пользователя.
        followers (int): Количество подписчиков.
        posts (int): Количество постов.
    """

    def __init__(self, username: str, followers: int = 0, posts: int = 0):
        if followers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным.")
        if posts < 0:
            raise ValueError("Количество постов не может быть отрицательным.")

        self.username = username
        self.followers = followers
        self.posts = posts

    def add_post(self) -> None:
        """
        Добавить новый пост.
        """
        self.posts += 1

    def follow(self, count: int) -> None:
        """
        Увеличить количество подписчиков.

        Args:
            count (int): Количество новых подписчиков.
        """
        if count <= 0:
            raise ValueError("Количество подписчиков должно быть положительным.")
        self.followers += count

    def engagement_rate(self) -> float:
        """
        Рассчитать уровень вовлечённости (Engagement Rate).

        Returns:
            float: Уровень вовлечённости (в %).

        >>> profile = SocialMediaProfile("user123", 1000, 50)
        >>> profile.engagement_rate()
        5.0
        """
        if self.followers == 0:
            return 0.0
        return (self.posts / self.followers) * 100


