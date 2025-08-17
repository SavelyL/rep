class BankAccount:
    def __init__(self, acc, summ):
        self.__acc = acc
        self.__summ = summ
        
    @property
    def acc(self):
        return self.__acc

    @property
    def summ(self):
        return self.__summ
    
    @summ.setter
    def summ(self,summ):
        if summ>=0:
            self.__summ = summ
        else:
            print("невозможно создать счёт с отрицательным вкладом")
    
    def add(self, dep=999999):
        self.__summ += dep
        print(f"ваш баланс после внесения средств: {self.__summ}")
    
    def withdraw(self, minus):
        if self.__summ >= minus:
            self.__summ -= minus
            print(f"ваш баланс после снятия средств: {self.__summ}")
        else:
            return None

number = int(input("Введите номер счёта: "))
nach = int(input("Введите начальную сумму счёта: "))
bank = BankAccount(number,nach)
summa = int(input("Введите сумму: "))
print(bank.acc)
bank.add(summa)
bank.summ = 5000
bank.withdraw(summa)


