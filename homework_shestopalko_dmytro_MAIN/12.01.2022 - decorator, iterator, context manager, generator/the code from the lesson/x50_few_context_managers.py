from context_manager.x30_context_manager_as_class_with_handling_exception import ProgrammerV3

# https://youtrack.jetbrains.com/issue/PY-42200
# https://bugs.python.org/issue12782

if __name__ == '__main__':
    with (
            ProgrammerV3() as programmer,
    context_manager_by_generator(),
    ):
        programmer.work(hours=8)