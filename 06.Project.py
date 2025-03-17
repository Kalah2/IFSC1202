with open("06.Project Input File.txt", "w") as f:
    f.write("Hello!\n")
    f.write("Welcome to 06.Project Input File.txt\n")
    f.write("**Insert Merge File Here**\n")
    f.write("This file is for testing purposes.\n")
    f.write("Good Luck!\n")

with open("06.Project Merge File.txt", "w") as f:
    f.write("This is line 1 of the merge file\n")
    f.write("This is line 2 of the merge file\n")

input_records = 0
merge_records = 0
output_records = 0

with open("06.Project output File.txt", "w") as output_file:
    with open("06.Project Input File.txt", "r") as input_file:
        for line in input_file:
            input_records += 1
            output_file.write(line)
            output_records += 1
            if "**Insert Merge File Here**" in line:
                with open("06.Project Merge File.txt", "r") as merge_file:
                    for merge_line in merge_file:
                        merge_records += 1
                        output_file.write(merge_line)
                        output_records += 1
                for line in input_file:
                    input_records += 1
                    output_file.write(line)
                    output_records += 1
                break

print(f"Number of records in the input file: {input_records}")
print(f"Number of records in the merge file: {merge_records}")
print(f"Number of records in the output file: {output_records}")





