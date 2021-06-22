
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'last_name' : '王',
    'first_name': '帅平',

    'address' : '阮辉职业技术学校',
    'job': 'Python developer',
    'tel': '0678282923',
    'email': 'kuaikuai@gmail.com',
    'description' : '我一直从事于web方面的工作，掌握的前端技术有ajax，Vue，js，div+css，html css，同事我也了解java语言和数据库表结构这块，更后台人员能更有效的沟通。我的性格方面不算外向，也不算内向，跟朋友，同事相处，比较外向，在工作中，代码开发时，我是比较内向的，我喜欢全心全意的投入工作中。我也喜欢交朋友，偶尔跟朋友聚聚，聊聊。对于工作我总是抱着认真负责，有责任心，吃苦耐劳的态度工作。',
    'social_media' : [
        {
            'link': 'https://www.facebook.com/nono',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img_nono.jpg',
    'EXPERIENCES' : [
        {
            'title' : 'Web 开发人员',
            'company': 'AZULIK',
            'description' : '多个 AZULIK 网站的项目经理和首席开发人员.',
            'timeframe' : 'July 2018 - November 2019'
        },
        {
            'title' : '自由网络开发人员',
            'company': 'Independant',
            'description' : '中小型公司创建 Wordpress 网站。 ',
            'timeframe' : 'February 2017 - Present'
        },
        {
            'title' : 'Sharepoint实习生',
            'company': 'ALTEN',
            'description' : '帮助管理 600 个 Sharepoint 站点平台（审核、迁移到 Sharepoint 更新版本）',
            'timeframe' : 'October 2015 - October 2016'
        }
    ],
    'EDUCATION' : [
        {
            'university': '湖北师范大学',
            'degree': '学士学位',
            'description' : '从事项目实战',
            'mention' : 'Bien',
            'timeframe' : '2015 - 2016'
        },
        {
            'university': '昆明西点学校',
            'degree': '学士学位',
            'description' : '知识积累',
            'mention' : 'Bien',
            'timeframe' : '2015'
        },
        {
            'university': '昭阳一中',
            'degree': '学士学位',
            'description' : '开始进入软件生涯',
            'mention' : 'N/A',
            'timeframe' : '2010 - 2012'
        }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['Dance', 'Travel', 'Languages']
}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))
   
@app.route('/chart')
def index():
	return render_template('chartsajax.html',  graphJSON=gm())

def gm(country='United Kingdom'):
	df = pd.DataFrame(px.data.gapminder())

	fig = px.line(df[df['country']==country], x="year", y="gdpPercap")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON


@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFCCCC',
										'size': '14',
										},
					'textfont': {'color': '#CCFF99',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
