import tweepy
import tkinter
import time
from credentials import *
from tkinter import *
import sys


def get_userdetails():
    #craw data
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        user = api.me()
        print("\033[1;37;40m ==========Login========== \n")
        print(  "Authentication Success "+user.name)
        print("")
        print("\033[1;37;40m ==========Deskripsi==========\n")
        print(  user.description)
        print("")
        print("\033[1;37;40m ==========Location==========\n")
        print(  user.location)
        print("")
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Login========== \n")
        print(e.response)

    return api

def get_lab2():
    return m2.get()
def keluar():
    print("\033[1;31;40m ==========Exiting Session========== \n")
    return exit()

def get_lab3():
    return m3.get()


def get_labd4():
    return m4.get()


def get_labd5():
    return m5.get()

def get_labd6():
    return m6.get()

def getExceptionMessage(msg):
    words = msg.split(' ')

    errorMsg = ""
    for index, word in enumerate(words):
        if index not in [0,1,2]:
            errorMsg = errorMsg + ' ' + word
    errorMsg = errorMsg.rstrip("\'}]")
    errorMsg = errorMsg.lstrip(" \'")
    return errorMsg
#SESSION 1
def spamUser():
    try:
        api = get_userdetails()
        no = get_labd5()
        for i in range(int(no)):

            tweetId = get_lab2()
            username = get_lab3()
            api.update_status("@" + username + " " + get_labd4()+ " " +str(i),
                            in_reply_to_status_id=tweetId)
            print("\033[1;35;40m ==========Active==========")
            print("Reply send : " + get_labd4()+" " + str(i))
            time.sleep(2)
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Error==========")
        print (e.api_code)
        print (getExceptionMessage(e.reason))
        print("\033[1;31;40m ==========Waiting==========")
        for i in range(7500,0,-1):
            print(f"{i}", end="\r", flush=True)
            time.sleep(1)
        print("\033[1;31;40m ==========Back to Reply==========")
        return spambaru()
#SESSION 2
def spambaru():
    try:
        api = get_userdetails()
        no = get_labd5()
        for i in range(int(no)):

            tweetId = get_lab2()
            username = get_lab3()
            api.update_status("@" + username + " " + get_labd4()+ " " +" " +str(i),
                            in_reply_to_status_id=tweetId)
            print("\033[1;35;40m ==========Active==========")
            print("Reply send : " + get_labd4()+" " + str(i))
            time.sleep(2)
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Error==========")
        print (e.api_code)
        print (getExceptionMessage(e.reason))
        print("\033[1;31;40m ==========Waiting==========")
        for i in range(10900,0,-1):
            print(f"{i}", end="\r", flush=True)
            time.sleep(1)
        print("\033[1;31;40m ==========Back to Reply==========")
        return spambaru1()
#SESSION 3
def spambaru1():
    try:
        api = get_userdetails()
        no = get_labd5()
        for i in range(int(no)):

            tweetId = get_lab2()
            username = get_lab3()
            api.update_status("@" + username + " " + get_labd4()+ " " +"*" +str(i),
                            in_reply_to_status_id=tweetId)
            print("\033[1;35;40m ==========Active==========")
            print("Reply send : " + get_labd4()+" " + str(i))
            time.sleep(2)
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Error==========")
        print (e.api_code)
        print (getExceptionMessage(e.reason))
        print("\033[1;31;40m ==========Waiting==========")
        for i in range(10900,0,-1):
            print(f"{i}", end="\r", flush=True)
            time.sleep(1)
        print("\033[1;31;40m ==========Back to Reply==========")
        return spambaru2()
#SESSION 4
def spambaru2():
    try:
        api = get_userdetails()
        no = get_labd5()
        for i in range(int(no)):

            tweetId = get_lab2()
            username = get_lab3()
            api.update_status("@" + username + " " + get_labd4()+ " " +"-" +str(i),
                            in_reply_to_status_id=tweetId)
            print("\033[1;35;40m ==========Active==========")
            print("Reply send : " + get_labd4()+" " + str(i))
            time.sleep(1)
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Error==========")
        print (e.api_code)
        print (getExceptionMessage(e.reason))
        print("\033[1;31;40m ==========Waiting==========")
        for i in range(10900,0,-1):
            print(f"{i}", end="\r", flush=True)
            time.sleep(1)
        print("\033[1;31;40m ==========Back to Reply==========")
        return spambaru3()
