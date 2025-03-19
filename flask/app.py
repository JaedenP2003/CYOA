from flask import Flask, render_template, request

app = Flask(__name__)

# Story dictionary
story = {
    "start": {
        "text": "Welcome to BYU-I! It's your first semester, and you're excited to meet your roommates at Centre Square. They invite you to go to 'First Friday,' a fun event for freshmen. Do you ACCEPT the invite or DECLINE?",
        "choices": {
            "accept": "Go with your roommates to First Friday",
            "decline": "Stay home and settle in"
        }
    },
    "accept": {
        "text": "You go with your roommates and build relationships with them. Now, it's Monday, and classes begin. Your last class is more work than expected but could be beneficial. Do you STICK with it or DROP the class?",
        "choices": {
            "stick": "Stick with the challenging class",
            "drop": "Drop the class and focus on others"
        }
    },
    "decline": {
        "text": "You stay home but feel a little regretful for missing out. Monday arrives, and your last class is tougher than expected. Do you STICK with it or DROP the class?",
        "choices": {
            "stick": "Stick with the challenging class",
            "drop": "Drop the class and focus on others"
        }
    },
    "stick": {
        "text": "You decide to challenge yourself and stick with the class. Week 2 arrives, and you need groceries. Do you STAY in town and shop or DRIVE to Idaho Falls for bulk shopping?",
        "choices": {
            "stay": "Shop in town at Walmart",
            "drive": "Drive to Idaho Falls for Costco shopping"
        }
    },
    "drop": {
        "text": "You drop the class, feeling relieved but wondering if it was the right decision. Now, you need groceries. Do you STAY in town or DRIVE to Idaho Falls?",
        "choices": {
            "stay": "Shop in town at Walmart",
            "drive": "Drive to Idaho Falls for Costco shopping"
        }
    },
    "stay": {
        "text": "You get your groceries easily, though they cost a bit more. Week 3 arrives, and you want to explore. Do you visit the SAND DUNES or hike R MOUNTAIN?",
        "choices": {
            "dunes": "Visit the sand dunes",
            "mountain": "Hike R Mountain"
        }
    },
    "drive": {
        "text": "You save money by shopping at Costco but spend time driving. Week 3 arrives, and you want to explore. Do you visit the SAND DUNES or hike R MOUNTAIN?",
        "choices": {
            "dunes": "Visit the sand dunes",
            "mountain": "Hike R Mountain"
        }
    },
    "dunes": {
        "text": "You enjoy the dunes, making great memories with friends. The end!",
        "choices": {}
    },
    "mountain": {
        "text": "You conquer R Mountain, feeling accomplished. The end!",
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
