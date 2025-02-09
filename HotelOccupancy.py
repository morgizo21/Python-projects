## Morgan Ntare
## 10/18/2024
## Intro to programming 1
## HMWK 05 - Hotel Occupancy Rate


# Initialize variables for total rooms and total occupied rooms
total_rooms = 8 * 30  # 8 floors, each floor has 30 rooms
total_occupied = 0

# Loop through each floor
for floor in range(1, 9):  # This loops from floor 1 to 8
    while True:
        # Ask the user for the number of occupied rooms
        rooms_occupied = input(f"Enter the number of rooms occupied on floor {floor} (max 30): ")
        
        # Validate the input
        if rooms_occupied.isnumeric() and 0 <= int(rooms_occupied) <= 30:
            rooms_occupied = int(rooms_occupied)  # Convert the valid input to an integer
            break  # Exit the loop if valid input
        else:
            print("Invalid input. Please enter a number between 0 and 30.")
    
    # Calculate and display the occupancy rate for this floor
    occupancy_rate = (rooms_occupied / 30) * 100
    print(f"Floor {floor}: {rooms_occupied} rooms occupied, Occupancy Rate: {occupancy_rate:.2f}%")

    # Add the valid number of occupied rooms to the total
    total_occupied += rooms_occupied

# After the loop, calculate and display the total occupancy rate
total_occupancy_rate = (total_occupied / total_rooms) * 100
print(f"\nTotal rooms occupied: {total_occupied}")
print(f"Overall Occupancy Rate: {total_occupancy_rate:.2f}%")
