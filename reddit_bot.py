import praw
import config
import time

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Executeyytest's bot comment responder v0.1")

    return r

def run_bot(r, comments_replied_to):
    print("Obtaining 10 comments...")
    for comment in r.subreddit('test').comments(limit=10):
        if "bot" in comment.body and comment.id not in comments_replied_to and comment.author!= r.user.me():
            print ("String with \"bot\" found!! in comment " + comment.id)
            #comment.reply("I love robots!! [Here](https://i.imgur.com/k4i5SOR.png) is a photo of one.")
            print ("Replied to comment" + comment.id)

            comments_replied_to.append(comment.id)

    print("Sleep for 10 seconds")
    time.sleep(10)

def get_saved_comments():
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")

r = bot_login()
comments_replied_to = []

while True:
    run_bot(r, comments_replied_to)