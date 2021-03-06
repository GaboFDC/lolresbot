#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import telebot
import logging
import random

TOKEN = '134776856:AAFtSET8UmwZkEglBPfxO97KdlWL66aDvFM'

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

mybot = telebot.TeleBot(TOKEN)

mybot.get_me()

MEMES = ["Davo Pls", "Smite al nexo", "GG izi",
         "Bronzooooooodia el immortal", "Soy smurf de diamante, yo carreo - 0/24/1", "Coño de la madre!!!", "</3",
         "Tu papá", "Report", "1vs1? n00b", "El dragon no esta, se perdió :o", "Me la pelan todos",
         "Lo siento, mis respuestas son limitadas", "El bot nunca duerme", "KS = Kill Secured",
         "Estas seguro de eso?", "La verdad no sé", "Dejame pensarlo", "Mejor haga una davo",
         "Creo que tengo que meditar sobre eso", "Sin palabras...", "Superminions OP, me mataron :c",
         "Ya tengo buena orografía", "Stop bullying :c", "Los quiero <3", "Anita es fakker detras de camaras"]

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
@mybot.message_handler(commands=['start'])
def send_welcome(message):
    mybot.reply_to(message, "Hola, este es el Bot del grupo de League of Legends de la Resistencia \n \n R&R")

@mybot.message_handler(commands=['help'])
def send_welcome(message):
    mybot.reply_to(message, "Los comandos son:\n"
                            " /pipol - Muestra la gente que juega\n"
                            " /davo \n"
                            " /dent \n"
                            " /gabo \n"
                            " /pregunta - Responde a una pregunta si, no, talvez \n")

@mybot.message_handler(commands=['pipol'])
def send_people(message):
    mybot.reply_to(message, "Los loleros son: \n"
                            " - Oscar alias @VincentJackal \n"
                            " - Jose alias Dent, ResportPls @Felizzola \n"
                            " - Leo alias RTBrownyE, lumacro @RioTBrownyE \n"
                            " - Davo alias DavoPls @Davox0 \n"
                            " - Gabo alias WardDragon, daredel @GaboFDC \n"
                            " - Leidy alias nos abandonó @Putoslolresis \n"
                            " - Natha alias KarenTsuki @NadieEspecial \n"
                            " - Daniela alias @Pardum"
                            " - David Tamayo alias niñorata DestructorMLG @pendiente \n"
                            " - Rataeltriforce alias @RATAELTRIFORCE \n"
                            " - Alfredo \n"
                            " - Adriana alias Atenea30 @pendiente \n"
                            " - Beto alias @Darkfields \n")

@mybot.message_handler(commands=['davo'])
def send_davo(message):
    mybot.reply_to(message, "Flash al red")

@mybot.message_handler(commands=['dent'])
def send_dent(message):
    mybot.reply_to(message, "Dent no penta")

@mybot.message_handler(commands=['gabo'])
def send_gabo(message):
    mybot.reply_to(message, "Allstar=Alistar")

@mybot.message_handler(commands=['niñorata'])
def send_gabo(message):
    mybot.reply_to(message, "Garen 6 Warmong build somalia")

@mybot.message_handler(commands=['pregunta'])
def send_pregunta(message):
    ANSWERS = ["Si", "No", "Talvez"]
    ANSWER=random.choice(ANSWERS)
    mybot.reply_to(message, ANSWER)

@mybot.message_handler(commands=['meme'])
def send_pregunta(message):
    MEME=random.choice(MEMES)
    mybot.reply_to(message, MEME)

mybot.polling() # Start the bot
