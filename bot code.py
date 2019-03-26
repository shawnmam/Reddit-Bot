import praw
import time
import os
import requests

def bot_authentication():

    print("Authenticating ...")

    reddit = praw.Reddit(username =
                         password =
                         client_id =
                         client_secret =
                         user_agent =)


    print("Authenticated as {user}".format(user= reddit.user.me()))

    return reddit



def run_bot(reddit, comments_replied_to):
    print('Obtaining 25 comments...')
    for comment in reddit.subreddit('test').comments(limit=25):
        if '!joke' in comment.body and comment.id not in comments_replied_to and comment.author != reddit.user.me():
            print('String found with {string} found in comment {comment_id}'.format(string='!joke',comment_id= comment.id ))

            comment_reply = "You requested a Chuck Norris joke! Here it is: \n\n"
            joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']

            comment_reply += '>' + joke

            comment_reply += '\n\nThis joke came from [ICNDB.com](http://icndb.com).'

            comment.reply(comment_reply)

            print('Replied to comment {comment_id}'.format(comment_id= comment.id))

            comments_replied_to.append(comment.id)

            with open("comments_replied_to_txt.txt","r") as f:
                 f.write(comment.id + '\n')

    print('Sleeping for 10 seconds...')
    # Sleep  for 10 seconds...
    time.sleep(10)




def get_saved_comments():
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt','r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = filter(None,comments_replied_to)


    return comments_replied_to



def main():
    run = bot_authentication()
    comments_replied_to = get_saved_comments()

    while True:
        run_bot(run, comments_replied_to)


if __name__ == '__main__':
    main()

