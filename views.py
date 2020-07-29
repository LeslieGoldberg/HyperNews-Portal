import json
from django.shortcuts import render
from django.conf import settings
from django.views import View

new_articles = [
    {"created": "2020-02-09 14:15:10",
     "text": "Text of the news 1",
     "title": "News 1",
     "link": 1},
    {"created": "2020-02-10 14:15:10",
     "text": "Text of the news 2",
     "title": "News 2",
     "link": 2},
    {"created": "2020-02-09 16:15:10",
     "text": "Text of the news 3",
     "title": "News 3",
     "link": 3}
]

path = settings.NEWS_JSON_PATH

# add new article to news.json
with open(path, 'a') as file:
    json.dump(new_articles, file)

# read articles from json file to display in NewsView
with open(path, 'r') as json_file:
    articles = json.load(json_file)


class NewsView(View):
    def get(self, request, *args, **kwargs):
        for article in articles:
            context = {
                "created": article.created,
                "text": article.text,
                "title": article.title,
                "link": article.link,
            }
            return render(request, 'news/templates/news/index.html', context=context)
