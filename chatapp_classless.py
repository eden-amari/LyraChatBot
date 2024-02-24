from tkinter import *
import time
import emoji
import random
import requests
import json
import re

BG_DARK = '#ff7ca6'
BG_COLOR = '#f7afc6'
TEXT_COLOR = '#240a12'
FONT = ('Cascadia Mono', 15)
FONT_BOLD = ('Cascadia Mono SemiBold', 15)


ChatApp = Tk()
ChatApp.title("LyraBot")
ChatApp.configure(width=1000, height=550, bg=BG_COLOR)
ChatApp.resizable(width=True, height=True)

# welcome label
welcome = Label(ChatApp, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
welcome.place(relwidth=1)

# top divider
line = Label(ChatApp, width=450, bg=BG_DARK)
line.place(relwidth=1, rely=0.07, relheight=0.012)

# Text widget
text_widget = Text(ChatApp, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=8)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
text_widget.configure(cursor='arrow', state=NORMAL)

# Bottom label
bottom_label = Label(ChatApp, bg=BG_DARK, height=80)
bottom_label.place(relwidth=1, rely=0.825)

def on_enter_pressed():
    msg = msg_entry.get()
    insert_message(msg, "You")

def insert_message(msg, sender):
    text_widget.config(state=NORMAL)
    text_widget.insert(END, f"{sender}: {msg}\n")
    text_widget.config(state=DISABLED)
    text_widget.see(END)

# Message entry box
msg_entry = Entry(bottom_label, bg="#2C3E50", fg="#fffbfc", font=FONT)
msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
msg_entry.focus()
msg_entry.bind("<Return>", on_enter_pressed)

# send button
send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_DARK, cursor="heart", command=on_enter_pressed)
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


def _insert_message(self, msg, sender):
    if not msg:
        return
    
    self.msg_entry.delete(0, END) # clear the entry box
    msg1 = f"{sender}: {msg}\n\n"
    self.text_widget.configure(state=NORMAL)
    self.text_widget.insert(END, msg1)
    self.text_widget.configure(state=DISABLED)
    msg2 = f"{'ChatBot'}: {conversations(msg)}\n\n" 
    self.text_widget.configure(state=NORMAL)
    self.text_widget.insert(END, msg2)
    self.text_widget.configure(state=DISABLED)
    self.text_widget.see(END)


