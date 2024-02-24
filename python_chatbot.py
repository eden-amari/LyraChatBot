# try to incorporate open AI
import random
import json
import requests
import re
import time

def remove_punc(pstr):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in pstr:
        if ele in punc:
            pstr = pstr.replace(ele, "")
    return pstr

def get_info(user_input):
    language_code = 'en'
    search_query = user_input
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

    if response['pages'] != []:
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
            print(f"Excerpt: {excerpt_text_no_tags}")
            print(f"Description: {description_text}")
            print(f"Article URL: {article_url}")
            output.append({'excerpt': excerpt_text_no_tags, 'description': description_text, 'article_url': article_url})

    else: 
        output.append({'excerpt': '', 'description': '', 'article_url': ''})
        return output
# -------------------------------------------------------------------------------------------------------------------------------------------
def chatbot():
    print("Hey girl!")
    name = input("What's your name? \n")
 
    user_input = ''
    while user_input.lower() != "bye":
        user_input = input("\nEnter your query: ")

        greetings = ["Hi", "Hello", "Howdy", "Hey", "'Sup"]
        if user_input.capitalize() in greetings:
            pick = random.randint(0, len(greetings) - 1)
            print(greetings[pick])

        elif user_input.capitalize() == "How are you?" or user_input.capitalize() == "How are you":
            print(f"I'm doing great {name}, thank you!")
            rate = int(input("On a scale of 1 to 5, how are you doing today? \n"))
            while (type(rate) != int) or (rate < 1) or (rate > 5):
                print("Please enter an integer from 1 to 5.")
                rate = int(input("On a scale of 1 to 5, how are you doing today? \n"))

            mood_dict = {
                1: "Aw, I'm sorry about that. :(",
                2: "Hm, your day could have been better. ",
                3: "Your day was okay! Could have been worse.",
                4: "Yay, you had a good day!",
                5: f"Wow, {name}, your day was awesome! :D"
            }
            print(mood_dict[rate])
    
        else:
            get_info(user_input)
chatbot()