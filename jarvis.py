continuing = True

#handlers
#every handler acceptslist of arguments and returns message to be printed to command line
def handler_greetings(args):
    return "How can I help you?"

handlers = {"hello": handler_greetings}
#key - command, value - handler.

#parcer
def parce(command):
    #returns list. first element - handler and the rest are arguments
    command = command.strip()
    parced_command = []
    for handler in handlers:
        if command.startswith(handler):
            command = command.removeprefix(handler)
            parced_command.append(handlers[handler])
            break
    parced_command += command.split()
    return parced_command

def main():
    while continuing:
        command = parce(input())
        print(command[0](command[1:]))

if __name__ == '__main__':
    main()