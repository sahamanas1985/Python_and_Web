# https://jsoncrack.com/editor
# Employee,Manager - in csv file

import csv
import json
from collections import defaultdict

def build_tree(data):
    # Create a mapping of managers to their employees
    children_map = defaultdict(list)

    for employee, manager in data:
        children_map[manager].append(employee)

    # Define a recursive function to build the tree
    def add_children(manager):
        if manager in children_map:
            return {manager: [add_children(emp) for emp in children_map[manager]]}
        return manager

    # Start building the tree from all top-level managers
    tree = {}
    for employee in children_map:
        if employee not in data_dict and employee != '':
            tree.update(add_children(employee))

    return tree

def csv_to_json_tree(csv_file, output_json_file):
    # Read the CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # Remove headers if present (assuming the first row is headers)
    headers = data[0]
    data = data[1:]

    # Create a dictionary for easy access
    global data_dict
    data_dict = {emp: mgr for emp, mgr in data}

    # Build the tree
    tree = build_tree(data)
    
    # Save the tree to a JSON file
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(tree, json_file, ensure_ascii=False, indent=4)

# Example usage
if __name__ == "__main__":
    csv_file = 'employees.csv'  # Path to your CSV file
    output_json_file = 'employees_tree.json'  # Output JSON file
    csv_to_json_tree(csv_file, output_json_file)
    print(f"JSON tree saved to {output_json_file}")
