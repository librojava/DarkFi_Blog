from flask import Flask, render_template, url_for, redirect, request
from markdown2 import markdown
from jinja2 import Environment, PackageLoader
import os
import pypandoc
from datetime import datetime
import subprocess
import requests


app = Flask(__name__)

posts = {}
for markdown_post in os.listdir('templates'):
  if markdown_post.endswith('md'):
   file_path = os.path.join('templates', markdown_post)
   with open(file_path, 'r') as file:
     posts[markdown_post] = markdown(file.read(), extras=['metadata'])
     convertin = subprocess.call('./bash.sh')

env = Environment(loader=PackageLoader('app', 'templates'))
test_template = env.get_template('index.html')
posts_metadata = [posts[post].metadata for post in posts]

datas = []
date = []
url = []
lat = []
date_list = []

for data in posts_metadata:
 url.append(data['url'])
 url.sort()
 my_date = datetime.strptime(data['list1'],"%Y.%m.%d")
 time = my_date.date()
 date.append(time)
 li = list(zip(date,url))
 latest_article = sorted(li, key=lambda tuple:tuple[0])
 latest = latest_article[-4:]

 d = data['list1']
 date_list.append(d)
 date_list.sort()
 new = list(zip(date_list,url))


for url_post in latest:
  url_posts = url_post[1]
  lat.append(url_posts)

for j in lat:
 for y in posts_metadata:
  if y['url'] == j:
   datas.append(y)


def prev_page(pages):
    for page in pages:
     p = 0
     global prev_url
     prev_url = pages[p][1]
     prev_page = pages[p][0]
     print(prev_page)
     if page[0] < prev_page:
            prev_page = page[0]
            prev_url = page[1]
            p += 1
    return prev_page, prev_url


prev_page = prev_page(new)


def next_page(pages,p):
    for page in pages:
     global next_url
     next_url = page[1]
     next_page = pages[p][0]
     global l
     l = []
     if page[0] > next_page:
            next_url = page[1]
            l.append(next_page)
     else:
            p +=1
    return next_page, next_url

next_page = next_page(new,0)

@app.route('/')
def test():
 csslink = url_for('static', filename='css/main.css')
 return render_template('index.html', posts=datas, articles=datas, csslink=csslink)

@app.route('/featured')
def featured():
 csslink = url_for('static', filename='css/main.css')
 return render_template('featured-article.html',csslink=csslink)

@app.route('/archive')
def archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/history_archive')
def history_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/insight_archive')
def insight_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('insight_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/technology_archive')
def technology_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('technology_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/market_archive')
def market_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('market_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/xenopoetisc_archive')
def xenopoetisc_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('xenopoetisc_archive.html',csslink=csslink,posts=posts_metadata)


@app.route('/history1')
def history1():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history1.html',csslink=csslink, posts=posts_metadata,prev_page=prev_page,next_page=next_page, prev_url=prev_url, next_url=next_url)

@app.route('/history2')
def history2():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history2.html',csslink=csslink,posts=posts_metadata,prev_page=prev_page,next_page=next_page, prev_url=prev_url, next_url=next_url)

@app.route('/history3')
def history3():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history3.html', csslink=csslink, posts=posts_metadata,prev_page=prev_page,next_page=next_page, prev_url=prev_url, next_url=next_url)

@app.route('/history4')
def history4():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history4.html', csslink=csslink, posts=posts_metadata,prev_page=prev_page,next_page=next_page,  prev_url=prev_url, next_url=next_url)


@app.route('/history6')
def history6():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history6.html', csslink=csslink, posts=posts_metadata,prev_page=prev_page,next_page=next_page ,  prev_url=prev_url,next_url=next_url)


if __name__ == '__app__':
        app.run()

