import wolframalpha as wl
import PySimpleGUI as sv
import pyttsx3 as pt
import wikipedia as wk

api =  wl.Client('6A585H-PGHRVT7WPU')

sv.theme('dark blue')
layout = [[sv.Text('Enter a word'),sv.InputText()],[sv.Button('ok'),sv.Button('Cancel')]]
window = sv.Window('Kcemaa',layout)
engine = pt.init()

while True:
    event, values =window.read()
    if event in (None,'Cancel'):
        break

    try:
        wiki_res = wk.summary(values[0],sentences =2)
        wolf_res = next(api.query(values[0]).results).text
        engine.say(wolf_res)
        sv.PopupNonBlocking("Results: "+ wolf_res,"Wikipedia Results: "+wiki_res)
    except wk.exceptions.PageError:
        wolf_res = next(api.query(values[0]).results).text
        engine.say(wolf_res)
        sv.PopupNonBlocking(wolf_res)
    except wk.exceptions.DisambiguationError:
        wolf_res = next(api.query(values[0]).results).text
        engine.say(wolf_res)
        sv.PopupNonBlocking(wolf_res)
    except:
        wiki_res = wk.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sv.PopupNonBlocking(wiki_res)
    engine.runAndWait()

window.close()