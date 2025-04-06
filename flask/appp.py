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
        "text": "You go with your roommates to first Friday and build some relationships with them. You feel closer to them than just a few days earlier when you moved in. They could turn out to be a great support system! Monday comes around and it’s time to go to your first classes, mostly generals. You go to all of your classes, but the final one in the afternoon seems like it’s going to be a lot more work than you anticipated. It could offer some heavy benefits down the road, but it’s not required for your major. Do you STICK with it, or DROP the class?",
        "choices": {
            "week2-1a": "Stick with it",
            "week2-1b": "Drop the class",
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
    "text": "The weather is very bleak this week, the snow is rolling in! It’s going to be very cold, snowy and windy, but you have a peer awaiting your help in a class. She’s really struggling with the concepts of the class, but you notice some ice outside your apartment window and think it might be a little risky. Do you HEAD to class, or try to AVOID the ice and stay home?",
    "choices": {
        "week7-1a": "Head to class",
        "week7-1b": "Avoid the ice and stay home",
        }
    },
    "week6-1b": {
    "text": "The weather is very bleak this week, the snow is rolling in! It’s going to be very cold, snowy and windy, but you have a peer awaiting your help in a class. She’s really struggling with the concepts of the class, but you notice some ice outside your apartment window and think it might be a little risky. Do you HEAD to class, or try to AVOID the ice and stay home?",
    "choices": {
        "week7-1a": "Head to class",
        "week7-1b": "Avoid the ice and stay home",
        }
    },
        "week7-1a": {
    "text": "As the end of semester nears, group projects are ramping up and your team has decided to hold a meeting Friday night this week. However, your friend invites you to a watch party for a new show that debuts for the same night. Do you meetup for your PROJECT or go to the WATCH party?",
    "choices": {
        "project": "Work on project",
        "watch": "Go to watch party",
        }
    },
        "week7-1b": {
    "text": "As the end of semester nears, group projects are ramping up and your team has decided to hold a meeting Friday night this week. However, your friend invites you to a watch party for a new show that debuts for the same night. Do you meetup for your PROJECT or go to the WATCH party?",
    "choices": {
        "project": "Work on project",
        "watch": "Go to watch party",
        }
    },
    #MC 3
    "decline": {
        "text": "You politely decline as you just want to get settled in more. As the night goes on you feel a little regret and wonder how much you’re missing out. It doesn’t help that your roommates came back raving about how fun it was. Monday comes around and it’s time to go to your first classes, mostly generals. You go to all of your classes, but the final one in the afternoon seems like it’s going to be a lot more work than you anticipated. It could offer some heavy benefits down the road, but it’s not required for your major. Do you STICK with it, or DROP the class?",
        "choices": {
            "week2-2a": "Stick with it",
            "week2-2b": "Drop the class",
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
    "text": "You’re watching your new binge-show when one of your roommates asks if you want to go study at the library with them. However, you are very comfortable with your current downtime. Do you continue to RELAX or go STUDY with your roommate?",
    "choices": {
        "study": "Study with your roomate",
        "relax": "Continue to relax",
        }
    },
    "week6-2b": {
    "text": "You’re watching your new binge-show when one of your roommates asks if you want to go study at the library with them. However, you are very comfortable with your current downtime. Do you continue to RELAX or go STUDY with your roommate?",
    "choices": {
        "study": "Study with your roomate",
        "relax": "Continue to relax",
        }
    },
    #MC 4
    "project": {
        "text": "You want to stay on top of your academics this semester and work hard on your project! You feel productive because of all your hard work.",
        "text": "You feel relieved to be done with your midterm exams and projects. A nearby relative invites you to a family dinner on Sunday, they seem excited that you're in Idaho! Do you GO or STAY at home?",
        "choices": {
            "week9-1a": "Go to Sunday dinner",
            "week9-1b": "Stay at home",
        }
    },
    "study": {
        "text": "Your show can wait, you’ve decided to study and put more time into your academics. You want to stay on top of your homework! You feel productive because of all your hard work.",
        "text": "You feel relieved to be done with your midterm exams and projects. A nearby relative invites you to a family dinner on Sunday, they seem excited that you're in Idaho! Do you GO or STAY at home?",
        "choices": {
            "week9-1a": "Go to Sunday dinner",
            "week9-1b": "Stay at home",
        }
    },
    "week9-1a": {
    "text": "Another week passes and you feel like you're getting the hang of college. You start thinking about some hobbies you could take up in the area. Some of your friends talked about starting an intramural volleyball team, but you've also wanted to get into rock climbing. Do you decide to do VOLLEYBALL or CLIMB?",
    "choices": {
        "week10-1a": "Play volleyball",
        "week10-1b": "Go rock climbing",
        }
    },
    "week9-1b": {
    "text": "Another week passes and you feel like you're getting the hang of college. You start thinking about some hobbies you could take up in the area. Some of your friends talked about starting an intramural volleyball team, but you've also wanted to get into rock climbing. Do you decide to do VOLLEYBALL or CLIMB?",
    "choices": {
        "week10-1a": "Play volleyball",
        "week10-1b": "Go rock climbing",
        }
    },
    "week10-1a": {
    "text": "You have been so busy with school and other activities that you realize you haven't been reading Come Follow Me very often. Your family has been doing weekly zoom calls to read together, but you've told them you have been too busy to join each week. This week you know you have a little bit more time. You could JOIN or you could NOT join.",
    "choices": {
        "week11-1a": "Join the family call",
        "week11-1b": "Put if off another week",
        }
    },
    "week10-1b": {
    "text": "You have been so busy with school and other activities that you realize you haven't been reading Come Follow Me very often. Your family has been doing weekly zoom calls to read together, but you've told them you have been too busy to join each week. This week you know you have a little bit more time. You could JOIN or you could NOT join.",
    "choices": {
        "week11-1a": "Join the family call",
        "week11-1b": "Put if off another week",
        }
    },
    "week11-1a": {
    "text": "Monday rolls around and as you're eating lunch at the crossroads, a stranger comes up to you and hands you a note. They say 'someone told me to give this to you.' You accept the note and read 'I think you're really cute, you should text me! 208-198-0000. You feel warm inside and can't help but blush. You look around a little bit without being too obvious. You haven't been on a date in college yet, but you're nervous about going on a blind date. Do you TEXT the number or NOT?",
    "choices": {
        "week12-1a": "Text the number",
        "week12-1b": "Don't text the number",
        }
    },
    "week11-1b": {
    "text": "Monday rolls around and as you're eating lunch at the crossroads, a stranger comes up to you and hands you a note. They say 'someone told me to give this to you.' You accept the note and read 'I think you're really cute, you should text me! 208-198-0000. You feel warm inside and can't help but blush. You look around a little bit without being too obvious. You haven't been on a date in college yet, but you're nervous about going on a blind date. Do you TEXT the number or NOT?",
    "choices": {
        "week12-1a": "Text the number",
        "week12-1b": "Don't text the number",
        }
    },
    "week12-1a": {
    "text": "Its week 12 of the semester and you and your roommates decide to go on an adventure. You're driving to Idaho Falls and on the way you spot what looks like an abandoned building. You guys joke about exploring it, but then someone proposes you actually go explore it. You get a little hot inside. You've never explored an abandoned building. Two of your friends say they want to explore it, two of them say they don't. They all look at you for the tie breaker. Will you EXPLORE the abandoned building or NOT explore it?",
    "choices": {
        "week13-1a": "Explore the abandoned building",
        "week13-1b": "Don't explore it",
        }
    },
    "week12-1b": {
    "text": "Its week 12 of the semester and you and your roommates decide to go on an adventure. You're driving to Idaho Falls and on the way you spot what looks like an abandoned building. You guys joke about exploring it, but then someone proposes you actually go explore it. You get a little hot inside. You've never explored an abandoned building. Two of your friends say they want to explore it, two of them say they don't. They all look at you for the tie breaker. Will you EXPLORE the abandoned building or NOT explore it?",
    "choices": {
        "week13-1a": "Explore the abandoned building",
        "week13-1b": "Don't explore it",
        }
    },
    "week13-1a": {
    "text": "It's week 13 of the semester. After a long day of classes, your roommate invites you to a late-night food truck festival off campus. You’re tempted—it’s a chance to relax, try new foods, and just vibe. But earlier this week, you promised your friend you'd go to their open mic night at the campus café. They've been anxious about performing. Now both events are happening at the same time, and you have to choose. Will you go to the FOOD TRUCK festival or the OPEN MIC night?",
    "choices": {
        "week14-1a": "Go to the food truck festival",
        "week14-1b": "Go to the open mic night",
        }
    },
    "week13-1b": { 
    "text": "It's week 13 of the semester. After a long day of classes, your roommate invites you to a late-night food truck festival off campus. You’re tempted—it’s a chance to relax, try new foods, and just vibe. But earlier this week, you promised your friend you'd go to their open mic night at the campus café. They've been anxious about performing. Now both events are happening at the same time, and you have to choose. Will you go to the FOOD TRUCK festival or the OPEN MIC night?",
    "choices": {
        "week14-1a": "Go to the food truck festival",
        "week14-1b": "Go to the open mic night",
        }
    },
    "week14-1a": {
        "text": "Congrats, you passed your exams! Thanks to all your academic dedication, you feel on top of the world as you head home for winter break–you can’t wait to share the good news with your family. You make it home and when everyone asks you about how college has been, you were proud to say it was better than you expected!",
        "text": "The high you felt after succeeding this semester was addicting, you wanted more. Going into the new year and semester, you want to set some goals to stay on track. Are your goals to STUDY harder or expand your SOCIAL circle?",
    "choices": {
        "harder": "Study harder",
        "social": "Expand your social circle",
        }
    },
    "week14-1b": { 
        "text": "Congrats, you passed your exams! Thanks to all your academic dedication, you feel on top of the world as you head home for winter break–you can’t wait to share the good news with your family. You make it home and when everyone asks you about how college has been, you were proud to say it was better than you expected!",
        "text": "The high you felt after succeeding this semester was addicting, you wanted more. Going into the new year and semester, you want to set some goals to stay on track. Are your goals to STUDY harder or expand your SOCIAL circle?",
    "choices": {
        "harder": "Study harder",
        "social": "Expand your social circle",
        }
    },
    #MC 5
    "watch": {
        "text": "How could you miss the watch party? You want to make sure you’re staying social, you’re in college after all!",
        "text": "You feel relieved to be done with your midterm exams and projects. A nearby relative invites you to a family dinner on Sunday, they seem excited that you're in Idaho! Do you GO or STAY at home?",
        "choices": {
            "week9-2a": "Go to Sunday dinner",
            "week9-2b": "Stay at home",
        }
    },
    "relax": {
        "text": "You are deep into your show and politely decline the offer from your roommate. You have all semester, right? You tell them maybe next time.",
        "text": "You feel relieved to be done with your midterm exams and projects. A nearby relative invites you to a family dinner on Sunday, they seem excited that you're in Idaho! Do you GO or STAY at home?",
        "choices": {
            "week9-2a": "Go to Sunday dinner",
            "week9-2b": "Stay at home",
        }
    },
    "week9-2a": {
    "text": "Another week passes and you feel like you're getting the hang of college. You start thinking about some hobbies you could take up in the area. Some of your friends talked about starting an intramural volleyball team, but you've also wanted to get into rock climbing. Do you decide to do VOLLEYBALL or CLIMB?",
    "choices": {
        "week10-2a": "Play volleyball",
        "week10-2b": "Go rock climbing",
        }
    },
    "week9-2b": {
    "text": "Another week passes and you feel like you're getting the hang of college. You start thinking about some hobbies you could take up in the area. Some of your friends talked about starting an intramural volleyball team, but you've also wanted to get into rock climbing. Do you decide to do VOLLEYBALL or CLIMB?",
    "choices": {
        "week10-2a": "Play volleyball",
        "week10-2b": "Go rock climbing",
        }
    },
    "week10-2a": {
    "text": "You have been so busy with school and other activities that you realize you haven't been reading Come Follow Me very often. Your family has been doing weekly zoom calls to read together, but you've told them you have been too busy to join each week. This week you know you have a little bit more time. You could JOIN or you could NOT join.",
    "choices": {
        "week11-2a": "Join the family call",
        "week11-2b": "Put if off another week",
        }
    },
    "week10-2b": {
    "text": "You have been so busy with school and other activities that you realize you haven't been reading Come Follow Me very often. Your family has been doing weekly zoom calls to read together, but you've told them you have been too busy to join each week. This week you know you have a little bit more time. You could JOIN or you could NOT join.",
    "choices": {
        "week11-2a": "Join the family call",
        "week11-2b": "Put if off another week",
        }
    },
    "week11-2a": {
    "text": "Monday rolls around and as you're eating lunch at the crossroads, a stranger comes up to you and hands you a note. They say 'someone told me to give this to you.' You accept the note and read 'I think you're really cute, you should text me! 208-198-0000. You feel warm inside and can't help but blush. You look around a little bit without being too obvious. You haven't been on a date in college yet, but you're nervous about going on a blind date. Do you TEXT the number or NOT?",
    "choices": {
        "week12-2a": "Text the number",
        "week12-2b": "Don't text the number",
        }
    },
    "week11-2b": {
    "text": "Monday rolls around and as you're eating lunch at the crossroads, a stranger comes up to you and hands you a note. They say 'someone told me to give this to you.' You accept the note and read 'I think you're really cute, you should text me! 208-198-0000. You feel warm inside and can't help but blush. You look around a little bit without being too obvious. You haven't been on a date in college yet, but you're nervous about going on a blind date. Do you TEXT the number or NOT?",
    "choices": {
        "week12-2a": "Text the number",
        "week12-2b": "Don't text the number",
        }
    },
    "week12-2a": {
    "text": "Its week 12 of the semester and you and your roommates decide to go on an adventure. You're driving to Idaho Falls and on the way you spot what looks like an abandoned building. You guys joke about exploring it, but then someone proposes you actually go explore it. You get a little hot inside. You've never explored an abandoned building. Two of your friends say they want to explore it, two of them say they don't. They all look at you for the tie breaker. Will you EXPLORE the abandoned building or NOT explore it?",
    "choices": {
        "week13-2a": "Explore the abandoned building",
        "week13-2b": "Don't explore it",
        }
    },
    "week12-2b": {
    "text": "Its week 12 of the semester and you and your roommates decide to go on an adventure. You're driving to Idaho Falls and on the way you spot what looks like an abandoned building. You guys joke about exploring it, but then someone proposes you actually go explore it. You get a little hot inside. You've never explored an abandoned building. Two of your friends say they want to explore it, two of them say they don't. They all look at you for the tie breaker. Will you EXPLORE the abandoned building or NOT explore it?",
    "choices": {
        "week13-2a": "Explore the abandoned building",
        "week13-2b": "Don't explore it",
        }
    },
    "week13-2a": {
    "text": "It's week 13 of the semester. After a long day of classes, your roommate invites you to a late-night food truck festival off campus. You’re tempted—it’s a chance to relax, try new foods, and just vibe. But earlier this week, you promised your friend you'd go to their open mic night at the campus café. They've been anxious about performing. Now both events are happening at the same time, and you have to choose. Will you go to the FOOD TRUCK festival or the OPEN MIC night?",
    "choices": {
        "week14-2a": "Go to the food truck festival",
        "week14-2b": "Go to the open mic night",
        }
    },
    "week13-2b": {
    "text": "It's week 13 of the semester. After a long day of classes, your roommate invites you to a late-night food truck festival off campus. You’re tempted—it’s a chance to relax, try new foods, and just vibe. But earlier this week, you promised your friend you'd go to their open mic night at the campus café. They've been anxious about performing. Now both events are happening at the same time, and you have to choose. Will you go to the FOOD TRUCK festival or the OPEN MIC night?",
    "choices": {
        "week14-2a": "Go to the food truck festival",
        "week14-2b": "Go to the open mic night",
        }
    },
    "week14-2a": {
    "text": "Yikes, you failed your exams! As you reflect back on this semester, you must’ve slacked off more than you realized. As you’re driving home for winter break, all you can think about is what you’re going to tell your family. You make it home and everyone has asked you about your experience at college.It came out that you didn’t do so well; and christmas dinner was a nightmare with all the relatives pestering you, especially Uncle Brad. As the new year rolls around, you’ve been weighing out your options. You don’t know how well another semester would treat you. You could DROP out, take a BREAK, go BACK from embarrassment, or PROVE everyone wrong next semester.",
    "choices": {
        "drop": "Drop out of school",
        "break": "Take a break",
        "back": "Go back from embarrassment",
        "prove": "Prove everyone wrong",
        }
    },
    "week14-2b": {
    "text": "Yikes, you failed your exams! As you reflect back on this semester, you must’ve slacked off more than you realized. As you’re driving home for winter break, all you can think about is what you’re going to tell your family. You make it home and everyone has asked you about your experience at college.It came out that you didn’t do so well; and christmas dinner was a nightmare with all the relatives pestering you, especially Uncle Brad. As the new year rolls around, you’ve been weighing out your options. You don’t know how well another semester would treat you. You could DROP out, take a BREAK, go BACK from embarrassment, or PROVE everyone wrong next semester.",
    "choices": {
        "drop": "Drop out of school",
        "break": "Take a break",
        "back": "Go back from embarrassment",
        "prove": "Prove everyone wrong",
        }
    },
    #MC 6
    "harder": {
    "text": "You had a restful and calm break! Now you're back in school and ready for the winter semester. You find out your new roommates are chill like that, kawabunga baby. They wanna hangout and go sledding but you need to get groceries. Do you choose to go HANGOUT with them or do you go out and get GROCERIES?",
    "choices": {
        "week18-1a": "Hang out with your roommates",
        "week18-1b": "Go get groceries",
        }
    },

"week18-1a": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-1a": "Study for classes",
        "week19-1b": "Go to the game night",
    }
},
"week18-1b": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-1a": "Study for classes",
        "week19-1b": "Go to the game night",
    }
},
"week19-1a": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-1a": "Go on the hike",
        "week20-1b": "Talk to your professors",
    }
},
"week19-1b": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-1a": "Go on the hike",
        "week20-1b": "Talk to your professors",
    }
},
"week20-1a": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-1a": "Go to open mic night",
        "week21-1b": "Pick up the extra shift",
    }
},
"week20-1b": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-1a": "Go to open mic night",
        "week21-1b": "Pick up the extra shift",
    }
},
"week21-1a": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-1a": "Go to dinner with classmates",
        "week22-1b": "Go to the lounge with roommates",
    }
},
"week21-1b": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-1a": "Go to dinner with classmates",
        "week22-1b": "Go to the lounge with roommates",
    }
},
"week22-1a": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23": "Get pancakes",
        "week23": "Go to volunteer fair",
    }
},
"week22-1b": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23-1a": "Get pancakes",
        "week23-1b": "Go to volunteer fair",
    }
},
"week23-1a": {
    "text": """Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend. 
              The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night. 
              You’ve been out with this person a handful of times and you’re starting to really like them. Do you go out on the DATE, 
              or reschedule it so you can get help with your HOMEWORK?""",
    "choices": {
        "date1": "Go out on the date",
        "homework": "Get help with homework",
    }
},"week23-1b": {
    "text": """Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend. 
              The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night. 
              You’ve been out with this person a handful of times and you’re starting to really like them. Do you go out on the DATE, 
              or reschedule it so you can get help with your HOMEWORK?""",
    "choices": {
        "date1": "Go out on the date",
        "homework": "Get help with homework",
    }
},
    #MC 7
    "social": {
    "text": "You had a restful and calm break! Now you're back in school and ready for the winter semester. You find out your new roommates are chill like that, kawabunga baby. They wanna hangout and go sledding but you need to get groceries. Do you choose to go HANGOUT with them or do you go out and get GROCERIES?",
    "choices": {
        "week18-2a": "Hang out with your roommates",
        "week18-2b": "Go get groceries",
    }
},
"week18-2a": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-2a": "Study for classes",
        "week19-2b": "Go to the game night",
    }
},
"week18-2b": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-2a": "Study for classes",
        "week19-2b": "Go to the game night",
    }
},
"week19-2a": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-2a": "Go on the hike",
        "week20-2b": "Talk to your professors",
    }
},
"week19-2b": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-2a": "Go on the hike",
        "week20-2b": "Talk to your professors",
    }
},
"week20-2a": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-2a": "Go to open mic night",
        "week21-2b": "Pick up the extra shift",
    }
},
"week20-2b": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-2a": "Go to open mic night",
        "week21-2b": "Pick up the extra shift",
    }
},
"week21-2a": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-2a": "Go to dinner with classmates",
        "week22-2b": "Go to the lounge with roommates",
    }
},
"week21-2b": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-2a": "Go to dinner with classmates",
        "week22-2b": "Go to the lounge with roommates",
    }
},
"week22-2a": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23-2a": "Get pancakes",
        "week23-2b": "Go to volunteer fair",
    }
},
"week22-2b": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23-2a": "Get pancakes",
        "week23-2b": "Go to volunteer fair",
    }
},
"week23-2a": {
        "text": "You’ve gone out with this one person over the past month, you might really be starting to like them but now is time to make a decision. Valentine's day is almost here and you’re weighing out your options. You could ask them to be your VALENTINE, go further and ask them to be OFFICIAL, or NOT worry about it.",
        "choices": {
            "valentine": "Ask them to be your valentine",
            "official": "Ask them to be official",
            "not": "Don't worry about it",
    }
},
"week23-2b": {
        "text": "You’ve gone out with this one person over the past month, you might really be starting to like them but now is time to make a decision. Valentine's day is almost here and you’re weighing out your options. You could ask them to be your VALENTINE, go further and ask them to be OFFICIAL, or NOT worry about it.",
        "choices": {
            "valentine": "Ask them to be your valentine",
            "official": "Ask them to be official",
            "not": "Don't worry about it",
        }
},
    #MC 8
    "prove": {
    "text": "You had a restful and calm break! Now you're back in school and ready for the winter semester. You find out your new roommates are chill like that, kawabunga baby. They wanna hangout and go sledding but you need to get groceries. Do you choose to go HANGOUT with them or do you go out and get GROCERIES?",
    "choices": {
        "week18-3a": "Hang out with your roommates",
        "week18-3": "Go get groceries",
    }
},
"week18-3a": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-3a": "Study for classes",
        "week19-3b": "Go to the game night",
    }
},
"week18-3b": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-3a": "Study for classes",
        "week19-3b": "Go to the game night",
    }
},
"week19-3a": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-3a": "Go on the hike",
        "week20-3b": "Talk to your professors",
    }
},
"week19-3b": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-3a": "Go on the hike",
        "week20-3b": "Talk to your professors",
    }
},
"week20-3a": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-3a": "Go to open mic night",
        "week21-3b": "Pick up the extra shift",
    }
},
"week20-3b": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-3a": "Go to open mic night",
        "week21-3b": "Pick up the extra shift",
    }
},
"week21-3a": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-3a": "Go to dinner with classmates",
        "week22-3b": "Go to the lounge with roommates",
    }
},
"week21-3b": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-3a": "Go to dinner with classmates",
        "week22-3b": "Go to the lounge with roommates",
    }
},
"week22-3a": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23-3a": "Get pancakes",
        "week23-3b": "Go to volunteer fair",
    }
},
"week22-3b": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23-3a": "Get pancakes",
        "week23-3b": "Go to volunteer fair",
    }
},
"week23-3a": {
        "text": "Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend. The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night. You’ve been out with this person a handful of times and you’re starting to really like them, but you’re also stressed out with your homework. Do you go on the DATE, reschedule it so you can get help with your ASSIGNMENTS or take some time to relax and watch that new SHOW you started?",
        "choices": {
            "assignments": "Get help with your assignments",
            "date2": "Go on the date",
            "show": "Watch the new show you started",
        }
},
"week23-3b": {
        "text": "Another week of school and you’re back to it. However, there was some homework that you had some trouble with over the weekend. The department is having an open lab and homework help on Wednesday, but you have a date scheduled that night. You’ve been out with this person a handful of times and you’re starting to really like them, but you’re also stressed out with your homework. Do you go on the DATE, reschedule it so you can get help with your ASSIGNMENTS or take some time to relax and watch that new SHOW you started?",
        "choices": {
            "assignments": "Get help with your assignments",
            "date2": "Go on the date",
            "show": "Watch the new show you started",
        }
},
    #MC 9
    "back": {
    "text": "You had a restful and calm break! Now you're back in school and ready for the winter semester. You find out your new roommates are chill like that, kawabunga baby. They wanna hangout and go sledding but you need to get groceries. Do you choose to go HANGOUT with them or do you go out and get GROCERIES?",
    "choices": {
        "week18-4a": "Hang out with your roommates",
        "week18-4b": "Go get groceries",
    }
},
"week18-4a": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-4a": "Study for classes",
        "week19-4b": "Go to the game night",
    }
},
"week18-4b": {
    "text": """The winter semester is in full swing, and your routine is starting to settle in.
        The snow outside blankets the campus in a crisp, quiet beauty, but your schedule is anything but serene.
        This week, you have a decision to make. Your campus club is hosting a winter-themed game night on Friday,
        complete with board games, snacks, and plenty of laughter. It’s a chance to relax, connect with classmates, and maybe even show off your mad strategy skills.
        On the other hand, you’ve been eyeing the upcoming project in your toughest class,
        and you know dedicating some extra study hours this week could make a huge difference in your performance.
        Do you choose to STUDY or go to GAME NIGHT?""",
    "choices": {
        "week19-4a": "Study for classes",
        "week19-2b": "Go to the game night",
    }
},
"week19-4a": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-4a": "Go on the hike",
        "week20-4b": "Talk to your professors",
    }
},
"week19-4b": {
    "text": """It’s the beginning of February, and the winter semester is already picking up steam.
        Snow piles high on the sidewalks, and the icy breeze makes you bury your face deeper into your scarf as you head to class.
        By now, your schedule feels familiar, but there’s still plenty of time to make the most of the semester.
        This week, you’re torn between two options. The campus recreation center is organizing a winter hike this weekend.
        It’s the perfect chance to break out of your routine, marvel at the beauty of the frozen landscape, and maybe catch a sunset over the snow-capped hills.
        Your professors have opened office hours specifically to help students prepare for midterms.
        You’ve been feeling a little overwhelmed in your statistics class, and this might be your best opportunity to solidify your understanding before tests start looming.
        Do you choose to go on the HIKE or go to the OFFICE to talk with your professors?""",
    "choices": {
        "week20-4a": "Go on the hike",
        "week20-4b": "Talk to your professors",
    }
},
"week20-4a": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-4a": "Go to open mic night",
        "week21-4b": "Pick up the extra shift",
    }
},
"week20-4b": {
    "text": """It's mid-February, and the winter semester feels like it's been going on forever.
        The snow outside is relentless, piling up on the sidewalks and making every trip across campus an arctic expedition.
        Despite the chill, you've been managing to juggle classes, social life, and work fairly well.
        But this week, you're faced with a decision that could shape how your semester progresses.
        Your favorite club—the Creative Writing Society—is hosting an open mic night for students to share their work.
        It's a warm, cozy evening filled with poetry, short stories, and camaraderie. You know you'd enjoy the event,
        and it might even inspire some fresh ideas for your own writing projects.
        Your part-time job has offered an extra shift this week. The money would be helpful for that ski trip you've been dreaming of,
        but it means giving up your free time to stay late at the cafe and deal with the dinner rush.
        Do you choose to go to open MIC night or pick up up the extra SHIFT?""",
    "choices": {
        "week21-4a": "Go to open mic night",
        "week21-4b": "Pick up the extra shift",
    }
},
"week21-4a": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-4a": "Go to dinner with classmates",
        "week22-4b": "Go to the lounge with roommates",
    }
},
"week21-4b": {
    "text": """Classes are settling into a rhythm, but you’re looking for a break from the grind and a chance to connect with friends.
        Today, you’re faced with two enticing opportunities. A classmate invites you to join their study group for a casual dinner at a trendy downtown.
        It’s a chance to get to know people from your class better! But then Your roommate mentions a Mario Kart tournament in the lounge.
        It’s nothing serious—just a group of students coming together for lighthearted competition, snacks, and some laughs.
        Do you go to DINNER with your classmates or choose to stay with your roomamtes and go to the LOUNGE?""",
    "choices": {
        "week22-4a": "Go to dinner with classmates",
        "week22-4b": "Go to the lounge with roommates",
    }
},
"week22-4a": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23-4a": "Get pancakes",
        "week23-4b": "Go to volunteer fair",
    }
},
"week22-4b": {
    "text": """Life on campus is keeping you busy. With midterms on the horizon,
        you’re torn between sticking to your responsibilities or making room for some fun. Today,
        two intriguing opportunities come your way. Your apartment manager announces a surprise pancake night in the common room!
        It’s a chance to mingle with dormmates, enjoy some syrupy goodness, and take a break from the monotony of studying!
        But then your roomate lets you know that your campus is hosting a volunteer fair showcasing opportunities to get involved with community projects.
        Do you decide to get some PANCAKES at your apartment complex or would you like to go to the VOLUNTEER fair to give back to the community?""",
    "choices": {
        "week23-4a": "Get pancakes",
        "week23-4b": "Go to volunteer fair",
    }
},
"week23-4a": {
            "text": "You’re back at another week of school and things aren’t doing great. The weekend is coming up and you want to have some fun. You’re weighing out your options. You could ASK someone out on a date, watch some TV to decompress or attempt to baptize your CAR.",
        "choices": {
            "ask": "Ask someone on a date",
            "tv": "Watch tv to decompress",
            "car": "Baptize your car",
        }
    },
