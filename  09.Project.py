import csv

def read_distances(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        distances = [row for row in reader]
    return distances

def print_distances(distances):
    for row in distances:
        print("\t".join(row))

def find_distance(distances, from_city, to_city):
    from_city_index = -1
    to_city_index = -1
    
    for i in range(1, len(distances)):
        if distances[i][0] == from_city:
            from_city_index = i
            break
            
    for j in range(1, len(distances[0])):
        if distances[0][j] == to_city:
            to_city_index = j
            break
            
    if from_city_index == -1:
        print("Invalid From City")
        return
    if to_city_index == -1:
        print("Invalid To City")
        return
    
    distance = distances[from_city_index][to_city_index]
    print(f"{from_city} to {to_city} - {distance} miles")

def main():
    distances = read_distances('09.ProjectDistances.csv')
    print_distances(distances)
    
    from_city = input("Enter From City: ")
    to_city = input("Enter To City: ")
    
    find_distance(distances, from_city, to_city)

if __name__ == "__main__":
    main()