
class GetDetailInfo:
    def __init__(self, *args):
        # self.dict_config = {0: {'id':0, 'severity': '3.2', 'isThread': False, 'faskSize': None, 'leng': 1, 'diam': 2, 'isFask': False}, 1: {'id':1, 'severity': '3.2', 'isThread': False, 'faskSize': None, 'leng': 2, 'diam': 4, 'isFask': False}, 2: {'id':2, 'severity': '3.2', 'isThread': False, 'faskSize': None, 'leng': 3, 'diam': 6, 'isFask': False}, 3: {'id':3, 'severity': '3.2', 'isThread': False, 'faskSize': None, 'leng': 4, 'diam': 3, 'isFask': False}, 4: {'id':4, 'severity': '3.2', 'isThread': False, 'faskSize': None, 'leng': 5, 'diam': 8, 'isFask': False}}
        self.count_level = self.get_count_level()
        self.dict_config = {a: {'id':a, 'diam':None, 'leng':None, 'severity':None, 'isThread':False, 'isFask':False, 'faskSize':None} for a in range(int(self.count_level))}
        self.isFask = False

        self.get_diameter(self.count_level)
        self.get_leng_level(self.count_level)
        self.get_severity_level()
        self.get_thread()
        self.get_fask()
        self.get_size_fask()

    def get_config(self):
        return self.dict_config

    def get_count_level(self):
        _data = input("Введіть кількість ступенів: ")
        try:
            _item = int(_data)
        except Exception:
            print("Введено невірне значення!\n")
            return self.get_count_level()
        else:
            return _item

    def get_item(self, mess, index):
        _data = input(mess % (index+1))
        try:
            _item = int(_data)
        except Exception:
            print("Введено невірне значення!\n")
            return self.get_item(mess, index)
        else:
            return _item

    def get_diameter(self, count_level):

        for i in range(int(count_level)):
            self.dict_config[i]['diam'] = self.get_item("Введіть діаметр %s-го ступеню: ", i)

    def get_leng_level(self, count_level):
        for i in range(int(count_level)):
            self.dict_config[i]['leng'] = self.get_item("Введіть довжину %s-го ступеню: ",i)

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

        def _get_action():
            _data = input(
                "Вызначіть Ra ступенів:\n\t1 - жорсткість Ra  однакова для всіх ступенів\n\t2 - жорсткість Ra різна для кожного ступеня\n"
            )
            try:
                _item = int(_data)
            except Exception:
                print("Введено невірне значення!\n")
                return _get_action()
            else:
                if _item in [1, 2]:
                    return _item
                else:
                    print("Введено невірне значення!\n")
                    return _get_action()

        severity_level = _get_action()

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


    def get_thread(self):
        def _get_one_item():
            item = input("На яких ступенях присутьня різьба: ")
            array_item = item.replace(".", ",").split(",")
            _zero = False
            for val in array_item[:self.count_level]:
                try:
                    _val = int(val)
                except Exception:
                    continue
                else:
                    if _val > self.count_level:
                        continue
                    if _val is 0:
                        print("Більше немає різьби!")
                        _zero = True
                        break
                    else:
                        self.dict_config[_val-1]['isThread'] = True

            if _zero is False:
                _get_one_item()

        def _get_action():
            _data = input("Наявність різьби на поверхні:\n\t1 - є різьба\n\t0 - немає різьби\n")
            try:
                _item = int(_data)
            except Exception:
                print("Введено невірне значення!\n")
                return _get_action()
            else:
                if _item in [0, 1]:
                    return _item
                else:
                    print("Введено невірне значення!\n")
                    return _get_action()


        _thread = _get_action()
        if int(_thread) is 1:
            _get_one_item()
        elif int(_thread) is 0:
            print("Різьби немає!")

    def get_fask(self):

        def _get_one_item():
            item = input("На яких ступенях присутня фаска: ")
            array_item = item.replace(".", ",").split(",")
            _zero = False
            for val in array_item[:self.count_level]:
                try:
                    _val = int(val)
                except Exception:
                    continue
                else:
                    if _val > self.count_level:
                        continue
                    if _val is 0:
                        print("більше немає фасок!")
                        _zero = True
                        break
                    else:
                        self.dict_config[_val-1]['isFask'] = True

            if _zero is False:
                _get_one_item()

        def _get_action():
            _data = input("Чи наявні фаски:\n\t1 - так\n\t0 - ні\n")
            try:
                _item = int(_data)
            except Exception:
                print("Введено невірне значення!\n")
                return _get_action()
            else:
                if _item in [0, 1]:
                    return _item
                else:
                    print("Введено невірне значення!\n")
                    return _get_action()

        _fask = _get_action()
        if int(_fask) is 1:
            self.isFask = True
            _get_one_item()
        elif int(_fask) is 0:
            print("Фасок немає!")

    def get_size_fask(self):
        if self.isFask is False:
            return

        for i in self.dict_config:
            if self.dict_config[i]['isFask'] is False:
                continue
            self.dict_config[i]['faskSize'] = self.get_item("Введіть розмір %s-ї фаски: ", i)


