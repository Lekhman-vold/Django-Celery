import json

import requests


def get_todo():
    url = 'https://jsonplaceholder.typicode.com/todos/2'
    r = requests.get(url)
    pg_content = r.text
    probably_json = pg_content.replace("\\'", "'")
    feed = json.loads(probably_json)
    title = feed['title']
    return title
