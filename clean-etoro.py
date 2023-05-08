# Using readlines()
file1 = open('etoro-year.csv', 'r')
Lines = file1.readlines()

count = 0
lines = []
# Strips the newline character
for line in Lines:
    count += 1
    line = line.replace('"', '').replace(', Inc.', '').strip().rstrip(',')
    lines.append(line.strip()+"\n")

file1 = open('etoro-cleaned.csv', 'w')
file1.writelines(lines)
file1.close()
