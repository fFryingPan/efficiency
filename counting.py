import json


class Main:
    def __init__(self, file_name):
        self.file_name = file_name
        self.inputs = []
        self.object = {}

    def getJSON(self):
        # ! Placing block's stats in a dict
        try:
            with open('blocks/' + self.file_name + '.json') as file:
                self.object = json.load(file)
            print('Taking block passed.')
            return self.object
        except Exception as e:
            print(f"Error: {e}")

    def getInput(self):
        # * Taking object
        object = self.getJSON()

        # ? If 3 inputs exists
        if hasattr(object, 'input3'):
            self.inputs = [object['input1'] / object['input1_time'],
                           object['input2'] / object['input2_time'],
                           object['input3'] / object['input3_time']]
            print("3 inputs taken.")
            return self.inputs[0] + self.inputs[1] + self.inputs[2]
        else:
            self.inputs = [object['input1'] / object['input1_time'],
                           object['input2'] / object['input2_time']]
            print("2 inputs taken.")
            return self.inputs[0] + self.inputs[1]

    def getResult(self, input):
        # * Taking object
        object = self.object
        # ! Calculating output and returning result
        output = (object['prod_time'] + object['energy']) / object['size']
        return round(input + output, 2)