"week23-4b": {
            "text": "You’re back at another week of school and things aren’t doing great. The weekend is coming up and you want to have some fun. You’re weighing out your options. You could ASK someone out on a date, watch some TV to decompress or attempt to baptize your CAR.",
        "choices": {
            "ask": "Ask someone on a date",
            "tv": "Watch tv to decompress",
            "car": "Baptize your car",
        }
    },
    #MC 10
    "homework": {
        "text": "You want to keep up the good work and continue the grind! Although you wanted to go out, the help you got at the open lab was extremely helpful. You came out feeling much better about the course than you did earlier.",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
                are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
                or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
    "choices": {
        "week25-1a": "Saturday B-Dubs",
        "week25-1b": "BOGO Tuesday B-Dubs",
        }
    },
    "valentine": {
        "text": "You aren’t quite ready for the full commitment of a new relationship but you do really like this person. So you pull out some of the stops- flowers and chocolate. You have a valentine!",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
    "choices": {
        "week25-1a": "Saturday B-Dubs",
        "week25-1b": "BOGO Tuesday B-Dubs",
        }
    },
"week25-1a": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-1a": "Go camping",
        "week26-1b": "Stay home",
    }
},
"week25-1b": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-1a": "Go camping",
        "week26-1b": "Stay home",
    }
},
"week26-1a": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-1a": "Clean their dishes",
        "week27-1b": "Put their dishes on the bed",
    }
},
"week26-1b": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-1a": "Clean their dishes",
        "week27-1b": "Put their dishes on the bed",
    }
},
"week27-1a": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-1a": "Get ready for class",
        "week28-1b": "Sleep in",
    }
},
"week27-1b": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-1a": "Get ready for class",
        "week28-1b": "Sleep in",
    }
},
"week28-1a": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-1a": "Skip devotional",
        "week29-1b": "Go to devotional",
    }
},
"week28-1b": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-1a": "Skip devotional",
        "week29-1b": "Go to devotional",
    }
},
"week29-1a": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-1a": "Go to the party",
        "week30-1b": "Stay and watch Netflix",
    }
},
"week29-1b": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-1a": "Go to the party",
        "week30-1b": "Stay and watch Netflix",
    }
},
"week30-1a": {
    "text": """It’s finals week and you’ve made it so far! You’ve got lots of exams and almost no time. You’ve been seeing your lover over the last 
              couple of months and you know they could be the one. They ask to go out this week, but it happens to be a night you were going to study. 
              You know you’ve studied hard, you could afford one night off, right? Do you want to play it safe and study for FINALS or take your person out for 
              something SPECIAL?""",
    "choices": {
        "finals": "Study for finals",
        "special": "Take out your person",
    }
},
"week30-1b": {
    "text": """It’s finals week and you’ve made it so far! You’ve got lots of exams and almost no time. You’ve been seeing your lover over the last 
              couple of months and you know they could be the one. They ask to go out this week, but it happens to be a night you were going to study. 
              You know you’ve studied hard, you could afford one night off, right? Do you want to play it safe and study for FINALS or take your person out for 
              something SPECIAL?""",
    "choices": {
        "finals": "Study for finals",
        "special": "Take out your person",
    }
},
    #MC 11
    "date1": {
        "text": "How could you say no to a date? Things are going so well, you don’t want to jeopardize your relationship over some homework! The date goes great and you don’t even think twice about the missed lab.",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
        are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
        or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
        "choices": {
            "week25-2a": "Saturday B-Dubs",
            "week25-2b": "BOGO Tuesday B-Dubs",
        }
    },
    "official": {
        "text": "This person makes you happy! You decide it’s time to make things official with them. You pull out all the stops- flowers, chocolates and a handwritten note. When you prompted the question, it was obvious the feelings were mutual. Congrats!! You feel like the luckiest person in the world.",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
    "choices": {
        "week25-2a": "Saturday B-Dubs",
        "week25-2b": "BOGO Tuesday B-Dubs",
        }
    },
    "assignments": {
        "text": "You felt the need to keep the promise you made with yourself. You felt a desire– petty or not– to prove everyone wrong and that you could do this. Although you wanted to go out, the help you got at the open lab was extremely helpful. You came out feeling much better about the course than you did earlier.",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
        are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
        or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
    "choices": {
        "week25-2a": "Saturday B-Dubs",
        "week25-2b": "BOGO Tuesday B-Dubs",
    }
    },
    "week24-2a": {
    "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
    "choices": {
        "week25-2a": "Saturday B-Dubs",
        "week25-2b": "BOGO Tuesday B-Dubs",
    }
},
"week24-2b": {
    "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
    "choices": {
        "week25-2a": "Saturday B-Dubs",
        "week25-2b": "BOGO Tuesday B-Dubs",
    }
},
"week25-2a": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-2a": "Go camping",
        "week26-2b": "Stay home",
    }
},
"week25-2b": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-2a": "Go camping",
        "week26-2b": "Stay home",
    }
},
"week26-2a": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-2a": "Clean their dishes",
        "week27-2b": "Put their dishes on the bed",
    }
},
"week26-2b": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-2a": "Clean their dishes",
        "week27-2b": "Put their dishes on the bed",
    }
},
"week27-2a": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-2a": "Get ready for class",
        "week28-2b": "Sleep in",
    }
},
"week27-2b": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-2a": "Get ready for class",
        "week28-2b": "Sleep in",
    }
},
"week28-2a": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-2a": "Skip devotional",
        "week29-2b": "Go to devotional",
    }
},
"week28-2b": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-2a": "Skip devotional",
        "week29-2b": "Go to devotional",
    }
},
"week29-2a": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-2a": "Go to the party",
        "week30-2b": "Stay and watch Netflix",
    }
},
"week29-2b": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-2a": "Go to the party",
        "week30-2b": "Stay and watch Netflix",
    }
},
"week30-2a": {
    "text": """It’s finals week and you’ve made it so far! You’ve been seriously dating someone over the last couple of months and you know a big decision 
            is coming up. This week you’ve got lots of exams and almost no time; you are stressed out to the max. You have the choice to study for FINALS, take your lover 
            out for something SPECIAL, or hit pause and go out for some FUN with your friends. What will it be?""",
    "choices": {
        "finals": "Study for finals",
        "special": "Take out your person",
        "fun": "Go out with friends",
    }
},
"week30-2b": {
    "text": """It’s finals week and you’ve made it so far! You’ve been seriously dating someone over the last couple of months and you know a big decision 
            is coming up. This week you’ve got lots of exams and almost no time; you are stressed out to the max. You have the choice to study for FINALS, take your lover 
            out for something SPECIAL, or hit pause and go out for some FUN with your friends. What will it be?""",
    "choices": {
        "finals": "Study for finals",
        "special": "Take out your person",
        "fun": "Go out with friends",
    }
},
    #MC 12
    "not": {
        "text": "You don’t feel worried about asking them to be your valentine because it didn’t feel that serious to you. It was just a little holiday so did it really matter?",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
        "choices": {
            "week25-3a": "Saturday B-Dubs",
            "week25-3b": "BOGO Tuesday B-Dubs",
        }
    },
    "date2": {
        "text": "How could you say no to a date? Things are going so well, you don’t want to jeopardize your relationship over some homework! You remembered the promise you made to yourself, but you also want things to look forward to. The date goes great and you don’t even think twice about the missed lab. You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown in fear of a commitment?",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
        "choices": {
        "week25-3a": "Saturday B-Dubs",
        "week25-3b": "BOGO Tuesday B-Dubs",
        }
    },
    "ask": {
        "text": "A date sounds like the best option! You’ve been seeing this one person for some time now and you want to continue to pursue a relationship with them. Although you weren’t excited to come back to school, things might actually start to be looking up, in at least one aspect. You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown in fear of a commitment?",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
        "choices": {
        "week25-3a": "Saturday B-Dubs",
        "week25-3b": "BOGO Tuesday B-Dubs",
        }
    },
