from pprint import pprint
import datetime
from functools import wraps


def to_log(path):
    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            start = datetime.datetime.now()

            print(f'{old_function.__name__} was called at {start}')
            result = old_function(*args, **kwargs)

            finish = datetime.datetime.now()
            work_time = finish - start
            print(f'{result} \n was returned at {finish} with', *args, **kwargs)
            _args = tuple(*args)
            _kwargs = dict(**kwargs)

            with open(path, "a") as log:
                log.write(
                    f'''{old_function.__name__} was called at {start} with following arguments:, {_args}, {_kwargs}
it returned: {result}
function worked for {work_time}\n''')

            return result

        return new_function

    return decorator
