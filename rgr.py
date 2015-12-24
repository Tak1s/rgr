
class GetDetailInfo:
    def __init__(self, *args):
        self.count_level = input("Введіть кількість ступенів: ")
        self.arr_level = []
        self.severity_level = []
        self.arr_thread = []

        self.get_lang_level(self.count_level)
        self.get_severity_level()
        self.get_thread()

        print(self.arr_level)


    def get_severity_level(self):

        def _get_one_severity(text):
            const_severity = ["12.5", "6.3", "3.2", "1.6", "0.8"]
            item = input(text)
            item = item.replace(",", ".")
            if item in const_severity:
                return item
            else:
                print("Неверній параметр жосткости!!!\n")
                _get_one_severity(text)

        severity_level = input(
            """Вызначіть Ra ступенів:
    1 - шорсткість Ra  однакова для всіх ступенів
    2 - шорсткість Ra різна для кожного ступеня
"""
        )

        if int(severity_level) is 1:
             self.severity_level.append(_get_one_severity("Введіть жорсткість Ra для ступенів: "))
        elif int(severity_level) is 2:
            for i in range(int(self.count_level)):
                self.severity_level.append(_get_one_severity("Введіть жорсткість Ra %s-го ступеню: " % (i+1)))
        else:
            print("Невірне значення!!!\n\n")
            self.get_severity_level()

    def get_lang_level(self, count_level):
        for i in range(int(count_level)):
            self.arr_level.append(input("Введіть довжину %s-го ступеню: " % (i+1)))

    def get_thread(self):

        def _get_one_item():
            item = input("На яких ступенях присутьня різьба: ")
            item = item.split(",")
            if isinstance(item, 'list'):
                self.arr_thread = item
            else:
                self.arr_thread.append()
            if item in const_severity:
                return item
            else:
                print("Неверній параметр жосткости!!!\n")
                _get_one_severity(text)

        _thread = input("""Наявність різьби на поверхні:
    1 - є різьба
    0 - немає різьби
""")
        if int(_thread) is 1:
            print("На яких ступенях присутня різьба:")
            _get_one_item()
        elif int(_thread) is 0:
            print("Більше немає різьби!")

        else:
            print("Невірне значення!!!\n\n")
            self.get_thread()


GetDetailInfo()



