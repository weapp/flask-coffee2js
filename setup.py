"""
flask-coffee2js
===============

A small Flask extension that makes it easy to use CoffeeScript with your Flask application.

Usage
-----

You can activate it by calling the ``coffee2js`` function with your Flask app as a parameter:

      from flaskext.coffee2js import coffee2js
      coffee2js(app, js_folder='js', coffee_folder='src/coffee')

This will intercept the request to ``js_folder`` and compile de file if is necesary using the files from ``coffee_folder``.

When you deploy your app you might not want to accept the overhead of checking the modification time of your ``.coffee`` and ``.jss`` files on each request. A simple way to avoid this is wrapping the coffee2js call in an if statement:

      if app.debug:
          from flaskext.coffee2js import coffee2js
          coffee2js(app)
          
If you do this you'll be responsible for rendering the ``.coffee`` files into ``.js`` when you deploy in non-debug mode to your production server.


- documentation_
- development_


.. _documentation: https://github.com/weapp/flask-coffee2js
.. _development: https://github.com/weapp/flask-coffee2js

"""

from setuptools import setup


setup(
    name='flask-coffee2js',
    version='0.1.2',
    url='https://github.com/weapp/flask-coffee2js',
    license='MIT',
    author='Manuel Albarran',
    #author_email='',
    description='A small Flask extension that adds CoffeScript support to Flask.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'CoffeeScript'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
