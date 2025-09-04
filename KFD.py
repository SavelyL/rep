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
guest_books = []
guest_debts = []
guest_count = -1

def get_comand(max_comand, error = "Выбранное число не является командой", min_comand = 1):
    while True:
        try:
            user_input = int(input())
            if (user_input<min_comand or user_input>max_comand):
                raise Exception(error)
            if (user_input>=min_comand and user_input<=max_comand):
                    return user_input
        except ValueError:
            print("Пожалуйста, введите корректную команду.")
        except Exception as e:
            print(e)

def get_index(default_index = visitors_index):
    while True:
        try:
            user_index = int(input("Введите пятизначный индекс пользователя: "))
            if(user_index in default_index):
                return user_index
            else:
                print("Такой индекс отсутствует в списке, попробуйте ещё раз")
        except:
            print("Некорректный ввод, попробуйте ещё раз")

class Person:
    default_status = "Guest"
    default_name = "None"
    
    def __init__(self, name, index, taken_books, debt, status, max_debt, max_taken_books):
        if name:
            self.__name = name
        else:
            self.__name = Person.default_name
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
            for j in taken_books:
                free_books.append(j)
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
        print("Как гостю вам доступна только 1 книга сроком на 7 дней\nЕсли вы хотите вернуть книгу, обратитесь к администратору")

    def take_a_book_for_guest(self, taken_books, debt, max_taken_books, max_debt):
        print("Выберите по индексу книгу, которую хотите взять:")
        for j in range(0, len(free_books)):
            print(f"{j+1} - {free_books[j]}")
        chosen_index = get_comand(len(free_books)) - 1
        taken_books.append(free_books[chosen_index])
        free_books.pop(chosen_index)
        print("Выход из личного кабинета")


    @staticmethod   
    def return_a_book_for_guest(index, taken_books, debt):
        for i in taken_books:
            free_books.append(i)
        taken_books.clear()
        print("Книга возвращается в библиотеку")
    
        



while True:
    print("""Добро пожаловать в библиотеку \'Читательный сад\'!\n
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
            print("Придумайте пятизначный индекс")
            while True:
                flag = 0
                user_index = get_comand(99999, "Число не подходит под формат индекса", 10000)
                for i in range(0, len(visitors_index)):
                    if (user_index==visitors_index[i]):
                        flag = 1
                for i in range(0,len(guest_index)):
                    if (user_index==guest_index[i]):
                        flag = 1
                if (flag!=0):
                    print("Придумайте другой индекс, этот уже занят")
                else:
                    break
            guest_count+=1
            guest_index.append(user_index)
            guest_books.append([])
            guest_debts.append(7)
            Visitor = Guest("", guest_index[guest_count], guest_books[guest_count], guest_debts[guest_count], "", 1, 7)
            print(Visitor)
            Visitor.info()           
            Visitor.take_a_book_for_guest(guest_books[guest_count], guest_debts[guest_count], 1, 7)
    else:
        #тут тип будет режим админа, можно будет добавлять и удалять книги а ещё смотреть должников
        print("""Вы вошли в режим Админа\nПожалуйста, выберите необходимую вам операцию\n
1 - Добавить новую книгу\n2 - Просмотреть список должников\n3 - Подтвердить операцию возврата для незарегистрированных пользователей\n4 - Удалить книгу из библиотеки""")
        command_3 = get_comand(5)
        if (command_3==1):
            new_book = input("Введите название книги: ")
            autor = input("И её автора: ")
            free_books.append(f"{new_book} - {autor}")
            print("Новая книга добавлена в библиотеку")
        elif (command_3==2):
            print("\n\n______________________________________________\n\n")
            for i in range(0,len(visitors_index)):
                if(len(visitors_books[i])!=0):
                   print(f"""Индекс пользователя - {visitors_index[i]}\nИмя пользователя - {visitors_names[i]}\nСтатус - {visitors_status[i]}\nКоличество книг - {len(visitors_books[i])}
Дней до возврата - {visitors_debts[i]}""")
                   print("\n\n______________________________________________\n\n")
            
            for i in range(0,len(guest_index)):
                print(f"Индекс гостя - {guest_index[i]}\nДней до возврата - {guest_debts[i]}")
                print("\n\n______________________________________________\n\n")
        elif (command_3==3):
            if (len(guest_index)!=0):
                user_index = get_index(guest_index)
                if user_index in guest_index:
                    i = guest_index.index(user_index)
                    Guest.return_a_book_for_guest(guest_index[i], guest_books[i], guest_debts[i])
                    del guest_index[i]
                    del guest_books[i]
                    del guest_debts[i]
                    guest_count-=1
            else:
                print("Среди гостей должников нет")

        elif (command_3==4):
            
            print("Введите название книги и её автора через дефис\nПример:\tВойна и мир - Лев Толстой")
            flag = -1
            while True:
                book_search = input()
                for i in range(0,len(free_books)):
                    if book_search==free_books[i]:
                        flag = i
                        print(flag)
                if(flag == -1):
                    print("Название книги было введено некорректно")
                else:
                    free_books.pop(flag)
                    print("Книга была удалена из библиотеки")
                    break

    print("\n\n\n\n\n\n")





