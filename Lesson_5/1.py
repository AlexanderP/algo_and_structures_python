"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


class Company():

    def __init__(self, name=None, q1=None, q2=None, q3=None, q4=None):
        if name is None:
            self.name = input("Введите имя компании: ")
        else:
            self.name = name
        if q1 is None:
            self.q1 = float(input(f"Укажите объем прибыли {self.name}"
                                  f" за 1 кв: "))
        else:
            self.q1 = float(q1)
        if q2 is None:
            self.q2 = float(input(f"Укажите объем прибыли {self.name}"
                                  f" за 2 кв: "))
        else:
            self.q2 = float(q2)
        if q3 is None:
            self.q3 = float(input(f"Укажите объем прибыли {self.name}"
                                  f" за 3 кв: "))
        else:
            self.q3 = float(q1)
        if q4 is None:
            self.q4 = float(input(f"Укажите объем прибыли {self.name}"
                                  f" за 4 кв: "))
        else:
            self.q4 = float(q1)

    @property
    def year_profit(self):
        return self.q1 + self.q2 + self.q3 + self.q4

    def __str__(self):
        return (f"Имя компании: {self.name}\n"
                f"Прибыль за 1 кв: {self.q1} руб.\n"
                f"Прибыль за 2 кв: {self.q2} руб.\n"
                f"Прибыль за 3 кв: {self.q3} руб.\n"
                f"Прибыль за 4 кв: {self.q4} руб.\n"
                f"Итого за год: {self.year_profit}")


class CompReport():

    def __init__(self, number: int = 0):

        if number == 0:
            self.number = int(input("Введите количество компаний: "))
            print("-" * 60)
        else:
            self.number = number

        self.companys = []
        for i in range(self.number):
            print(f'{i + 1} компания:')
            self.companys.append(Company())

    def average(self):
        print("-" * 60)
        if len(self.companys) == 1:
            print(f"Занесена информация об одной компании:\n"
                  f"{self.companys[0]}")
        elif len(self.companys) == 0:
            print("Нет информации об компаниях :(")
        elif len(self.companys) > 1:
            sums = 0
            for i in self.companys:
                sums += i.year_profit
            average_profit = sums / len(self.companys)
            filter_company = [j for j in self.companys if
                              j.year_profit >= average_profit]
            print(f"Средняя прибыль за год по {len(self.companys)} компаниям "
                  f"составляет {round(average_profit, 2)} руб.\n"
                  f"\nКомпании с прибылью больше средней:")
            for j in filter_company:
                print()
                print(j)

            filter_company = [j for j in self.companys if
                              j.year_profit < average_profit]
            print(f"\nКомпании с прибылью меньше средней:")
            for j in filter_company:
                print()
                print(j)
        print("-" * 60)


run = CompReport()
run.average()
