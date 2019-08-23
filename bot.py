import datetime
import telepot
import os
import time
from random import choice, randint
from unicodedata import normalize
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#Codigo Python para bot de telegram con telepot
#Tutorial recomendado: youtu.be/YqVK_0eu5OA

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    namebot = normalize('NFKC', normalize('NFKD', bot.getMe().get("username")).translate(trans_tab)).lower()

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    # - # - # Normalizando string comando # - # - #
    texto = msg.get("text","sinTexto")
    parametros=texto.split(" ",1)
    stringCMD=parametros[0].split("@")
    comando=normalize('NFKC', normalize('NFKD', stringCMD[0]).translate(trans_tab)).lower()
    if len(stringCMD) > 1:
        callbot = normalize('NFKC', normalize('NFKD', stringCMD[1]).translate(trans_tab)).lower()
    else:
        callbot = namebot

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def sendRandom(c_type,answer,capt = None):
        try:
            if c_type == "photo":
                bot.sendPhoto(chat_id, answer, caption=capt, parse_mode="HTML")
            elif c_type == "text":
                bot.sendMessage(chat_id, answer, parse_mode="HTML")
            elif c_type == "sticker":
                bot.sendSticker(chat_id, answer)
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas de envio")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def initial():
        try:
            if chat_type == 'private':
                if comando == "/start":
                    txt="Que quieres?:\n\n"\
                    "Puedes enviar /galletadelafortuna\n"\
                    "para recibir una galleta de la fortuna\n\n"\
                    "envía /help para ver los demas comandos"
                elif comando == "/help":
                    txt="<b>Lista de Comandos</b>:\n"\
                    "/GalletadelaFortuna - una galleta de la fortuna.\n"\
                    "/Haluze - imagen random de un servidor ruso.\n"\
                    "/sticker - se envia un sticker\n"\
                    "/dedGrup -  envia el meme de ded grup.\n"\
                    "/Horoscopo [signo]* - tu horoscopo.\n\n"\
                    "<pre>* : parametro obigatorio</pre>"
            # - # - # - # - # - #
            elif callbot == namebot:
                if comando == "/start":
                    txt="¿Que quieres?:\n\n"\
                    "Puedes enviar /galletadelafortuna\n"\
                    "para recibir una galleta de la fortuna"
                elif comando == "/help":
                    txt = "Solo por interno"
            # - # - # - # - # - #
            sendRandom("text",txt)
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas iniciales")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def galletas_Random():
        try:
            idRandom = str(randint(4,178))
            Photo = "t.me/picturesBank/" + idRandom
            capt = "Tu <b>galleta de la fortuna</b>, puedes solicitar luego"
            # - # - # - # - # - #
            sendRandom("photo",Photo,capt)
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas con galletas")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def haluze_Random():
        try:
            rndPhoto = str(randint(7,21787))
            Photo = "halbot.haluze.sk/image/" + rndPhoto
            capt = "servidor <a href=\""+Photo+"\">haluze</a> de Rusia"
            # - # - # - # - # - #
            sendRandom("photo",Photo,capt)
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas con haluze")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def sticker_Random():
        try:
            if comando == "/sticker":
                stickersList = [
                    "CAADAQADxwEAAxi_A_v9_T_9ezeBFgQ","CAADAQADwgEAAxi_A5DDSzE--rx0FgQ",
                    "CAADBQADyRkAAribGhZcu8LcUrw5phYE","CAADBQADyBkAAribGhaiuCpwS1kBjBYE"
                    ]
            rndSticker = choice(stickersList)
            sendRandom("sticker",rndSticker)
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas con sticker")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def horoscopo_Random():
        try:
            if len(parametros) > 1:
                listSigno = parametros[1].split(" ",1)
                signo = normalize('NFKC', normalize('NFKD', listSigno[0]).translate(trans_tab)).lower()
            else:
                signo = "ninguno"
            # - # - # - # - # - #
            if signo=="aries":
                text = "Aries: siempre con humitos en la cabeza, hace algo por la vida, el horoscopo no sirve wn!"
            elif signo=="tauro":
                text = "Tauro: que mierda buscai en el horoscopo, levantate de esa silla y sal a trabajar."
            elif signo=="geminis":
                text = "Géminis: weon bipolar, aqui esta toda la verdad, pero es mentira."
            elif signo=="cancer":
                text = "Cáncer: gente weona que cree que le dire que le va a pasar hoy, bañate antes de salir."
            elif signo=="leo":
                text = "Leo: no wn, no estan los numeros del loto aca, no gasti tu plata en wea y comprate comida de verdad."
            elif signo=="virgo":
                text = "Virgo: eres un virgo de mierda, deja de leer el horóscopo, moriras virgen!!"
            elif signo=="libra":
                text = "Libra: balanceate este, si queri balance hace mas deporte y sale a carretear con los amigos."
            elif signo=="escorpio":
                text = "Escorpio: uy, que miedo, ahí viene el alacran!!"
            elif signo=="escorpion":
                text = "Escorpio: el signo es ESCORPIO, no escorpion!!"
            elif signo=="sagitario":
                text = "Sagitario: ni tan santo, igual seiya te cago con la armadura."
            elif signo=="capricornio":
                text = "Capricornio: otro wn mas buscando su salud aca, sale a respirar aigre."
            elif signo=="acuario":
                text = "Acuario: sale a trabajar, la plata no llega sola, leyendo el horoscopo no te vai a jubilar antes."
            elif signo=="piscis":
                text = "Piscis: el horoscopo es pa mentes cerradas, abrete y lanzate a la vida."
            elif signo=="negro":
                text = "Negro teni el hoyo"
            elif signo=="chino":
                text = "no te conformas con las galletas?"
            elif signo=="ninguno":
                text = "debes ingresar un signo. ej: <code>/horoscopo aries</code>"
            else:
                text = "Algo esta mal, revisalo e intenta de nuevo"
            # - # - # - # - # - #
            sendRandom("text",text)
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas con horoscopo")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def dedgrup_Random():
        try:
            sendRandom("text","ded grup")
            sendRandom("sticker","CAADBAADZgADddnUCDenF6VnTTiDFgQ")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas con dedgrup")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def noRandom():
        try:
            if chat_type == 'private':
                if texto[0] == "/":
                    noComando =  "El comando " +comando+ " no está implementado \nMás información en /help"                    
                else:
                    noComando =  "esto no funciona así\nMás información en /help"
                sendRandom("text", noComando)
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"problemas de no Random")

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    try:
        if comando=="/start" or comando=="/help":
            initial()
        elif comando=="/galletadelafortuna":
            galletas_Random()
        elif comando=="/haluze":
            haluze_Random()
        elif comando=="/horoscopo":
            horoscopo_Random()
        elif comando=="/sticker":
            sticker_Random()
        elif comando=="/dedgrup":
            dedgrup_Random()
        else:
            noRandom()
    except(IndexError):
        bot.sendMessage(chat_id,"problemas con el Bot")
        print ('error...')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
TOKEN=("__1234556789:aqui-va-el-TOKEN-bot__") #aqui colocar el TOKEN del bot
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Estoy escuchando...')

while 1:
     time.sleep(10)
