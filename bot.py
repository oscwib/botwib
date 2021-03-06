# -*- coding: utf-8 -*-

import Aan
from Aan.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, glob, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia
import requests
from gtts import gTTS
import goslate
from urllib import urlopen
import urllib2
import urllib3
import tempfile
import html5lib

cl = Aan.LINE()
cl.login(qr=True)
#cl.login(qr=True)
cl.loginResult()

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.loginResult()

#kc = LINETCR.LINE()
#kc.login(qr=True)
#kc.loginResult()

print "Login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 
╔═══════M.E.N.U 1════════
☆ Hi
☆ Me (Info Contact)
☆ Gift (Gift Thema)
☆ Ginfo (Group info)
☆ Welcome
☆ Cancel (cancel member pending)
☆ Tagall (Tag semua member)
☆ pp @ (lihat foto di tag)
☆ cover @ (lihat sampul di tag)
☆ Kedapkedip (text)
☆ Apakah (Text)
☆ /translate-en (txt) 
☆ /set (cek sider)
☆ /check (melihat sider)
☆ /lagu penyanyi)(judul)
☆ /lirik (penyanyi)(judul)
☆ /ig (username)
☆ /youtube (text)
☆ image (text)
☆ /say (text)
╚═══════M.E.N.U 1════════
☞ Creator (Pembuat Bot) """

KAC=[cl]
dmid = cl.getProfile().mid
#Amid = ki.getProfile().mid
#Bmid = kk.getProfile().mid
#Cmid = kc.getProfile().mid
Bots = [dmid]
admin = ["ube187443474747c3ec352e7efeb48c1b"]
owner = ["ube187443474747c3ec352e7efeb48c1b"]
creator = ["ube187443474747c3ec352e7efeb48c1b"]
Owner = ["ube187443474747c3ec352e7efeb48c1b"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    "lang":"JP",
    "comment":"",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}

setTime = {}
setTime = wait2['setTime']

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += '\n ☞ ' + Name
                    wait2['ROM'][op.param1][op.param2] = '☞ ' + Name
            else:
                pass

        if op.type == 13:
                if op.param3 in dmid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in dmid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
                if dmid in op.param3:
                    if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
                        print "Bot 1 Join"
                        cl.sendText(op.param1,'Hallo Come Back Kevin :)')
                    else:
                        print "Error"
                if Amid in op.param3:
                    if wait["autoJoin"] == True:
                        ki.acceptGroupInvitation(op.param1)
                        print "Bot 2 Join"
                    else:
                        print "Error"
                if Bmid in op.param3:
                    if wait["autoJoin"] == True:
                        kk.acceptGroupInvitation(op.param1)
                        print "Bot 3 Join"
                    else:
                        print "Error"
                if Cmid in op.param3:
                    if wait["autoJoin"] == True:
                        kc.acceptGroupInvitation(op.param1)
                        print "Bot 4 Join"
                    else:
                        print "Error"

        if op.type == 19:
                    if op.param3 in Bots:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[Bots])

        if op.type == 19:
                if dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if dmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(G)
#           random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
#               random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            elif wait["inviteprotect"] == True:
                cl.cancelGroupInvitation(op.param1,[op.param3])
#                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 not in Bots:
                    if op.param2 in Bots:
                        pass
                    elif wait["cancelprotect"] == True:
                        cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])

        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            elif wait["linkprotect"] == True:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
#                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
                cl.sendText(op.param1,"")

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ube187443474747c3ec352e7efeb48c1b":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 0:
                    if msg.to in wait2['readPoint']:
                        if msg.from_ in wait2["ROM"][msg.to]:
                            del wait2["ROM"][msg.to][msg.from_]
                    else:
                        pass
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"added")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"「 Name 」 :\n" + msg.contentMetadata["displayName"] + "\n「 Mid 」 :\n" + msg.contentMetadata["mid"] + "\n「 Status 」 :\n" + contact.statusMessage + "\n「 Profile 」 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n「 Cover 」 :\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"「 Name 」 :\n" + contact.displayName + "\n「 Mid 」 :\n" + msg.contentMetadata["mid"] + "\n「 Status 」 :\n" + contact.statusMessage + "\n「 Profile 」 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n「 Cover 」 :\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#----------------------------------------------------------------------------
#---------------------------- HELP COMMAND ----------------------------------
            elif msg.text.lower() in ["key","help","/help","/key"]:
                cl.sendText(msg.to,helpMessage)
            else:
                cl.sendText(msg.to,'Error.')
#----------------------------------------------------------------------------
#---------------------------- SPAM CHAT -------------------------------------
            elif "/spam " in msg.text:
                if msg.from_ in staff:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[1])
                    teks = msg.text.replace("/spam " + str(jmlh) + " ","")
                    if jmlh <= 999:
                        for x in range(jmlh):
                            cl.sendText(msg.to,teks)
#----------------------------------------------------------------------------
#---------------------------- CHANGE GROUP NAME -----------------------------
            elif "/gn " in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("/gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"It can't be used besides the group.")
#----------------------------------------------------------------------------
#-------------------------------- MID ---------------------------------------
            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
#----------------------------------------------------------------------------
#------------------------------- CREATOR ------------------------------------
            elif msg.text.lower() in ["creator","admin"]:
                msg.contentType = 13
                adm = 'ube187443474747c3ec352e7efeb48c1b'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Instagram : @dekaprabowoo\nLine : situ.sehat\nTwitter : -")
#----------------------------------------------------------------------------
#--------------------------------- GIFT -------------------------------------
            elif msg.text.lower() in ["gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '40ed630f-22d2-4ddd-8999-d64cef5e6c7d',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#----------------------------------------------------------------------------
#------------------------------ CANCEL PENDING ------------------------------
            elif msg.text.lower() in ["cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ OPEN URL ------------------------------------
            elif msg.text.lower() in ["ourl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ CLOSE URL -----------------------------------
            elif msg.text.lower() in ["curl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ GET GROUP LINK ------------------------------
            elif  msg.text.lower() in ["gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,x.name + " : line://ti/g/" + gurl)
                    print "[Command] Get Grup Link"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#------------------------------ GROUP INFO ----------------------------------
            elif msg.text.lower() in ["ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"「 Grup Name 」 :\n" + str(ginfo.name) + "\n「 Grup ID 」 :\n" + msg.to + "\n「 Grup Creator 」 :\n" + gCreator + "\n「 Grup Status 」 :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nTotal Anggota : " + str(len(ginfo.members)) + " Orang\nPending : " + sinvitee + " Orang")#URL : " + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"「 Grup Name 」 :\n" + str(ginfo.name) + "\n「 Grup ID 」 :\n" + msg.to + "\n「 Grup Creator 」 :\n" + gCreator + "\n「 Grup Status 」 :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Grup Only Boy")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#----------------------------------------------------------------------------
#---------------------------------- Invite -------------------------------------
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       cl.sendText(msg.to,"Grup Creator Telah Diinvite")
                       print "success inv gCreator"
                    except:
                       pass
#---------------------------------- Kalender -------------------------------------
            elif msg.text in ["/kalender"]:
	    	       wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	              cl.sendText(msg.to, "KALENDER\n\n" + (wait2['setTime'][msg.to]))
#---------------------------------- Time -------------------------------------
            elif msg.text in ["/time","/waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to,rst)
#---------------------------------- Quote ------------------------------------
            elif msg.text in ["/quote"]:
                quote = ['janji emang manis,tapi pahit tidak lakukan','ibu adalah malaikat tak bersayap','Barangsiapa yang suka meninggalkan barang di tempat umum maka ia akan kehilangan barangnya tersebut','Kunci KESUKSESAN itu cuma satu, yakni lu harus BERHASIL']
                rio = random.choice(quote)
                cl.sendText(msg.to,rio)
#---------------------------------- MID -------------------------------------
            elif msg.text.lower() in ["mid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                cl.sendText(msg.to,middd)
#----------------------------------------------------------------------------
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
#------------------------------ CHANGE NAME ---------------------------------
            elif "/cn " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/cn ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
#----------------------------------------------------------------------------
#------------------------------ CHANGE BIO ----------------------------------
            elif "/bio " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("/bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Done")
#----------------------------------------------------------------------------                    
            elif msg.text.lower() in ["contact on"]:
                if msg.from_ in admin:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact ON")
                        else:
                            cl.sendText(msg.to,"Contact ON")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact ON")
                        else:
                            cl.sendText(msg.to,"Contact ON")

            elif msg.text.lower() in ["contact off"]:
                if msg.from_ in admin:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact OFF")
                        else:
                            cl.sendText(msg.to,"Contact OFF")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Contact OFF")
                        else:
                            cl.sendText(msg.to,"Contact OFF")

            elif msg.text.lower() in ["join on"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin ON")
                        else:
                            cl.sendText(msg.to,"AutoJoin ON")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin ON")
                        else:
                            cl.sendText(msg.to,"AutoJoin ON")

            elif msg.text.lower() in ["join off"]:
                if msg.from_ in admin:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin OFF")
                        else:
                            cl.sendText(msg.to,"AutoJoin OFF")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"AutoJoin OFF")
                        else:
                            cl.sendText(msg.to,"AutoJoin OFF")

            elif msg.text in ["Gcancel:"]:
                if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text.lower() in ["leave on"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave ON")
                        else:
                            cl.sendText(msg.to,"Leave ON")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave ON")
                        else:
                            cl.sendText(msg.to,"Leave ON")

            elif msg.text.lower() in ["leave off"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave OFF")
                        else:
                            cl.sendText(msg.to,"Leave OFF")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Leave OFF")
                        else:
                            cl.sendText(msg.to,"Leave OFF")

            elif msg.text.lower() in ["protect on"]:
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection ON")
                        else:
                            cl.sendText(msg.to,"Protection ON")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection ON")
                        else:
                            cl.sendText(msg.to,"Protection ON")

            elif msg.text.lower() in ["protect off"]:
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection OFF")
                        else:
                            cl.sendText(msg.to,"Protection OFF")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection OFF")
                        else:
                            cl.sendText(msg.to,"Protection OFF")

            elif msg.text.lower() in ["qr on"]:
                if msg.from_ in admin:
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr ON")
                        else:
                            cl.sendText(msg.to,"Protection Qr ON")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr ON")
                        else:
                            cl.sendText(msg.to,"Protection Qr ON")

            elif msg.text.lower() in ["qr off"]:
                if msg.from_ in admin:
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr OFF")
                        else:
                            cl.sendText(msg.to,"Protection Qr OFF")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Qr OFF")
                        else:
                            cl.sendText(msg.to,"Protection Qr OFF")

            elif msg.text.lower() in ["invite on"]:
                if msg.from_ in admin:
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite ON")
                        else:
                            cl.sendText(msg.to,"Protection Invite ON")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite ON")
                        else:
                            cl.sendText(msg.to,"Protection Invite ON")

            elif msg.text.lower() in ["invite off"]:
                if msg.from_ in admin:
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Protection Invite OFF")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Protection Invite OFF")

            elif msg.text.lower() in ["cancel on"]:
                if msg.from_ in admin:
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection ON")
                        else:
                            cl.sendText(msg.to,"Cancel Protection ON")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection ON")
                        else:
                            cl.sendText(msg.to,"Cancel Protection ON")

            elif msg.text.lower() in ["cancel off"]:
                if msg.from_ in admin:
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
                        else:
                            cl.sendText(msg.to,"Cancel Protection Invite OFF")
#------------------------------ STATUS BOT ----------------------------------
            elif "/status" in msg.text.lower():
                md = ""
                if wait["contact"] == True: md+="[*] Contact : on\n"
                else: md+="[*] Contact : off\n"
                if wait["autoJoin"] == True: md+="[*] Auto join : on\n"
                else: md +="[*] Auto join : off\n"
                if wait["leaveRoom"] == True: md+="[*] Auto leave : on\n"
                else: md+="[*] Auto leave : off\n"
                if wait["autoAdd"] == True: md+="[*] Auto add : on\n"
                else:md+="[*] Auto add : off\n"
                if wait["protect"] == True: md+="[*] Protect : on\n"
                else:md+="[*] Protect : off\n"
                if wait["linkprotect"] == True: md+="[*] Link Protect : on\n"
                else:md+="[*] Link Protect : off\n"
                if wait["inviteprotect"] == True: md+="[*] Invite Protect : on\n"
                else:md+="[*] Invite Protect : off\n"
                if wait["cancelprotect"] == True: md+="[*] Cancel Protect : on"
                else:md+="[*] Cancel Protect : off"
                cl.sendText(msg.to,md)
#----------------------------------------------------------------------------
#---------------------------- GROUP ID / LIST--------------------------------
            elif msg.text.lower() in ["/grup id"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[*] %s\n%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)

            elif msg.text.lower() in ["/list grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[*] %s \n" % (cl.getGroup(i).name + " : " + str(len(cl.getGroup(i).members)) + " Members")
                    cl.sendText(msg.to,"「List Group」\n" + h + "Total Group : " + str(len(gid)))
#----------------------------------------------------------------------------
#------------------------------ CANCEL GROUP --------------------------------
            elif msg.text.lower() in ["cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Done")
                else:
                    cl.sendText(msg.to,"Nothing invite.")
#----------------------------------------------------------------------------
#------------------------------- JOIN GROUP ---------------------------------
            elif msg.text.lower() in ["join"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "[Command] Join"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#----------------------------------------------------------------------------
#-------------------------------- OUT GROUP ---------------------------------
            elif msg.text.lower() in ["bye"]:
                if msg.toType == 2:
                  if msg.from_ in staff:
                    print "[Command] Bye"
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
#----------------------------------------------------------------------------
#------------------------------ BROADCAST PC --------------------------------
            elif "/bc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bc ", "")
                    orang = cl.getAllContactIds()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Contact"
#----------------------------------------------------------------------------
#----------------------------- BROADCAST Group ------------------------------
            elif "/bcgc " in msg.text:
                if msg.from_ in admin:
                    broadcasttxt = msg.text.replace("/bcgc ", "")
                    orang = cl.getGroupIdsJoined()
                    for manusia in orang:
                        cl.sendText(manusia,(broadcasttxt))
                        print "[Command] BC Grup"
#----------------------------------------------------------------------------
#-------------------------------- WELCOME -----------------------------------
            if msg.text.lower() in ["wc","welcome"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
#----------------------------------------------------------------------------
#------------------------------- KICK BY TAG --------------------------------
            elif "nk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                      print "[Command] Kick"
                   except:
                      pass
#----------------------------------------------------------------------------
#------------------------------ BAN BY TAG ----------------------------------
            elif "/ban " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Banned")
                            print "[Command] Bannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#------------------------------- UNBAN BY TAG -------------------------------
            elif "/unban " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[Command] Unbannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#----------------------------- TAG ALL MEMBER -------------------------------
            if msg.text.lower() in ["tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "Done : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
#----------------------------------------------------------------------------
#------------------------------- CHECK SIDER --------------------------------
            if msg.text.lower() in ["/set"]:
                if msg.toType == 2:
                    cl.sendText(msg.to, "Point Set ♪")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "[Command] Set"

            if msg.text.lower() in ["/check"]:
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print "[Command] Check"
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "✔ Read : %s\n\n✖ Sider :\n%s\nPoint creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "[Command] Set"
                    else:
                        cl.sendText(msg.to,"Read point tidak tersedia, Silahkan ketik /set untuk membuat Read point.")
#----------------------------------------------------------------------------
#------------------------------- COVER BY TAG -------------------------------
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#----------------------------------------------------------------------------
#-------------------------------- PP BY TAG ---------------------------------
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
#----------------------------------------------------------------------------
#--------------------------------- HI / HAI ---------------------------------
            elif msg.text.lower() in ["hi","hai","hy"]:
                if msg.from_ in admin:
                    beb = "Hi Beb " + cl.getContact(msg.from_).displayName #+ " 􀸂􀆇starry heart􏿿"
                    kk.sendText(msg.to,beb)
                else:
                    hi = "Hi " + cl.getContact(msg.from_).displayName
                    cl.sendText(msg.to,hi)
#----------------------------------------------------------------------------
#--------------------------------- DUGEM ------------------------------------
            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#----------------------------------------------------------------------------
#--------------------------------- Remove Chat ------------------------------
            elif "/removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#----------------------------------------------------------------------------
#------------------------------- Kerang Ajaib -------------------------------
            elif "Apakah " in msg.text.lower():
                apk = msg.text.replace("Apakah ","")
                rnd = ['Ya','Tidak']
                p = random.choice(rnd)
                cl.sendText(msg.to,p)
                print "[Command] Kerang Ajaib"

            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya " + tanya + "adalah " + jawaban + " Banyak banyak tobat Nak ")

	          elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("0%","20%","40%","50%","60%","Tak ada")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")
#----------------------------------------------------------------------------
#---------------------------------- SONG ------------------------------------
            elif "/lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"

            elif "/lagu " in msg.text.lower():
                songname = msg.text.replace("/lagu ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"Judul : " + song[0] + "\nDurasi : " + song[1])
                    cl.sendAudioWithURL(msg.to,song[3])
                    print "[Command] Lagu"
#----------------------------------------------------------------------------
#--------------------------------- INSTAGRAM --------------------------------
            elif "/ig " in msg.text.lower():
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig ","")
                nk1 = nk0.rstrip('  ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"Profile "+username+"\n\nUsername : "+username+"\nFull Name : "+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"Not Found...")
                else:
                    cl.sendText(msg.to,"Contoh /ig hairu.ones")
#----------------------------------------------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif "/youtube " in msg.text:
                query = msg.text.replace("/youtube ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
            elif "/translate-en " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/translate-id " in msg.text:
                txt = msg.text.replace("/translate-en ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    cl.sendText(msg.to,'Error.')
#----------------------------------------------------------------------------    
#--------------------------------- Image ------------------------------------        
            elif "image " in msg.text:
                search = msg.text.replace("image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
#--------------------------------- /Say ------------------------------------   
	           elif "/say " in msg.text:
                 psn = msg.text.replace("/say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
#--------------------------------- ABSEN ------------------------------------
            elif msg.text.lower() in ["absen"]:
                cl.sendText(msg.to,"Siap Boy 􀜁􀅹Salute􏿿")
                ki.sendText(msg.to,"Siap Boy  􀜁􀅹Salute􏿿")
                kk.sendText(msg.to,"Siap Boy 􀜁􀅹Salute􏿿")
                kc.sendText(msg.to,"Siap Boy 􀜁􀅹Salute􏿿")
#----------------------------------------------------------------------------
#------------------------------ RESPON SPEED --------------------------------
            elif msg.text.lower() in ["sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "Respon : %s00000 /Detik" % (elapsed_time))
#----------------------------------------------------------------------------
#---------------------------- CEK BAN LIST ----------------------------------
            elif msg.text.lower() in ["banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "[*] " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
#----------------------------------------------------------------------------
#------------------------- CEK BAN LIST ( MID ) -----------------------------
            elif msg.text.lower() in ["banlist mid"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
#----------------------------------------------------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            		#ki.sendText(msg.to,text)
            		#kc.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            			#ki.sendMessage(msg)
            			#kc.sendMessage(msg)
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
#-------------------------------- KILL BAN ----------------------------------
            elif msg.text.lower() in ["kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        pass
#----------------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        pass


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
