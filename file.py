from functools import wraps

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
    keys = required_keys

    def dict_decorator(func):
        def in_func(*args, **kwargs):
            in_values = func(*args, **kwargs)
            out_dict = dict()
            try:
                for key in keys:
                    if '__' in key:
                        list = key.split('__')
                        value = ''
                        for element in list:
                            value += in_values[element] + ' '
                        value = value[:-1]
                    else:
                        value = in_values[key]
                    if value == '':
                        value = 'Empty value'
                    out_dict.update({key: value})
                return out_dict
            except:
                raise ValueError
        return in_func
    return dict_decorator 


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return decorator

