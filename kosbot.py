import os
import sleekxmpp
import requests
from urlparse import urljoin

class KOSCheckBot(sleekxmpp.ClientXMPP):

    KOS_API_URL = 'http://kos.cva-eve.org/api/'

    def __init__(self, jid, password, rooms, nickname):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.rooms = rooms
        self.nickname = nickname
        
        self.add_event_handler('session_start', self.session_start)
        self.add_event_handler('groupchat_message', self.muc_message)
        
    def session_start(self, event):
        for room in self.rooms:
            self.plugin['xep_0045'].joinMUC(room, self.nickname, wait=True)
        
    def muc_message(self, msg):
        if msg['mucnick'] == self.nickname or msg['body'][0] != '!':
            return
        
        cmd = msg['body'].split(' ')[0][1:]
        args = msg['body'].split(' ')[1:]
        
        if cmd == 'kos':
            return self.cmd_kos(msg, cmd, args)
            
    def cmd_kos(self, msg, cmd, args)
        arg = ' '.join(args)
        resp = requests.get(urljoin(KOS_API_URL, params={
            'c': 'json',
            'q': arg
        })
        if resp.status_code != requests.codes.ok:
            return "Something went wrong (Error %s)" % resp.status_code
        try:
            data = resp.json()
        except:
            return "KOS API returned invalid data."
        if data['message'] != 'OK':
            return "KOS API returned an error."
        if data['total'] == 0:
            return "KOS returned no results (Not on KOS)"
        
        results = []
        for result in data['results']
            text = '%s (%s) - %s'.format(
                result['label'],
                result['type'],
                'KOS' if result['kos'] else 'Not KOS'
            )
            results.append(text)
        return '\n'.join(results)
            
            
if __name__ == '__main__':
    jid = os.environ.get('KOSBOT_JID')
    password = os.environ.get('KOSBOT_PASSWORD')
    nickname = os.environ.get('KOSBOT_NICKNAME', 'KOSBot')
    rooms = os.environ.get('KOSBOT_CHANNELS')
    
    rooms = [x.strip() for x in rooms.split(',')]
    
    bot = KOSCheckBot(jid, password, rooms, nickname)
    bot.register_plugin('xep_0030') # Service Discovery
    bot.register_plugin('xep_0045') # Multi-User Chat
    bot.register_plugin('xep_0199') # XMPP Ping
    
    if bot.connect():
        bot.process(block=True)
