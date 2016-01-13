
class GetDetailInfo:
    def __init__(self, *args):
        self.dict_config = {0: {'diam':'6', 'isThread': False, 'leng': '1', 'faskSize': None, 'severity': '3.2', 'isFask': False}, 1: {'diam':'3', 'isThread': False, 'leng': '2', 'faskSize': None, 'severity': '3.2', 'isFask': False}}
        # self.count_level = input("Введіть кількість ступенів: ")
        # self.dict_config = {a: {'diam':None, 'leng':None, 'severity':None, 'isThread':False, 'isFask':False, 'faskSize':None} for a in range(int(self.count_level))}
        # self.isFask = False
        #
        # self.get_leng_level(self.count_level)
        # self.get_severity_level()
        # self.get_thread()
        # self.get_fask()
        # self.get_size_fask()

    def get_config(self):
        return self.dict_config

    def get_diameter(self):
        for i in range(int(count_level)):
            self.dict_config[i]['diam'] = input("Введіть діаметр %s-го ступеню: " % (i+1))

    def get_leng_level(self, count_level):
        for i in range(int(count_level)):
            self.dict_config[i]['leng'] = input("Введіть довжину %s-го ступеню: " % (i+1))

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
            if int(item) is 0:
                print("більше немає фасок!")
                return 'break'
            elif int(item) <= int(self.count_level):
                self.dict_config[index]['faskSize'] = item

        for i in self.dict_config:
            if self.dict_config[i]['isFask'] is False:
                continue
            if _get_one_item(i) is 'break':
                break

class DisplayMachinePperation:

    def __init__(self, _detalConfig):
        self.detalConfig = _detalConfig

        self.list_operation = []
        self.ra_tpl = {
            '12.5':'Чорнове точіння довжини {0} діаметром {1}',
            '6.3':'Чорнове, напівчистове точіння довжини {0} діаметром {1}',
            '3.2':'Чорнове, напівчистове, чистове точіння довжини {0} діаметром {1}',
            '1.6':'Чорнове, напівчистове, чистове точіння довжини {0} діаметром {1}',
            '0.8':'Чорнове, напівчистове, чистове точіння, шліфування довжини {0} діаметром {1}'
        }

        for i in self.detalConfig:
            _severity = self.detalConfig[i]['severity']
            _diam = self.detalConfig[i]['diam']
            _leng = self.detalConfig[i]['leng']
            _tpl_operation = self.ra_tpl[_severity]
            self.list_operation.append(_tpl_operation.format(_leng, _diam))

        self.full_string = ('''005 Заготівельна\n010 Токарна\nПідрізати торець\n%s\n015 Контрольна''' % ("\n".join(self.list_operation)))

        # print(str(self.detalConfig))
        print(self.full_string)


detalConfig = GetDetailInfo()
DisplayMachinePperation(detalConfig.get_config())

