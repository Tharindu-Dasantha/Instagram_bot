from instagrapi import Client
import random

username = input('Username: ')
password = input('Password: ')

client = Client()
client.login(username, password)

hashtag = input('Hashtag: ')
if not hashtag:
    hashtags = ["programming", "trending", "hot", "development", "production", "finance"]
    hashtag = random.choice(hashtags)
comments = ["Awsome","Great", "Nice", "Wonderful", "Amazing", "Lovely", "😎", "🥳", "😶‍🌫️", "🥹", "😁", "😍", "🥰", "😘", "🥸", "🙃", "Great", "😽", "🙀", "❤️", "💞"]

medias = client.hashtag_medias_recent(hashtag, 20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post number {i + 1} of hashing {hashtag}")
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"Followed user {media.user.username}")
        client.media_comment(media.id, "Awsome post")
        comment = random.choice(comments)
        print(f"Commented {comment} under post number {i+1}")