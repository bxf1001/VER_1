import json
import datetime
import Whatsappcall
try:
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty dictionary
    user_data = {}

def store_data():
    user_id = input("Enter User ID: ")
    if user_id in user_data:
        print("User already exists.")
    else:
        value1 = input("Enter No1: ")
        value2 = input("Enter No2: ")
        value3 = input("Enter No3: ")
        user_data[user_id] = {'1': value1, '2': value2, '3': value3}
        # Write the updated data to the file
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f)

def retrieve_data():
    user_id = input("Enter User ID: ")
    if user_id in user_data:
        print("choose (1, 2, or 3):", user_data[user_id])
        field = input("Enter field to print (or 'all' to print all fields): ")
        if field.lower() == 'all':
            print(user_data[user_id])
        elif field in user_data[user_id]:
            add_time=int(input("enter time:: "))
            Whatsappcall.phone_number(user_data[user_id][field])
            Whatsappcall.timer(add_time)
            add_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"{user_data[user_id][field]} (Called at {add_time})")

            # Create a new dictionary to store timestamped data
            timestamped_data = {
                "user_id": user_id,
                "field": field,
                "number": user_data[user_id][field],
                "timestamp": add_time
            }

            # Write the timestamped data to a new file
            with open('timestamped_data.json', 'a') as f:
                json.dump(timestamped_data, f)
                f.write('\n')  # Add a newline for readability
        else:
            print("Invalid field.")
    else:
        print("User not found.")
def print_timestamped_data(user_id):
    try:
        with open('timestamped_data.json', 'r') as f:
            data_found = False  # Flag to track if data exists for the user ID
            for line in f:
                entry = json.loads(line)  # Parse each line as a separate JSON object
                if entry['user_id'] == user_id:
                    print("-------------------------------------             ")
                    print(f"User ID: {entry['user_id']}")
                    print(f"Field: {entry['field']}")
                    print(f"Value: {entry['number']}")  # Corrected key name
                    print(f"Timestamp: {entry['timestamp']}\n")
                    print("-------------------------------------             ")
                    data_found = True  # Data exists for the specified user ID
            if not data_found:
                print("No data found for the specified user ID.")
    except FileNotFoundError:
        print("No timestamped data file found.")
# Example usage:

while True:
    print("         -------------------------------------             ")
    print("             WELCOME TO PUZHAL PHONE PORTAL              ")
    print("           ----------------------------------             ")
    print("\n1. Store Data\n2. Make Call\n3. Search Data\n4. Quit")
    option = input("Enter your option: ")
    if option == '1':
        store_data()
    elif option == '2':
        retrieve_data()
    elif option == '3':
        user_id_input = input("Enter User ID to retrieve data: ")
        print_timestamped_data(user_id_input)
    elif option == '4':
        break
    else:
        print("Invalid option. Please try again.")
