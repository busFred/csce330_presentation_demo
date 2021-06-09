# %%
# valid function definition without type hint
def print_hung_tien_in_map(input):
    print(input["Hung-Tien Huang"])


# %%
# valid function call
input = dict({"Hung-Tien Huang": "279-FR", "Chien-Ping, Wu": "KKA-0580"})
print_hung_tien_in_map(input)

# %%
# generate type error
input = list(["Hung-Tien Huang", "Chien-Ping, Wu"])
print_hung_tien_in_map(input)
