import counting as count


class Main:
    def __init__(self):
        self.object_name = "small_sili"
        self.object = count.Main(self.object_name)

if __name__ == "__main__":
    cs = count.Main(Main().object_name)
    input = cs.getInput()

    print(f"Block's efficiency is {cs.getResult(input)}")