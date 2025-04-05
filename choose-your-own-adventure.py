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
    
    print(f"Welcome to BYU-I {name}! BYU-I is a bit different from {location}.")
    print("""It's your first semester at BYU-I, and you're excited to meet your roomates at Centre Square! After you get all settled in, 
          you decide to see what Rexburg has to offer.""")
    print("""Monday comes around and it’s time to go to your first classes, mostly generals. You go to all of your classes, but the final
        one in the afternoon seems like it’s going to be a lot more work than you anticipated. It could offer some heavy benefits down the 
        road, but it’s not required for your major. Do you STICK with it, or DROP the class?""")
    choice = input("STICK or DROP?").lower()
    if choice == "stick":
        print()
    elif choice == "drop":
        print()
        
   # Week 1 Major choice 1 ----------------------------------------------------------
   
    print("""Before you know it, the First Friday party for freshmen rolls around. Your roommates are one of many students excited and invite 
            you to go out with them! Do you ACCEPT the invite or DECLINE?""")
    choice = input("ACCEPT or DECLINE?").lower()
    if choice == "accept": ## Leads toward MC 2
        print("""You go with your roommates to first Friday and build some relationships with them. You feel closer to them than just a few days
               earlier when you moved in. They could turn out to be a great support system!""")
        friend = True ## Establishes a persistent friend status that can be referenced in later code ex. "if friend: \\ print("***")" \\ else: \\ print("***")
    elif choice == "decline": ## Leads toward MC 3
        print("""You politely decline as you just want to get settled in more. As the night goes on you feel a little regret and wonder how much
               you’re missing out. It doesn’t help that your roommates came back raving about how fun it was.""")
        friend = False ## maintains the friend status as false
    # Week 2
        
    print("""Congratulations! You’ve got through your first week of school, but the food you came up with has almost ran out. 
          You really could use some groceries. Wal-Mart is right in town, it’s very convenient, but is a little more expensive than you want it to be. 
          However, you could drive to Idaho Falls and save money by buying in bulk at Costco, 
          it’s just a 25-mile drive. Do you STAY in town, or DRIVE to Idaho Falls?""")
    choice = input("STAY or DRIVE? ").lower()
    if choice == "stay":
        print("")
    elif choice == "drive":
        print("")
    
    # Week 3
        
    print("""You’re officially settled in and want to explore around a little bit. A lot of people recommend going to the sand dunes, but you also
        heard that R Mountain is a fun, casual hike. Do you go to the DUNES, or try to hike the MOUNTAIN?""")
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
    
    print(f"""The weather is very bleak this week, the snow is rolling in! It’s going to be very cold, 
              snowy and windy, but you have a peer awaiting your help in a class. She’s really struggling 
              with the concepts of the class, but you notice some ice outside your apartment window and 
              think it might be a little risky. Do you HEAD to class, or try to AVOID the ice and stay home?""")
    choice = input("HEAD or AVOID?").lower()
    if choice == "head":
        print("")
    elif choice == "avoid":
        print("")
        
    # Week 7 Major Choice 2,3 ----------------------------------------------------------
    # choice 2 dialogue
    # this choice will ONLY appear if you WENT to first friday 
    if friend: 
        print(f"""As midterms near, group projects are ramping up and your team has decided to hold a meeting 
        Friday night this week. However, since you got close to your friends at first friday, they invite
        you to a watch party for a new show that debuts for the same night. Do you meetup for your PROJECT or go to the WATCH party?""")
        w7choice = input("PROJECT or WATCH? ").strip().lower()
    if w7choice == "project": ## Leads to MC 4
        print(f"""You want to stay on top of your academics this semester and work hard on your project! 
              You feel productive because of all your hard work.""")
    elif w7choice == "watch": ## Leads to MC 5
        print(f"""How could you miss the watch party? You want to make sure 
              you’re staying social, you’re in college after all!""") 
    
    # choice 3 dialogue
    # this choice will appear if you DID NOT go to first friday 
    else: 
        print(f"""Since you're not super close with your roommates, you decide to spend some free time binge-watching a new TV show.
              One of your roommates asks if you want to go to the library to study, but you're really comfortable watching your TV show 
              right now. Do you WATCH your show or STUDY with your roommate at the library?""")
        w7_2choice = input("WATCH or STUDY").strip().lower()
        if w7_2choice == "watch": ## Leads to MC 5
            print(f"""You are deep into your show and politely decline the offer from your roommate. 
                  You have all semester, right? You tell them maybe next time.""")
        elif w7_2choice == "study": ## Leads to MC 4
            print (f"""Your show can wait, you’ve decided to study and put more time into your academics. 
                   You want to stay on top of your homework! You feel productive because of all your hard work.""")
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
    choice = input("STUDY or SOCIAL?").lower()
    if choice == "study": ## Leads to MC 6
        print(f"""The high you felt after succeeding this semester was addicting, you wanted more. 
              Your new year's goal is to study hard in the upcoming semester.""")
    elif choice == "social": ## Leads to MC 7
        print(f"""The academic success you had was exciting but you want to try something new in the upcoming semester. 
              You want to push yourself out of your comfort zone and expand your social circle!""")

    # Week 14-16 Major Choice 5 -------------------------------------------------
    
        print(f"""Yikes, you failed your exams! As you reflect back on this semester, you must’ve slacked off more than you realized. 
              As you’re driving home for winter break, all you can think about is what you’re going to tell your family. 
              You make it home and everyone has asked you about your experience at college.It came out that you didn’t do so well, 
              and christmas dinner was a nightmare with all the relatives pestering you, especially Uncle Brad. 
              As the new year rolls around, you’ve been weighing out your options. You don’t know how well another semester would treat you. 
              You could DROP out, take a BREAK, go BACK from embarrassment, or PROVE everyone wrong next semester.""")
    choice = input("DROP, BREAK, PROVE, or BACK?").lower()
    if choice == "drop": ##dropping out (MC 18)
        print("It’s all too much, the pressure has built up and gotten to you. You feel like you just weren’t cut out for college.")
    elif choice == "break": ##leads to death (MC19)
        print(f"""You decide to take a break thinking it will help clear your mind. While working at home, you decide to meet up with some old friends. 
              They invite you out to go snowmobiling! You’re having the time of your life while you’re riding but make the mistake of looking back at your friends behind you. 
              They shout at you and you notice a giant tree come into view as you face forward. You attempt to swerve out of the way, but it’s too late.""")
    elif choice == "prove": ##Leads to MC 8
        print(f"""You may have done poorly last semester but you won’t make the same mistake again. 
              You make the promise that you’ll clear your name and come home next semester proud instead of ashamed. 
              You’re going to prove Uncle Brad wrong.""") 
    elif choice == "back": ##Leads to MC 9
        print(f"""Last semester was awful but you’ll never live it down if you quit now. 
              You’ve got to go back. You’re not excited but it’s better than the humiliation of another choice.""") 
    
    # Week 17  
   
        print("""You had a restful and calm break! Now you're back in school and ready for the winter semester.
        You find out your new roommates are chill like that, kawabunga baby.
        they wanna hangout and go sledding but you need to get groceries. Do you choose to go HANGOUT with them or
        do you go out and get GROCERIES?""")
    choice = input("HANGOUT or GROCERY?").lower()
    if choice == "hangout":
        print("""You grab your coat and follow your roommates out the door, their excitement contagious.
        The snow crunches beneath your boots as you trek to the perfect sledding spot.
        Laughter fills the air as you take turns speeding down the hill, wiping out gloriously, and cheering each other on.
        The day is capped off with steaming cups of cocoa and stories of epic sledding fails. It's a moment of pure winter joy!""")
    elif choice == "grocery":
        print("""You grab your list and head to the store. The biting winter air greets you as you step outside,
        but the thought of a well-stocked fridge keeps you focused.
        After navigating the aisles and enduring the checkout line, you return home feeling accomplished, if not slightly exhausted.
        At least now you have the ingredients for a good meal.""")
           
    # Week 18
   
        print("""The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""")
    choice = input("STUDY or GAME NIGHT?").lower()
    if choice == "study":
        print("""You choose to dedicate the week to studying and tackling your upcoming project head-on. Armed with a cup of steaming tea and your laptop,
        you set up camp in the quiet corner of the library, ready to focus.
        The hours pass as you dive deep into research, organize your notes, and sketch out your ideas.
        By the end of the week, your project is taking shape, and you feel a sense of accomplishment.
        It’s not flashy or exciting, but the payoff in peace of mind and preparation is undeniable.""")
    elif choice == "game night":
        print("""Laughter and friendly competition fill the room as you dive into the games. The stress of the week melts away,
        replaced by warm camaraderie and the thrill of shouting out (sometimes wrong) answers.
        For a moment, life feels perfectly simple, and you go to bed that night with a light heart and some newfound friendships.""")
           
    # Week 19
   
        print("""It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""")
    choice = input("HIKE or OFFICE?").lower()
    if choice == "hike":
        print("""You decide that a winter hike is exactly what you need this week, a chance
        to clear your head and take in the frosty beauty of February. Bundled up in your coziest gear, you join the group at the trailhead,
        where the snowy landscape stretches endlessly in every direction. The crunch of snow beneath your boots, the fresh scent of pine trees,
        and the occasional burst of laughter from your fellow hikers create a rhythm that feels both peaceful and energizing.
        The sky erupts in vibrant shades of pink, orange, and gold, reflecting off the untouched snow. You pause to take it all in—the breathtaking view
        and the feeling of accomplishment that comes from pushing yourself to try something new!""")
    elif choice == "office":
        print("""You decide to make the most of the professors’ open office hours this week,
        it’s time to get ahead in your studies and tackle the challenges head-on.
        You pull up your notes and dive into the material with your professor’s guidance. Concepts that seemed hazy before start to click as the discussion unfolds.
        You take meticulous notes, feeling your confidence grow with every question answered.
        By the end of the session, you walk out of the office feeling relieved and prepared. Sure, it took discipline to prioritize studying,
        but the payoff is undeniable—you’re ready to tackle midterms with a clear understanding and a solid plan.""")
           
    # Week 20
   
        print("""It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""")
    choice = input("MIC or SHIFT?").lower()
    if choice == "mic":
        print("""You decide to attend the open mic night—you’ve been craving an escape
        from the routine and the chance to immerse yourself in creativity.
        he cozy venue hums with energy as students share heartfelt poems, witty anecdotes, and captivating stories.
        You listen intently, occasionally laughing, applauding, or nodding in appreciation.
        The atmosphere feels like a safe haven where creativity thrives, and the stress of midterms melts away.
        Someone nudges you and whispers, "Are you gonna go up and share something?"
        You hesitate but decide to keep your seat—tonight, you’re happy being a supportive listener.
        As the event wraps up, you leave with a refreshed mind and a notebook full of inspiration, ready to take on the week ahead.""")
    elif choice == "shift":
        print("""You decide to take the extra shift at work—making some extra cash
        now will bring you closer to that dream ski trip later.
        The cafe is bustling with activity, customers coming and going as the dinner rush kicks into high gear.
        You move through your tasks efficiently, balancing orders, handling the register,
        and flashing polite smiles despite the steady stream of patrons.
        It's tiring, but the thought of your goal keeps you motivated.
        At the end of the night, as you’re wiping down the counters,
        your manager gives you a quick nod. "Great work tonight. We couldn’t have done it without you!".""")
           
    # Week 21
   
        print("""Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""")
    choice = input("DINNER or LOUNGE?").lower()
    if choice == "dinner":
        print("""You decide to join the group at the diner, figuring it’s a chance to unwind and
        connect with classmates outside of the usual lecture halls.You order your favorite burger and
        quickly find yourself immersed in conversation—not just about the essay, but about everything from weekend plans to your favorite shows.
        Someone cracks a joke about how none of you actually understand the course reading, and suddenly everyone’s in stitches.
        The sense of camaraderie feels refreshing after weeks of sticking to your own bubble!""")
    elif choice == "lounge":
        print("""You decide to head to the dorm lounge for the Mario Kart tournament, armed with a bag of chips as your entry fee.
        You’re handed a controller and find yourself immersed in the action! The competition is intense but friendly,
        with everyone rooting for each other despite the occasional “Blue Shell disaster” that sparks roars of laughter.
        Even if you’re not the best player, the energy in the room is contagious, and you feel yourself letting go of the week’s stress.""")
           
    # Week 22
   
        print("""life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""")
    choice = input("PANCAKE or LOUNGE?").lower()
    if choice == "pancake":
        print("""You decide to head down to the common room for the surprise pancake night,
        drawn in by the promise of syrupy goodness and the chance to take a break from studying.
        The warm scent of pancakes wafts through the air as you walk in,
        and you’re greeted by a crowd of dormmates laughing, chatting, and flipping pancakes on a hot griddle.
        The energy in the room is contagious, and you immediately feel glad you came!""")
    elif choice == "volunteer":
        print("""You decide to head over to the campus volunteer fair, curious about the possibilities and
        excited to explore opportunities that could add meaning to your college experience!
        As you step into the event hall, the lively atmosphere draws you in—tables are set up with colorful banners,
        flyers, and enthusiastic representatives eager to talk about their organizations. You have a great time and
        find that this was an awesome way to get connected with more people just like you!
        By the time you leave, you’ve collected a handful of brochures and signed up for an email list or two.
        You might not know exactly which project you'll commit to, but the event sparks a sense of purpose you hadn’t expected!""")
           
    # Week 23 Major Choice 6, 7, 8, 9 ----------------------------------------------------------
    
     # choice 6 dialogue -------------------------
        print(f"""Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend. 
              The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night. 
              You’ve been out with this person a handful of times and you’re starting to really like them. Do you go out on the DATE, 
              or reschedule it so you can get help with your HOMEWORK?""")
    choice = input("HOMEWORK or DATE?").lower()
    if choice == "homework": ##Leads to MC 10
        print(f"""You want to keep up the good work and continue the grind! 
              Although you wanted to go out, the help you got at the open lab was extremely helpful. 
              You came out feeling much better about the course than you did earlier.""")
    elif choice == "date": ##Leads to MC 11
        print(f"""How could you say no to a date? Things are going so well, you don’t want to jeopardize your relationship over some homework! 
              The date goes great and you don’t even think twice about the missed lab.""") 

    # choice 7 dialogue  -------------------------
        print("""You’ve gone out with this one person over the past month, you might really be starting to like them. 
        Valentine's day is almost here and you’re weighing out your options. You could ask them to be your VALENTINE, 
        go further and ask them to be OFFICIAL, or NOT worry about it.""")
    choice = input("VALENTINE, OFFICIAL, or NOT?").lower()
    if choice == "valentine": ##Leads to MC 10
        print(f"""You aren’t quite ready for the full commitment of a new relationship but you do really like this person. 
              So you pull out some of the stops- flowers and chocolate. You have a valentine!""")
    elif choice == "official": ##Leads to MC 11
        print(f"""This person makes you happy! You decide it’s time to make things official with them. 
              You pull out all the stops- flowers, chocolates and a handwritten note. 
              When you prompted the question, it was obvious the feelings were mutual. Congrats!! You feel like the luckiest person in the world.""") 
    elif choice == "not": ##Leads to MC 12
        print(f"""You don’t feel worried about asking them to be your valentine because it didn’t feel that serious to you. 
              It was just a little holiday so did it really matter?""") 

    # choice 8 dialogue -------------------------
        print(""""Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend.
        The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night.
        You’ve been out with this person a handful of times and you’re starting to really like them, but you’re also stressed out with your homework. 
        Do you go on the DATE, reschedule it so you can get help with your HOMEWORK or take some time to relax and watch that new SHOW you started?""")
    choice = input("DATE, HOMEWORK, or RELAX?").lower()
    if choice == "date": ##Leads to MC 12
        print(f"""How could you say no to a date? Things are going so well, you don’t want to jeopardize your relationship over some homework! 
              You remembered the promise you made to yourself, but you also want things to look forward to. 
              The date goes great and you don’t even think twice about the missed lab.""")
    elif choice == "homework": ##Leads to MC 11
        print(f"""You felt the need to keep the promise you made with yourself. 
              You felt a desire– petty or not– to prove everyone wrong and that you could do this. 
              Although you wanted to go out, the help you got at the open lab was extremely helpful. 
              You came out feeling much better about the course than you did earlier.""") 
    elif choice == "show": ##Leads to MC 13
        print(f"""It was hard finding time for yourself so you decided to take a breather. 
              You feel it would benefit you most to hit pause. The homework and date could wait, right? Well unfortunately, the date couldn’t. 
              They felt like a last priority and called things off. Yikes, that didn’t go how you pictured.""") 

    # choice 9 dialogue ------------------------
        print("""You’re back at another week of school and things aren’t doing great. 
        The weekend is coming up and you want to have some fun. You’re weighing out your options.
         You could ask someone out on a DATE, watch some TV to decompress or attempt to baptize your CAR.""")
    choice = input("DATE, TV or CAR?").lower()
    if choice == "date": ##Leads to MC 12
        print(f"""A date sounds like the best option! You’ve been seeing this one person for some time now and you want to continue to pursue a relationship with them. 
              Although you weren’t excited to come back to school, things might actually start to be looking up, in at least one aspect.""")
    elif choice == "tv": ##Leads to MC 13
        print(f"""You wanted to have fun and relax, not push your limits emotionally or physically. You switch on your comfort show: The Bachelor. 
              Your mind rests as the girls fight over the guy- you laugh at seemingly annoying comments and shout at the one girl that loves to cause drama.""") 
    elif choice == "car": ##Leads to MC 14
        print(f"""You decide you want to try and baptize your car, how hard could it be? You hop in your car and drive onto the freeway. 
              You grab your steering wheel tightly and drive a few miles before building up the courage to press the gas pedal to the floor.""") 

