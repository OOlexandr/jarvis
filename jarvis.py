contacts = {}

#error handler. I didn't come up with a better way to do it
def error_handler(func):
    def inner(args):
        try:
            return func(args)
        except KeyError:
            return "The user is not in the list"
        except ValueError:
            return "Number is invalid"
        except IndexError:
            return "Please enter user name and number"
    return inner

def is_phone_number(string):
    string = string.strip()
    if string[0] == '+':
        string = string[1:]
    string = string.replace('(', '').replace(')', '').replace('-',  '')
    return string.isdigit()

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
    if not is_phone_number(args[1]):
        raise ValueError
    contacts[args[0]] = args[1]
    return "Contact was added succesfully"

@error_handler
def handler_change(args):
    if not args[0] in contacts:
        raise KeyError
    if not is_phone_number(args[1]):
        raise ValueError
    contacts[args[0]] = args[1]
    return "Contact was changed seccesfully"

@error_handler
def handler_phone(args):
    return contacts[args[0]]

@error_handler
def handler_show_all(args):
    message = "Here are all saved contacts:\n"
    for c in contacts:
        message += c + ': ' + contacts[c] + '\n'
    return message

handlers = {"hello": handler_greetings,
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