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
    def real_wrapper(func):
        def insider_wrapper(*args):
            got_dict = func(*args)
            
            list_of_keys = []
            for record in required_keys:
                for result in record.split('__'):
                    list_of_keys.append(result)
                    
            list_of_values = []
            help_dict = {}
            for key in list_of_keys:
                if(key in got_dict):
                    dict_value = got_dict.get(key)
                    if dict_value == '':
                        help_dict[key] = "Empty value"
                    else:
                       help_dict[key] = dict_value
                else:
                    raise ValueError
            
            help_list = [record.split('__') for record in required_keys]
            response_dict = {}
            
            for record in help_list:
                if len(record) > 1:
                    value_list = [help_dict.get(key) for key in record]
                    response_dict['__'.join(record)] = ' '.join(value_list)
                else:
                    response_dict[record[0]] = help_dict.get(record[0])
                    
            return response_dict                  
        return insider_wrapper
    return real_wrapper


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return decorator

