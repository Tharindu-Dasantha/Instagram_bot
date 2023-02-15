from instagrapi import Client
import random
import sys

accounts = {}
# getting the number of users
try:
    user_amount = int(input("number of users: "))
except:
    print("invalid input set the value to 1")
    user_amount = 1
    
for _ in range(1): # change here for user_amount
    # add users to a dictionary
    user_name = input('Username: ')
    pw = input('Password: ')
    accounts[user_name] = pw

# making hashtags
try:
    hashamount = int(input("How many hashtags: "))
except:
    print("Please fill up the hash amount with a number")
    sys.exit(1)

hashtags = []    
for _ in range(hashamount):
    try:
        hash_tag = input("Hashtag: ")
        hashtags.append(hash_tag)
    except:
        pass
    
# getting comments from the users
try:
    commt_amount = int(input("How many comments: "))
except:
    print("Please fill up the comment amount with a number")
    sys.exit(1)
    
comments = []    
for _ in range(commt_amount):
    # getting comments from the user
    try:
        commented = input("Comment: ")
        comments.append(commented)
    except:
        pass

# getting how many clients he need to comment on
try:
    com_num = int(input("How many comments to make: "))
except:
    print("Invalid input changed to 10")
    com_num = 10
    
         

usernames = accounts.keys()
for user in usernames:
    # taking the username and password
    username = user
    password = accounts[user]
    
    # logging into a instagram account using the given username and password
    client = Client()
    client.login(username, password)

    hashtag = random.choice(hashtags)

    medias = client.hashtag_medias_recent(hashtag, 2) # change this later too

    for i, media in enumerate(medias):
        # liking the post
        client.media_like(media.id)
        print(f"Liked post number {i + 1} of hashing {hashtag}")
        # following the post
        client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username}")
        # commenting the post
        comment = random.choice(comments)
        client.media_comment(media.id, comment)
        print(f"Commented {comment} under post number {i+1}")
        
    # logout from the user
    client.logout()