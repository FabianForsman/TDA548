# package samples

# A dictionary, aka a map, is a structure for storing and looking up
# values using keys (like old paper telephone book).
# NOTE: One direction is prioritized (given key, find value).
from typing import Dict


def use_a_map_program():
    literal_name_sv: Dict[str, int] = {}

    # Store key (str) and value (int)
    literal_name_sv["ett"] = 1
    literal_name_sv["två"] = 2
    literal_name_sv.update([("tre", 3), ("fyra", 4)])

    # Retrieve value using key
    print(literal_name_sv["ett"])
    print(literal_name_sv["fyra"])

    # Access all key's or all values
    keys = list(literal_name_sv.keys())
    print(keys)
    values = list(literal_name_sv.values())
    print(values)

    # Possible to traverse keys
    for k in literal_name_sv:
        print(f"{k}: {literal_name_sv[k]}")


if __name__ == "__main__":
    use_a_map_program()
