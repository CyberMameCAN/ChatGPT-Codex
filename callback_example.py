# Example of using a callback function

def say_hello(name):
    print(f"Hello, {name}!")


def handler(func, *args, **kwargs):
    """Executes a function passed as a callback."""
    return func(*args, **kwargs)


if __name__ == "__main__":
    # Basic example using a callback
    callback = say_hello
    handler(callback, 'World')

    # Another example using a lambda as a callback
    result = handler(lambda x, y: x + y, 3, 4)
    print('3 + 4 =', result)
