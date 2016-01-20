# класс для получения данных от пользователя
class GetDetailInfo:
    def __init__(self, *args):
        self.count_level = self.get_count_level() #количество ступеней
        self.dict_config = {a: {'id':a, 'diam':None, 'leng':None, 'severity':None, 'isThread':False, 'isFask':False, 'faskSize':None} for a in range(int(self.count_level))} # создаем дефолтный конфиг на количество ступеней
        self.isFask = False # вспомагательная переменная - будут ли точиться фаски

        # вызов функций
        self.get_diameter(self.count_level)
        self.get_leng_level(self.count_level)
        self.get_severity_level()
        self.get_thread()
        self.get_fask()
        self.get_size_fask()

    # функция с помощю которой мы можем получить готовый конфиг за пределами данного класса
    def get_config(self):
        return self.dict_config
    # функция для получения количества ступеней
    def get_count_level(self):
        _data = input("Введіть кількість ступенів: ") # получаем инфо
        #блок для проверки коректности данных
        try:
            _item = int(_data) #преобразовуем в int значение
        except Exception:
            print("Введено невірне значення!\n")
            return self.get_count_level() # если данные не цифра значит сообщаем пользователю и запускаем эту же функция что бы спросить заново
        else:
            return _item # если данные коректны возвращаем введенные данные коду который вызвал данную функцию
        #### Аналогичный код комментировать больше не буду

    # функция для получения значения к конкретной ступене
    def get_item(self, mess, index):
        _data = input(mess % (index+1))
        try:
            _item = int(_data)
        except Exception:
            print("Введено невірне значення!\n")
            return self.get_item(mess, index)
        else:
            return _item
    # функция для получения диаметра
    def get_diameter(self, count_level):
        for i in range(int(count_level)): # проходим по массиву
            self.dict_config[i]['diam'] = self.get_item("Введіть діаметр %s-го ступеню: ", i) # получаем информацию по ступени и записываем в конфиг
    # функция для получения длинны ступени
    def get_leng_level(self, count_level):
        for i in range(int(count_level)):
            self.dict_config[i]['leng'] = self.get_item("Введіть довжину %s-го ступеню: ",i)
    # функция для получения досткости Ra изделия
    def get_severity_level(self):
        # функция для парсинга введенной строки - данные досткости
        def _get_one_severity(text):
            const_severity = ["12.5", "6.3", "3.2", "1.6", "0.8"] #массив с условиями
            item = input(text) # получаем инфу от юзера
            item = item.replace(",", ".") # заменяем розделительные знаки на подходящие нам
            if item in const_severity:
                return item # если значение подходит, возвращаем его программе
            else:
                print("Неверній параметр жосткости!!!\n")
                _get_one_severity(text) # ошибка и спрашиваем заново
        # функция для выбора дальнейшего действитя
        def _get_action():
            _data = input(
                "Вызначіть Ra ступенів:\n\t1 - жорсткість Ra  однакова для всіх ступенів\n\t2 - жорсткість Ra різна для кожного ступеня\n"
            ) # получаем значение
            try:
                _item = int(_data)
            except Exception:
                print("Введено невірне значення!\n")
                return _get_action()
            else:
                if _item in [1, 2]: # если значение попадает в наш диапазон, возвращаем программе
                    return _item
                else:
                    print("Введено невірне значення!\n")
                    return _get_action() # если ошибка, заново

        severity_level = _get_action() # вызываем функцию и записываем результат

        if int(severity_level) is 1: # если введено 1 то получаем
            _severity_level = _get_one_severity("Введіть жорсткість Ra для ступенів: ") # получаем жосткость для всех ступеней
            for i in range(int(self.count_level)):
                self.dict_config[i]['severity'] = _severity_level # в цикле зписываем жосткость для всех
        elif int(severity_level) is 2:
            for i in range(int(self.count_level)):
                self.dict_config[i]['severity'] = _get_one_severity("Введіть жорсткість Ra %s-го ступеню: " % (i+1)) # в цикле спрашиваем жосткость для каждого елемента и записываем
        else:
            print("Невірне значення!!!\n\n")
            self.get_severity_level() # неверное значение, спрашиваем заново.

    # функция которая получает информацию по резьбе
    def get_thread(self):
        # функция которая парсит массив номеров ступеней из введенной строки
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
        # функция для выбора дальнейшего действитя
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
    # Функция получает инфу по фаскам
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
    # функция получает инфу по размерам фаски
    def get_size_fask(self):
        if self.isFask is False:
            return

        for i in self.dict_config:
            if self.dict_config[i]['isFask'] is False:
                continue
            self.dict_config[i]['faskSize'] = self.get_item("Введіть розмір %s-ї фаски: ", i)

# класс для построения результата программы и вывода в файл
class DisplayMachineOperation:

    def __init__(self, _detalConfig):
        self.detalConfig = _detalConfig
        self.detalConfig = self.sort_mass() # сортируем конфиг и получаем итоговый массив для вывода
        self.list_operation_conf = []
        self.list_operation = []
        _first = True
        self.ra_tpl = {
            '12.5':'Чорнове точіння ',
            '6.3':'Чорнове, напівчистове точіння ',
            '3.2':'Чорнове, напівчистове, чистове точіння ',
            '1.6':'Чорнове, напівчистове, чистове точіння ',
            '0.8':'Чорнове, напівчистове, чистове точіння, шліфування '
        } # шаблон для вывода
        # Пробегаем по массиву конфига
        for _arr in self.detalConfig:
            #пробегаем по подмассиву
            for obj in _arr:
                _severity = obj['severity'] # получаем жосткость ступени
                _diam = obj['diam'] # получаем диаметр
                _leng = obj['leng'] # получаем длинну
                _tpl_operation = self.ra_tpl[_severity] # получаем шаблон для действия
                if _first is True: # проверяем на первый елемент в массиве
                    _first = False
                    self.list_operation.append((_tpl_operation+'поверхні діаметром %s') % _diam) # спец шаблон без длинны
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

        for _arr in self.detalConfig:
            for obj in _arr:
                _id = obj['id']
                _severity = obj['severity']
                _diam = obj['diam']
                _leng = obj['leng']
                _isThread = obj['isThread']
                _isFask = obj['isFask']
                _faskSize = obj['faskSize']
                self.list_operation_conf.append("""
ID - {0}\n
Диаметр - {1}\n
Довжина - {2}\n
Жорсткість Ra - {3}\n
Різьба - {4}\n
Фаска - {5}\n
Розмір фаска - {6}\n
                """.format(_id, _diam, _leng, _severity, _isThread, _isFask, _faskSize))



        self.full_string = ('''
        Підсистема проектування технології\n
           виготовлення деталей класу 71\n
          (підкласи 711000 713000 715000)\n
        Виконав: Нестеренко А.О. гр. ПБ-21\n\n
---------------------------------
005 Заготівельна\n
010 Токарна\n
Підрізати торець\n
{0}\n
Відрізати заготовку\n
015 Контрольна\n\n
---------------------------------
{1}'''.format("\n".join(self.list_operation), "\n".join(self.list_operation_conf)))

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

