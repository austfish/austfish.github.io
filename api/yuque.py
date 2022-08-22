# -*- coding: utf8 -*-
import requests
def main_handler(event, context):
    r = requests.post("https://api.github.com/repos/austfish/yuque_blog/dispatches",
    json = {"event_type": "start"},
    headers = {"User-Agent":'curl/7.52.1',
              'Content-Type': 'application/json',
              'Accept': 'application/vnd.github.everest-preview+json',
              'Authorization': 'token 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'})
    if r.status_code == 204:
        return "This's OK!"
    else:
        return r.status_code