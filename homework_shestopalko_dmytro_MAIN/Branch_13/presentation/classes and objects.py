class Robot:
    def __init__(self, name: str, model: str, language: str):
        self.name = name # name is  the value provided when you create a Robot object
        self.model = model
        self.language = language

    def speak_robot():
        print("Hello, humans!")


robot_01 = Robot("R2-D2", "droid", "vocalisation of binary")
print(type(robot_01))
robot_02 = Robot("C-3PO", "humanoid", "galactic basic")

#we specify the name of the field here, not the value!!!!!!!
print(f"My name is {robot_01.name}. I am a {robot_01.model}. I speak in {robot_01.language}")
print(f"My name is {robot_02.name}. I am a {robot_02.model}. I speak in {robot_02.language}")

if __name__ == "__main__":
    Robot.speak_robot()
