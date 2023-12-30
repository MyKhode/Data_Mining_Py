import re
import json
import requests
from bs4 import BeautifulSoup
from khmernltk import pos_tag

base_url = 'https://www.khsearch.com/qna/'

intents = []

for i in range(1, 20):  # Iterate through pages 1 to 9 (adjust as needed)
    url = f'{base_url}{i}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the content you need from the soup object
        
        # Example: Extracting tag, questions, and answers
        tags = soup.find_all('a', class_='qna-tag')
        questions = soup.find_all('a', class_='qna-title')
        answers = soup.find_all('div', class_='answer-content')
        
        # Assuming questions, answers, and tags have similar lengths
        for index, (tag, q, a) in enumerate(zip(tags, questions, answers)):
            tagged_sentence = pos_tag(q.get_text(strip=True))
            
            nouns = []  # Initialize a list to store nouns
            for word, tag in tagged_sentence:
                if tag == "n" and word not in nouns:  # Check if the tag is a noun and not already in nouns
                    nouns.append(word)  # Collect unique nouns in the sentence
            
            # Remove redundant words and spaces when joining nouns
            noun_pattern = ''.join(n for n in nouns if n.strip())
            
            # Clean the response by removing text before the date format
            cleaned_response = re.sub(r'^.*?(?=\d{4}-\d{2}-\d{2} \d{2}:\d{2})', '', a.get_text(strip=True))
            
            # Check if the intent already exists before adding it
            existing_tags = [intent['tag'] for intent in intents]
            if f"id_{i}" not in existing_tags:
                intent = {
                    "tag": f"id_{i}",  # Creating a unique tag/id
                    "patterns": [q.get_text(strip=True)] + [noun_pattern],  # Use the cleaned noun pattern
                    "responses": [cleaned_response.strip()]  # Strip to remove leading/trailing spaces
                }
                intents.append(intent)
                print(intent)

# Save data as JSON file
with open('data_intents.json', 'w', encoding='utf-8') as json_file:
    json.dump({"intents": intents}, json_file, indent=4, ensure_ascii=False)