#SESSION 5
def spambaru3():
    try:
        api = get_userdetails()
        no = get_labd5()
        for i in range(int(no)):

            tweetId = get_lab2()
            username = get_lab3()
            api.update_status("@" + username + " " + get_labd4()+ " " +"--" +str(i),
                            in_reply_to_status_id=tweetId)
            print("\033[1;35;40m ==========Active==========")
            print("Reply send : " + get_labd4()+" " + str(i))
            time.sleep(1)
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Error==========")
        print (e.api_code)
        print (getExceptionMessage(e.reason))
        print("\033[1;31;40m ==========Waiting==========")
        for i in range(10950,0,-1):
            print(f"{i}", end="\r", flush=True)
            time.sleep(1)
        print("\033[1;31;40m ==========Back to Reply==========")
        return spambaru4()
#SESSION 6
def spambaru4():
    try:
        api = get_userdetails()
        no = get_labd5()
        for i in range(int(no)):

            tweetId = get_lab2()
            username = get_lab3()
            api.update_status("@" + username + " " + get_labd4()+ " " +"." +str(i),
                            in_reply_to_status_id=tweetId)
            print("\033[1;35;40m ==========Active==========")
            print("Reply send : " + get_labd4()+" " + str(i))
            time.sleep(2)
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Error==========")
        print (e.api_code)
        print (getExceptionMessage(e.reason))
        print("\033[1;31;40m ==========Waiting==========")
        for i in range(10980,0,-1):
            print(f"{i}", end="\r", flush=True)
            time.sleep(1)
        print("\033[1;31;40m ==========Back to Reply==========")
        return spambaru5()
#SESSION 7
def spambaru5():
    try:
        api = get_userdetails()
        no = get_labd5()
        for i in range(int(no)):

            tweetId = get_lab2()
            username = get_lab3()
            api.update_status("@" + username + " " + get_labd4()+ " " +".." +str(i),
                            in_reply_to_status_id=tweetId)
            print("\033[1;35;40m ==========Active==========")
            print("Reply send : " + get_labd4()+" " + str(i))
            time.sleep(1)
    except tweepy.TweepError as e:
        print("\033[1;31;40m ==========Error==========")
        print (e.api_code)
        print (getExceptionMessage(e.reason))
        print("\033[1;31;40m ==========Waiting==========")
        for i in range(10980,0,-1):
            print(f"{i}", end="\r", flush=True)
            time.sleep(1)
        print("\033[1;31;40m ==========Back to Reply==========")
        return spambaru1()
root = Tk()
root.title('Tweet Bot by Paul')

submit = Button(root, text="Get User", command=get_userdetails)
submit.pack()


lab1 = Label(root, text="Tweet nyepamna")
lab1.pack()

lab2 = Label(root, text="tweetId", fg = "blue" ,font ="Times")
lab2.pack()
m2 = Entry(root, bd=5,font = "Times 20 bold italic",fg = "blue")
m2.pack()

lab3 = Label(root, text="user name without @", fg = "blue" ,font ="Times")
lab3.pack()
m3 = Entry(root, bd=5,font = "Times 20 bold italic",fg = "blue")
m3.pack()

lab4 = Label(root, text="Isi Spam Pesan", fg = "blue" ,font ="Times")
lab4.pack()
m4 = Entry(root, bd=5, font = "Times 15")
m4.pack(ipadx=200, ipady=20)

lab5 = Label(root, text="Berapa banyak nyepamnya")
lab5.pack()
m5 = Entry(root, bd=5,)
m5.pack()
lab6 = Label(root, text="rentang reply")
lab6.pack()
m6 = Entry(root, bd=5,)
m6.pack()

submit = Button(root, text="Meluncur", command=spamUser)
submit.pack(side=BOTTOM)
submit = Button(root, text="keluar", command=keluar)
submit.pack()
root.mainloop()
