continuing = True
contacts = {}

#handlers
#every handler acceptslist of arguments and returns message to be printed to command line
def handler_greetings(args):
    return "How can I help you?"

def handler_exit(args):
    global continuing
    continuing = False
    return "Good bye!"

def handler_add(args):
    contacts[args[0]] = args[1]
    return "contact was added succesfully"

def handler_change(args):
    contacts[args[0]] = args[1]
    return "contact was changed seccesfully"

def handler_phone(args):
    return contacts[args[0]]

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
    command = command.strip()
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
    while continuing:
        command = parce(input())
        if command:
            print(command[0](command[1:]))
        else:
            print("unknown command") #I should change this message. Later.

if __name__ == '__main__':
    main()