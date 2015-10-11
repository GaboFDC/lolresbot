#!/usr/bin/python
import os
import telebot
import random

TOKEN = '134776856:AAFtSET8UmwZkEglBPfxO97KdlWL66aDvFM'

mybot = telebot.TeleBot(TOKEN)

mybot.get_me()

MEMES = ["Davo Pls", "Dent no penta", "Allstar=Alistar", "Flash al red", "Smite al nexo", "GG izi", "Bronzooooooodia el inmortal", "Soy smurf de diamante, yo carreo - 0/24/1"]

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

def application(environ, start_response):

    ctype = 'text/plain'
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        ctype = 'text/html'
        response_body = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Welcome to OpenShift</title>
</head>
<body>
    <h1>Hello world!</h1>
</body>
</html>'''

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()

# Defining message for handling start and help commands
@mybot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    mybot.reply_to(message, "Hola, este es el Bot del grupo de League of Legends de la Resistencia \n \n R&R")

@mybot.message_handler(commands=['pipol'])
def send_people(message):
    mybot.reply_to(message, "Los loleros son: \n"
                            " - Oscar alias @VincentJackal \n"
                            " - Jose alias Dent @Felizzola \n"
                            " - Leo alias RTBrownyE @RioTBrownyE \n"
                            " - DavoPls alias Davox0 @Davo76 \n"
                            " - Gabo alias WardDragon @GaboFDC \n"
                            " - Leidy alias aniita @aniita13 \n")

@mybot.message_handler(func=lambda message: True)
def reply_all(message):
    MEME=random.choice(MEMES)
    mybot.reply_to(message, message.text+"??"+MEME)

mybot.polling() # Start the bot