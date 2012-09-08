"""
flask-coffee2js
----------

A small Flask extension that makes it easy to use CoffeeScript with your Flask
application.

Links
`````

* `documentation <https://github.com/weapp/flask-coffee2js>`_
* `development version
  <https://github.com/weapp/flask-coffee2js`_


"""
from setuptools import setup


setup(
    name='flask-coffee2js',
    version='0.1',
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
