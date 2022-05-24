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
    def decorator(func):
        def wrapper(*args):
            dict1 = func(*args)
            new_dict = {}
            for key in required_keys:
                new_list = []
                for i in key.split("__"):
                    if i in dict1.keys():
                        if dict1[i] == '':
                            new_list.append('Empty value')
                        else:
                            new_list.append(dict1[i])
                    else:
                        raise ValueError
                    new_dict[key] = ' '.join(new_list)
            return new_dict
        return wrapper
    return decorator


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return decorator

