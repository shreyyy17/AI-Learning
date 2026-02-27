read_lines = open('csv_data', 'r')
lines = read_lines.readlines()
read_lines.close()



lines = [line.strip() for line in lines[1:]]
print(lines)

for line in lines:
    person_data = line.split(',')
    name =person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]

    print(f"{name.title()} is {age} years old and studiying {degree.capitalize()} in {university.title()}")

sample_csv_value = ','.join(lines[1:])
print(sample_csv_value)