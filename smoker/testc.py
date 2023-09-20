
file_path = "bb90.txt" 
lines = []
with open(file_path, "r") as file:
    lines = file.readlines()
a=len(lines) -1
print(a)
if a> 0:
    
    first_line = lines.pop(0)
    print(first_line)
    with open(file_path, "w") as file:
        file.writelines(lines)
    print("File updated.")
else:
    print("File is empty.")
