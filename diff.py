import json

file1_name = 'small_sili'
file2_name = 'big_sili'

# Write block's info
with open('blocks/' + file1_name + '.json') as file:
    object1 = json.load(file)
    
with open('blocks/' + file2_name + '.json') as file:
    object2 = json.load(file)

def getInput(object):
    # Count inputs
    input1 = object['input1'] / object['input1_time']
    input2 = object['input2'] / object['input2_time']
    
    # Third property check
    if hasattr(object, 'input3'):
        input3 = object['input3'] / object['input3_time']
        return input1 + input2 + input3
    else:
        return input1 + input2

def getResult(input1, input2):
    # Getting result
    first = input1 / object1['prod_time'] + object1['energy'] / object1['size']
    second = input2 / object2['prod_time'] + object2['energy'] / object2['size']
    return first / second

if __name__ == "__main__":
    print(f"First is more efficiency on: {getResult(getInput(object1), getInput(object2))}")