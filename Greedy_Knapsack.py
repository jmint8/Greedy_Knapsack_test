import sys

def read_items(file_name, max_items):
    items = []
    with open(file_name, 'r') as file:
        for i in range(max_items):
            name = file.readline().strip()
            if not name:  # Stop if EOF is reached
                break
            I_weight = int(file.readline().strip())  # Read item weight
            I_value = int(file.readline().strip())  # Read item value
            items.append((I_value, I_weight))
    return items

def by_value(items, weight_limit): # so it is funny, all of  the test cases for "by_vlaue" passed without sorting the list except for test 9.
    new_items = sorted(items, key=lambda x: x[0] , reverse=True) 
    t_value = 0
    t_weight = 0
    binary_string = ['0'] * len(items)
    
    # Tracking i of the original item list :/ this is dumb I had to look up how to do this.
    item_indices = {item: i for i, item in enumerate(items)} # way too complicated just for binary representation of original input list.
    
    for value, weight in new_items:
        og_index = item_indices[(value, weight)]
        if t_weight + weight <= weight_limit:
            t_weight += weight
            t_value += value
            binary_string[og_index] = '1'
    
    return ''.join(binary_string), t_weight, t_value

def by_value_weight(items, weight_limit):
    new_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True) 
    t_value = 0
    t_weight = 0
    binary_string = ['0'] * len(items)
    
    # Tracking i of the original item list :/ this is dumb I had to look up how to do this.
    item_indices = {item: i for i, item in enumerate(items)} # way too complicated just for binary representation of original input list.
    
    for value, weight in new_items:
        og_index = item_indices[(value, weight)]
        if t_weight + weight <= weight_limit:
            t_weight += weight
            t_value += value
            binary_string[og_index] = '1'
    
    return ''.join(binary_string), t_weight, t_value

def main():

    max_items = int(sys.argv[1])
    #max_items = 10
    weight_limit = int(sys.argv[2])
    #weight_limit = 10
    heuristic_name = sys.argv[3]
    #3heuristic_name = 'by_value'
    #heuristic_name = 'value_to_weight'
    input_file_name = sys.argv[4]
    #input_file_name = 'knapsack_input1.txt'

    items = read_items(input_file_name, max_items)
    #items = [(200, 2), (205, 3), (500, 11), (20, 2), (90, 15), (120, 25), (5000, 90), (400, 150), (40, 2), (110, 1)]


    if heuristic_name == "by_value":
        binary_string, total_weight, total_value = by_value(items, weight_limit)
    elif heuristic_name == "value_to_weight":
        binary_string, total_weight, total_value = by_value_weight(items, weight_limit)
    else:
        print("Use 'by_value' or 'value_to_weight' as the heuristic name.")
        return

    print(binary_string)
    print(total_weight)
    print(total_value)
main()
if __name__ == "__main()__":
    main()
