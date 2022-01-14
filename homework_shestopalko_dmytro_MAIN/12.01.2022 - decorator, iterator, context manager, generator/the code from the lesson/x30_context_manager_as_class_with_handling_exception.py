from context_manager.x20_context_manager_as_class import ProgrammerV2


class ProgrammerV3(ProgrammerV2):
    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)

        print(f'Exception "{exc_type.__name__}" handled')

        return True


if __name__ == '__main__':
    with ProgrammerV3() as programmer:
        programmer.work(hours=8)