"week25-3a": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-3a": "Go camping",
        "week26-3b": "Stay home",
    }
},
"week25-3b": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-3a": "Go camping",
        "week26-3b": "Stay home",
    }
},
"week26-3a": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-3a": "Clean their dishes",
        "week27-3b": "Put their dishes on the bed",
    }
},
"week26-3b": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-3a": "Clean their dishes",
        "week27-3b": "Put their dishes on the bed",
    }
},
"week27-3a": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-3a": "Get ready for class",
        "week28-3b": "Sleep in",
    }
},
"week27-3b": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-3a": "Get ready for class",
        "week28-3b": "Sleep in",
    }
},
"week28-3a": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-3a": "Skip devotional",
        "week29-3b": "Go to devotional",
    }
},
"week28-3b": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-3a": "Skip devotional",
        "week29-3b": "Go to devotional",
    }
},
"week29-3a": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-3a": "Go to the party",
        "week30-3b": "Stay and watch Netflix",
    }
},
"week29-3b": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-3a": "Go to the party",
        "week30-3b": "Stay and watch Netflix",
    }
},
"week30-3a": {
    "text": """You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to 
              the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown 
              in fear of a commitment?""",
    "choices": {
        "gardens": "Go to the gardens",
        "hide": "Hide in your apartment",
        "escape": "Escape back home",
    }
},
"week30-3b": {
    "text": """You have one more opportunity for a date, this could be the start of something new or the end of something great. Your lover has asked to go to 
              the gardens tonight. You know what could be at the end of this road. Do you go to the GARDENS, HIDE in your apartment or ESCAPE back to your hometown 
              in fear of a commitment?""",
    "choices": {
        "gardens": "Go to the gardens",
        "hide": "Hide in your apartment",
        "escape": "Escape back home",
    }
},
    #MC 13
    "show": {
        "text": "It was hard finding time for yourself so you decided to take a breather. You feel it would benefit you most to hit pause. The homework and date could wait, right? Well unfortunately, the date couldn’t. They felt like a last priority and called things off. Yikes, that didn’t go how you pictured. You’re back at another week of school and things aren’t doing great. Maybe your family was right after all. Is it even worth it to try if you know you’re going to fail? Do you want to attempt your EXAMS, give in to your family by dropping OUT of school, or ignore it all and go for an emotional late night DRIVE?",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
        "choices": {
        "week25-4a": "Saturday B-Dubs",
        "week25-4b": "BOGO Tuesday B-Dubs",
        }
    },
    "tv": {
        "text": "You wanted to have fun and relax, not push your limits emotionally or physically. You switch on your comfort show: The Bachelor. Your mind rests as the girls fight over the guy- you laugh at seemingly annoying comments and shout at the one girl that loves to cause drama. You’re back at another week of school and things aren’t doing great. Maybe your family was right after all. Is it even worth it to try if you know you’re going to fail? Do you want to attempt your EXAMS, give in to your family by dropping OUT of school, or ignore it all and go for an emotional late night DRIVE?",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
        "choices": {
        "week25-4a": "Saturday B-Dubs",
        "week25-4b": "BOGO Tuesday B-Dubs",
        }
    },
