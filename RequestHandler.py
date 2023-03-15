import wiktionaryparser as wp
from config_reader import config
import requests


def get_definition(text, language=None):
    parser = wp.WiktionaryParser()
    data = parser.fetch(text, language)
    definitions = []
    try:
        data[0].get('definitions')[0].get('text')
    except IndexError:
        definitions.append("No definitions found")
        return definitions

    contents = []
    for item in data:
        contents.append(item.get('definitions')[0].get('text'))
    if len(contents) == 0:
        definitions.append("No definitions found")
    for definition in contents:
        definitions.extend(definition[1:len(definition)])
    return definitions


def get_udict_definition(text):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term": text}
    headers = {"X-RapidAPI-Key": config.RapidAPI_key.get_secret_value(),
               "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    definitions = []
    if not response.status_code == 200:
        definitions.append(("Connection Error " + str(response.status_code)))
        return definitions
    contents = response.json().get('list')
    for item in contents:
        definitions.append(item.get('definition').replace('[', '').replace(']', ''))
        if len(definitions) > 3:
            break
    if len(definitions) == 0:
        definitions.append("No definitions found")

    return definitions