class DisplayMachineOperation:

    def __init__(self, _detalConfig):
        self.detalConfig = _detalConfig

        self.detalConfig = self.sort_mass()
        self.list_operation = []
        _first = True
        self.ra_tpl = {
            '12.5':'Чорнове точіння ',
            '6.3':'Чорнове, напівчистове точіння ',
            '3.2':'Чорнове, напівчистове, чистове точіння ',
            '1.6':'Чорнове, напівчистове, чистове точіння ',
            '0.8':'Чорнове, напівчистове, чистове точіння, шліфування '
        }

        for _arr in self.detalConfig:
            for obj in _arr:
                _severity = obj['severity']
                _diam = obj['diam']
                _leng = obj['leng']
                _tpl_operation = self.ra_tpl[_severity]
                if _first is True:
                    _first = False
                    self.list_operation.append((_tpl_operation+'поверхні діаметром %s') % _diam)
                else:
                    self.list_operation.append((_tpl_operation+'довжини {0} діаметром {1}').format(_leng, _diam))
            for obj in _arr:
                if obj['isFask']:
                    _size_fask = obj['faskSize']
                    self.list_operation.append('Точити фаску {0} величиною {1}'.format((int(obj['id'])+1), _size_fask))
            for obj in _arr:
                if obj['isThread']:
                    self.list_operation.append('Точити різьбу %s' % (int(obj['id'])+1))

            self.list_operation.append('Переустановити')
        else:
            self.list_operation.pop()


        self.full_string = ('''005 Заготівельна\n010 Токарна\nПідрізати торець\n%s\nВідрізати заготовку\n015 Контрольна''' % ("\n".join(self.list_operation)))

        print(self.full_string)

        self.print_to_file()

    def sort_mass(self):
        _flag = None
        _index = 0
        _stack = [[]]
        _stack[_index].append(self.detalConfig[0])

        def _sort_stack(_stack):
            for i in _stack:
                i.sort(key=lambda x: x['diam'], reverse=True)
            _stack.sort(key=lambda x: x[0]['diam'], reverse=True)
            return _stack

        for i in self.detalConfig:
            if int(i)+1 < len(self.detalConfig):
                _cur_diam = self.detalConfig[i]['diam']
                _next_diam = self.detalConfig[i+1]['diam']
                if _cur_diam < _next_diam:
                    if _flag is "+":
                        _stack[_index].append(self.detalConfig[i+1])
                    elif _flag is "-":
                        _index = _index+1
                        _stack.append([])
                        _stack[_index].append(self.detalConfig[i+1])
                        _flag = None
                    else:
                        _flag = "+"
                        _stack[_index].append(self.detalConfig[i+1])
                elif _cur_diam > _next_diam:
                    if _flag is "+":
                        _index = _index+1
                        _stack.append([])
                        _stack[_index].append(self.detalConfig[i+1])
                        _flag = None
                    elif _flag is "-":
                        _stack[_index].append(self.detalConfig[i+1])
                    else:
                        _flag = "-"
                        _stack[_index].append(self.detalConfig[i+1])
                else:
                    continue
        return _sort_stack(_stack)



    def print_to_file(self):
        f = open('result-machine-operation.txt', 'w')
        f.write(self.full_string)
        f.close()


detalConfig = GetDetailInfo()
DisplayMachineOperation(detalConfig.get_config())

