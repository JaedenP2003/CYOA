from flask import Flask, render_template

app = Flask(__name__)

# Dictionary containing the game's story paths
story = {
    "start": {
        "text": "Welcome to BYU-I! It's your first semester, and your roommates invite you to 'First Friday.' Do you ACCEPT or DECLINE?",
        "choices": {
            "accept": "Go to First Friday",
            "decline": "Stay home and settle in"
        }
    },
    "accept": {
        "text": "You meet great people at First Friday! Monday arrives, and a class is harder than expected. Do you STICK with it or DROP it?",
        "choices": {
            "stick": "Stick with the class",
            "drop": "Drop the class"
        }
    },
    "decline": {
        "text": "You stay home but feel left out. Monday arrives, and a class is harder than expected. Do you STICK with it or DROP it?",
        "choices": {
            "stick": "Stick with the class",
            "drop": "Drop the class"
        }
    },
    "stick": {
        "text": "Your commitment pays off! You need groceries. Do you SHOP locally or DRIVE to Costco?",
        "choices": {
            "shop": "Shop in town",
            "drive": "Drive to Idaho Falls"
        }
    },
    "drop": {
        "text": "You free up time, but question your decision. You need groceries. Do you SHOP locally or DRIVE to Costco?",
        "choices": {
            "shop": "Shop in town",
            "drive": "Drive to Idaho Falls"
        }
    },
    "shop": {
        "text": "You find what you need, but prices are high. Do you VISIT the DUNES or HIKE the MOUNTAIN?",
        "choices": {
            "dunes": "Go to the dunes",
            "mountain": "Hike R Mountain"
        }
    },
    "drive": {
        "text": "You save money but spend time driving. Do you VISIT the DUNES or HIKE the MOUNTAIN?",
        "choices": {
            "dunes": "Go to the dunes",
            "mountain": "Hike R Mountain"
        }
    },
    "dunes": {
        "text": "You enjoy the dunes! Later, you're invited to a study group. Do you JOIN or SKIP?",
        "choices": {
            "join": "Join the study group",
            "skip": "Skip and relax"
        }
    },
    "mountain": {
        "text": "You conquer the mountain! Later, you're invited to a study group. Do you JOIN or SKIP?",
        "choices": {
            "join": "Join the study group",
            "skip": "Skip and relax"
        }
    },
    "join": {
        "text": "Your grades improve, and you meet new friends. One night, you can STUDY for a test or go to a PARTY. What do you do?",
        "choices": {
            "study": "Study hard",
            "party": "Party and have fun"
        }
    },
    "skip": {
        "text": "You relax but struggle in class. One night, you can STUDY for a test or go to a PARTY. What do you do?",
        "choices": {
            "study": "Study hard",
            "party": "Party and have fun"
        }
    },
    "study": {
        "text": "You ace the test! Later, a career fair comes up. Do you ATTEND or SKIP?",
        "choices": {
            "attend": "Attend the career fair",
            "skip_fair": "Skip the fair"
        }
    },
    "party": {
        "text": "You have fun, but your grades slip. Later, a career fair comes up. Do you ATTEND or SKIP?",
        "choices": {
            "attend": "Attend the career fair",
            "skip_fair": "Skip the fair"
        }
    },
    "attend": {
        "text": "You network well and land an internship! Congratulations, you reached ENDING #1!",
        "choices": {}
    },
    "skip_fair": {
        "text": "You miss a great opportunity, but enjoy college life. You reached ENDING #2.",
        "choices": {}
    }
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