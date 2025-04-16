def main():
    # Initialize lists for boys and girls names
    boys_names = []
    girls_names = []
    

    # Read and process the file
    try:
        with open('Exam Two Names.txt', 'r') as file:
            for line in file:
                # Split the line into boy and girl names
                names = line.strip().split(',')
                if len(names) == 2:
                    # Strip whitespace and add to respective lists
                    boy_name = names[0].strip().title()
                    girl_name = names[1].strip().title()
                    boys_names.append(boy_name)
                    girls_names.append(girl_name)
    except FileNotFoundError:
        print("Error reading file")
        return
    
    # Main program loop

    while True:
        # Get user input
        user_input = input("Enter a name to search (or 'Q' to quit): ").strip()
        
        # Check for quit condition
        if user_input.upper() == 'Q':
            print("Goodbye!")
            break
        
        # Format the name (title case)
        search_name = user_input.title()
        
        # Search boys names
        found = False
        for i in range(len(boys_names)):
            if boys_names[i] == search_name:
                print(f"Boy's Name - Rank: {i+1}")
                found = True
                break
        
        # If not found in boys, search girls
        if not found:
            for i in range(len(girls_names)):
                if girls_names[i] == search_name:
                    print(f"Girl's Name - Rank: {i+1}")
                    found = True
                    break
        
        # If still not found
        if not found:
            print("Name Not Found")

if __name__ == "__main__":
    main()