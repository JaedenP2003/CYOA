import time
import random

# Start the Story

#comment

#we are dope


def start_adventure():
    name = input("Enter your name: ")
    location = input("Enter your location: ")
    print(f"Welcome to BYU-I {name}! Rexburg is a bit different from {location}.")
    print("It's your first semester at BYU-I, and you're excited to meet your roomates at Centre Square! After you get all settled in, you decide to see what Rexburg has to offer.")
    print("You discover an activity for freshmen called 'First Friday', and it looks pretty fun. Maybe you'll go if you have the time. When you get back to your apartment, your roomates invite you to go with them to First Friday. Do you ACCEPT the invite or DECLINE?")
    choice = input("ACCEPT or DECLINE?").lower()
    if choice == "accept":
        print("You go with your roomates to First Friday and build some relationships with them. You get to know them a little better!")
    elif choice == "decline":
        print("You politely decline as you just want to get settled in more, but, as the night goes on, you feel a little regretful that you didn't go.")
        
    print("Monday comes around and it’s time to go to your first classes, mostly generals. You go to all of your classes, but the final one in the afternoon seems like it’s going to be a lot more work than you anticipated. It could offer some heavy benefits down the road, but it’s not required for your major. Do you STICK with it, or DROP the class?")
    choice = input("STICK or DROP?").lower()
    if choice == "stick":
        print("")
    elif choice == "drop":
        print("")
        
    print("Congratulations! You’ve got through your first week of school, but the food you came up with has almost ran out. You really could use some groceries. Wal-Mart is right in town, it’s very convenient, but is a little more expensive than you want it to be. However, you could drive to Idaho Falls and save money by buying in bulk at Costco, it’s just a 25-mile drive. Do you STAY in town, or DRIVE to Idaho Falls?")
    choice = input("STAY or DRIVE?").lower()
    if choice == "stay":
        print("")
    elif choice == "drive":
        print("")
        
    print("You’re officially settled in and want to explore around a little bit. A lot of people recommend going to the sand dunes, but you also heard that R Mountain is a fun, casual hike. Do you go to the DUNES, or try to hike the MOUNTAIN?")
    choice = input("DUNES or MOUNTAIN?").lower()
    if choice == "dunes":
        print("")
    elif choice == "mountain":
        print("")
        
    print("After a relatively successful week of school, you’re back to it the next week. However, there was some homework that you had some trouble with over the weekend. The department is having an open lab and homework help on Wednesday night, but you have a date scheduled that night. Do you go OUT on the date, or RESCHEDULE it so you can get help with your homework?")
    choice = input("OUT or RESCHEDULE?").lower()
    if choice == "out":
        print("")
    elif choice == "reschedule":
        print("")
        
    print("It’s that point in the semester where you find yourself in a little bit of a slump. The motivation just isn’t as prevalent as it was. Regardless you know you have to stay on top on things. You’re reading a book for one of your classes and highly engaged in homework when a friend texts you about a new show that debuts tonight and asks for you to come over and watch it. Do you go over and WATCH the new show, or STAY at home and continue your studies?")
    choice = input("WATCH or STAY?").lower()
    if choice == "watch":
        print("")
    elif choice == "stay":
        print("")



# Start the adventure
start_adventure()


def continue_adventure():
    print("Welcome to your adventure!")
    print("You find yourself at a fork in the road. What will you do?")
    print("1. Go left to the mysterious forest.")
    print("2. Go right to the bustling town.")
    print("3. Head straight towards the towering mountains.")
    print("4. Explore the dark cave nearby.")
    print("5. Stay where you are and set up camp.")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        forest_path()
    elif choice == "2":
        town_path()
    elif choice == "3":
        mountain_path()
    elif choice == "4":
        cave_path()
    elif choice == "5":
        camp_path()
    else:
        print("Invalid choice. Please try again.")
        continue_adventure()

def forest_path():
    print("You venture into the forest and hear the rustling of leaves...")
    # Add more story development here.

def town_path():
    print("You walk into the lively town and meet an old merchant...")
    # Add more story development here.

def mountain_path():
    print("You begin climbing the mountains, feeling the cold wind against your face...")
    # Add more story development here.

def cave_path():
    print("You enter the dark cave and feel a chill run down your spine...")
    # Add more story development here.

def camp_path():
    print("You set up camp and gaze at the stars above. It's peaceful here...")
    # Add more story development here.

# Start the adventure
start_adventure()
