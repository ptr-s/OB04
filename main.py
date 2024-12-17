"""
Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle)
         в Разработке Простой Игры

Цель: Цель этого домашнего задание - закрепить понимание и навыки применения
    принципа открытости/закрытости (Open/Closed Principle), одного из пяти SOLID
    принципов объектно-ориентированного программирования. Принцип гласит, что
    программные сущности (классы, модули, функции и т.д.) должны быть открыты
    для расширения, но закрыты для модификации.

Задача: Разработать простую игру, где игрок может использовать различные типы
    оружия для борьбы с монстрами. Программа должна быть спроектирована таким
    образом, чтобы легко можно было добавлять новые типы оружия, не изменяя
    существующий код бойцов или механизм боя.

Исходные данные:
- Есть класс `Fighter`, представляющий бойца.
- Есть класс `Monster`, представляющий монстра.
- Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

Шаг 1:Создайте абстрактный класс для оружия
- Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.

Шаг 2: Реализуйте конкретные типы оружия
- Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`.
  Каждый из этих классов реализует метод `attack()` своим уникальным способом.

Шаг 3: Модифицируйте класс `Fighter`
- Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
- Добавьте метод `changeWeapon()`, который позволяет изменить оружие бойца.

Шаг 4: Реализация боя
- Реализуйте простой механизм для демонстрации боя между бойцом и монстром,
  исходя из выбранного оружия.

Требования к заданию:

- Код должен быть написан на Python.
- Программа должна демонстрировать применение принципа открытости/закрытости: новые типы
  оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
- Программа должна выводить результат боя в консоль.

Пример результата:

Боец выбирает меч.
Боец наносит удар мечом.
Монстр побежден!
Боец выбирает лук.
Боец наносит удар из лука.
Монстр побежден!
"""
from abc import abstractmethod

class Monster:
    def __init__(self, name: str):
        self.name = name
        self.health = 100

    def damage(self, value):
        self.health -= value
        if self.health < 0:
            self.health = 0

    def is_dead(self):
        if self.health > 0:
            print(f"Монстр '{self.name}' всё ещё жив")
            return False
        else:
            print(f"Монстр '{self.name}' мёртв")
            return True

class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"Боец выбирает {weapon.name}")

    def attack(self, monster):
        print(f"Боец '{self.name}' делает ", end='')
        self.weapon.attack(monster)

class Weapon:
    @abstractmethod
    def attack(self, monster):
        pass

class Sword(Weapon):
    name = "Меч"
    def attack(self, monster):
        print(f"удар мечем по монстру '{monster.name}'")
        monster.damage(100)

class Bow(Weapon):
    name = "Лук"
    def attack(self, monster):
        print(f"выстрел из лука по монстру '{monster.name}'")
        monster.health -= 50

def main():
    fighter = Fighter('Боромир')
    weapon1 = Sword()
    weapon2 = Bow()

    monster1 = Monster('Гоблин')
    monster2 = Monster('Орк')

    # Сражение с гоблином
    fighter.change_weapon(weapon1)
    while not monster1.is_dead():
        fighter.attack(monster1)

    # Сражение с орком
    fighter.change_weapon(weapon2)
    while not monster2.is_dead():
        fighter.attack(monster2)


if __name__ == "__main__":
    main()