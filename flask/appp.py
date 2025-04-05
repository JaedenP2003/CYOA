from flask import Flask, render_template

app = Flask(__name__)

# Dictionary containing the game's story paths
story = {
        "start": {
        "text": "Welcome to BYU-I! It's your first semester, and the First Friday party for freshmen rolls around. Your roommates are one of many students excited and invite you to go out with them! Do you ACCEPT the invite or DECLINE?",
        "choices": {
            "accept": "Go to First Friday",
            "decline": "Stay home and settle in"
        }
    },
    #MC 2
    "accept": {
        "text": "You go with your roommates to first Friday and build some relationships with them. You feel closer to them than just a few days earlier when you moved in. They could turn out to be a great support system! As the end of semester nears, group projects are ramping up and your team has decided to hold a meeting Friday night this week. However, your friend invites you to a watch party for a new show that debuts for the same night. Do you meetup for your PROJECT or go to the WATCH party?",
        "choices": {
            "week2-1a": "Meet up for your project",
            "week2-1b": "Go to the watch party",
        }
    },
    "week2-1a": {
        "text": "Congratulations! You’ve got through your first week of school, but the food you came up with has almost run out. You really could use some groceries. Conveniently, Wal-Mart is right in town but it’s a little more expensive than you want it to be. However, you could drive to Idaho Falls and save money by buying in bulk at Costco, it’s just a 25-mile drive. Do you STAY in town, or DRIVE to Idaho Falls?",
        "choices": {
            "week3-1a": "Stay in town",
            "week3-1b": "Drive to Idaho Falls",
        }
    },
    "week2-1b": {
        "text": "Congratulations! You’ve got through your first week of school, but the food you came up with has almost run out. You really could use some groceries. Conveniently, Wal-Mart is right in town but it’s a little more expensive than you want it to be. However, you could drive to Idaho Falls and save money by buying in bulk at Costco, it’s just a 25-mile drive. Do you STAY in town, or DRIVE to Idaho Falls?",
        "choices": {
            "week3-1a": "Stay in town",
            "week3-1b": "Drive to Idaho Falls",
        }
    },
    "week3-1a": {
    "text": "You’re officially settled in and want to explore around a little bit.  Many people recommend going to the sand dunes, but you also heard that R Mountain is a fun, casual hike. Do you go to the DUNES, or try to hike the MOUNTAIN?",
    "choices": {
        "week4-1a": "Go to the dunes",
        "week4-1b": "Hike R Mountain",
        }
    },
    "week3-1b": {
    "text": "You’re officially settled in and want to explore around a little bit.  Many people recommend going to the sand dunes, but you also heard that R Mountain is a fun, casual hike. Do you go to the DUNES, or try to hike the MOUNTAIN?",
    "choices": {
        "week4-1a": "Go to the dunes",
        "week4-1b": "Hike R Mountain",
        }
    },
    "week4-1a": {
    "text": "It’s late in the night and you’re about to pass out when you realize you haven’t submitted an assignment for one of your classes. You are exhausted and hardly have any motivation to get out of bed. Is it TOMORROW’S problem, or will you work on it NOW?",
    "choices": {
        "week5-1a": "Worry about it tomorrow",
        "week5-1b": "Work on it now",
        }
    },
    "week4-1b": {
    "text": "It’s late in the night and you’re about to pass out when you realize you haven’t submitted an assignment for one of your classes. You are exhausted and hardly have any motivation to get out of bed. Is it TOMORROW’S problem, or will you work on it NOW?",
    "choices": {
        "week5-1a": "Worry about it tomorrow",
        "week5-1b": "Work on it now",
        }
    },
    "week5-1a": {
    "text": "It’s that point in the semester where you find yourself in a bit of a slump. The motivation just isn’t as prevalent as it was. Regardless, you know you need to stay on top of things. You’re reading a book for one of your classes and highly engaged in homework when a friend texts you about a new show that debuts tonight and asks for you to come over and watch it. Do you go over and WATCH the new show, or STAY at home and continue your studies?",
    "choices": {
        "week6-1a": "Watch the new show",
        "week6-1b": "Study at home",
        }
    },
    "week5-1b": {
    "text": "It’s that point in the semester where you find yourself in a bit of a slump. The motivation just isn’t as prevalent as it was. Regardless, you know you need to stay on top of things. You’re reading a book for one of your classes and highly engaged in homework when a friend texts you about a new show that debuts tonight and asks for you to come over and watch it. Do you go over and WATCH the new show, or STAY at home and continue your studies?",
    "choices": {
        "week6-1a": "Watch the new show",
        "week6-1b": "Study at home",
        }
    },
    "week6-1a": {
    "text": "As the end of semester nears, group projects are ramping up and your team has decided to hold a meeting Friday night this week. However, your friend invites you to a watch party for a new show that debuts for the same night. Do you meetup for your PROJECT or go to the WATCH party?",
    "choices": {
        "project": "Work on project",
        "watch": "Go to watch party",
        }
    },
    "week6-1b": {
    "text": "As the end of semester nears, group projects are ramping up and your team has decided to hold a meeting Friday night this week. However, your friend invites you to a watch party for a new show that debuts for the same night. Do you meetup for your PROJECT or go to the WATCH party?",
    "choices": {
        "project": "Work on project",
        "watch": "Go to watch party",
        }
    },
    #MC 3
    "decline": {
        "text": "You politely decline as you just want to get settled in more. As the night goes on you feel a little regret and wonder how much you’re missing out. It doesn’t help that your roommates came back raving about how fun it was. You’re watching your new binge-show when one of your roommates asks if you want to go study at the library with them. However, you are very comfortable with your current downtime. Do you continue to RELAX or go STUDY with your roommate?",
        "choices": {
            "study": "Go study with your roommate",
            "relax": "Continue to relax",
        }
    },
    "week2-2a": {
    "text": "Congratulations! You’ve got through your first week of school, but the food you came up with has almost run out. You really could use some groceries. Conveniently, Wal-Mart is right in town but it’s a little more expensive than you want it to be. However, you could drive to Idaho Falls and save money by buying in bulk at Costco, it’s just a 25-mile drive. Do you STAY in town, or DRIVE to Idaho Falls?",
    "choices": {
        "week3-2a": "Stay in town",
        "week3-2b": "Drive to Idaho Falls",
        }
    },
    "week2-2b": {
    "text": "Congratulations! You’ve got through your first week of school, but the food you came up with has almost run out. You really could use some groceries. Conveniently, Wal-Mart is right in town but it’s a little more expensive than you want it to be. However, you could drive to Idaho Falls and save money by buying in bulk at Costco, it’s just a 25-mile drive. Do you STAY in town, or DRIVE to Idaho Falls?",
    "choices": {
        "week3-2a": "Stay in town",
        "week3-2b": "Drive to Idaho Falls",
        }
    },
    "week3-2a": {
    "text": "You’re officially settled in and want to explore around a little bit.  Many people recommend going to the sand dunes, but you also heard that R Mountain is a fun, casual hike. Do you go to the DUNES, or try to hike the MOUNTAIN?",
    "choices": {
        "week4-2a": "Go to the dunes",
        "week4-2b": "Hike R Mountain",
        }
    },
    "week3-2b": {
    "text": "You’re officially settled in and want to explore around a little bit.  Many people recommend going to the sand dunes, but you also heard that R Mountain is a fun, casual hike. Do you go to the DUNES, or try to hike the MOUNTAIN?",
    "choices": {
        "week4-2a": "Go to the dunes",
        "week4-2b": "Hike R Mountain",
        }
    },
    "week4-2a": {
    "text": "It’s late in the night and you’re about to pass out when you realize you haven’t submitted an assignment for one of your classes. You are exhausted and hardly have any motivation to get out of bed. Is it TOMORROW’S problem, or will you work on it NOW?",
    "choices": {
        "week5-2a": "Worry about it tomorrow",
        "week5-2b": "Work on it now",
        }
    },
    "week4-2b": {
    "text": "It’s late in the night and you’re about to pass out when you realize you haven’t submitted an assignment for one of your classes. You are exhausted and hardly have any motivation to get out of bed. Is it TOMORROW’S problem, or will you work on it NOW?",
    "choices": {
        "week5-2a": "Worry about it tomorrow",
        "week5-2b": "Work on it now",
        }
    },
    "week5-2a": {
    "text": "It’s that point in the semester where you find yourself in a bit of a slump. The motivation just isn’t as prevalent as it was. Regardless, you know you need to stay on top of things. You’re reading a book for one of your classes and highly engaged in homework when a friend texts you about a new show that debuts tonight and asks for you to come over and watch it. Do you go over and WATCH the new show, or STAY at home and continue your studies?",
    "choices": {
        "week6-2a": "Watch the new show",
        "week6-2b": "Study at home",
        }
    },
    "week5-2b": {
    "text": "It’s that point in the semester where you find yourself in a bit of a slump. The motivation just isn’t as prevalent as it was. Regardless, you know you need to stay on top of things. You’re reading a book for one of your classes and highly engaged in homework when a friend texts you about a new show that debuts tonight and asks for you to come over and watch it. Do you go over and WATCH the new show, or STAY at home and continue your studies?",
    "choices": {
        "week6-2a": "Watch the new show",
        "week6-2b": "Study at home",
        }
    },
    "week6-2a": {
    "text": "The weather is very bleak this week, the snow is rolling in! It’s going to be very cold, snowy and windy, but you have a peer awaiting your help in a class. She’s really struggling with the concepts of the class, but you notice some ice outside your apartment window and think it might be a little risky. Do you HEAD to class, or try to AVOID the ice and stay home?",
    "choices": {
        "project": "Head to class",
        "watch": "Avoid the ice and stay home",
        }
    },
    "week6-2b": {
    "text": "The weather is very bleak this week, the snow is rolling in! It’s going to be very cold, snowy and windy, but you have a peer awaiting your help in a class. She’s really struggling with the concepts of the class, but you notice some ice outside your apartment window and think it might be a little risky. Do you HEAD to class, or try to AVOID the ice and stay home?",
    "choices": {
        "project": "Head to class",
        "watch": "Avoid the ice and stay home",
        }
    },
    #MC 4
    "project": {
        "text": "You want to stay on top of your academics this semester and work hard on your project! You feel productive because of all your hard work. Congrats, you passed your exams! Thanks to all your academic dedication, you feel on top of the world as you head home for winter break– you can’t wait to share the good news with your family. You make it home and when everyone asks you about how college has been, you were proud to say it was better than you expected! Going into the new year and semester, you want to set some goals to stay on track. Are your goals to study HARDER or expand your SOCIAL circle?",
        "choices": {
            "harder": "Study harder",
            "social": "Expand your social circle",
        }
    },
    "study": {
        "text": "Your show can wait, you’ve decided to study and put more time into your academics. You want to stay on top of your homework! You feel productive because of all your hard work. Congrats, you passed your exams! Thanks to all your academic dedication, you feel on top of the world as you head home for winter break– you can’t wait to share the good news with your family. You make it home and when everyone asks you about how college has been, you were proud to say it was better than you expected! Going into the new year and semester, you want to set some goals to stay on track. Are your goals to study HARDER or expand your SOCIAL circle?",
        "choices": {
            "harder": "Study harder",
            "social": "Expand your social circle",
        }
    },
    #MC 5
    "watch": {
        "text": "How could you miss the watch party? You want to make sure you’re staying social, you’re in college after all! Yikes, you failed your exams! As you reflect back on this semester, you must’ve slacked off more than you realized. As you’re driving home for winter break, all you can think about is what you’re going to tell your family.  You make it home and everyone has asked you about your experience at college.It came out that you didn’t do so well; and christmas dinner was a nightmare with all the relatives pestering you, especially Uncle Brad. As the new year rolls around, you’ve been weighing out your options. You don’t know how well another semester would treat you. You could DROP out, take a BREAK, go BACK from embarrassment, or PROVE everyone wrong next semester.",
        "choices": {
            "drop": "Drop out",
            "break": "Take a break",
            "prove": "Prove everyone wrong next semester",
            "back": "Go back from embarrassment",
        }
    },
    "relax": {
        "text": "You are deep into your show and politely decline the offer from your roommate. You have all semester, right? You tell them maybe next time. Yikes, you failed your exams! As you reflect back on this semester, you must’ve slacked off more than you realized. As you’re driving home for winter break, all you can think about is what you’re going to tell your family. You make it home and everyone has asked you about your experience at college.It came out that you didn’t do so well; and christmas dinner was a nightmare with all the relatives pestering you, especially Uncle Brad. As the new year rolls around, you’ve been weighing out your options. You don’t know how well another semester would treat you. You could DROP out, take a BREAK, go BACK from embarrassment, or PROVE everyone wrong next semester.",
        "choices": {
            "drop": "Drop out",
            "break": "Take a break",
            "prove": "Prove everyone wrong next semester",
            "back": "Go back from embarrassment",
        }
    },
    #MC 6
    "harder": {
        "text": "The high you felt after succeeding this semester was addicting, you wanted more. Your new year's goal is to study hard in the upcoming semester. Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend. The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night. You’ve been out with this person a handful of times and you’re starting to really like them. Do you go out on the DATE, or reschedule it so you can get help with your HOMEWORK?",
        "choices": {
            "homework": "Get help with homework",
            "date1": "Go out on the date",
        }
    },
    #MC 7
    "social": {
        "text": "The academic success you had was exciting but you want to try something new in the upcoming semester. You want to push yourself out of your comfort zone and expand your social circle! You’ve gone out with this one person over the past month, you might really be starting to like them but now is time to make a decision. Valentine's day is almost here and you’re weighing out your options. You could ask them to be your VALENTINE, go further and ask them to be OFFICIAL, or NOT worry about it.",
        "choices": {
            "valentine": "Ask them to be your valentine",
            "official": "Ask them to be official",
            "not": "Don't worry about it",
        }
    },
    #MC 8
    "prove": {
        "text": "You may have done poorly last semester but you won’t make the same mistake again. You make the promise that you’ll clear your name and come home next semester proud instead of ashamed. You’re going to prove Uncle Brad wrong. Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend. The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night. You’ve been out with this person a handful of times and you’re starting to really like them, but you’re also stressed out with your homework. Do you go on the DATE, reschedule it so you can get help with your ASSIGNMENTS or take some time to relax and watch that new SHOW you started?",
        "choices": {
            "assignments": "Get help with your assignments",
            "date2": "Go on the date",
            "show": "Watch the new show you started",
        }
    },
    #MC 9
    "back": {
        "text": "Last semester was awful but you’ll never live it down if you quit now. You’ve got to go back. You’re not excited but it’s better than the humiliation of another choice. You’re back at another week of school and things aren’t doing great. The weekend is coming up and you want to have some fun. You’re weighing out your options. You could ASK someone out on a date, watch some TV to decompress or attempt to baptize your CAR.",
        "choices": {
            "ask": "Ask someone on a date",
            "tv": "Watch tv to decompress",
            "car": "Baptize your car",
        }
    },
    #MC 10
    "homework": {
        "text": "You want to keep up the good work and continue the grind! Although you wanted to go out, the help you got at the open lab was extremely helpful. You came out feeling much better about the course than you did earlier. It’s finals week and you’ve made it so far! You’ve got lots of exams and almost no time. You’ve been seeing your lover over the last couple of months and you know they could be the one. They ask to go out this week, but it happens to be a night you were going to study. You know you’ve studied hard, you could afford one night off, right? Do you want to play it safe and study for FINALS or take your person out for something SPECIAL?",
        "choices": {
            "finals": "Study for finals",
            "special": "Take your person out for something special",
        }
    },
    "valentine": {
        "text": "You aren’t quite ready for the full commitment of a new relationship but you do really like this person. So you pull out some of the stops- flowers and chocolate. You have a valentine! It’s finals week and you’ve made it so far! You’ve got lots of exams and almost no time. You’ve been seeing your lover over the last couple of months and you know they could be the one. They ask to go out this week, but it happens to be a night you were going to study. You know you’ve studied hard, you could afford one night off, right? Do you want to play it safe and study for FINALS or take your person out for something SPECIAL?",
        "choices": {
            "finals": "Study for finals",
            "special": "Take your person out for something special",
        }
    },
    #MC 11
    "date1": {
        "text": "How could you say no to a date? Things are going so well, you don’t want to jeopardize your relationship over some homework! The date goes great and you don’t even think twice about the missed lab. It’s finals week and you’ve made it so far! You’ve been seriously dating someone over the last couple of months and you know a big decision is coming up. This week you’ve got lots of exams and almost no time; you are stressed out to the max. You have the choice to study for FINALS, take your lover out for something SPECIAL, or hit pause and go out for some FUN with your friends. What will it be?",
        "choices": {
            "finals": "Study for finals",
            "special": "Take your lover out for something special",
            "fun": "Go out and have some fun with your friends",
        }
    },
    "official": {
        "text": "This person makes you happy! You decide it’s time to make things official with them. You pull out all the stops- flowers, chocolates and a handwritten note. When you prompted the question, it was obvious the feelings were mutual. Congrats!! You feel like the luckiest person in the world. It’s finals week and you’ve made it so far! You’ve been seriously dating someone over the last couple of months and you know a big decision is coming up. This week you’ve got lots of exams and almost no time; you are stressed out to the max. You have the choice to study for FINALS, take your lover out for something SPECIAL, or hit pause and go out for some FUN with your friends. What will it be?",
        "choices": {
            "finals": "Study for finals",
            "special": "Take your lover out for something special",
            "fun": "Go out and have some fun with your friends",
        }
    },
    "assignments": {
        "text": "You felt the need to keep the promise you made with yourself. You felt a desire– petty or not– to prove everyone wrong and that you could do this. Although you wanted to go out, the help you got at the open lab was extremely helpful. You came out feeling much better about the course than you did earlier. It’s finals week and you’ve made it so far! You’ve been seriously dating someone over the last couple of months and you know a big decision is coming up. This week you’ve got lots of exams and almost no time; you are stressed out to the max. You have the choice to study for FINALS, take your lover out for something SPECIAL, or hit pause and go out for some FUN with your friends. What will it be?",
        "choices": {
            "finals": "Study for finals",
            "special": "Take your lover out for something special",
            "fun": "Go out and have some fun with your friends",
        }
    },
    #MC 12
    "not": {
        "text": "You don’t feel worried about asking them to be your valentine because it didn’t feel that serious to you. It was just a little holiday so did it really matter? You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown in fear of a commitment?",
        "choices": {
            "gardens": "Go to the gardens",
            "hide": "Hide in your apartment",
            "escape": "Escape back to your hometown",
        }
    },
    "date2": {
        "text": "How could you say no to a date? Things are going so well, you don’t want to jeopardize your relationship over some homework! You remembered the promise you made to yourself, but you also want things to look forward to. The date goes great and you don’t even think twice about the missed lab. You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown in fear of a commitment?",
        "choices": {
            "gardens": "Go to the gardens",
            "hide": "Hide in your apartment",
            "escape": "Escape back to your hometown",
        }
    },
    "ask": {
        "text": "A date sounds like the best option! You’ve been seeing this one person for some time now and you want to continue to pursue a relationship with them. Although you weren’t excited to come back to school, things might actually start to be looking up, in at least one aspect. You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown in fear of a commitment?",
        "choices": {
            "gardens": "Go to the gardens",
            "hide": "Hide in your apartment",
            "escape": "Escape back to your hometown",
        }
    },
    #MC 13
    "show": {
        "text": "It was hard finding time for yourself so you decided to take a breather. You feel it would benefit you most to hit pause. The homework and date could wait, right? Well unfortunately, the date couldn’t. They felt like a last priority and called things off. Yikes, that didn’t go how you pictured. You’re back at another week of school and things aren’t doing great. Maybe your family was right after all. Is it even worth it to try if you know you’re going to fail? Do you want to attempt your EXAMS, give in to your family by dropping OUT of school, or ignore it all and go for an emotional late night DRIVE?",
        "choices": {
            "exams": "Attempt your exams",
            "out": "Drop out of school",
            "drive": "Go for a late night drive",
        }
    },
    "tv": {
        "text": "You wanted to have fun and relax, not push your limits emotionally or physically. You switch on your comfort show: The Bachelor. Your mind rests as the girls fight over the guy- you laugh at seemingly annoying comments and shout at the one girl that loves to cause drama. You’re back at another week of school and things aren’t doing great. Maybe your family was right after all. Is it even worth it to try if you know you’re going to fail? Do you want to attempt your EXAMS, give in to your family by dropping OUT of school, or ignore it all and go for an emotional late night DRIVE?",
        "choices": {
            "exams": "Attempt your exams",
            "out": "Drop out of school",
            "drive": "Go for a late night drive",
        }
    },
    #MC 14
    "car": {
        "text": "You decide you want to try and baptize your car, how hard could it be? You hop in your car and drive onto the freeway. You grab your steering wheel tightly and drive a few miles before building up the courage to press the gas pedal to the floor. You’re driving fast, cruising, adrenaline is rushing through you. You’re at 90, 95, and just like that you’ve hit 100mph. You smile and shout out in pure excitement. How fast could you push it?  Just as you’re about to push the pedal further, you see sirens flash in your rearview mirror. You weigh out your options. Do you PULL over or RUN away?",
        "choices": {
            "pull": "Pull over",
            "run": "Run away",
        }
    },
    #MC 15, Ending 1
    "finals": {
        "text": "It’s time to lock in. Finals are here and you want to be all the way prepared. As great as your relationship is, now is not the time to add more onto either of your plates. You’ve never been so zoned in before, but this week has been like no other. As you go into your finals, you feel prepared more than ever before. Congrats, you have aced all your exams!! Your hard work and dedication has truly paid off. That scholarship is all yours! You should be proud of all your academic achievements this semester.",
        "choices": {}
    },
    #MC 16, Ending 2
    "special": {
        "text": "You want to take your special someone out for a special night. You go out to Millhollow for dinner, a rather expensive diner, and then walk through the campus gardens just as the sun is setting. Is there really a better time than now? Before you realize it, you’re strolling right into the gazebo with the love of your life right next to your side. You leave the gardens, one of you with a gem dazzling on your ring finger. The day was filled with love, laughter, and the warmth of family and friends. Vows were exchanged, promises made, and happy tears shared. Music played, laughter shared, and love filled the air. By the end of the day you walked away hand in hand, ready to begin forever together.",
        "choices": {}
    },
    "gardens": {
        "text": "You decide to take your special someone up on their invitation. You go out to Millhollow for dinner, a rather expensive diner, and then walk through the campus gardens just as the sun is setting. Is there really a better time than now? Before you realize it, you’re strolling right into the gazebo with the love of your life right next to your side. You leave the gardens, one of you with a gem dazzling on your ring finger. The day was filled with love, laughter, and the warmth of family and friends. Vows were exchanged, promises made, and happy tears shared. Music played, laughter shared, and love filled the air. By the end of the day you walked away hand in hand, ready to begin forever together.",
        "choices": {}
    },
    #MC 17, Ending 3
    "fun": {
        "text": "You decide to go out for some fun over the weekend! You’ve been studying so what’s the harm? Well, apparently your relationship and your grades. You had mentioned extreme stress from finals but then went out for the weekend with some friends. Your partner felt like a last priority and decided to break things off for now. It didn’t help that you didn’t feel confident in any of your exams either. Everything feels like it’s falling apart. Maybe you should’ve studied more… Wow, you’ve totally bombed your exams! You must’ve slacked off more than you realized. Everyone faces challenges, but what matters most is how you move forward. Maybe next semester will be yours…",
        "choices": {}
    },
    "hide": {
        "text": "You’re paralyzed by your decision. Are you ready? Are they ready? You’ve been out with them for some time now but the fear of how little you know about this person eats you alive. You stay up all night, consumed by your thoughts. Before you realize, it’s light outside and you had several final exams lined up for the day. Hopefully it works out. Wow, you’ve totally bombed your exams! You must’ve slacked off more than you realized. Everyone faces challenges, but what matters most is how you move forward. Maybe next semester will be yours…",
        "choices": {}
    },
    "exams": {
        "text": "This semester just felt like a complete repeat of the last but you weren’t one to just give up. Even though you went in expecting an unfortunate outcome, you were still going to do your best. Whether or not you failed, you were proud of your perseverance through it all. Wow, you’ve totally bombed your exams! You must’ve slacked off more than you realized. Everyone faces challenges, but what matters most is how you move forward. Maybe next semester will be yours…",
        "choices": {}
    },
    #MC 18, Ending 4
    "escape" : {
        "text": "It all happened so fast and you didn’t feel ready for any of it. You’d heard the saying “byu-i do” but you didn’t expect to experience that firsthand. In fear of such a commitment, you run back to your hometown. You took the time to take a breather, but in turn you missed your final exams! You start to think maybe you weren’t cut out for this whole college thing… You’ve decided to drop out of school and pursue other ambitions. Your journey at byu-idaho has officially ended. Good luck with the rest of your endeavors, you’ll be missed.",
        "choices": {}
    },
    "out": {
        "text": "This semester just felt like a complete repeat of the last, and nothing could stop the feelings of failure. It’s all too much, the pressure has built up and gotten to you. You feel like you just weren’t cut out for college.",
        "choices": {}
    },
    "pull": {
        "text": "Why did you even think of trying to get away? You felt insane for having that thought. You pull over as the good citizen you are. As you are lectured on the danger of speeding, you realize how much life has to offer and how quickly it can be over. What were you doing by spending it in a classroom all day? In that moment you decide that there’s so much more you’d rather be doing and seeing in the world.",
        "choices": {}
    },
    "drop": {
        "text": "It’s all too much, the pressure has built up and gotten to you. You feel like you just weren’t cut out for college.",
        "choices": {}
    },
    #MC 19, Ending 5
    "drive": {
        "text": "You hop in your car late at night, annoyed by the rain that’s beginning to come down. You turn up your radio to full blast as you start to cruise on the freeway. You’re shouting at the top of your lungs when all of the sudden a deer hops right in front of you! In shock, you smash the brakes and jerk the steering wheel, sending you spinning out of control. You don’t see much before you pass out. You’ve been in a fatal car crash and have died. Your journey has officially ended. You will be missed. Perhaps this is the end. Or maybe, it's the beginning of something else. Perhaps, in another life, another choice could have changed everything.",
        "choices": {}
    },
    "run": {
        "text": "This is it– your moment, just like the movies. You press the gas pedal harder and cut across lanes, maneuvering through the vehicles on the road. Is this what Mario Kart felt like? If you had a shell, you’d throw it behind you. At that thought, you glance in your rearview mirror and miss the deer that has jumped in your path.You smash the brakes and jerk the steering wheel, sending you spinning out of control. You don’t see much before you pass out. You’ve been in a fatal car crash and have died. Your journey has officially ended. You will be missed. Perhaps this is the end. Or maybe, it's the beginning of something else. Perhaps, in another life, another choice could have changed everything.",
        "choices": {}
    },
    "break": {
        "text": "You decide to take a break thinking it will help clear your mind. While working at home, you decide to meet up with some old friends. They invite you out to go snowmobiling! You’re having the time of your life while you’re riding but make the mistake of looking back at your friends behind you. They shout at you and you notice a giant tree come into view as you face forward. You attempt to swerve out of the way, but it’s too late. You have died and your journey has officially ended. You will be missed. Perhaps this is the end. Or maybe, it's the beginning of something else. Perhaps, in another life, another choice could have changed everything.",
        "choices": {}
    },
}

@app.route("/")
def home():
    return render_template("index.html", story=story["start"], path="start")

@app.route("/choice/<path>")
def choice(path):
    if path in story:
        return render_template("index.html", story=story[path], path=path)
    return "Story not found!", 404

if __name__ == "__main__":
    app.run(debug=True)