"week25-4a": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-4a": "Go camping",
        "week26-4b": "Stay home",
    }
},
"week25-4b": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-4a": "Go camping",
        "week26-4b": "Stay home",
    }
},
"week26-4a": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-4a": "Clean their dishes",
        "week27-4b": "Put their dishes on the bed",
    }
},
"week26-4b": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-4a": "Clean their dishes",
        "week27-4b": "Put their dishes on the bed",
    }
},
"week27-4a": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-4a": "Get ready for class",
        "week28-4b": "Sleep in",
    }
},
"week27-4b": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-4a": "Get ready for class",
        "week28-4b": "Sleep in",
    }
},
"week28-4a": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-4a": "Skip devotional",
        "week29-4b": "Go to devotional",
    }
},
"week28-4b": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-4a": "Skip devotional",
        "week29-4b": "Go to devotional",
    }
},
"week29-4a": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-4a": "Go to the party",
        "week30-4b": "Stay and watch Netflix",
    }
},
"week29-4b": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-4a": "Go to the party",
        "week30-4b": "Stay and watch Netflix",
    }
},
"week30-4a": {
    "text": """You’re back at another week of school and things aren’t doing great. Maybe your family was right after all. Is it even worth it to try if you know you’re 
            going to fail? Do you want to attempt your EXAMS, give in to your family by dropping OUT of school, or ignore it all and go for a late night DRIVE?""",
    "choices": {
        "exams": "Attempt your exams",
        "out": "Drop out of school",
        "drive": "Go for a late night drive",
    }
},
"week30-4b": {
    "text": """You’re back at another week of school and things aren’t doing great. Maybe your family was right after all. Is it even worth it to try if you know you’re 
            going to fail? Do you want to attempt your EXAMS, give in to your family by dropping OUT of school, or ignore it all and go for a late night DRIVE?""",
    "choices": {
        "exams": "Attempt your exams",
        "out": "Drop out of school",
        "drive": "Go for a late night drive",
    }
},
    #MC 14
    "car": {
        "text": "You decide you want to try and baptize your car, how hard could it be? You hop in your car and drive onto the freeway. You grab your steering wheel tightly and drive a few miles before building up the courage to press the gas pedal to the floor. You’re driving fast, cruising, adrenaline is rushing through you.",
        "text": """Your bank account is looking pretty sad these days, but your roommates are going to Buffalo Wild Wings. Those wings
       are calling your name. It's Saturday so there's no deals going on. Do you hope for a money miracle, and go to to B Dubs with the gang
       or do you SUGGEST going on Tuesday instead for the BOGO wings?""",
        "choices": {
        "week25-5a": "Saturday B-Dubs",
        "week25-5b": "BOGO Tuesday B-Dubs",
        }
},
"week25-5a": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-5a": "Go camping",
        "week26-5b": "Stay home",
    }
},
"week25-5b": {
    "text": "Some of your buddies are going camping this weekend. You have a bit more homework than usual this week but camping in Yellowstone sounds like a blast. Do you go CAMPING or do you STAY home?",
    "choices": {
        "week26-5a": "Go camping",
        "week26-5b": "Stay home",
    }
},
"week26-5a": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-5a": "Clean their dishes",
        "week27-5b": "Put their dishes on the bed",
    }
},
"week26-5b": {
    "text": "Your roommate has been slacking off on dishes all semester. The sink is filled with what seems like their whole shelf. Do you CLEAN their dishes once again hoping it's the last time, or do you SNAP and put their soggy dishes on their bed?",
    "choices": {
        "week27-5a": "Clean their dishes",
        "week27-5b": "Put their dishes on the bed",
    }
},
"week27-5a": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-5a": "Get ready for class",
        "week28-5b": "Sleep in",
    }
},
"week27-5b": {
    "text": """You stayed up way too late last night watching Netflix. You wake up and check your phone, it's 5 minutes past
           the start of your first class. If it were any other class you would easily just go back to bed, but this professor counts
           attendance for a grade. You could RUSH and get ready for class and be 20 minutes late, or you could SLEEP in and make
           up some lame excuse later.""",
    "choices": {
        "week28-5a": "Get ready for class",
        "week28-5b": "Sleep in",
    }
},
"week28-5a": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-5a": "Skip devotional",
        "week29-5b": "Go to devotional",
    }
},
"week28-5b": {
    "text": "These last weeks have been rough. College is no joke. You’re feeling swamped with all your homework and studies. So much so you need all the time you can get to get them done. Including that one hour of devotional time… Do you SKIP devo and work on homework or do you GO and enjoy that spiritual feast?",
    "choices": {
        "week29-5a": "Skip devotional",
        "week29-5b": "Go to devotional",
    }
},
"week29-5a": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-5a": "Go to the party",
        "week30-5b": "Stay and watch Netflix",
    }
},
"week29-5b": {
    "text": """It's so close to the end of the semester and you just finished up homework and studying for the night. You head to the kitchen to
       get yourself a rewarding snack when you see a flyer on the fridge. “End of Semester Party at the Cove” it says. Do you go to the PARTY with some of your roommates or do you stay and enjoy your snacks and NETFLIX? """,
    "choices": {
        "week30-5a": "Go to the party",
        "week30-5b": "Stay and watch Netflix",
    }
},
"week30-5a": {
    "text": "It's the end of the semester, and you have had enough of school so you decide to go for another late night drive. As you drive, You're at 90, 95, and just like that you've hit 100mph. You smile and shout out in pure excitement. How fast could you push it? Just as you’re about to push the pedal further, you see sirens flash in your rearview mirror. You mutter under your breath as you weigh out your options. Do you PULL over or try to RUN away?",
    "choices": {
        "pull": "Pull over",
        "run": "Try to run away",
    }
},
"week30-5b": {
    "text": "It's the end of the semester, and you have had enough of school so you decide to go for another late night drive. As you drive, You're at 90, 95, and just like that you've hit 100mph. You smile and shout out in pure excitement. How fast could you push it? Just as you’re about to push the pedal further, you see sirens flash in your rearview mirror. You mutter under your breath as you weigh out your options. Do you PULL over or try to RUN away?",
    "choices": {
        "pull": "Pull over",
        "run": "Try to run away",
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