def conversations(request):
    greetings = ["Hi!", "Hi", "Hi.", "Hi","Hello!", 
                 "Hello there!", "Hello there", "Hello", "Hello.", "Hello there.", 
                 "Howdy", "Howdy!,", "Howdy.", 
                 "Hey", "Hey!", "Hey.", 
                 "'Sup", "Sup", "'Sup!", "Sup!", "Sup.", "'Sup.",
                 "Hey there", "Hey there!", "Hey there.",
                 "Yo", "Yo!", "Yo.", "Yo",
                 "Heyo", "Heyo!", "Heyo.", "Heyo",
                 "Hiya", "Hiya!", "Hiya.", "Hiya",
                 "Heya", "Heya!", "Heya.", "Heya",
                 "Hola", "Hola!", "Hola.", "Hola",
                 "Konichiwa", "Konichiwa!", "Konichiwa.", "Konichiwa",
                 "Que pasa", "Que pasa?", "Que pasa!", "Que pasa",
                 "Que tal", "Que tal?", "Que tal!", "Que tal",
                 "Que onda", "Que onda?", "Que onda!", "Que onda",
                 "Bonjour", "Bonjour!", "Bonjour.", "Bonjour",
                 "Ciao", "Ciao!", "Ciao.", "Ciao",
                 "Hallo", "Hallo!", "Hallo.", "Hallo",
                 "Salut", "Salut!", "Salut.", "Salut",
                 "Namaste", "Namaste!", "Namaste.", "Namaste",
                 "Salaam", "Salaam!", "Salaam.", "Salaam",
                 "Shalom", "Shalom!", "Shalom.", "Shalom",
                 "Sawubona", "Sawubona!", "Sawubona.", "Sawubona",
                 "Jambo", "Jambo!", "Jambo.", "Jambo",
                 "Salam", "Salam!", "Salam.", "Salam",
                 "Aloha", "Aloha!", "Aloha.", "Aloha",
                 "Konnichiwa", "Konnichiwa!", "Konnichiwa.", "Konnichiwa",
                 "Guten tag", "Guten tag!", "Guten tag.", "Guten tag",
                 "G'day", "G'day!", "G'day.", "G'day",
                 "G'day mate", "G'day mate!", "G'day mate.", "G'day mate",
                 "Ola", "Ola!", "Ola.", "Ola",
                 "Hej", "Hej!", "Hej.", "Hej",
                 "Hei", "Hei!", "Hei.", "Hei",
                 "Merhaba", "Merhaba!", "Merhaba.", "Merhaba",
                 "Sveiki", "Sveiki!", "Sveiki.", "Sveiki",
                 "Sveikas", "Sveikas!", "Sveikas.", "Sveikas",
                 "Pryvit", "Pryvit!", "Pryvit.", "Pryvit",
                 "Privet", "Privet!", "Privet.", "Privet",
                 "Asaalomu alaykum", "Asaalomu alaykum!", "Asaalomu alaykum.", "Asaalomu alaykum",
                 "Asaalam alaikum", "Asaalam alaikum!", "Asaalam alaikum.", "Asaalam alaikum",
                 "Ann-yeong", "Ann-yeong!", "Ann-yeong.", "Ann-yeong","Annyeong", "Annyeong!", "Annyeong.", "Annyeong",
                 "Anyeong", "Anyeong!", "Anyeong.", "Anyeong",
                 "Anyeonghaseyo", "Anyeonghaseyo!", "Anyeonghaseyo.", "Anyeonghaseyo","Anyeong haseyo", 
                 "Nihao", "Nihao!", "Nihao.", "Nihao", "Nǐ hǎo", "Nǐ hǎo!", "Nǐ hǎo.", "Nǐ hǎo", "Nǐn hǎo", "Nǐn hǎo!", "Nǐn hǎo.", "Nǐn hǎo", "Nín hǎo", "Nín hǎo!", "Nín hǎo.", "Nín hǎo", "Ni hao", "Ni hao!", "Ni hao.", "Ni hao","Nihao", "Nihao!", "Nihao.", "Nihao", "Nǐ hǎo", "Nǐ hǎo!", "Nǐ hǎo.", "Nǐ hǎo", "Nǐn hǎo", "Nǐn hǎo!", "Nǐn hǎo.", "Nǐn hǎo", "Nín hǎo", "Nín hǎo!", "Nín hǎo.", "Nín hǎo",
                 "Nǐ hǎo", "Nǐ hǎo!", "Nǐ hǎo.", "Nǐ hǎo", "Nǐn hǎo", "Nǐn hǎo!", "Nǐn hǎo.", "Nǐn hǎo", "Nín hǎo", "Nín hǎo!", "Nín hǎo.", "Nín hǎo", 
                 "Zdravstvuyte", "Zdravstvuyte!", "Zdravstvuyte.", "Zdravstvuyte",]
    greet_backs = ["Hi!", "Hello there :D", "Howdy \N{Face with Cowboy Hat}", "Hey!", "'Sup.", "Hello :]"]
    
    day_asks = ["Hru", "Hru?", "How was your day", "How was your day?", 
                "How are you?", "How are you", 
                "How are you doing?", "How are you doing", 
                "How are you doing today?", "How are you doing today", 
                "How you doing", "How you doing?", "How you doing today?", "How you doing today", 
                "How's your day?", "How's your day", "How's your day going?", "How's your day going", 
                "How's your day going today?", "How's your day going today", "How's your day today?", "How's your day today", 
                "How's your day been?", "How's your day been going today?", "How's your day been going today", 
                "How's your day been today?", "How's your day been going today", "How's your day been",
                "How's your day been today", "How's your day been going?",
                "How's your day been going today","How's your day been going", 
                "What's up?", "What's up", "What's up?", "What's up", "Whats up?", "Whats up", "Whats up?", "Whats up",
                "Que pasa?", "Que pasa", "Que pasa?", "Que pasa", "Que tal?", "Que tal", "Que tal?", "Que tal", "Que onda?", "Que onda", "Que onda?", "Que onda",
                "Como estas?", "Como estas", "Como estas?", "Como estas", "Como te va?", "Como te va", "Como te va?", "Como te va", "Como te va hoy?", "Como te va hoy", "Como te va hoy?", "Como te va hoy",
    ]
    day_responses = [f"I'm doing great, thank you! (•◡•)/", "I'm having a lovely day!", f"I'm well, thank you! (❛‿❛✿)", "I'm doing well, thanks!", 
                     "I'm doing great, thanks!", "Just chillin, you know how it be B:]"]
    
    goodbyes = ["Bye!", "Bye", "Bye,", "Goodbye!", "Goodbye", "Goodbye,", "See you later!", "See you later", "See you later,", "Later!", "Later", "Later,", 
                "Take care!", "Take care", "Take care,", 
                "Peace out!", "Peace out", "Peace out,", 
                "Catch you later!", "Catch you later", "Catch you later,", "Catch ya later!", "Catch ya later", "Catch ya later,", 
                "Catch you on the flip side!", "Catch you on the flip side", "Catch you on the flip side.,", "Catch ya on the flip side!", "Catch ya on the flip side", "Catch ya on the flip side,", 
                "Catch you later alligator!", "Catch you later alligator", "Catch you later alligator,", 
                "In a while crocodile!", "In a while crocodile", "In a while crocodile,", 
                "Toodles!", "Toodles", "Toodles,", 
                "Farewell!", "Farewell", "Farewell,"
                "Adios!", "Adios", "Adios,", 
                "Sayonara!", "Sayonara", "Sayonara,", 
                "Hasta la vista!", "Hasta la vista", "Hasta la vista,", "Hasta la vista, baby!", "Hasta la vista, baby", "Hasta la vista, baby,", 
                "See you soon!", "See you soon", "See you soon,", "See you!", "See you", "See you.", 
                "See ya!", "See ya", "See ya,", "See you next time!", "See you next time", "See you next time,", 
                "See you around!", "See you around", "See you around,", "See you on the flip side!", "See you on the flip side", "See you on the flip side,"]
    
    # print(f"(╭ರᴥ•́)")
    # ≧◉◡◉≦
    # (❛‿❛✿)
    # (─‿‿─)
    

    request = request.capitalize()
    request_list = request.split(" ")
    for x in request_list:
        x.capitalize()
        
    if request_list[0]in greetings:
        pick = random.randint(0, len(greet_backs) - 1)
        return greet_backs[pick]

    elif request in day_asks:
        for x in day_asks:
            if (x in request_list[0]) and (x=="Hru"):
                pick = random.randint(0, len(day_responses) - 1)
                return day_responses[pick]
            
            elif (x in request):
                pick = random.randint(0, len(day_responses) - 1)
                return day_responses[pick]
            
            elif "your day" in request:
                pick = random.randint(0, len(day_responses) - 1)
                return day_responses[pick]
        rate_day(request)
    
    # rate_day(ChatApp, request)
    else: 
        search(request)
    
