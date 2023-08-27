class Humen:
    def __init__(self, name: str = 'Человек', age: int = 18, work: str = 'GB') -> None:
        self.name = name
        self.age = age
        self.work = work

    def greetings(self):
        return f'{self.name} Hello!'

andrey = Humen('Андрей', '18', 'DP')
stone = Humen('Стоун', '39', 'GB')

print(stone.name)
print(andrey.name)

print(stone.greetings())
print(andrey.greetings())