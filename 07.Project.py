def ParseDegreeString(ddmmss):
    degree_symbol = chr(176)
    minute_symbol = "'"
    second_symbol = '"'
    
    degrees = float(ddmmss.split(degree_symbol)[0])
    minutes = float(ddmmss.split(degree_symbol)[1].split(minute_symbol)[0])
    seconds = float(ddmmss.split(minute_symbol)[1].split(second_symbol)[0])
    
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    return degrees + (minutes / 60) + (seconds / 3600)

def convert_angles(input_file, output_file):
    with open("07.Project Angles Input.txt", "r") as infile, open("07.Project Angles Output.txt", "w") as outfile:
        for line in infile:
            line = line.strip()
            degrees, minutes, seconds = ParseDegreeString(line)
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
            outfile.write(f"{decimal_degrees}\n")

convert_angles("07.Project Angles Input.txt", "07.Project Angles Output.txt")