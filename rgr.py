
class GetDetailInfo:
    def __init__(self, *args):
        self.dict_config = {}
        self.count_level = input("Введіть кількість ступенів: ")
        self.arr_level = []
        self.severity_level = []
        self.arr_thread = []
        self.arr_fask = []
        self.arr_size_fask = []

        self.get_lang_level(self.count_level)
        self.get_severity_level()
        self.get_thread()
        self.get_fask()
        self.get_size_fask()

        print(self.arr_size_fask)


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
            "Вызначіть Ra ступенів:\n\t1 - шорсткість Ra  однакова для всіх ступенів\n\t2 - шорсткість Ra різна для кожного ступеня\n"
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

    # Нужно доделать обработчик количества елементов!!!!!
    def get_thread(self):

        def _check_item(item):
            try:
                return int(item)
            except ValueError:
                return False

        def _get_one_item():
            item = input("На яких ступенях присутьня різьба: ")
            array_item = item.split(",")
            self._zero = False
            for val in array_item:
                if int(val) is 0 :
                    print("Більше немає різьби!")
                    self._zero = True
                    break
                elif int(val) <= int(self.count_level):
                    self.arr_thread.append(int(val))
                else:
                    break
            if self._zero is False and len(array_item) <= int(self.count_level):
                _get_one_item()


        _thread = input("Наявність різьби на поверхні:\n\t1 - є різьба\n\t0 - немає різьби\n")
        if int(_thread) is 1:
            _get_one_item()
        elif int(_thread) is 0:
            print("Різьби немає!")
        else:
            print("Невірне значення!!!\n\n")
            self.get_thread()

    def get_fask(self):

        def _get_one_item():
            item = input("На яких ступенях присутня фаска: ")
            array_item = item.split(",")
            self._zero = False
            for val in array_item:
                if int(val) is 0:
                    print("більше немає фасок!")
                    self._zero = True
                    break
                elif int(val) <= int(self.count_level):
                    self.arr_fask.append(int(val))
                else:
                    break
            if self._zero is False and len(array_item) <= int(self.count_level):
                _get_one_item()

        _fask = input("Чи наявні фаски:\n\t1 - так\n\t0 - ні\n")
        if int(_fask) is 1:
            _get_one_item()
        elif int(_fask) is 0:
            print("Фасок немає!")
        else:
            print("Невірне значення!!!\n\n")
            self.get_fask()

    def get_size_fask(self):

        def _get_one_item():
            item = input("На яких ступенях присутня фаска: ")
            array_item = item.split(",")
            self._zero = False
            for val in array_item:
                if int(val) is 0:
                    print("більше немає фасок!")
                    self._zero = True
                    break
                elif int(val) <= int(self.count_level):
                    self.arr_size_fask.append(int(val))
                else:
                    break
            if self._zero is False and len(array_item) <= int(self.count_level):
                _get_one_item()


        _get_one_item()



GetDetailInfo()



