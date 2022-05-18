from types import MethodType

def greeter(func):
    def wrapped(*args):
        output = func(args)
        parts = output.split()
        return "Aloha " + " ".join(name.capitalize() for name in parts)

    return wrapped


def sums_of_str_elements_are_equal(func):
    def sum_digits(number: str):
        if int(number) < 0:
            return sum([-1 * int(d) for d in number if d.isdigit()])
        return sum([int(d) for d in number if d.isdigit()])

    def wrapped(*args):
        output = func(args)
        left, right, *rest = output.split()
        if rest:
            raise Exception("Bad return")

        sum_left = sum_digits(left)
        sum_right = sum_digits(right)

        eq = "==" if sum_right == sum_left else "!="

        return f"{sum_left} {eq} {sum_right}"

    return wrapped


def format_output(*required_keys):
    def decorator(func):
        def wrapped(*args):
            output = func(args)
            final_output = {}
            for key in required_keys:
                if "__" in key:
                    sub_keys = key.split("__")
                    try:
                        final_output[key] = " ".join(output[sub_key] for sub_key in sub_keys)
                    except:
                        raise ValueError()
                else:
                    try:
                        final_output[key] = output[key] if output[key] != "" else "Empty value"
                    except:
                        raise ValueError()

            return final_output

        return wrapped

    return decorator


def add_method_to_instance(klass):
    def decorator(func):
        def wrapped(self):
            return func()
        setattr(klass, func.__name__, wrapped)
        return func

    return decorator


def add_method_to_class(klass):
    def decorator(func):
        setattr(klass, func.__name__, func)
        return func

    return decorator
