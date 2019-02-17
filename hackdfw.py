from flask import Flask, render_template, url_for
from forms import SearchShelters

app = Flask(__name__)
app.config['SECRET_KEY'] = '932913485416995c0c3e5a3777affc3b'

events_list = [
	{
		'date': '2/16/2019',
		'location': 'Women Museum Fair Park',
		'time': '9 AM - 11:59 PM',
		'name': 'HackDFW',
		'description': 'Compete with other people to program a project for prizes or for fun.',
		'image': 'https://scontent-dfw5-1.xx.fbcdn.net/v/t1.0-9/16114220_1025027550937354_5025196976278028909_n.png?_nc_cat=110&_nc_ht=scontent-dfw5-1.xx&oh=fb6adca7da26543f005d089f1477d3a6&oe=5CF4DBE7',
		'entry_fee': 'Registration/No Fee'
	},
	{
		'date': '3/15/2019',
		'location': 'McDonalds Near Women Museum Fair Park',
		'time': '7 AM - 11 PM',
		'name': 'BIG MAC FREEDOM',
		'description': 'Get a Big Mac for free.',
		'image': 'https://vignette.wikia.nocookie.net/logopedia/images/1/1e/Plain-mcdonalds-logo.jpg/revision/latest?cb=20161208155014',
		'entry_fee': 'Free'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route('/shelters', methods=['GET', 'POST'])
def shelters():
	form = SearchShelters()
	return render_template('shelters.html', form=form)

@app.route('/events')
def events():
	return render_template('events.html', events_list=events_list)

@app.route('/emergency')
def emergency():
	return render_template('emergency.html')

@app.route('/weather')
def weather():
	return render_template('weather.html')

if __name__ == '__main__':
     app.run()
