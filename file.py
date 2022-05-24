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
    def decorator_function(decor):
        def decoration(*args, **kwargs):
            mod_dict = decor(*args, **kwargs)

            out_dict = {}
            for key in required_keys:
                out_dict[key] = ""

            for r_key in required_keys:
                temp_list = []
                temp_len = 0
                for sub_key in str(r_key).split("__"):
                    if sub_key in dict(mod_dict).keys():
                        temp_len += len(mod_dict[sub_key])
                        temp_list.append(mod_dict[sub_key])
                    else:
                        raise ValueError("Nope")
                if temp_len == 0:
                    out_dict[r_key] = "Empty value"
                else:
                    out_dict[r_key] = " ".join(temp_list)

            return out_dict
        return decoration
    return decorator_function


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return decorator

