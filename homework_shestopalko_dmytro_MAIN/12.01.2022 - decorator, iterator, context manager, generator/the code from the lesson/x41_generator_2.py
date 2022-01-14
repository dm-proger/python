from contextlib import contextmanager


@contextmanager
def context_manager_by_generator():
    print('Begin')
    try:
        yield
    finally:
        print('End')


if __name__ == '__main__':
    with context_manager_by_generator():
        print('Inside')
        raise ValueError