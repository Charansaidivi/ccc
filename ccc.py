from plyer import notification
import time
status=input("Enter Your Status(📢Remainder / 🔔Notification):")
name=input("Enter Your Name:")
def get_time():
    hour=int(input("⏳Enter today's working time⌚ in hours:"))
    m=int(input("⏳Enter today's working time⌚ in minute:"))
    return hour*3600+m*60
if __name__ == '__main__':
    s=status.lower()
    if(s=='remainder'):
        print("🙂👋HELLO 🖥PR0GRAMMER🖥")
        print("❤THIS WILL HELPS YOU TO SET 📢REMAINDER📢 ❤")
        t=get_time()
        notification.notify(title="**😊HELLO {0} 😊**".format(name),
                            message="*I Will 📢Remaind📢 your work As Per Given⌚ Time ⌚",
                            app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\smile.ico",
                            timeout=15)
        remainder=input("Enter Your 📢Remainder📢:")
        print("Minimize screen after giving valid details:")
        time.sleep(t)
        notification.notify(
            title='📢 ....'+remainder+'....📢',
            message="You Should Go Through Your Remainder That This Is The Time To Have "+remainder+"\nGo With It "+name+'!!!',
            app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\REAMINDER.ico",
            timeout=20)
    elif(s=='notification'):
        profession=input("Enter Your Current Profession(Working/Studying)")
        S1=profession.lower()
        if(S1=='studying'):
            print("🙂👋HELLO 🖥PR0GRAMMER🖥")
            print("❤THIS WILL HELPS YOU A LOT FOR BETTER FOCUS ON STUDIES❤")
            t=int(input("⏳Enter Today's Working Time⌚ In Hours:"))
            print("Minimize Screen After Giving Valid Details:")
            notification.notify(title="**😊HELLO {0} 😊**".format(name),message="*Let you Start The Work\n*Give Require Details",
                                app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\smile.ico",
                                timeout=15)
            t2=50*60
            b=10*60
            c=0
            while True:
                time.sleep(t2)
                notification.notify(
                    title="🔔TAKE A SMALL BREAK🔔 ",
                    message=" Please Take a Small Break To Improve Your Concetration {0} ".format(name),
                    app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\b.ico",
                    timeout=15)
                c=c+1
                time.sleep(b)
                notification.notify(
                    title="🔔🔔🔔Start work {0}🔔🔔🔔".format(name),
                    message="It's Time To Get Back To Work!\nStart Your Focused Work Session Now.\nDon't 📵Use Mobile📵 During Work",
                    app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\work.ico",
                    timeout=15)
                if(c==t):
                    notification.notify(title="✅✅COMPLETED✅✅",
                                        message="⏰Your Working Time Is Completed⏰\n☺☺HAVE A NICE DAY☺☺\nTAKE CARE AND 👋👋BYE BYE👋👋",
                                        app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\cm.ico",
                                        timeout=15)
                    break
        elif(S1=="working"):
            count=0
            print("🙂👋HELLO 🖥PR0GRAMMER🖥")
            print("❤THIS WILL HELPS YOU A LOT FOR BETTER HEALTH❤")
            t=int(input("⏳Enter Today's Working Time⌚ In Hours:"))
            print("Minimize Screen After Giving Valid Details:")
            notification.notify(title="**😊HELLO {0} 😊**".format(name.upper()),message="*Let you Start The Work\n*Follow Instructions While You Get a Notiocation\n*FOLLOW INSTRUCTION-STAY HEALTH",
                                app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\smile.ico",
                                timeout=15)
            while True:
                time.sleep(25*60)
                notification.notify(title="🔔TAKE A SMALL BREAK🔔",message="!!Do Some Exersise",
                                    app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\b.ico",
                                    timeout=15)
                notification.notify(title="🙆🏻‍EXERCISES🙆🏻‍",message="1.Bend Your Neck in Different Directions\n2.Rub Your Two hands And keep both hands on your 👀Eyes👀 and Take a deep 🫁breath🫁 4-5 times\nThen,Start Your Work  With Fresh Mind..",
                                    app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\workout.ico",
                                    timeout=15)
                count=count+1
                time.sleep(5*60)
                if(count%2==0):
                    notification.notify(title="**t💦TIME TO DRINK WATER💦**",
                                        message="!!💧Drink a Glass Of Water",
                                        app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\water.ico",timeout=15)
                if(count==t*2):
                    notification.notify(title="✅✅COMPLETED✅✅",
                                        message="⏰Your Working Time Is Completed⏰\n☺☺HAVE A NICE DAY☺☺\nTAKE CARE AND 👋👋BYE BYE👋👋",
                                        app_icon="C:\\Users\\CHARANSAI &YASWITHA\\Downloads\\cm.ico",
                                        timeout=15)
                    break
        else:
            print("Please Enter Correct Profession {0} !!!".format(name))
            
    else:
        print("This Application Can Only Setup Remainder / Notification {0}!!!!".format(name))
    
        
            
    

        
