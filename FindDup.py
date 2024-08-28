my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 6, 8, 1]

def find_and_remove_duplicates(input_list):
    seen = set()
    duplicates = set()
    noduplist = []

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            noduplist.append(item)

    print(f"Original List: {input_list}")
    print(f"List without Duplicates: {noduplist}")
    print(f"Duplicate element(s): {list(duplicates)}")

find_and_remove_duplicates(my_list)
