#!/usr/bin/python3
print("Content-Type: text/html") # header
print()
import cgi, os, view

form = cgi.FieldStorage()

if 'id' in form: 
    pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello WEB'

print('''
    <!doctype html>
    <html>
        <head>
            <title>WEB - Welcome</title>
            <meta charset="utf-8">
            <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
        </head>
        <body>
            <h1><a href="index.py">WEB</a></h1>
            <ol>
                {listStr}
            </ol>
            <a href="create.py">Create</a>
            <form action="process_create.py" method="POST">
                <p><input type="text" name="title" placeholder="ex. kotlin"></p>
                <p><textarea rows="4" name="description" placeholder="ex. kotlin is ..."></textarea></p>
                <p><input type="submit" value="완료"></p>
            </form>
        </body>
    </html>
'''.format(
    title = pageId, 
    desc = description, 
    listStr = view.getList()
    ))