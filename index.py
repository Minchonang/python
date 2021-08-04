#!/usr/bin/python3
print("Content-Type: text/html") # header
print()

# module

import cgi, view
# import html_sanitizer
# sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
pageId = form.getvalue("id")

if 'id' in form: 
    title = pageId = form["id"].value
    description = open('data/' + pageId, 'r').read()
    # description = sanitizer.sanitize(description)
    # title = sanitizer.sanitize(title)
    update_link = '<a href="update.py?id={}">Update</a>'.format(pageId)
    delete_action = '''
    <form action="process_delete.py" method="POST">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="Delete">
    </form>
    '''.format(pageId)
else:
    title = pageId = 'Welcome'
    description = 'Hello WEB'
    update_link = ''
    delete_action = ''

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
            {update_link}
            {delete_action}
            <h2>{title}</h2>
            <p>{desc}</p>
        </body>
    </html>
'''.format(
    title = title, 
    desc = description, 
    listStr = view.getList(), 
    update_link = update_link, 
    delete_action = delete_action
    ))