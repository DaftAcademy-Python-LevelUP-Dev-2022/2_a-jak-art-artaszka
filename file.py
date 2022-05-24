def greeter(func):
    def inner(*args, **kwargs):
        data_from_function = func(*args, **kwargs).title()
        result = "Aloha " + data_from_function
        return result
    
    return inner


def sums_of_str_elements_are_equal(func):
    def inner(*args):
        def suma(count):
            how_many = 0
            if str(count)[0] == "-":
                for numbers in str(count)[1:]:
                    how_many -= int(numbers)
            else:
                for numbers in str(count):
                    how_many += int(numbers)
            return how_many
        my_list = func(*args).split()
        num_one = suma(my_list[0])
        num_two = suma(my_list[1])
        if num_one == num_two:
            return str(num_one) + ' == ' + str(num_two)
        else:
            return str(num_one) + ' != ' + str(num_two)
    return inner


def format_output(*required_keys):
    def leave_proper_keys(func):
        def format_dict(*args, **kwargs):
            create_keys = {k: k.split('__') for k in required_keys}
            create_dict = func(*args, **kwargs)
            flat_list_of_new_keys_value = [item for sublist in create_keys.values() for item in sublist]
            for k in flat_list_of_new_keys_value:
                if k not in create_dict.keys():
                    raise ValueError
            new_dict = {key: ' '.join([create_dict[v] if create_dict[v] != '' else 'Empty value' for v in value]) for
                        key, value in create_keys.items()}
            return new_dict
        return format_dict
    return leave_proper_keys


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return decorator

