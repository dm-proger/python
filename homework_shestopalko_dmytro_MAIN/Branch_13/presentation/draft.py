class Robot:
    def __init__(self, name: str, model: str, language: str):
        self.name_field = name
        self.model_field = model
        self.language_field = language

    def speak_robot(self):
        print("Hello human")


def main():
    robot_01 = Robot("R2-D2", "droid", "vocalisation of binary")
    print(f"My name is {robot_01.name_field}. I am {robot_01.model_field}. I speak in {robot_01.language_field}")
    robot_01.speak_robot()


if __name__ == "__main__":
    main()