def rate_day(request):
    mood_dict = {
        1: "Aw, I'm sorry about that. :(",
        2: "Hm, your day could have been better. ",
        3: "Your day was okay! Could have been worse.",
        4: "Yay, you had a good day!",
        5: "Wow, your day was awesome! :D"}
    
    rate = Tk.user_entry.get()
    if 1 <= rate <= 5:
        return mood_dict[rate]
    
    else:
        return f"Not that!"
#         while (type(rate) != int) or (rate < 1) or (rate > 5):
#             print("Please enter an integer from 1 to 5.")
#             rate = int(input("On a scale of 1 to 5, how are you doing today? \n"))
            



#     rate = int(request.get("On a scale of 1 to 5, are you doing today?"))

#     if 1 <= rate <= 5:
#         mood_dict = {
#             1: "Aw, I'm sorry about that. :(",
#             2: "Hm, your day could have been better. ",
#             3: "Your day was okay! Could have been worse.",
#             4: "Yay, you had a good day!",
#             5: "Wow, your day was awesome! :D"
#         }
#         return mood_dict[rate]
#     else:
#         while (type(rate) != int) or (rate < 1) or (rate > 5):
#             print("Please enter an integer from 1 to 5.")
#             rate = int(input("On a scale of 1 to 5, how are you doing today? \n"))
            
    
def search(request):
    language_code = 'en'
    search_query = request
    number_of_results = 1
    headers = {
    # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
    }

    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint
    parameters = {'q': search_query, 'limit': number_of_results}
    response = requests.get(url, headers=headers, params=parameters)

    response = json.loads(response.text)
    output = []

    for page in response['pages']:
        display_title = page['title']
        article_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
        try:
            article_description = page['description']
        except:
            article_description = 'a Wikipedia article'
        try:
            thumbnail_url = 'https:' + page['thumbnail']['url']
        except:
            thumbnail_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/200px-Wikipedia-logo-v2.svg.png'
        excerpt_text = page['excerpt']

    # removes tags 
        excerpt_text_no_tags = re.sub('<span.*?>|&.*;|</span>', '', excerpt_text)
        description_text = page['description']
        return f"""\nExcerpt: {excerpt_text_no_tags}
        \nDescription: {description_text}
        \nArticle URL: {article_url}"""
        # output.append({'excerpt': excerpt_text_no_tags, 'description': description_text, 'article_url': article_url})

    # else: 
    #     output.append({'excerpt': '', 'description': '', 'article_url': ''})
    #     return output



ChatApp.mainloop()