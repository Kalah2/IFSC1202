def read_constitution(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def find_section(lines, search_term):
    section_start = None
    section_end = None
    for i, line in enumerate(lines):
        if search_term in line:
            if section_start is None:
                section_start = i
            section_end = i

    if section_start is not None and section_end is not None:
        while section_start > 0 and lines[section_start - 1]:
            section_start -= 1
        while section_end < len(lines) - 1 and lines[section_end + 1]:
            section_end += 1
        return section_start, section_end
    return None

def main():
    lines = read_constitution('08.Project constitution.txt')
    found_sections = set()

    while True:
        search_term = input("Enter a search term (or press Enter to exit): ").strip()
        if not search_term:
            break

        section_indices = find_section(lines, search_term)
        if section_indices and section_indices not in found_sections:
            start, end = section_indices
            print(f"\nSection containing '{search_term}' (Lines {start + 1} to {end + 1}):")
            for line in lines[start:end + 1]:
                print(line)
            found_sections.add(section_indices)

if __name__ == "__main__":
    main()