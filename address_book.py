from collections import UserDict

class RecordAlreadyExists(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value
    
    def change_value(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def __init__(self, name, phones):
        self.name = Name(name)
        self.phones = []
        for i in phones:
            self.phones.append(Phone(i))
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def change_phone(self, phone, new_phone):
        for i in self.phones:
            if i.value == phone:
                i.change_value(new_phone)
    
    def delete_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

class AddressBook(UserDict):
    def add_record(self, name):
        #if no record with this name exists - create a new one
        #if record already exists - raise exeption
        if name in self.data:
            raise RecordAlreadyExists
        self.data[name] = Record(name)
    
    def add_record(self, name, phone):
        #if no record with this name exists - create a new one
        #if record already exists add the phone to the record
        if name in self.data:
            self.data[name].add_phone(phone)
        else:
            self.data[name] = Record(name, phone)


if __file__ == "__main__":
    #for testing
    book = AddressBook()
    book.add_record()