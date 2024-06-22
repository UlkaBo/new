
CONTACTS = {}
NOT_FOUND_ERROR = "Contact not found."


def input_error(func):
    def inner(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                return result
            except ValueError: #(KeyError): #, TypeError, ValueError, IndexError):
                return "Incorrect value. Please, try again."

    return inner


def handler(action):
    return ACTIONS[action]


@input_error
def hello():
    return "How can I help you?"


@input_error
def add(name, phone):
    if name not in CONTACTS:
        CONTACTS[name] = phone
        return "Contact added successfully!"
    return "Contact with such name already exists."


@input_error
def change(name, phone):
    if name in CONTACTS:
        CONTACTS[name] = phone
        return "Contact updated successfully!"
    return NOT_FOUND_ERROR


@input_error
def phone(name):
    return CONTACTS[name]


@input_error
def show_all():
    if len(CONTACTS) > 0:
        return "\n".join([f"{k}: {v}" for k, v in CONTACTS.items()])
    elif len(CONTACTS) == 0:
        return "Contacts library is empty"


ACTIONS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all
}


def main():
    while True:
        #try:
            customer_input = input().split()
            action = customer_input.pop(0).lower()
            full_action = ""

            if action in ("add", "change"):
                name, phone = customer_input
                result = handler(action)
                print(result(name, phone))

            elif action in ("phone"):
                name = customer_input[0]
                result = handler(action)
                print(result(name))

            elif action == "hello":
                result = handler(action)
                print(result())

            elif action == "show" and customer_input[0].lower() == "all":
                full_action = f"{action.lower()} {customer_input[0].lower()}"
                result = handler(full_action)
                print(result())

            elif action in ("close", "exit", ".") or \
                    (action == "good" and customer_input[0].lower() == "bye"):
                print("Good bye!")
                break

            elif full_action or action not in ACTIONS:
                print("Unknown action. Please, try again.")

        #except (IndexError, ValueError, KeyError):
        #    print("Error occurred. Try again.")


if __name__ == '__main__':
    main()
