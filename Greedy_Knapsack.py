import sys

def read_input_file(input_file_name, max_items):
    items = []
    with open(input_file_name, 'r') as file:
        for i, line in enumerate(file):
            if i >= max_items:
                break
            value, weight = map(int, line.split())
            items.append((value, weight))
    return items

def greedy_knapsack_by_value(items, weight_limit):
    items.sort(key=lambda x: x[0], reverse=True)
    return select_items(items, weight_limit)

def greedy_knapsack_by_value_to_weight(items, weight_limit):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    return select_items(items, weight_limit)

def select_items(items, weight_limit):
    total_value = 0
    total_weight = 0
    selected_items = [0] * len(items)
    
    for i, (value, weight) in enumerate(items):
        if total_weight + weight <= weight_limit:
            selected_items[i] = 1
            total_value += value
            total_weight += weight
    
    return selected_items, total_value, total_weight

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 greedy_knapsack.py <max_items> <weight_limit> <heuristic_name> <input_file_name>")
        return
    
    max_items = int(sys.argv[1])
    weight_limit = int(sys.argv[2])
    heuristic_name = sys.argv[3]
    input_file_name = sys.argv[4]
    
    items = read_input_file(input_file_name, max_items)
    
    if heuristic_name == "by_value":
        selected_items, total_value, total_weight = greedy_knapsack_by_value(items, weight_limit)
    elif heuristic_name == "value_to_weight":
        selected_items, total_value, total_weight = greedy_knapsack_by_value_to_weight(items, weight_limit)
    else:
        print("Invalid heuristic name. Use 'by_value' or 'value_to_weight'.")
        return
    
    print("".join(map(str, selected_items)))
    print(total_value)
    print(total_weight)

if __name__ == "__main__":
    main()