# Week 24
  
       print("""Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""")
   choice = input("GO or SUGGEST").lower()
   if choice == "go":
       print("""You go to Buffalo and get your favorite meal. You feast and then your roommate suggests getting ice cream. They just happened to
       choose the most expensive place around. You can't not get ice cream. The B Dubs was already a hit to the finances, but flavor of the month just happens
       to be your favorite AND 10 percent off. You'll just have to save extra hard next week.""")
   elif choice == "SUGGEST":
       print("""You suggest going on Tuesday, but your roommates say the game they want is on tonight. They call you a bum and go without you, its okay you
             needed to save money anyways.""")
         
   # Week 25
  
       print("Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?")
   choice = input("CAMPING or STAY?").lower()
   if choice == "camping":
       print("You go camping with your buddies and it’s more fun than you thought! You saw a moose, wolf and plenty of bison. Plus the sun made a guest appearance and you were able to get some good ol’ vitamin D. ")
   elif choice == "stay":
       print("You stay home and feel a bit sad about not going. But you are able to get all your assignments done and you get a head start and some of next week’s material. You’re feeling good.")
          
   # Week 26
  
       print("You’re roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?")
   choice = input("CLEAN or SNAP?").lower()
   if choice == "clean":
       print("You decide to clean their dishes for the millionth time. Just as you're halfway through, the culprit walks through the door. They apologize once again but this time they seem more sincere. They offer to take you out to dinner anywhere you’d like. Your acts of service paid off")
   elif choice == "snap":
       print("You let out a huff and start taking the wet dishes to their bed. Just as you’ve picked up the last load they walk through the door. You let them have it explaining why their bed now has week old dishes on it. They are surprisingly understanding, considering they now have to wash their sheets. They apologize for the dishes but are still a bit angry about their bed.")
         
   # Week 27
  
       print(""""You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""")
   choice = input("RUSH or SLEEP").lower()
   if choice == "rush":
       print("""You count down from 5 and pop out of bed. You rush and make it out the door in 5 minutes. You haven't been late to
             this class all semester so you have no idea how the professor will react. You walk in 24 minutes late and your professor
             greets you with a smile and says "Glad you could make it!" Relieved at his response, you sit down and prepare for another day
             of classes.""")
   elif choice == "sleep":
       print("""You try to fight your fatigue but it takes you out with a gust of wind from the window, reminding you how warm your bed is.
             You wake up again and not only have you missed your first class, but you've missed another and the meeting you had with your group.
             Now you scramble to come up with your best excuse, at least one better than "I gave 5 hours of my life to Netflix last night." """)
         
   # Week 28
  
       print("These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?")
   choice = input("SKIP or GO?").lower()
   if choice == "skip":
       print("You skip devo and work on homework in the crossroads. You’re so distracted by your hunger you can’t get anything done. You decide to get some chick fil a, but then remember it's closed for devo. Just as your stomach grumbles your roommate texts, “They had donuts at devo! I got like 5 you should’ve come.” Guess you really did miss out on a feast.")
   elif choice == "GO":
       print("You get to devo feeling stressed about your classes. Just to find the speaker is talking about not letting trials get you down. The devotional ends and you’re feeling more uplifting than ever, plus they had free donuts!")
         
   # Week 29
  
       print("""It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """)
   choice = input("PARTY or NETFLIX?").lower()
   if choice == "party":
       print("You go to the party and it's okay at best. You look around and it's just a bunch of sweaty guys trying to pick up girls. You try to enjoy yourself when someone says the cops are coming for a noise complaint. You round up your roommates and dip. Later, you hear rumors of people from the party being sent to the Honor Code office. You’re glad you didn’t have to deal with that mess.")
   elif choice == "netflix":
       print("You stay home and enjoy your snacks but feel a slight bit of FOMO. Later, your roommates get back surprisingly early saying the cops were showing up and it was lame. You’re glad you skipped out, you didn’t need any more stress so close to finals week.")
        
    # Week 30 Major Choice 10, 11, 12, 13, 14 ----------------------------------------------------------
    
     # choice 10 dialogue -------------------------
        print("""It’s finals week and you’ve made it so far! You’ve got lots of exams and almost no time. You’ve been seeing your lover over the last 
              couple of months and you know they could be the one. They ask to go out this week, but it happens to be a night you were going to study. 
              You know you’ve studied hard, you could afford one night off, right? Do you want to play it safe and study for FINALS or take your person out for 
              something SPECIAL?""")
    choice = input("FINALS or SPECIAL?").lower()
    if choice == "finals": ## Leads to Ending 15
        print(f"""It’s time to lock in. Finals are here and you want to be all the way prepared. 
              As great as your relationship is, now is not the time to add more onto either of your plates. 
              You’ve never been so zoned in before, but this week has been like no other. 
              As you go into your finals, you feel prepared more than ever before.""")
    elif choice == "special": ##Leads to Ending 16
        print("""You decide to take your special someone out for a special night. You go out to Millhollow for dinner, a rather expensive diner, and 
        then walk through the campus gardens just as the sun is setting. Is there really a better time than now? Before you realize it, you’re strolling 
        right into the gazebo with the love of your life right next to your side. You leave the gardens, one of you with a gem dazzling on your ring finger.""")
    
     # choice 11 dialogue -------------------------
        print("""It’s finals week and you’ve made it so far! You’ve been seriously dating someone over the last couple of months and you know a big decision 
            is coming up. This week you’ve got lots of exams and almost no time; you are stressed out to the max. You have the choice to study for FINALS, take your lover 
            out for something SPECIAL, or hit pause and go out for some FUN with your friends. What will it be?""")
    choice = input("FINALS, SPECIAL, or FUN?").lower()
    if choice == "finals": ##Leads to Ending 15
        print(f"""It’s time to lock in. Finals are here and you want to be all the way prepared. 
              As great as your relationship is, now is not the time to add more onto either of your plates. 
              You’ve never been so zoned in before, but this week has been like no other. 
              As you go into your finals, you feel prepared more than ever before.""")
    elif choice == "special": ##Leads to Ending 16
        print(f"""You want to take your special someone out for a special night. 
              You go out to Millhollow for dinner, a rather expensive diner, and then walk through the campus gardens just as the sun is setting. 
              Is there really a better time than now? Before you realize it, you’re strolling right into the gazebo with the love of your life right next to your side. 
              You leave the gardens, one of you with a gem dazzling on your ring finger.""")
    elif choice == "fun": ##Leads to Ending 17
        print(f"""You decide to go out for some fun over the weekend! You’ve been studying so what’s the harm? Well, apparently your relationship and your grades.
            You had mentioned extreme stress from finals but then went out for the weekend with some friends. Your partner felt like a last priority and decided
            to break things off for now. It didn’t help that you didn’t feel confident in any of your exams either. Maybe you should’ve studied more…""") 
    # choice 12 dialogue  -------------------------
        print(f"""You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to 
              the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown 
              in fear of a commitment?""")
    choice = input("GARDENS, HIDE, or ESCAPE?").lower()
    if choice == "gardens": ##Leads to Ending 16
        print(f"""You decide to take your special someone up on their invitation. You go out to Millhollow for dinner, a rather expensive diner, and then walk through
            the campus gardens just as the sun is setting. Is there really a better time than now? Before you realize it, you’re strolling right into the gazebo with 
            the love of your life right next to your side. You leave the gardens, one of you with a gem dazzling on your ring finger.""")
    elif choice == "hide": ##Leads to Ending 17
        print("""You’re paralyzed by your decision. Are you ready? Are they ready? You’ve been out with them for some time now but the fear of how little you know about
            this person eats you alive. You stay up all night, consumed by your thoughts. Before you realize, it’s light outside and you had several final exams lined up 
            for the day. Hopefully it works out.""")
    elif choice == "escape": ##Leads to Ending 18
        print("""It all happened so fast and you didn’t feel ready for any of it. You’d heard the saying “byu-i do” but you didn’t expect to experience that firsthand. 
            In fear of such a commitment, you run back to your hometown. You took the time to take a breather, but in turn you missed your final exams! You start to think 
            maybe you weren’t cut out for this whole college thing…""") 

    # choice 13 dialogue -------------------------
        print("""You’re back at another week of school and things aren’t doing great. Maybe your family was right after all. Is it even worth it to try if you know you’re 
            going to fail? Do you want to attempt your EXAMS, give in to your family by dropping OUT of school, or ignore it all and go for a late night DRIVE?""")
    choice = input("EXAMS, OUT, or DRIVE?").lower()
    if choice == "exams": ##Leads to Ending 17
        print(f"""This semester just felt like a complete repeat of the last but you weren’t one to just give up. 
              ven though you went in expecting an unfortunate outcome, you were still going to do your best. 
              Whether or not you failed, you were proud of your perseverance through it all.""")
    elif choice == "out": ##Leads to Ending 18
        print(f"""This semester just felt like a complete repeat of the last, and nothing could stop the feelings of failure. 
              It’s all too much, the pressure has built up and gotten to you. You feel like you just weren’t cut out for college.""")
    elif choice == "drive": ##Leads to Ending 19
        print("""You hop in your car late at night, annoyed by the rain that’s beginning to come down. 
              You turn up your radio to full blast as you start to cruise on the freeway.
            You’re shouting at the top of your lungs when all of the sudden a deer hops right in front of you! 
              In shock, you smash the breaks and jerk the steering wheel, sending
            you spinning out of control. You don’t see much before you pass out. You’ve been in a fatal car crash and have died.

            Your journey has officially ended. You will be missed.""") 

    # choice 14 dialogue ------------------------
        print("""You’re driving fast, cruising, adrenaline is rushing through you. You’re at 90, 95, and just like that you’ve hit 100mph.
        You smile and shout out in pure excitement. How fast could you push it? 
         Just as you’re about to push the pedal further, you see sirens flash in your rearview mirror.
        You mutter under your breath as you weigh out your options. Do you PULL over or try to RUN away?""")
    choice = input("PULL or RUN?").lower()
    if choice == "pull": ##Leads to Ending 18
        print(f"""Why did you even think of trying to get away? You felt insane for having that thought. 
              You pull over as the good citizen you are. As you are lectured on the danger of speeding, you realize how much life has to offer and how quickly it can be over. 
              What were you doing by spending it in a classroom all day? 
              In that moment you decide that there’s so much more you’d rather be doing and seeing in the world.""")
    elif choice == "run": ##Leads to Ending 19
        print(f"""This is it– your moment, just like the movies. You press the gas pedal harder and cut across lanes, maneuvering through the vehicles on the road. 
              Is this what Mario Kart felt like? If you had a shell, you’d throw it behind you. At that thought, you glance in your rearview mirror and miss the deer that has jumped in your path.
              You smash the brakes and jerk the steering wheel, sending you spinning out of control. You don’t see much before you pass out. You’ve been in a fatal car crash and have died. 
              
              Your journey has officially ended. You will be missed.""") 




















    if choice == "":
        print("")

    elif choice == "":
        print("") 

    elif choice == "":
        print("") 

    elif choice == "":
        print("")

    elif choice == "":
        print("") 