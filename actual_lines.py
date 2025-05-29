comments=['//','/*','*/']

with open('problem3/tester.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(lines)
actual_lines=0
lines_iter=iter(lines)
for line in lines_iter:
    line = line.strip()
    if line=='':
       continue
    if line.startswith('//'):
        continue
    if line.startswith('/*'):
        while not line.endswith('*/'):
            line = next(lines_iter, '').strip()
        continue
            
    actual_lines += 1
print(f'The number of actual lines in the file is: {actual_lines}')
    