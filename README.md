What is this: 
    This is a instagram bot which we can use to like posts base on hashtags and follow people who are also interested in that kind of stuff.
    It is a great way to grow your community without getting tired

How to start: 
    clone the code into a codespace and run the code using a terminal window.
    how to do it in git-bash:
        type python main.py  
        then enter the username and password when prompted (this does not keep a data base or save your password so you need to enter the password everytime for safty reasons)
        then if you have a hashtag that you need to enter type it out else a random hashtag will be used.
    
How the app works: 
    line 4 & 5 => taking inputs to log into the instagram account
    line 7 & 8 => loginto the instagram account using the credentials you have inputted
    line 10 - 14 => getting a hashvalue (if not given assingn a random hashtag) and comments to write.
    line 16 => how many recent posts did the bot like at once and how the post is picked up most viewed or recent.
    line 18 and so forth => take each media and like each post untill it reach the number of maximum posts and make a comment