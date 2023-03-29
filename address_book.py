from collections import UserDict

class RecordAlreadyExists(Exception):
    pass

class PhoneAlreadyExistsError(Exception):
    pass

class PhoneNotFoundError(Exception):
    pass

def is_phone_number(string):
    string = string.strip()
    if string[0] == '+':
        string = string[1:]
    string = string.replace('(', '').replace(')', '').replace('-',  '')
    return string.isdigit()

class Field:
    def __init__(self, value):
        self.value = value
    
    def change_value(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if is_phone_number(value):
            self.value = value
        else:
            raise ValueError
    
    def change_value(self, value):
        if is_phone_number(value):
            self.value = value
        else:
            raise ValueError

class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def __init__(self, name, phones):
        self.name = Name(name)
        self.phones = []
        if type(phones) == list:
            for i in phones:
                self.phones.append(Phone(i))
        else:
            self.phones.append(Phone(phones))
    
    def add_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                raise PhoneAlreadyExistsError
        self.phones.append(Phone(phone))
    
    def change_phone(self, phone, new_phone):
        #I haven't find a better way to do it
        for i in self.phones:
            if i.value == phone:
                i.change_value(new_phone)
                return
        raise PhoneNotFoundError
    
    def delete_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                return
        raise PhoneNotFoundError

class AddressBook(UserDict):
    def add_record(self, name, phones = ''):
        #if no record with this name exists - create a new one
        #if record already exists add the phone to the record
        #if record exists and list phones is empty - raises an exception
        if name in self.data:
            if phones:
                self.data[name].add_phone(phones)
            else:
                raise RecordAlreadyExists
        else:
            self.data[name] = Record(name, phones)
    
    def get_record(self, name):
        #returns the record as a dictionary.
        record = self.data[name]
        return {"name": name,
                "phones": record.phones}

    def change_phone(self, name, old_phone, new_phone):
        self.data[name].change_phone(old_phone, new_phone)