import re

file_path = r"C:\Users\User\Desktop\Data\mockdata.txt"

with open(file_path, "r", encoding='utf-8') as f:
    text = f.read()

lines = text.strip().split('\n')

names = []
surnames = []
file_types = []

type_regex = re.compile(r'\.([a-zA-Z0-9]+)')

for line in lines:
    parts = line.split('\t')  
    if len(parts) >= 4:
        names.append(parts[0])
        surnames.append(parts[1])
        
        match = type_regex.search(parts[3])
        if match:
            file_types.append(match.group(1))

with open("name.txt", "w", encoding='utf-8') as f:
    f.write("\n".join(names))

with open("surname.txt", "w", encoding='utf-8') as f:
    f.write("\n".join(surnames))

with open("typeFile.txt", "w", encoding='utf-8') as f:
    f.write("\n".join(file_types))

print("Данные успешно записаны!")
