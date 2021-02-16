
def pres_names():
    with open('DATA/presidents.txt') as pres_in:
        for line in pres_in:
#            _, last_name, first_name, *_ = line.split(':')
            fields = line.split(':')
            # print(first_name, last_name)
            # yield f"{first_name} {last_name}"
            yield f"{fields[2]} {fields[1]}"
            # yield "{} {}".format(first_name, last_name)
            # yield first_name + " " + last_name
