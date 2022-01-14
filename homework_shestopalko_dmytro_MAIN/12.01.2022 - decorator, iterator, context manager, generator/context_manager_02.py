from context_manager import Programmer


class ProgrammerV2(Programmer):

    def __enter__(self):
        self.at_begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        self.at_end()


if __name__ == "__main__":
    with ProgrammerV2() as programmer:
        programmer.work(hours=8)