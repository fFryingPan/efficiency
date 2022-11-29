import json


class Main:
    def __init__(self):
        self.file_name = 'small_sili'
        self.inputs = []
        self.object = {}
        
    def getJSON(self):
        try:
            with open ('blocks/' + self.file_name + '.json') as file:
                self.object = json.load(file)
            print('Got.')
            
            return self.object
        except Exception as e:
            print(f"Error: {e}")
            
    def getInput(self):
        object = Main().getJSON()
        
        if hasattr(object, 'input3'):
            self.inputs = [object['input1'] / object['input1_time'],
                           object['input2'] / object['input2_time'],
                           object['input3'] / object['input3_time']]
            
            return self.inputs[0] + self.inputs[1] + self.inputs[2]
        else:
            self.inputs = [object['input1'] / object['input1_time'],
                           object['input2'] / object['input2_time']]
            
            return self.inputs[0] + self.inputs[1]
            
    def getResult(self, input):
        object = Main().getJSON()
        
        return round(input + object['prod_time'] + object['energy'] / object['size'], 2)
            
if __name__ == "__main__":
    output = Main().getResult(Main().getInput())
    
    print(f"Block's efficiency: {output}.")