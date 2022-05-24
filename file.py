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
    def collect_keys(func):
        def check_keys(*args):
            input_dict = func(*args)
            output_dict = dict()
            for required_key in required_keys:
                if required_key in input_dict:
                    if value := input_dict[required_key]:
                        output_dict[required_key] = value
                    else:
                        output_dict[required_key] = "Empty value"
                else:
                    split_keys = required_key.split('__')
                    tmp = list()
                    for split_key in split_keys:
                        if split_key in input_dict:
                            if value := input_dict[split_key]:
                                tmp.append(value)
                            else:
                                tmp.append("Empty value")
                        else:
                            raise ValueError
                    output_dict[required_key] = " ".join(tmp)

            return output_dict

        return check_keys

    return collect_keys


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return decorator

