

class Users_class:
    def __init__(self, id_user, f_name, s_name,  number, date_reg, time_reg):
        ''' id_user, f_name, s_name,  number, date_reg, time_reg  '''
        self.__id_user = id_user #ID пользователя
        self.__f_name = f_name #Имя пользователя
        self.__s_name = s_name #Фамилия пользователя
        self.__number = number #Номер телефона пользователя
        self.__date_reg = date_reg #дата регистрации
        self.__time_reg = time_reg #Время последнего обращения

    def get_id_user(self):
        return self.__id_user

    def set_id(self):
        if self.__id_user != 0:
            return self.__id_user
        else:
            print('Данные не коректны')

    def get_f_name(self):
        return self.__f_name

    def set_f_name(self):
        if self.__f_name != " ":
            return self.__f_name
        else:
            print('Данные не коректны')

    def get_s_name(self):
        return self.__s_name

    def set_s_name(self):
        if self.__s_name != " ":
            return self.__s_name
        else:
            print('Данные не коректны')

    def get_number(self):
        return self.__number

    def set_number(self):
        if self.__number != '':
            return self.__number
        else:
            print('Данные не коректны')

    def get_date_reg(self):
        return self.__date_reg

    def set_date_reg(self):
        if self.__date_reg != " ":
            return self.__date_reg
        else:
            print('Данные не коректны')

    def get_time_reg(self):
        return self.__time_reg


    def set_time_reg(self):
        if self.__time_reg != '':
            return self.__time_reg
        else:
            print('Данные не коректны')

class SMS_class:
    def __init__(self, id_sms, id_user, txt_sms, date_sms, time_sms):
        ''' id_sms, id_user, txt_sms, date_sms, time_sms'''
        self.__id_sms = id_sms           #sms ID
        self.__id_user = id_user         #ID  пользователя
        self.__txt_sms = txt_sms         #sms пользователя
        self.__date_sms = date_sms         #sms пользователя
        self.__time_sms = time_sms        #sms пользователя


    def get_id_sms(self):
        return self.__id_sms

    def set_id_sms(self):
        if self.__id_sms != 0:
            return self.__id_sms
        else:
            print('Данные не коректны')

    def get_id_user(self):
        return self.__id_user


    def set_id_user(self):
        if self.__id_user != 0:
            return self.__id_user
        else:
            print('Данные не коректны')

    def get_txt_sms(self):
        return self.__txt_sms

    def set_txt_sms(self):
        if self.__txt_sms != " ":
            return self.__txt_sms
        else:
            print('Данные не коректны')

    def get_date_sms(self):
        return self.__date_sms

    def set_date_sms(self):
        if self.__date_sms != '':
            return self.__date_sms
        else:
            print('Данные не коректны')

    def get_time_sms(self):
        return self.__time_sms

    def set_time_sms(self):
        if self.__time_sms != '':
            return self.__time_sms
        else:
            print('Данные не коректны')