from instabot import Bot
bot = Bot()
bot.login(username="enter username" , password = "enter password")


#upload the photo
bot.upload_photo("enter full path" , caption="write caption") #caption is optional

# follow your favourite person :)
bot.follow('enter username')
# unfollow who you dont like :)
bot.unfollow('enter username')

# enter username and messages will be sent automaticallys
bot.send_message("hello python lover" , ['username' , 'username' , 'username'])

# get a list of your followers
followers=bot.get_user_followers("username")
for i in followers:
    print(bot.get_user_info(i))


# get a list of  people in your following list 
following=bot.get_user_following("username")
for j in following:
    print(bot.get_user_following(j))