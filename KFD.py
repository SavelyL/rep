free_books = [
    "Война и мир - Лев Толстой",
    "Анна Каренина - Лев Толстой",
    "Преступление и наказание - Фёдор Достоевский",
    "Идиот - Фёдор Достоевский",
    "Братья Карамазовы - Фёдор Достоевский",
    "Отцы и дети - Иван Тургенев",
    "Мёртвые души - Николай Гоголь",
    "Ревизор - Николай Гоголь",
    "Евгений Онегин - Александр Пушкин",
    "Капитанская дочка - Александр Пушкин",
    "Герой нашего времени - Михаил Лермонтов",
    "Обломов - Иван Гончаров",
    "Гроза - Александр Островский",
    "Бесприданница - Александр Островский",
    "Вишнёвый сад - Антон Чехов",
    "Три сестры - Антон Чехов",
    "Чайка - Антон Чехов",
    "Дама с собачкой - Антон Чехов",
    "Муму - Иван Тургенев",
    "Тарас Бульба - Николай Гоголь",
    "Пиковая дама - Александр Пушкин",
    "Бедные люди - Фёдор Достоевский",
    "Детство - Лев Толстой",
    "Отрочество - Лев Толстой",
    "Юность - Лев Толстой",
    "Шинель - Николай Гоголь",
    "Записки охотника - Иван Тургенев",
    "Воскресение - Лев Толстой",
    "Каштанка - Антон Чехов",
    "Бесы - Фёдор Достоевский"
]

visitors_index = (12345, 54321, 25345, 17364, 65867, 36456, 98079, 75864, 55555)
visitors_status = ('student', 'professor', 'student', 'student', 'professor', 'student', 'professor', 'professor', 'professor')
visitors_names = ('Sasha', 'Tolya', 'Masha', 'Vasya', 'Nikita', 'Veronika', 'Sonya', 'Anton', 'Valera')
visitors_books = [["Дворянское гнездо - Иван Тургенев", "Шинель - Николай Гоголь"],
                  ["Дубровский - Александр Пушкин","Маскарад - Михаил Лермонтов"],
                  ["None"],
                  ["Демон - Михаил Лермонтов"],
                  ["Казаки - Лев Толстой"],
                  ["Униженные и оскорблённые - Фёдор Достоевский"],
                  ["None"],
                  ["Что делать? - Николай Чернышевский", "Записки из мёртвого дома - Фёдор Достоевский", "Смерть Ивана Ильича - Лев Толстой", "Дядя Ваня - Антон Чехов"],
                  ["Мцыри - Михаил Лермонтов"]
]
visitors_debts = [12, 23, 14, 0, 17, 5, 30, 26, 7]

guest_index = []
guest_names = []
guest_books = []
guest_debts = []


class Person:
    default_status = "Guest"
    
    def __init__(self, name, index, taken_books, debt, status):
        self.__name = name
        self.__index = index
        self.__taken_books = taken_books
        self.__debt = debt
        if status:
            self.__status = status
        else:
            self.__status = Person.default_status

    def __str__(self):
        return f"Имя пользователя - {self.__name}\nИндекс пользователя - {self.__index}\nВзятые книги - {self.__taken_books}\nОсталось дней до возврата - {self.__debt}\nСтатус - {self.__status}"

    def info(self):
        pass

    def take_a_book(self, taken_books, debt):
        pass

    def return_a_book(self, taken_books, debt):
        pass
    

class Student(Person):
    def info(self):
        print("Вы вошли в свой личный кабинет!\nКак студенту вам доступны максимум 3 книги сроком на 14 дней\nНажмите\n1 - сли хотите вернуть книги обратно\n2 - если хотите взять ещё")

    
    def take_a_book(self, taken_books, debt):
        pass

    def return_a_book(self, taken_books, debt):
        pass
    
class Professor(Person):
    def info(self):
        print("Вы вошли в свой личный кабинет!\nКак преподавателю вам доступно максимум 10 книг сроком на 30 дней\nНажмите\n1 - сли хотите вернуть книги обратно\n2 - если хотите взять ещё")

    def take_a_book(self, taken_books, debt):
        pass

    def return_a_book(self, taken_books, debt):
        pass

class Guest(Person):
    def info(self):
        print("Вы вошли в свой личный кабинет!\nКак гостю вам доступна только 1 книга сроком на 7 дней")

    def take_a_book(self, taken_books, debt):
        pass

    def return_a_book(self, taken_books, debt):
        pass

    
def get_comand(max_comand):
    while True:
        try:
            user_input = int(input())
            if (user_input<1 or user_input>max_comand):
                raise Exception("Выбранное число не является командой")
            if (user_input>=1 and user_input<=max_comand):
                    return user_input
        except ValueError:
            print("Пожалуйста, введите корректную команду.")
        except Exception as e:
            print(e)
        

print("""Добро пожаловать в библиотеку \'Читательный сад!\'\n
У нас вы можете взять книгу напрокат совершенно бесплатно\n
Пожалуйста, выберите режим, в котором будете работать:\n
1:  Студент или преподаватель(обязательно нужно быть зарегистрированным в списке библиотеки)\n
2:  Гость(регисрация не требуется)\n
3:  Админ(добавление новых книг, просмотр базы должников и списка доступных книг)\n
""")

guest_count = -1
while True:
    command_1 = get_comand(3)
    print(f"Вы выбрали режим {command_1}")
    if command_1!=3:
        if command_1 != 2:
            while True:
                try:
                    user_index = int(input("Введите пятизначный индекс пользователя: "))
                    if(user_index in visitors_index):
                        break
                    else:
                        print("Такой индекс отсутствует в списке, попробуйте ещё раз")
                except:
                    print("Некорректный ввод, попробуйте ещё раз")
            number = 0
            for i in range(0,len(visitors_index)):
                if (user_index == visitors_index[i]):
                    user_name = visitors_names
                    number = i
                    break
            if (visitors_status[number]=="student"):
                Visitor = Student(visitors_names[number], visitors_index[number], visitors_books[number], visitors_debts[number], visitors_status[number])
                print(Visitor)
                Visitor.info()
            else:
                Visitor = Professor(visitors_names[number], visitors_index[number], visitors_books[number], visitors_debts[number], visitors_status[number])
                print(Visitor)
                Visitor.info()

            command_2 = get_comand(2)
            if (command_2==1):
                Visitor.return_a_book()
            else:
                Visitor.take_a_book()
            
        else:
            user_name = input("Введите имя пользователя: ")
            guest_count +=1
            guest_index.append(guest_count+1)
            guest_names.append(user_name)
            guest_books.append("None")
            guest_debts.append(7)
            Visitor = Guest(guest_names[guest_count], guest_index[guest_count], guest_books[guest_count], guest_debts[guest_count], "")
            print(Visitor)
            Visitor.info()           

    else:
        #тут тип будет режим админа, можно будет добавлять и удалять книги а ещё смотреть должников
        print("Вы вошли в режим администратора")




