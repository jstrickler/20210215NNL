
# mary_in = open(...)
with open('DATA/mary.txt') as mary_in:
    with open('donna.txt', 'w') as donna_out:
        for old_line in mary_in:
            new_line = old_line.replace('Mary', 'Donna')
            donna_out.write(new_line)
print("-" * 60)
