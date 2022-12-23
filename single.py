import counting as count


class Main:
    def __init__(self):
        self.object_name = "small_sili"
        # ! Creating an object through the library
        self.object = count.Main(self.object_name)
        # * Taking the input
        self.input = self.object.getInput()

    def showResult(self):
        result = self.object.getResult(self.input)
        print(f"Block's efficiency: {result}")


if __name__ == "__main__":
    Main().showResult()
