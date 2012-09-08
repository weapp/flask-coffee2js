# -*- coding: utf-8 -*-
"""
    flaskext.coffee2js
    ~~~~~~~~~~~~~

    A small Flask extension that makes it easy to use CoffeeScript with your
    Flask application.

    :copyright: (c) 2012 by Manuel Albarrán.
    :license: MIT, see LICENSE for more details.
"""

import os.path
import codecs

import coffeescript

def _convert(src, dst):
    source = codecs.open(src, 'r', encoding='utf-8').read()
    output = coffeescript.compile(source)
    outfile = codecs.open(dst, 'w', encoding='utf-8')
    outfile.write(output)
    outfile.close()

    print 'compiled "%s" into "%s"' % (src, dst)

def coffee2js(app, js_folder='js', coffee_folder='src/coffee', force=False):
    if not hasattr(app, 'static_url_path'):
        from warnings import warn
        warn(DeprecationWarning('static_path is called '
                                'static_url_path since Flask 0.7'),
                                stacklevel=2)
        static_url_path = app.static_path
    else:
        static_url_path = app.static_url_path

    def _coffee2js(filepath):
        coffefile = "%s/%s.coffee" % (coffee_folder, filepath)
        filename = "%s/%s.js" % (js_folder, filepath)
        jsfile = "%s%s/%s" % (app.root_path, static_url_path, filename)

        if os.path.exists(coffefile) and (force or \
           not os.path.exists(jsfile) or \
           os.path.getmtime(coffefile) > os.path.getmtime(jsfile)):
            _convert(coffefile, jsfile)
            
        return app.send_static_file(filename)
        
    app.add_url_rule("%s/%s/<path:filepath>.js" %(static_url_path, js_folder), 'coffee2js', _coffee2js)