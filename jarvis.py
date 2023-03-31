import address_book

contacts = address_book.AddressBook()

def error_handler(func):
    def inner(args):
        try:
            return func(args)
        except KeyError:
            return "The user is not in the address book"
        except ValueError:
            return "Number is invalid"
        except IndexError:
            return "Please enter user name and number"
        except address_book.RecordAlreadyExists:
            return "The user is already in the address book"
        except address_book.PhoneAlreadyExistsError:
            return "The phone already exists"
        except address_book.PhoneNotFoundError:
            return "The phone is not found"
    return inner

#handlers
#every handler acceptslist of arguments and returns message to be printed to command line
@error_handler
def handler_greetings(args):
    return "How can I help you?"

@error_handler
def handler_exit(args):
    return "Good bye!"

@error_handler
def handler_add(args):
    name = address_book.Name(args[0])
    phone = address_book.Phone(args[1]) if args[1:] else None
    contacts.add_record(name, phone)
    return "Contact was added succesfully"

@error_handler
def handler_change(args):
    old_phone = address_book.Phone(args[1])
    new_phone = address_book.Phone(args[2])
    contacts[args[0]].change_phone(old_phone, new_phone)
    return "Contact was changed seccesfully"

@error_handler
def handler_phone(args):
    contact = contacts[args[0]]
    result = contact.name.value + ':'
    for phone in contact.phones:
        result += " " + phone.value
    return result

@error_handler
def handler_show_all(args):
    if not contacts:
        return "Contacts list is currently empty"
    message = "Here are all saved contacts:"
    for c in contacts:
        message += '\n' + handler_phone([c])
    return message

handlers = {"hello": handler_greetings,
            "good bye": handler_exit,
            "close": handler_exit,
            "exit": handler_exit,
            "add": handler_add,
            "change": handler_change,
            "phone": handler_phone,
            "show all": handler_show_all}
#key - command, value - handler.

#parcer
def parce(command):
    #returns list. first element - handler and the rest are arguments
    #returns None if command is not recognized
    command = command.strip().lower()
    parced_command = []
    for handler in handlers:
        if command.startswith(handler):
            command = command.removeprefix(handler)
            parced_command.append(handlers[handler])
            break
    if parced_command:
        parced_command += command.split()
        return parced_command
    return None

def main():
    while True:
        command = parce(input())
        if command:
            result = command[0](command[1:])
            print(result)
            if result == "Good bye!":
                return
        else:
            print("unknown command")

if __name__ == '__main__':
    main()