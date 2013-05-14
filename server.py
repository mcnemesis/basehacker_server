import json
import web
import subprocess

urls = (
  '', 'hello',
  '/', 'hello',
  '/fortune', 'fortune',
)

#------------- STATIC --------------
BASE_URI = '/basehacker'
APP_TITLE = 'Base Hacker'
APK_NAME = 'b45EH4CK3R.apk'
APP_URI = '%s/static/app/%s' % (BASE_URI, APK_NAME)
BACKGROUND_MUSIC = '%s/static/audio/all_credit_to_phone_booth_robbers__greasy_mechanism.ogg' % (BASE_URI)
FEATURE_REQ_MAIL = 'joewillrich 4t gmail D0t com'

#------------- GLOBALS -------------
#db = web.database(dbn='postgres', user='postgres', pw='postgres', db='globalclip')

#------------- utils ---------------

def j_e(msg,status='401 Invalid',**kwargs):
    d = {'payload' : msg,'status':401}
    d.update(kwargs)
    web.status = status
    return json.dumps(d)

def j_s(msg,status='200 OK',**kwargs):
    d = {'payload' : msg, 'status':200}
    d.update(kwargs)
    web.status = status
    return json.dumps(d)

#--------- Templates ----------
render = web.template.render('/var/opt/basehacker_server/templates/', cache=False)


#~~~~~~~~~~~~~~ VIEWS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class hello:
    """ say hello and introduce guests to the baseHacker Server"""
    def POST(self):
        return j_e("Not Supported")
    def GET(self):
        web.ctx
        web.ctx.status = '200 OK'
        web.header('Content-Type', 'text/html')
        return render.index({
            'APP_TITLE' : APP_TITLE,
            'APP_URI' : APP_URI,
            'BASE_URI' : BASE_URI,
            'BACKGROUND_MUSIC' : BACKGROUND_MUSIC,
            'FEATURE_REQ_MAIL' : FEATURE_REQ_MAIL,
            })

def get_fortune():
    return subprocess.Popen(['fortune'], stdout=subprocess.PIPE).communicate()[0]

class fortune:
    '''Just return a good ol' fortune cookie...'''
    def GET(self):
        return j_s( get_fortune() )
    def POST(self):
        return j_e("Not Supported")

application = web.application(urls, globals()).wsgifunc()

web.webapi.internalerror = web.debugerror
if __name__ == '__main__': application.run()
