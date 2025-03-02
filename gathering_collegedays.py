name = input("Enter your name :\n")
print("Welcome "+name+", To 'Indala College of 'Engineering'")
print("""Todays Events :
1. Sports
2. Dj night
Enter your choice : """)
choice = int(input())
if choice==1:
    print("Sports - Go to Ground - 10:00 am to 4:00 pm")
elif choice==2:
    print("Dj night - Go to College Campus - 7:00 pm to 9:00 pm")
else:
    print("Invalid Input")
print("""\nTo Register for Dj Night
1.Enter your name
2.Class""")
participants = []  

def register_participant():
    name = input("Enter Participant's Name: ")
    student_class = input("Enter Participant's Class: ")
    participants.append({"Name": name, "Class": student_class})
    print(f"\n✅ {name} has been successfully registered!\n")

def display_participants():
    if not participants:
        print("\n❌ No participants have registered yet!\n")
        return
    
    print("\n📋 List of Registered Participants:")
    for index, participant in enumerate(participants, start=1):
        print(f"{index}. {participant['Name']} - Class {participant['Class']}")
    
    print(f"\n📢 Total Participants: {len(participants)}\n")

while True:
    print("\n🎉 Welcome to Event Registration 🎉")
    print("1. Register a Participant")
    print("2. Display Registered Participants")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        register_participant()
    elif choice == "2":
        display_participants()
    elif choice == "3":
        print("\n🚀 Exiting the Registration System. Have a great event!\n")
        break
    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 3.\n")
