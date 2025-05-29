import re

def count_useful_lines(java_code):
    # Remove all multiline comments (/* ... */)
    java_code = re.sub(r'/\*.*?\*/', '', java_code, flags=re.DOTALL)
    
    # Remove all single line comments (// ...)
    lines = java_code.split('\n')
    #print(len(lines))
    #print(lines)
    cleaned_lines = []

    for line in lines:
        # Remove single-line comments
        line = re.sub(r'//.*', '', line)
        # Strip whitespace
        stripped = line.strip()
        # Add to cleaned_lines if it's not empty
        if stripped:
            cleaned_lines.append(stripped)

    return len(cleaned_lines)

# Example usage:
with open('problem3/tester.txt', 'r') as file:
    java_code = file.read()

useful_lines = count_useful_lines(java_code)
print("Useful lines of code:", useful_lines)