
names = ['Clare', 'Seth', 'James', 'Kelly', 'Carrie', 'John', 'Jack']

# list comprehension
# new_list = [EXPR for VAR in ITERABLE if CONDITION]
names_upper = [n.upper() for n in names]
print("names_upper: {}\n".format(names_upper))

# dict comprehension
# new_dict = { KEY:VALUE for VAR in ITERABLE if CONDITION]
names_dict = {n.lower():len(n) for n in names}
print("names_dict: {}\n".format(names_dict))

# set comprehension
# new_set = {EXPR for VAR in ITERABLE if CONDITION}
names_set = {n[0] for n in names}
print("names_set: {}\n".format(names_set))



# generator