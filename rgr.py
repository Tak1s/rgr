
class GetDetailInfo:
    def __init__(self, *args):
        self.count_level = input("Введіть кількість ступенів: ")
        self.dict_config = {a: {'lang':None, 'severity':None, 'isThread':False, 'isFask':False, 'faskSize':None} for a in range(int(self.count_level))}
        # self.arr_level = []
        # self.severity_level = []
        # self.arr_thread = []
        self.isFask = False
        # self.arr_fask = []
        self.arr_size_fask = []

        self.get_lang_level(self.count_level)
        self.get_severity_level()
        self.get_thread()
        self.get_fask()
        self.get_size_fask()
        print(str(self.dict_config))


    def get_lang_level(self, count_level):
        for i in range(int(count_level)):
            self.dict_config[i]['lang'] = input("Введіть довжину %s-го ступеню: " % (i+1))

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
            "Вызначіть Ra ступенів:\n\t1 - жорсткість Ra  однакова для всіх ступенів\n\t2 - жорсткість Ra різна для кожного ступеня\n"
        )

        if int(severity_level) is 1:
            _severity_level = _get_one_severity("Введіть жорсткість Ra для ступенів: ")
            for i in range(int(self.count_level)):
                self.dict_config[i]['severity'] = _severity_level
        elif int(severity_level) is 2:
            for i in range(int(self.count_level)):
                self.dict_config[i]['severity'] = _get_one_severity("Введіть жорсткість Ra %s-го ступеню: " % (i+1))
        else:
            print("Невірне значення!!!\n\n")
            self.get_severity_level()


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
                    self.dict_config[int(val)-1]['isThread'] = True
                    # self.arr_thread.append(int(val))
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
                    self.dict_config[int(val)-1]['isFask'] = True
                    # self.arr_fask.append(int(val))
                else:
                    break
            if self._zero is False and len(array_item) <= int(self.count_level):
                _get_one_item()

        _fask = input("Чи наявні фаски:\n\t1 - так\n\t0 - ні\n")
        if int(_fask) is 1:
            self.isFask = True
            _get_one_item()
        elif int(_fask) is 0:
            print("Фасок немає!")
        else:
            print("Невірне значення!!!\n\n")
            self.get_fask()

    def get_size_fask(self):
        if self.isFask is False:
            return
        def _get_one_item(index):
            item = input("Введіть розмір %s-ї фаски: " % (index+1))
            # array_item = item.split(",")
            # self._zero = False
            # for val in array_item:
            if int(item) is 0:
                print("більше немає фасок!")
                # self._zero = True
                # break
                return 'break'
            elif int(item) <= int(self.count_level):
                self.dict_config[index]['faskSize'] = item
                # self.arr_size_fask.append(int(val))
                # else:
                #     break
                # if self._zero is False and len(array_item) <= int(self.count_level):
                #     _get_one_item()

        for i in self.dict_config:
            if self.dict_config[i]['isFask'] is False:
                continue
            if _get_one_item(i) is 'break':
                break

GetDetailInfo()



