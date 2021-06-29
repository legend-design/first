
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': '平',
    'last_name' : '王',
    'address' : '湖北黄石市',
    'job': '中级软件设计师',
    'tel': '0678282923',
    'email': 'nohossat.tra@yahoo.com',
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
    'img': 'img/img.jpg',
    'experiences' : [
        {
            'title' : '微信小程序开发',
            'company': '湖师',
            'description' : '实训实战',
            'timeframe' : '2020-2021'
        },
        {
            'title' : '数据库设计',
            'company': '湖师',
            'description' : '实训工作 ',
            'timeframe' : '2019-2020'
        },
        {
            'title' : 'web开发',
            'company': '湖师',
            'description' : '购票网页开发',
            'timeframe' : '2018-2019'
        }
    ],
    'education' : [
        {
            'university': '湖师',
            'degree': '进修学士学位',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2020'
        },
        {
            'university': '湖师',
            'degree': '进修学士学位',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2021'
        },
        {
            'university': '湖师',
            'degree': '获得学士学位',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2022'
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
    return render_template('resume.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))

@app.route('/chart')
def index():
	return render_template('chartsajax.html',  graphJSON0 = gm0(),graphJSON1 = gm1(),graphJSON2 = gm2(),graphJSON3 = gm3()
                           , graphJSON4 = gm4(), graphJSON5 = gm5(),graphJSON6 = gm6() ,graphJSON7 = gm7(),graphJSON8= gm8()
                           , graphJSON9 = gm9(),graphJSON10 = gm10(),graphJSON11 = gm11(),graphJSON12 = gm12(), graphJSON13 = gm13(),
                           graphJSON14 = gm14(), graphJSON15 = gm15() )


def gm0():
    df = pd.read_csv("penguins.csv")

    fig = px.scatter(df, x="flipper_length_mm", y='body_mass_g',color="species")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def gm1():
    df = pd.read_csv("penguins.csv")

    fig = px.scatter(df, x="flipper_length_mm", y='body_mass_g',color="species" ,facet_col ='island',log_x=True)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm2():
    df = pd.read_csv("penguins.csv")
    fig = px.histogram(df, x="flipper_length_mm", y='body_mass_g', color="species")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def gm3():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.scatter(df, x="flipper_length_mm", y='body_mass_g', color="species",marginal_y="rug", marginal_x="histogram")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def gm4():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.box(df, x="body_mass_g", y="species", orientation="h", color="sex", notched=True)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm5():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.violin(df, y="bill_length_mm", x="island", color="sex", box=True, points="all")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm6():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.scatter(df, x="bill_length_mm", y="species", color="sex",  marginal_x="violin", marginal_y="box")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm7():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.scatter_matrix(df, dimensions=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g'], color='species')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm8():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.parallel_coordinates(df,
                                  color="species_id",
                                  labels={"species_id":"species",
                                          'bill_length_mm':'bill_length',
                                          'bill_depth_mm':'bill_depth',
                                          'flipper_length_mm':'flipper_length',
                                          'body_mass_g':'body_mass'},
                                  color_continuous_scale=px.colors.diverging.Tealrose,
                                  color_continuous_midpoint=2)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm9():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.parallel_categories(df, color="species_id", color_continuous_scale=px.colors.sequential.Inferno)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm10():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.line(df, x="island", y="bill_depth_mm", color="species",
                  line_group="species", hover_name="species",
                  line_shape="spline", render_mode="svg")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm11():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig = px.area(df, x="island", y="bill_depth_mm", color="species",
        line_group="species")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm12():
    df = pd.read_csv("penguins.csv")
    # gapminder = px.data.gapminder()
    # gapminder2007 = gapminder.query('year == 2007')
    fig =px.density_contour(df, x='bill_length_mm', y='bill_depth_mm', color="species")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def gm13():
    df = pd.read_csv("penguins.csv")
    fig = px.density_heatmap(df, x='bill_length_mm', y='bill_depth_mm')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm14():
    df = pd.read_csv("penguins.csv")
    fig =px.bar(df, x="island", y="flipper_length_mm", color="sex", barmode="group")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm15():
    df = pd.read_csv("penguins.csv")
    fig =px.pie(df, values='flipper_length_mm', names='island')
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
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
