import time
import random
from flask import Flask, render_template, request
app = Flask(__name__)

# Start the Story

def start_adventure():
    friend = False ## Initializes friend status as false
    name = input("Enter your name: ") 
    location = input("Enter your location: ") 
    
    # Introduction
    
    print(f"Welcome to BYU-I {name}! Rexburg is a bit different from {location}.")
    print("It's your first semester at BYU-I, and you're excited to meet your roomates at Centre Square! After you get all settled in, you decide to see what Rexburg has to offer.")
    print("Monday comes around and it’s time to go to your first classes, mostly generals. You go to all of your classes, but the final one in the afternoon seems like it’s going to be a lot more work than you anticipated. It could offer some heavy benefits down the road, but it’s not required for your major. Do you STICK with it, or DROP the class?")
    choice = input("STICK or DROP?").lower()
    if choice == "stick":
        print()
    elif choice == "drop":
        print()
        
   # Week 1 Major choice 1 ----------------------------------------------------------
   
    print("Before you know it, the First Friday party for freshmen rolls around. Your roommates are one of many students excited and invite you to go out with them! Do you ACCEPT the invite or DECLINE?")
    choice = input("ACCEPT or DECLINE?").lower()
    if choice == "accept":
        print("You go with your roommates to first Friday and build some relationships with them. You feel closer to them than just a few days earlier when you moved in. They could turn out to be a great support system!")
        friend = True ## Establishes a persistent friend status that can be referenced in later code ex. "if friend: \\ print("***")" \\ else: \\ print("***")
    elif choice == "decline":
        print("You politely decline as you just want to get settled in more. As the night goes on you feel a little regret and wonder how much you’re missing out. It doesn’t help that your roommates came back raving about how fun it was.")
        friend = False ## maintains the friend status as false
    # Week 2
        
    print("Congratulations! You’ve got through your first week of school, but the food you came up with has almost ran out. You really could use some groceries. Wal-Mart is right in town, it’s very convenient, but is a little more expensive than you want it to be. However, you could drive to Idaho Falls and save money by buying in bulk at Costco, it’s just a 25-mile drive. Do you STAY in town, or DRIVE to Idaho Falls?")
    choice = input("STAY or DRIVE? ").lower()
    if choice == "stay":
        print("")
    elif choice == "drive":
        print("")
    
    # Week 3
        
    print("You’re officially settled in and want to explore around a little bit. A lot of people recommend going to the sand dunes, but you also heard that R Mountain is a fun, casual hike. Do you go to the DUNES, or try to hike the MOUNTAIN?")
    choice = input("DUNES or MOUNTAIN? ").lower()
    if choice == "dunes":
        print("")
    elif choice == "mountain":
        print("")
    
    # Week 4
        
    print(f"""After a relatively successful week of school, you’re back to it the next week. However, there was some 
    homework that you had some trouble with over the weekend. The department is having an open lab and homework 
    help on Wednesday night, but you have a date scheduled that night. Do you go OUT on the date, or RESCHEDULE 
    it so you can get help with your homework?""")
    choice = input("OUT or RESCHEDULE? ").lower()
    if choice == "out":
        print("")
    elif choice == "reschedule":
        print("")
    
    # Week 5
        
    print(f"""It’s that point in the semester where you find yourself in a little bit of a slump. The motivation just isn’t 
    as prevalent as it was. Regardless you know you have to stay on top on things. You’re reading a book for one of 
    your classes and highly engaged in homework when a friend texts you about a new show that debuts tonight and 
    asks for you to come over and watch it. Do you go over and WATCH the new show, or STAY at home and continue your studies?""")
    choice = input("WATCH or STAY? ").lower()
    if choice == "watch":
        print("") 
    elif choice == "stay":
        print("")

    # Week 6
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")
        
    # Week 7 Major Choice 2,3 ----------------------------------------------------------

    # this choice will ONLY appear if you WENT to first friday 
    if friend: 
        print(f"""As midterms near, group projects are ramping up and your team has decided to hold a meeting 
        Friday night this week. However, since you got close to your friends at first friday your first week, they invite
        you to a watch party for a new show that debuts for the same night. Do you meetup for your PROJECT or go to the WATCH party?""")
        w7choice = input("PROJECT or WATCH? ").strip().lower()
        if w7choice == "project":
            print(f"""You decide to go work on your project with your team. Your roommate is a little bummed out and was persistent
            but eventually accepted your decision to be diligent and responsible. You and your team meet on Fridday and get a lot 
            of work done. You feel really good about your decision and are confident you and your team will get a good grade""")
        elif w7choice == "watch":
            print(f"""You've been looking for an excuse to get out of meeting with your team anyways. You tell your group that you
            wont be able to make it. You feel a slight internal guilt, but your excitment overpowers the guilt.""") 
    # this choice will appear if you DID NOT go to first friday 
    else: 
        print(f"""Since you're not super close with your roommates, you decide to spend some free time binge-watching a new TV show.
              One of your roommates asks if you want to go to the library to study, but you're really comfortable watching your TV show 
              right now. Do you WATCH your show or STUDY with your roommate at the library?""")
        w7_2choice = input("WATCH or STUDY").strip().lower()
        if w7_2choice == "watch":
            print(f"""You thank your roommate but tell him that you're taking a mental break and that you're just going to chill for now.""")
        elif w7_2choice == "study":
            print (f"""[placeholder]""")
    # Week 8
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
          
    # Week 9
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")
        
    # Week 10
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 11
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 12
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")  
          
    # Week 13
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 14-16 Major Choice 4 --------------------------------------------------
    
        print(f"""Congrats, you passed your exams! Thanks to all your academic dedication, you feel on top of the world as you head home for winter break– 
              you can’t wait to share the good news with your family.
              You make it home and when everyone asks you about how college has been, 
              you were proud to say it was better than you expected! Going into the new year and semester, 
              you want to set some goals to stay on track. Are your goals to STUDY harder or expand your SOCIAL circle?""")
    choice = input("STUDY or SOCIAL").lower()
    if choice == "":
        print("study")
    elif choice == "":
        print("social")

    # Week 14-16 Major Choice 5 -------------------------------------------------
    
        print(f"""Yikes, you failed your exams! As you reflect back on this semester, you must’ve slacked off more than you realized. As you’re driving home for winter break, all you can think about is what you’re going to tell your family. 
              You make it home and everyone has asked you about your experience at college.It came out that you didn’t do so well; and christmas dinner was a nightmare with all the relatives pestering you, especially Uncle Brad. 
              As the new year rolls around, you’ve been weighing out your options. You don’t know how well another semester would treat you. You could DROP out, take a BREAK, go BACK from embarrassment, or PROVE everyone wrong next semester.""")
    choice = input("DROP, BREAK, PROVE, or BACK").lower()
    if choice == "drop": #dropping out
        print("")
    elif choice == "break": #leads to death
        print("")
    elif choice == "prove":
        print("") 
    elif choice == "back":
        print("") 
    
    # Week 17  
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 18
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 19
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")
            
    # Week 20
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")
            
    # Week 21
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 22
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 23 Major Choice 6, 7, 8, 9 ----------------------------------------------------------
    
     # choice 6 dialogue -------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 

    # choice 7 dialogue  -------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
    elif choice == "":
        print("") 

    # choice 8 dialogue -------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
    elif choice == "":
        print("") 

    # choice 9 dialogue ------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
    elif choice == "":
        print("") 

    # Week 24
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 25
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")
            
    # Week 26
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 27
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 28
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 
           
    # Week 29
    
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")
        
    # Week 30 Major Choice 10, 11, 12, 13, 14 ----------------------------------------------------------
    
     # choice 10 dialogue -------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("")
    
     # choice 11 dialogue -------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 

    # choice 12 dialogue  -------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 

    # choice 13 dialogue -------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 

    # choice 14 dialogue ------------------------
        print("")
    choice = input("").lower()
    if choice == "":
        print("")
    elif choice == "":
        print("") 

        
start_adventure()