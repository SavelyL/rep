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

visitors_index = (12345, 54321, 22334, 17364, 65867, 36456, 98079, 75864, 55555)
visitors_status = ('student', 'professor', 'student', 'student', 'professor', 'student', 'professor', 'professor', 'professor')
visitors_names = ('Sasha', 'Tolya', 'Masha', 'Vasya', 'Nikita', 'Veronika', 'Sonya', 'Anton', 'Valera')
visitors_books = [["Дворянское гнездо - Иван Тургенев", "Шинель - Николай Гоголь"],
                  ["Дубровский - Александр Пушкин","Маскарад - Михаил Лермонтов"],
                  [],
                  ["Демон - Михаил Лермонтов"],
                  ["Казаки - Лев Толстой"],
                  ["Униженные и оскорблённые - Фёдор Достоевский", "Кавказский пленник - Михаил Лермонтов", "Горе от ума - Александр Грибоедов"],
                  [],
                  ["Что делать? - Николай Чернышевский", "Записки из мёртвого дома - Фёдор Достоевский", "Смерть Ивана Ильича - Лев Толстой", "Дядя Ваня - Антон Чехов"],
                  ["Мцыри - Михаил Лермонтов"]
]
visitors_debts = [12, 23, 14, 0, 17, 5, 30, 26, 7]

guest_index = []
guest_names = []
guest_books = []
guest_debts = []


def get_comand(max_comand, error = "Выбранное число не является командой"):
    while True:
        try:
            user_input = int(input())
            if (user_input<1 or user_input>max_comand):
                raise Exception(error)
            if (user_input>=1 and user_input<=max_comand):
                    return user_input
        except ValueError:
            print("Пожалуйста, введите корректную команду.")
        except Exception as e:
            print(e)

class Person:
    default_status = "Guest"

    
    def __init__(self, name, index, taken_books, debt, status, max_debt, max_taken_books):
        self.__name = name
        self.__index = index
        self.__taken_books = taken_books
        self.__debt = debt
        self.__max_debt = max_debt
        self.__max_taken_books = max_taken_books
        if status:
            self.__status = status
        else:
            self.__status = Person.default_status

    def __str__(self):
        return f"Имя пользователя - {self.__name}\nИндекс пользователя - {self.__index}\nВзятые книги - {self.__taken_books}\nОсталось дней до возврата - {self.__debt}\nСтатус - {self.__status}"

    def info(self):
        pass

    def take_a_book(self, taken_books, debt, max_taken_books, max_debt):
        if (debt==0 or len(taken_books)== max_taken_books):
            print("Вы не можете взять новые книги, пока не вернёте предыдущие")
        else:
            print("Введите количество книг, которые планиуете взять")
            count_book = get_comand(max_taken_books - len(taken_books),f"максимально количество книг, которые вы можете взять - {max_taken_books-len(taken_books)}")
            print(f"Количество книг, которые вы хотите взять - {count_book}")
            for i in range(0, count_book):
                print("Выберите по индексу книгу, которую хотите взять:")
                for j in range(0, len(free_books)):
                    print(f"{j+1} - {free_books[j]}")
                chosen_index = get_comand(len(free_books)) - 1
                taken_books.append(free_books[chosen_index])
                free_books.pop(chosen_index)
        print("Выход из личного кабинета")

    def return_a_book(self, taken_books, debt, index, max_debt):
        if len(taken_books) == 0:
            print("У вас нет книг из библиотеки")
        else:
            for book in taken_books:
                free_books.append(book)
            taken_books.clear()
            print("Вы сдали все книги")
            debt_index = visitors_index.index(index)
            visitors_debts[debt_index] = max_debt
        print("Выход из личного кабинета")
    

class Student(Person):
    
    def info(self):
        print("Вы вошли в свой личный кабинет!\nКак студенту вам доступны максимум 3 книги сроком на 14 дней\nНажмите\n1 - сли хотите вернуть книги обратно\n2 - если хотите взять ещё")


    



class Professor(Person):
    
    def info(self):
        print("Вы вошли в свой личный кабинет!\nКак преподавателю вам доступно максимум 10 книг сроком на 30 дней\nНажмите\n1 - сли хотите вернуть книги обратно\n2 - если хотите взять ещё")



class Guest(Person):
    def info(self):
        print("Вы вошли в свой личный кабинет!\nКак гостю вам доступна только 1 книга сроком на 7 дней")

    def take_a_book_for_guest(self, taken_books, debt, max_taken_books, max_debt):
        print("Выберите по индексу книгу, которую хотите взять:")
        for j in range(0, len(free_books)):
            print(f"{j+1} - {free_books[j]}")
        chosen_index = get_comand(len(free_books)) - 1
        taken_books.append(free_books[chosen_index])
        free_books.pop(chosen_index)
        print("Выход из личного кабинета")

    
        



guest_count = -1
while True:
    print("""Добро пожаловать в библиотеку \'Читательный сад!\'\n
У нас вы можете взять книгу напрокат совершенно бесплатно\n
Пожалуйста, выберите режим, в котором будете работать:\n
1:  Студент или преподаватель(обязательно нужно быть зарегистрированным в списке библиотеки)\n
2:  Гость(регисрация не требуется)\n
3:  Админ(добавление новых книг, просмотр базы должников и списка доступных книг)\n
""")
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
                max_books = 3
                max_debt = 14
                Visitor = Student(visitors_names[number], visitors_index[number], visitors_books[number], visitors_debts[number], visitors_status[number], max_debt, max_books)
                print(Visitor)
                Visitor.info()
            else:
                max_books = 10
                max_debt = 30
                Visitor = Professor(visitors_names[number], visitors_index[number], visitors_books[number], visitors_debts[number], visitors_status[number], max_debt, max_books)
                print(Visitor)
                Visitor.info()

            command_2 = get_comand(2)
            if (command_2==1):
                Visitor.return_a_book(visitors_books[number], visitors_debts[number], visitors_index[number], max_debt)
            else:
                Visitor.take_a_book(visitors_books[number], visitors_debts[number], max_books, max_debt)
            
        else:
            user_name = input("Введите имя пользователя: ")
            guest_count +=1
            guest_index.append(guest_count+1)
            guest_names.append(user_name)
            guest_books.append([])
            guest_debts.append(7)
            Visitor = Guest(guest_names[guest_count], guest_index[guest_count], guest_books[guest_count], guest_debts[guest_count], "", 1, 7)
            print(Visitor)
            Visitor.info()           
            Visitor.take_a_book_for_guest(guest_books[guest_count], guest_debts[guest_count], 1, 7)
    else:
        #тут тип будет режим админа, можно будет добавлять и удалять книги а ещё смотреть должников
        print("Chit-mod")




