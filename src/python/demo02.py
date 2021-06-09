# %%
from typing import List, Dict

# %%
# valid function definition with type hint


def print_hung_tien_in_map(input: Dict[str, str]):
    print(input["Hung-Tien Huang"])


# %%
# variable declaration
input: Dict[str, str] = dict({
    "Hung-Tien Huang": "279-FR",
    "Chien-Ping Wu": "KKA-0580"
})
input_1 = list(["Hung-Tien Huang", "Chien-Ping Wu"])

# %%
# valid function call
print_hung_tien_in_map(input)

# %%
# generate type error
print_hung_tien_in_map(input_1)

# %%
# valid function definition


def print_bus_assignment_table(input: Dict[str, str]):
    print("Bus Assignment Table")
    print(str.format("Mr. Huang is driving bus {}.", input["Hung-Tien Huang"]))
    print(str.format("Mr. Wu is driving bus {}.", input["Chien-Ping Wu"]))


# %%
# generate type error
print_bus_assignment_table(input_1)
