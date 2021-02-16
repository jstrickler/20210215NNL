

def get_info(*term_numbers):
    for term_number in term_numbers:
        print("Processing term", term_number)

raw_input = input("Enter list of terms: ")
raw_terms = raw_input.split()
terms = [int(t) for t in raw_terms]

results = get_info(1)
print("-" * 60)

results = get_info(2, 5, 26)
print("-" * 60)