from tkinter import*
from tkinter import simpledialog
from tkinter import font
import customtkinter
import time
import emoji
import random
import requests
import json
import re

BG_GRAY = '#ff7ca6'

BG_STRIP = "#FFE6EE"

BG_COLOR = '#f7afc6'

TEXT_COLOR = '#100307'

CHARCOAL = "#2C3E50"

WHITE = "#fffbfc"

FONT = ('Cascadia Mono', 15)
FONT_BOLD = ('Cascadia Mono SemiBold', 15)

class ChatApp():
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        # Adding title
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("LyraBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1000, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to the Chat!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)        

        #Text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=8)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.175, relx=-0.0001)
        self.text_widget.configure(cursor='arrow', state=NORMAL)

        rate_label = Label(self.window, bg=BG_STRIP, fg=TEXT_COLOR, text="Type RATE [Number] to rate your day from 1 to 5! Ex: RATE 3", font=FONT_BOLD, pady=5)
        rate_label.place(x=500, rely=.12, anchor="center", relwidth=1,)

        search_label = Label(self.window, bg=BG_STRIP, fg=TEXT_COLOR, text="Type SEARCH: [Query] to look something up!", font=('Cascadia Mono', 10), pady=5)
        search_label.place(x=500, rely=.17, anchor="center", relwidth=1, relheight=0.03,)

        # spacer = Label(self.window, text="New Line Text")
        # spacer.pack(padx=10, pady=10)

        # Bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        ## Step 7 (We need to create a new function to complete this step)
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg="#fffbfc", font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011,)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, cursor="heart", command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
    def _on_enter_pressed(self, event): # add function at Step 7
        # msg = self.msg_entry.get() # getting the contents of the chatbot
   
        # self._insert_message(msg, "You")
        # response = conversations(self, msg)
        # if response is not None:
        #     self._insert_message(response, "ChatBot")
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

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
                "Hiyaa", "Hiyaa!", "Hiyaa.", "Hiyaa",
                "Heya", "Heya!", "Heya.", "Heya",
                "Heyaa", "Heyaa!", "Heyaa.", "Heyaa",
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
                "How are you doing?", "How are you doing", "How you doin?", "How you doin", "How you doin today?", "How you doin today", "How you doin."
                "How are you doing today?", "How are you doing today", 
                "How you doing", "How you doing?", "How you doing today?", "How you doing today", 
                "How's your day?", "How's your day", "How's your day going?", "How's your day going", 
                "How's your day going today?", "How's your day going today", "How's your day today?", "How's your day today", 
                "How's your day been?", "How's your day been going today?", "How's your day been going today", 
                "How's your day been today?", "How's your day been going today", "How's your day been",
                "How's your day been today", "How's your day been going?",
                "How is your day?", "How is your day", "How is your day going?", "How is your day going", "How is your day today?", "How is your day today", "How is your day been?", "How is your day been", "How is your day been going?", "How is your day been going", "How is your day been going today?", "How is your day been going today", "How is your day been going today?", "How is your day been going today",
                "How has your day been?", "How has your day been", "How has your day been going?", "How has your day been going", "How has your day been going today", "How has your day been going today", "How has your day been going today?", "How has your day been going today",
                "How's your day been going today","How's your day been going", 
                "What's up?", "What's up", "What's up?", "What's up", "Whats up?", "Whats up", "Whats up?", "Whats up",
                "Que pasa?", "Que pasa", "Que pasa?", "Que pasa", "Que tal?", "Que tal", "Que tal?", "Que tal", "Que onda?", "Que onda", "Que onda?", "Que onda",
                "Como estas?", "Como estas", "Como estas?", "Como estas", "Como te va?", "Como te va", "Como te va?", "Como te va", "Como te va hoy?", "Como te va hoy", "Como te va hoy?", "Como te va hoy",]
    day_responses = [f"I'm doing great, thank you! (•◡•)/", "I'm having a lovely day!", f"I'm well, thank you! (❛‿❛✿)", "I'm doing well, thanks!", "I'm doing great, thanks!", "Just chillin, you know how it be B:]"]
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
                "See you around!", "See you around", "See you around,", "See you on the flip side!", "See you on the flip side", "See you on the flip side.",
                "Auf Wiedersehen!", "Auf Wiedersehen", "Auf Wiedersehen.",
                "Au revoir!", "Au revoir", "Au revoir.",
                "Arrivederci!", "Arrivederci", "Arrivederci.",
                "Adieu!", "Adieu", "Adieu.",
                "Dasvidaniya!", "Dasvidaniya", "Dasvidaniya.",
                "Zaijian!", "Zaijian", "Zaijian.",
                "Sayonara!", "Sayonara", "Sayonara.",
                "Adeus!", "Adeus", "Adeus.",
                "Annyeong!", "Ann-yeong", "Ann-yeong.",
                "Annyeonghi gasipsio!", "Annyeonghi gasipsio", "Annyeonghi gasipsio.",
                "lilaa alliquaa!", "lilaa alliquaa", "lilaa alliquaa.",
                "Farvel!", "Farvel", "Farvel.",
                "Kwaheri!", "Kwaheri", "Kwaheri.",
                "Dag!", "Dag", "Dag.",
                "Antio!", "Antio", "Antio.",
                "Do widzenia!", "Do widzenia", "Do widzenia.",
                "Sampai jumpa!", "Sampai jumpa", "Sampai jumpa.",
                "Namaste!", "Namaste", "Namaste.",
                "Adjø", "Adjø!", "Adjø.",
                "Hoşçakalın!", "Hoşçakalın", "Hoşçakalın.",
                "Lehitra’ot!", "Lehitra’ot", "Lehitra’ot.",
                "Hej då!", "Hej då", "Hej då.",
                ]
    
    gratitude = ["Thanks", "Thanks!", "Thanks.", "Thank you", "Thank you!", "Thank you.", "Thank", "Thank!", "Thank.", "Thx", "Thx!", "Thx.", "Thnx", "Thnx!", "Thnx.", "Tnx", "Tnx!", "Tnx.", "Tyvm", "Tyvm!", "Tyvm.", "TYVM", "TYVM!", "TYVM.", "Thank you so much",
                "Thank you so much", "Thank you so much!", "Thank you so much.", "Thank you very much", "Thank you very much!", "Thank you very much.",
                "Thanks a lot", "Thanks a lot!", "Thanks a lot.", "Thanks so much", "Thanks so much!", "Thanks so much.",
                "Thanks a bunch", "Thanks a bunch!", "Thanks a bunch.", "Thanks a ton", "Thanks a ton!", "Thanks a ton.",
                "Ty", "Ty!", "Ty.", "TY", "TY!", "TY.", "Tysm", "Tysm!", "Tysm.", "TYSM", "TYSM!", "TYSM.",
                "Dankie", "Dankie!", "Dankie.", "Dankie baie", "Dankie baie!", "Dankie baie.", "Dankie baie", "Dankie baie!", "Dankie baie.",
                "Shukran", "Shukran!", "Shukran.", "Shukriya", "Shukriya!", "Shukriya.", "Shukriya", "Shukriya!", "Shukriya.",
                "Ta", "Ta!", "Ta.", "Ta very much", "Ta very much!", "Ta very much.",
                "Doj jeh", "Doj jeh!", "Doj jeh.", "Doj jehi", "Doj jehi!", "Doj jehi.",
                "Xie xie", "Xie xie!", "Xie xie.", "Xie xie ni", "Xie xie ni!", "Xie xie ni.",
                "Dekuji", "Dekuji!", "Dekuji.", "Dekuji moc", "Dekuji moc!", "Dekuji moc.",
                "Tak", "Tak!", "Tak.", "Tak bardzo", "Tak bardzo!", "Tak bardzo.",
                "Kiitos", "Kiitos!", "Kiitos.", "Kiitos paljon", "Kiitos paljon!", "Kiitos paljon.",
                "Merci", "Merci!", "Merci.", "Merci beaucoup", "Merci beaucoup!", "Merci beaucoup.",
                "Danke", "Danke!", "Danke.", "Danke sehr", "Danke sehr!", "Danke sehr.",
                "Grazie", "Grazie!", "Grazie.", "Grazie mille", "Grazie mille!", "Grazie mille.",
                "Arigato", "Arigato!", "Arigato.", "Arigato gozaimasu", "Arigato gozaimasu!",
                "Efharisto", "Efharisto!", "Efharisto.", "Efharisto poli", "Efharisto poli!", "Efharisto poli.",
                "Dhanyavad", "Dhanyavad!", "Dhanyavad.", "Dhanyavad bahut", "Dhanyavad bahut!", "Dhanyavad bahut.",
                "Dhanyavad bahut", "Dhanyavad bahut!", "Dhanyavad bahut.", "Dhanyavad bahut", "Dhanyavad bahut!", "Dhanyavad bahut.",
                "Toda", "Toda!", "Toda.", "Toda raba", "Toda raba!", "Toda raba.",
                "Sukria", "Sukria!", "Sukria.", "Sukria bahut", "Sukria bahut!", "Sukria bahut.",
                "Terima kasih", "Terima kasih!", "Terima kasih.", "Terima kasih banyak", "Terima kasih banyak!",
                "Terima kasih banyak", "Terima kasih banyak!", "Terima kasih banyak.", "Terima kasih banyak", "Terima kasih banyak!", "Terima kasih banyak.",
                "Kamsahamnida", "Kamsahamnida!", "Kamsahamnida.", "Kamsahamnida kamsahamnida", "Kamsahamnida kamsahamnida!", "Kamsahamnida kamsahamnida.",
                "Kamsa hamnida", "Kamsa hamnida!", "Kamsa hamnida.", "Kamsa hamnida kamsa hamnida", "Kamsa hamnida kamsa hamnida!", "Kamsa hamnida kamsa hamnida.",
                "Takk", "Takk!", "Takk.", "Takk skal du ha", "Takk skal du ha!", "Takk skal du ha.",
                "Obrigado", "Obrigado!", "Obrigado.", "Obrigado muito", "Obrigado muito!", "Obrigado muito.",
                "Spasibo", "Spasibo!", "Spasibo.", "Spasibo bolshoe", "Spasibo bolshoe!", "Spasibo bolshoe.",
                "Istutiy", "Istutiy!", "Istutiy.", "Istutiy", "Istutiy!", "Istutiy.",
                "Asante", "Asante!", "Asante.", "Asante sana", "Asante sana!", "Asante sana.",
                "Tack", "Tack!", "Tack.", "Tack så mycket", "Tack så mycket!", "Tack så mycket.",
                "Kawp-kun krap/ka'", "Kawp-kun krap/ka'!", "Kawp-kun krap/ka'.", "Kawp-kun krap/ka' krap/ka'", "Kawp-kun krap/ka' krap/ka'!", "Kawp-kun krap/ka' krap/ka'.",
                "Tesekkür ederim", "Tesekkür ederim!", "Tesekkür ederim.", "Tesekkür ederim çok", "Tesekkür ederim çok!", "Tesekkür ederim çok.",
                ]
    youre_welcome = ["You're welcome", "You're welcome.", "You're welcome!"
                    "Je vous en prie", "Je vous en prie.", "Je vous en prie!", "De rien", "De rien.", "De rien!", "Il n'y a pas de quoi", "Il n'y a pas de quoi.", "Il n'y a pas de quoi!",
                    "Dōitashimashite", "Dōitashimashite.", "Dōitashimashite!",
                    "Bù kèqì", "Bù kèqì.", "Bù kèqì!", "Bù yòng xiè", "Bù yòng xiè.", "Bù yòng xiè!",
                    "Graag gedaan", "Graag gedaan.", "Graag gedaan!", "Geen dank", "Geen dank.", "Geen dank!",
                    "Gern geschehen", "Gern geschehen.", "Gern geschehen!", "Keine Ursache", "Keine Ursache.", "Keine Ursache!",
                    "Prego", "Prego.", "Prego!",
                    "De nada", "De nada.", "De nada!",
                    "Varsågod", "Varsågod.", "Varsågod!",
                    "Vaer så god", "Vaer så god.", "Vaer så god!",
                    "Aapaka svaagat hai", "Aapaka svaagat hai.", "Aapaka svaagat hai!",
                    "Rica ederim", "Rica ederim.", "Rica ederim!",
                    "Parakaló", "Parakaló.", "Parakaló!",
                    "Oleh hehva", "Oleh hehva.", "Oleh hehva!",
                    "Proszę", "Proszę.", "Proszę!",
                    "Karibu", "Karibu.", "Karibu!",
                    "Dit is 'n plesier", "Dit is 'n plesier.", "Dit is 'n plesier!",
                    "Pozhaluysta", "Pozhaluysta.", "Pozhaluysta!",
                    "Proshu", "Proshu.", "Proshu!",
                    "Walang anuman", "Walang anuman.", "Walang anuman!",
                    "Det var så lidt", "Det var så lidt.", "Det var så lidt!",
                    "Sama-sama", "Sama-sama.", "Sama-sama!",]
    # print(f"(╭ರᴥ•́)")
    # ≧◉◡◉≦
    # (❛‿❛✿)
    # (─‿‿─)
    
    request = request.capitalize()
    request_list = request.split(" ")
    for x in request_list:
        x.capitalize()
        
    if request_list[0].capitalize() in greetings:
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
      
    elif request_list[0].capitalize() in goodbyes:
        pick = random.randint(0, len(goodbyes) - 1)
        return goodbyes[pick]
    
    elif request_list[0].capitalize() in gratitude:
        pick = random.randint(0, len(youre_welcome) - 1)
        return youre_welcome[pick]

    elif request_list[0].capitalize() == "RATE":
        if 1 <= int(request_list[1]) <= 5:
            mood_dict = {
            1: "Aw, I'm sorry about that. :(",
            2: "Hm, your day could have been better. ",
            3: f"Seems that your day was okay! Could have been worse. (─‿‿─)",
            4: "Yay, you had a good day! :D",
            5: f"Wow, your day was awesome! ⸜(*ˊᗜˋ*)⸝"}

            return mood_dict[int(request_list[1])]
        else:
            return "Invalid rating. Please provide a rating from 1 to 5."
        
    elif request_list[0].upper() == "SEARCH:": 
        del request_list[0]
        new_request = " ".join(request_list)

        language_code = 'en'
        search_query = new_request
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
            return f"""\nHm... (╭ರᴥ•́)
            \nExcerpt: {excerpt_text_no_tags}
            \nDescription: {description_text}
            \nArticle URL: {article_url}"""
    
    else: 
        dont_know = [f"Yeah...I've got nothing. ┐(￣ヘ￣)┌", "I'm not sure what you mean.", "Erm...? (•_•)", "I'm not sure what you're asking.", "I don't get it. (・・ ) ?"]
        pick = random.randint(0, len(dont_know) - 1)
        return dont_know[pick]

 

app = ChatApp()
app.run()