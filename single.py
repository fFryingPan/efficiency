import counting as count


class Main:
    def __init__(self):
        self.object_name = "small_sili"
        # ! Creating a "counting" object through the library
        self.object = count.Main(self.object_name)


if __name__ == "__main__":
    cs = Main().object
    # * Taking an input from the object
    input = cs.getInput()
    print(f"Block's efficiency is {cs.getResult(input)}")
