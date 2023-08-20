import requests

url = 'https://cdn.discordapp.com/attachments/1093476470984294522/1142458530977304576/hideonbus__3996048057one_man_stands_in_front_of_car_70a80d6c-57ab-4cc9-a283-3f4272012947.png'
response = requests.get(url)
if response.status_code == 200:
    with open("img.png", 'wb') as f:
        f.write(response.content)
