import json

file_name = 'big_sili'

# Write block's info
with open('blocks/' + file_name + '.json') as file:
    object = json.load(file)
            
def getInput():
    # Count inputs
    input1 = object['input1'] / object['input1_time']
    input2 = object['input2'] / object['input2_time']
    
    # Thrid property check
    if hasattr(object, 'input3'):
        input3 = object['input3'] / object['input3_time']
        return input1 + input2 + input3
    else:
        return input1 + input2

def getResult(input):
    # Getting result
    return round(input + object['prod_time'] + object['energy'] / object['size'], 2)
    
if __name__ == '__main__':
    print(f"{file_name}'s efficiency: {getResult(getInput())}")
