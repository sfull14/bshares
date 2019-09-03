from flask import Flask, render_template, url_for, flash, redirect # import Flask class
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # setting app = instance of Flask class

app.config['SECRET_KEY'] = 'b54e04d10d8a6dadfec52f3671b9e0c6'

#Key: the code blocks in the HTML code get evaluated but are not included in the page source
#Key: template inheritance -- blocks are portions that child templates (home, about) can override in parent template (layout)

posts = [
	{
		'author': 'Sean Fuller',
		'title': 'Post 1',
		'content': 'First post content',
		'date_posted': '9/1/2019'
	},
	{
		'author': 'SFuller',
		'title': 'Post 2',
		'content': 'Second post content',
		'date_posted': '9/1/2019'
	}
]

@app.route("/") # handles complicated back end stuff...this allows us to write a function that returns the text.../ is just home page
@app.route("/home") # creates the home page at http://localhost:5000/
def home():
    # return "<h1>Home Page</h1>" #h1 tasks are HTML heading tags
    return render_template('home.html', posts=posts) #has to be in a folder called 'Templates'!!

@app.route("/about") # creates an about page at homepage/about (i.e. http://localhost:5000/about)
def about():
    # return "<h1>About Page</h1>" #h1 tasks are HTML heading tags
    return render_template('about.html', title='About') #has to be in a folder called 'Templates'!!

@app.route("/register", methods=["GET", "POST"]) # needs to accept post requests
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success') #bootstrap method
		return redirect(url_for('home')) #this is the NAME of THE FUNCTION
	return render_template('register.html', title='Register', form=form) #form keyword renders RegistrationForm class instance from forms.py

@app.route("/login") # creates registration page at register/about (i.e. http://localhost:5000/register)
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form) #form keyword renders RegistrationForm class instance from forms.py	

if __name__ == '__main__': # only True if we run this script directly...can't import
    app.run(debug=True)