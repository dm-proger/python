from contextlib import contextmanager

from context_manager.x10_without_context_manager import Programmer


# noinspection PyShadowingNames
@contextmanager
def programmer_by_generator():
    programmer = Programmer()
    programmer.at_begin()
    try:
        yield programmer
    finally:
        programmer.at_end()


if __name__ == '__main__':
    with programmer_by_generator() as programmer:
        programmer.work(hours=8)