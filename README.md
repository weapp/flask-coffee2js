.flask-coffee2js
===============

A small Flask extension that makes it easy to use CoffeeScript with your Flask application.


## Installation

### Install with PIP

    pip install -e git+git@github.com:weapp/flask-coffee2js.git#egg=flask-coffee2js


### Install with setup.py

    git clone https://github.com/weapp/flask-coffee2js.git
    python setup.py install


## Usage

You can activate it by calling the `coffee2js` function with your Flask app as a parameter:

    from flaskext.coffee2js import coffee2js
    coffee2js(app, js_folder='js', coffee_folder='src/coffee')

This will intercept the request to `js_folder` and compile de file if is necesary using the files from `coffee_folder`.

When you deploy your app you might not want to accept the overhead of checking the modification time of your `.coffee` and `.js` files on each request. A simple way to avoid this is wrapping the coffee2js call in an if statement:

    if app.debug:
        from flaskext.coffee2js import coffee2js
        coffee2js(app)
        
If you do this you’ll be responsible for rendering the `.coffee` files into `.js` when you deploy in non-debug mode to your production server.