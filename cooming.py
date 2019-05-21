
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
#cl.login(token="token")
cl.loginResult()

c2 = Aan.LINE()
#c2.login(token="token")
c2.loginResult()

c3 = Aan.LINE()
#c3.login(token="token")
c3.loginResult()

c4 = cl
c5 = c1
c6 = c2

#c4 = Aan.LINE()
#c4.login(token="token")
#c4.loginResult()

#c5 = Aan.LINE()
#c5.login(token="")
#c5.loginResult()

#c6 = Aan.LINE()
#c6.login(token="EoQWRbeN7FPR5gzhOyvb.VHH0q0Dhr8pSns5/+RsmgW.CPUNaL2uPZmGbAAiahXHnSxhdOxPEABgVlFFTtNKPvw=")
#c6.loginResult()

print "_________________________________"
print "=======[BOT Login Success]======="
print "_________________________________"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔══════════════════════
║ ✟.M.E.N.U   H.E.L.P✟   
╔══════════════════════
╠ ◆ Turn on/off - 「Command on/off」
╠ ◆ Command -「Look Command」
╠ ◆ Protect/help -「Protect Help」
╠ ◆ Private/help -「Private Help」
╠ ◆ Bot/help -「Bot Set Command」
╠ ◆ Anti/help -「Anti Command」
╠ ◆ Ban/help -「Ban Command」
╠ ◆ Pesan/help -「Sett Message」
╠══════════════════════
║NB: Gunakan Rasa Dewasa & Bijak
╚══════════════════════
"""
command ="""
╔══════════════════════
║  ✟ C.O.M.M.A.N.D ✟   
╔══════════════════════
╠ ♟ Me
╠ ♟ Mymid
╠ ♟ Broadcast:
╠ ♟ Spam on/off
╠ ♟ Speed
╠ ♟ Backup
╠ ♟ (2-6)Remove/pesan
╠ ♟ Remove/pesan
╠ ♟ Backup/all
╠ ♟ Bot/restart
╠ ♟ Dellpesan
╠ ♟ Myname:
╠ ♟ Mybio:
╠══════════[[Search Tools]]
╠ ♟ Image:
╠ ♟ Lirik:
╠ ♟ Youtube:
╠ ♟ Wikipedia:
╠ ♟ Reggae:
╠ ♟ Music:
╠ ♟ Lagu:
╠ ♟ Play:
╠ ♟ Instagram:
╠══════════[[Work With URL]]
╠ ♟ Getvideo: 
╠ ♟ Getimage: 
╠ ♟ Getaudio: 
╠ ♟ Unduh/yt:
╠══════════[[Work With Mid]]
╠ ♟ Invite:
╠ ♟ Kick:
╠ ♟ Contact:
╠ ♟ Clone:
╠ ♟ Cloning:
╠══════════[[Group Tools]]
╠ ♟ Gcreator
╠ ♟ Clone group
╠ ♟ Cloning group
╠ ♟ Recover
╠ ♟ Buatgrup:
╠ ♟ Mention
╠ ♟ Lurking
╠ ♟ Result
╠ ♟ Gurl
╠ ♟ Gname
╠ ♟ Gidlist
╠ ♟ Url on/off
╠ ♟ Undangke:
╠ ♟ Cancel
╠ ♟ Ginfo
╠ ♟ Glist
╠ ♟ Grupbc:
╠ ♟ Link on
╠ ♟ Link off
╠ ♟ Ratakan
╠ ♟ Grup image
╠══════════[[Ban Function]]
╠ ♟ Unban @
╠ ♟ Ban @
╠ ♟ Unban on/off
╠ ♟ Ban on/off
╠ ♟ Banlist
╠ ♟ Banlist mid
╠ ♟ Clear ban
╠ ♟ Sikat ban
╠══════════[[Clone Mention]]
╠ ♟ Clone @
╠ ♟ 2/clone @
╠ ♟ 3/clone @
╠ ♟ 4/clone @
╠ ♟ 5/clone @
╠ ♟ 6/clone @
╠ ♟ Clone/all @
╠══════════[[With Mention]]
╠ ♟ Mid @
╠ ♟ Kick @
╠ ♟ Clone @
╠ ♟ Clone/all @
╠ ♟ Getpp @
╠ ♟ Getcover @
╠ ♟ Getvidpp @
╠ ♟ Getvidcover @
╠ ♟ Getname @
╠ ♟ Getmid @
╠ ♟ Getbio @
╠ ♟ Getinfo @
╠══════════[[Status]]
╠ ♟ Anti/status
╠ ♟ Bot/status
╠ ♟ Private/status
╠ ♟ Ban/status
╠ ♟ Fitur/status
╠══════════════════════
║____ [Creator By Lips D3BL3NK] ____
║███■__ T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ __■███
╚══════════════════════

Note : Huftttt.... Cape Anjayyy Gw Ngerakit Ulang Nge Fixed Sama Add New Fiture... _- Kalo ada yg kagaa aktif commandnya Brarti Ituu Lgi Dalam Prosess... Btw Gw Blon Ada Vps Haha... Donate Dong Yg Bae....
Lips D3BL3NK BOT
 """

private ="""
║  ✟ P.R.I.V.A.T.E ✟   ║

╔══════════════════════
╠═══ [ Admin Add/Dell/List ] ════
╠══════════════════════
╠ ♛ Admin add @「With Mention」
╠ ♛ Admin dell @「With Mention」
╠ ♛ Addadmin on「With Contact」
╠ ♛ Delladmin on「With Contact」
╠ ♛ Addadmin off「With Contact」
╠ ♛ Delladmin off「With Contact」
╠ ♛ Adminlist
╠══════════════════════
╠════ [ Staff Add/Dell/List ] ════
╠══════════════════════
╠ ♛ Staff add @ 「With Mention」
╠ ♛ Staff dell @ 「With Mention」
╠ ♛ Addstaff on「With Contact」
╠ ♛ Dellstaff on「With Contact」
╠ ♛ Addstaff off「With Contact」
╠ ♛ Dellstaff off「With Contact」
╠ ♛ Stafflist
╠══════════════════════
║____ [Creator By Lips D3BL3NK] ____
║███■__ T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ __■███
╚══════════════════════
 """
 
plotek ="""
╔══════════════════════
║  ✟ P.R.O.T.E.C.T ✟   
╔══════════════════════
╠ ♚ Easy mode
╠ ♚ Hard mode
╠ ♚ Protect on
╠ ♚ Linkprotect on/off	   
╠ ♚ Inviteprotect on/off 
╠ ♚ Cancelprotect on/off
╠ ♚ Joinprotect on/off
╠══════════════════════
║____ [Creator By Lips D3BL3NK] ____
║███■__ T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ __■███
╚══════════════════════
"""
banmode ="""
╔══════════════════════
║   ✟ BAN SETTING ✟   
╔══════════════════════
╠ 🏴 Bancontact on/off
╠ 🏴 Bangambar on/off
╠ 🏴 Banlink on/off
╠ 🏴 Banvideo on/off
╠ 🏴 Banaudio on/off
╠ 🏴 Bansticker on/off
╠══════════════════════
║____ [Creator By Lips D3BL3NK] ____
║███■__ T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ __■███
╚══════════════════════
"""

pesen ="""
╔══════════════════════
║  ✟ PESAN SETTING ✟   
╔══════════════════════
╠ ✍͡ Pesanqr set:
╠ ⇨ Pesanqr
╠ ✍͡ Pesanjoin set:
╠ ⇨ Pesanjoin
╠ ✍͡ Pesankick set:
╠ ⇨ Pesankick
╠ ✍͡ Pesanjoin set:
╠ ⇨ Pesanjoin
╠ ✍͡ Pesansambut set:
╠ ⇨ Pesansambut
╠ ✍͡ Pesanleave set:
╠ ⇨ Pesanleave
╠ ✍͡ Pesanlike set:
╠ ⇨ Pesanlike
╠ ✍͡ Pesantag set:
╠ ⇨ Pesantag
╠══════════════════════
║____ [Creator By Lips D3BL3NK] ____
║███■__ T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ __■███
╚══════════════════════
"""

antimode ="""
╔══════════════════════
║  ✟ ANTI SETTING ✟   
╔══════════════════════
╠ ★ Anticontact
╠ ★ Antigambar on/off
╠ ★ Antivideo on/off
╠ ★ Antiaudio on/off
╠ ★ Antisticker on/off
╠ ★ Antilink on/off
╠══════════════════════
║____ [Creator By Lips D3BL3NK] ____
║███■__ T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ __■███
╚══════════════════════
"""

KAC=[cl,c2,c3,c4,c5,c6]
mid = cl.getProfile().mid
mid2 = c2.getProfile().mid
mid3 = c3.getProfile().mid
mid4 = c4.getProfile().mid
mid5 = c5.getProfile().mid
mid6 = c6.getProfile().mid

Bots = [mid,mid2,mid3,mid4,mid5,mid6]
admin = ["ube187443474747c3ec352e7efeb48c1b"]
owner = "ube187443474747c3ec352e7efeb48c1b"
staff = [admin,"ube187443474747c3ec352e7efeb48c1b"]
team = [mid,mid2,mid3,mid4,mid5,mid6,admin,staff]
blenk = random.choice(KAC)

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"Cie Udah Add, Salken Ya  \n\nChat Aja Engga Ganggu Ko",
    "lang":"JP",
    "comment":"Auto Like By T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ \n\nCreator : line://ti/p/~yud.xx",
    "commentOn":False,
    "invite":{},
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    }

protect = {
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "joinprotect":False,
    "kickbanlist":False,
}

private = {
    "addstaff":False,
    "dellstaff":False,
    "addadmin":False,
    "delladmin":False,
    "botoff":False,
}

fitur = {
    "undangadmin":True,
    "likeOn":False,
    "respontag":True,
    "sambutjoin":True,
    "autongoceh":True,
    "ngocehinvite":True,
    "ngocehleave":True,
    "ngocehread":True,
    "ngocehjoin":True,
    "ngocehkick":True,
    "ngocehcancel":True,
    "ngocehQR":True,
}

oceh = {
    "pesanQR":"Jangan Maenin QR yak sayy :* Ntar aq kick tau rasa ajaa.... :* ",
    "pesanjoin":"Salken semuaa.... :*",
    "pesansambut":"Welcome to this group.... Sans ajee disini... Lu berbaur ajaa... Asal jangan coli",
    "pesancancel":"Duhh sayy.... jangan Asal cancel dong.... Mau di geng beng yakk??... ",
    "pesankick":"Waduhh ada yg di kick..... Bila itu baik ( babayyy.... :v ).... Bila Negatif ( Kasiann ntuh orang.....:( )",
    "pesanleave":"Cya ilaahhh make kluar sgala....",
    "pesantag":"Jangan nge tag yaa sayy.... Pc aja yaa sayy :* ",
    "pesanlike":"Auto Like By Lips D3BL3NK \n Suport By T⃟E⃟A⃟M⃟ ᴄᴀᴄᴀᴅ ᴮᴼᵀˢ \n Pegasus Team Bot \n Tora Team \n Invoker Team Bot \n "
    "pesanspam":"Spammed!!!",
}

anti = {
    "antigambar":False, 
    "antivideo":False,
    "antisticker":False,
    "antiaudio":False,
    "anticontact":False,
    "antilink":False,
}

ban = {
    "bancontact":False, 
    "bangambar":False,
    "banvideo":False,
    "bansticker":False,
    "banlink":False,
    "banaudio":False,
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    }
    
mimic = {
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

ruang=op.param1
pelaku=op.param2
korban=op.param3

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Bots:
                        G = blenk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        Ticket = blenk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        blenk.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                if op.param3 in mid2:
                    if op.param2 in Bots:
                        G = blenk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        Ticket = blenk.reissueGroupTicket(op.param1)
                        c2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        blenk.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                if op.param3 in mid3:
                    if op.param2 in Bots:
                        G = blenk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        Ticket = blenk.reissueGroupTicket(op.param1)
                        c3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        blenk.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                if op.param3 in mid4:
                    if op.param2 in Bots:
                        G = blenk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        Ticket = blenk.reissueGroupTicket(op.param1)
                        c4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        blenk.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                if op.param3 in mid5:
                    if op.param2 in Bots:
                        G = blenk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        Ticket = blenk.reissueGroupTicket(op.param1)
                        c5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        blenk.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                if op.param3 in mid6:
                    if op.param2 in Bots:
                        G = blenk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        Ticket = blenk.reissueGroupTicket(op.param1)
                        c6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        blenk.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

         if op.type == 13:
             if mid in op.param3:
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
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
 #--------------------------------------------- [ Protect Type] 
        if op.type == 19:
            if op.param3 in mid:
                if op.param2 not in team:
                	try:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                    except:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            if op.param3 in mid2:
                if op.param2 not in team:
                	try:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                    except:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            if op.param3 in mid3:
                if op.param2 not in team:
                	try:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                    except:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            if op.param3 in mid4:
                if op.param2 not in team:
                	try:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                    except:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            if op.param3 in mid5:
                if op.param2 not in team:
                	try:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                    except:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            if op.param3 in mid6:
                if op.param2 not in team:
                	try:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                    except:
                        print "[ Kerjasama ] Start Backup "
                	    blenk.kickoutFromGroup(op.param1,[op.param2])
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        blenk.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = blenk.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
        if op.type == 19:
            if op.param2 not in team:
                elif wait["protect"] == True:
                       wait ["blacklist"][op.param2] = True
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in team:
                elif wait["inviteprotect"] == True:
                       wait ["blacklist"][op.param2] = True
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if protect["kickbanlist"] == True:
                    blenk.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 not in team:
                if wait["joinprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    blenk.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 32:
            if op.param2 not in team:
                if wait["cancelprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    blenk.cancelGroupInvitation(op.param1,[op.param3])
                    blenk.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 11:
	        if op.param2 not in team:
               elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 14:
            if op.param2 in admin:
                if wait["undangadmin"] == True:
                    blenk.inviteIntoGroup(op.param1,admin)
#---------------------------------------------------[ Auto Kerjasama Team ]
        if op.type == 19:
            if op.param3 in mid:
                if op.param2 not in team:
                    blenk.kickoutFromGroup(op.param1,[op.param2])
                    blenk.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in mid2:
                if op.param2 not in team:
                    blenk.kickoutFromGroup(op.param1,[op.param2])
                    blenk.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in mid3:
                if op.param2 not in team:
                    blenk.kickoutFromGroup(op.param1,[op.param2])
                    blenk.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in mid4:
                if op.param2 not in team:
                    blenk.kickoutFromGroup(op.param1,[op.param2])
                    blenk.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in mid5:
                if op.param2 not in team:
                    blenk.kickoutFromGroup(op.param1,[op.param2])
                    blenk.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in mid6:
                if op.param2 not in team:
                    blenk.kickoutFromGroup(op.param1,[op.param2])
                    blenk.inviteIntoGroup(op.param1,[op.param3])
#---------------------------------------------------[ Auto On Protect Jika Bot Di Kick ]
        if op.type == 19:
            if op.param3 in team:
              protect["protect"] == True
        if op.type == 19:
            if op.param3 in staff or op.param3 in Bots or op.param3 in admin:
              protect["inviteprotect"] == True
        if op.type == 19:
            if op.param3 in staff or op.param3 in Bots or op.param3 in admin:
              protect["joinprotect"] == True
        if op.type == 19:
            if op.param3 in staff or op.param3 in Bots or op.param3 in admin:
              protect["linkprotect"] == True
        if op.type == 19:
            if op.param3 in staff or op.param3 in Bots or op.param3 in admin:
               protect["cancelprotect"] == True
#--------------------------------------------------[ Backup Team Ketika Di Kick] 
        if op.type == 19:
            if op.param3 in team:
                blenk.kickoutFromGroup(op.param1,[op.param2])
                blenk.inviteIntoGroup(op.param1,[op.param3])
#---------------------------------------------------------------------
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in KAC:
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    blenk.updateGroup(G)
                    Ticket = blenk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    blenk.updateGroup(G)
                    Ticket =blenk.reissueGroupTicket(op.param1)
            if op.param3 in mid2:
                if op.param2 in KAC:
                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    c2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
            if op.param3 in mid3:
                if op.param2 in KAC:
                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    c3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
					
            if op.param3 in mid4:
                if op.param2 in KAC:
                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    c4.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
			
            if op.param3 in mid5:
                if op.param2 in KAC:
                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    c5.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
					
            if op.param3 in mid6:
                if op.param2 in KAC:
                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    c6.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
#-----------------------------------------------------------
#------------------------------------------------------------------------------------
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�����Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    c2.acceptGroupInvitationByTicket(op.param1,Ti)
                    c3.acceptGroupInvitationByTicket(op.param1,Ti)
                    c4.acceptGroupInvitationByTicket(op.param1,Ti)
                    c5.acceptGroupInvitationByTicket(op.param1,Ti)
                    c6.acceptGroupInvitationByTicket
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if mid2 in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�����Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    c2.acceptGroupInvitationByTicket(op.param1,Ti)
                    c3.acceptGroupInvitationByTicket(op.param1,Ti)
                    c4.acceptGroupInvitationByTicket(op.param1,Ti)
                    c5.acceptGroupInvitationByTicket(op.param1,Ti)
                    c6.acceptGroupInvitationByTicket
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid3 in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�����Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    c2.acceptGroupInvitationByTicket(op.param1,Ti)
                    c3.acceptGroupInvitationByTicket(op.param1,Ti)
                    c4.acceptGroupInvitationByTicket(op.param1,Ti)
                    c5.acceptGroupInvitationByTicket(op.param1,Ti)
                    c6.acceptGroupInvitationByTicket
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid4 in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�����Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    c2.acceptGroupInvitationByTicket(op.param1,Ti)
                    c3.acceptGroupInvitationByTicket(op.param1,Ti)
                    c4.acceptGroupInvitationByTicket(op.param1,Ti)
                    c5.acceptGroupInvitationByTicket(op.param1,Ti)
                    c6.acceptGroupInvitationByTicket
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid5 in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�����Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    c2.acceptGroupInvitationByTicket(op.param1,Ti)
                    c3.acceptGroupInvitationByTicket(op.param1,Ti)
                    c4.acceptGroupInvitationByTicket(op.param1,Ti)
                    c5.acceptGroupInvitationByTicket(op.param1,Ti)
                    c6.acceptGroupInvitationByTicket
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid6 in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                        blenk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client�����Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = blenk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    blenk.updateGroup(X)
                    Ti = blenk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    c2.acceptGroupInvitationByTicket(op.param1,Ti)
                    c3.acceptGroupInvitationByTicket(op.param1,Ti)
                    c4.acceptGroupInvitationByTicket(op.param1,Ti)
                    c5.acceptGroupInvitationByTicket(op.param1,Ti)
                    c6.acceptGroupInvitationByTicket
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

#---------------------------------------------------[ Bot Turn On/Off ]
        if op.type == 25:
        	msg = op.message
            elif msg.text in ["Bot off","Lips off","Turn off"]:
                if private["botoff"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    private["botoff"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Bot on","Lips on","Turn on"]:
                if private["botoff"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    private["botoff"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
        if op.type == 26:
        	msg = op.message
            if msg.from_ in admin or staff:
                elif msg.text in ["Bot off","Lips off","Turn off"]:
                    if private["botoff"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        private["botoff"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                elif msg.text in ["Bot on","Lips on","Turn on"]:
                    if private["botoff"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        private["botoff"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
#---------------------------------------------------[ Command Ketinggalan ]
#[Respon TAG SelfBot]
        if op.type == 26:
        	msg = op.message
            elif "@"+cl.getProfile().displayName in msg.text:
                 if fitur["respontag"] == True:
                     cl.sendText(msg.to,"██■___[Auto Respon Tag]___■██\n"+oceh["pesantag"])
                     msg.contentType = 13
                     msg.contentMetadata = {'mid': mid}
                     cl.sendMessage(msg)
                     cl.sendText(msg.to,"Tuh Kontaknya Kalo Penting PC")
#--------------------------------------------------------------------------
            elif msg.text.lower() == 'Bot/status':
                md = ""
                if wait["contact"] == True: md+="╔════════════════════\n╠ ☞ Contact →🚩\n"
                else: md+="╔════════════════════\n╠ ☞ Contact → 🏳\n"
                if wait["autoJoin"] == True: md+="╠ ☞ Auto Join → 🚩\n"
                else: md+="╠ ☞ Auto Join → 🏳\n"
                if wait["autoCancel"]["on"] == True:md+="╠ ☞ Auto cancel: " + str(wait["autoCancel"]["members"]) + " → 🚩\n"
                else: md+="╠ ☞ Group cancel → 🏳\n"
                if wait["leaveRoom"] == True: md+="╠ ☞ Auto leave →🚩\n"
                else: md+="╠ ☞ Auto leave → 🏳\n"
                if wait["timeline"] == True: md+="╠ ☞ share → 🚩\n"
                else:md+="╠ ☞ Share → 🏳\n"
                if wait["autoAdd"] == True: md+="╠ ☞ Auto add → 🚩\n"
                else:md+="╠ ☞ Auto add → 🏳\n"
                if wait["commentOn"] == True: md+="╠ ☞ Auto komentar →🚩\n╚════════════════════\n"
                else:md+="╠ ☞ Auto komentar → 🏳\n╚════════════════════\n"
                c2.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                c2.sendMessage(msg)
                c2.sendText(msg.to,"Hayuu Akrab Sama Creatornya... Baik Kok Dia Gak Gigit...")
                
            elif msg.text.lower() == 'Protect/status':
                md = ""
                if protect["protect"] == True: md+="╔════════════════════\n╠ ♚ Protect → 🚩\n"
                else:md+="╔════════════════════\n╠ ♚ Protect → 🏳\n"
                if protect["linkprotect"] == True: md+="╠ ♚ Link Protect → 🚩\n"
                else:md+="╠ ♚ Link Protect → 🏳\n"
                if protect["inviteprotect"] == True: md+="╠ ♚ Invite Protect → 🚩\n"
                else:md+="╠ ♚ Invite Protect → 🏳\n"
                if protect["joinprotect"] == True: md+="╠ ♚ Join Protect → 🚩\n"
                else:md+="╠ ♚ Join Protect → 🏳\n"
                if protect["cancelprotect"] == True: md+="╠ ♚ Cancel Protect →🚩\n╚════════════════════\n"
                else:md+="╠ ♚ Cancel Protect → 🏳\n╚════════════════════\n"
                c2.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                c2.sendMessage(msg)
                c2.sendText(msg.to,"Hayuu Akrab Sama Creatornya... Baik Kok Dia Gak Gigit...")

            elif msg.text.lower() == 'Private/status':
                md = ""
                if fitur["botoff"] == True: md+="[[___[[Bot Dalam Keadaan: Off]]___]]\n\n"
                else:md+="[[___[[Bot Dalam Keadaan: On]]___]]\n\n"
                if fitur["addadmin"] == True: md+="╔════════════════════\n╠ ◈ Like → 🚩\n"
                else:md+="╔════════════════════\n╠ ◈ Like → 🏳\n"
                if fitur["delladmin"] == True: md+="╠ ◈ Sambutjoin → 🚩\n"
                else:md+="╠ ◈ Sambutjoin → 🏳\n"
                if fitur["addstaff"] == True: md+="╠ ◈ Ngocehkick → 🚩\n"
                else:md+="╠ ◈ Ngocehkick → 🏳\n"
                if fitur["dellstaff"] == True: md+="╠ ◈ NgocehQR → 🚩\n╚════════════════════\n"
                else:md+="╠ ◈ NgocehQR → 🏳\n╚════════════════════\n"
                c2.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                c2.sendMessage(msg)
                c2.sendText(msg.to,"Hayuu Akrab Sama Creatornya... Baik Kok Dia Gak Gigit...")

            elif msg.text.lower() == 'Fitur/status':
                md = ""
                if fitur["likeOn"] == True: md+="╔════════════════════\n╠ ◈ Like → 🚩\n"
                else:md+="╔════════════════════\n╠ ◈ Like → 🏳\n"
                if fitur["sambutjoin"] == True: md+="╠ ◈ Sambutjoin → 🚩\n"
                else:md+="╠ ◈ Sambutjoin → 🏳\n"
                if fitur["respontag"] == True: md+="╠ ◈ Respontag → 🚩\n"
                else:md+="╠ ◈ Respontag → 🏳\n"
                if fitur["ngocehleave"] == True: md+="╠ ◈ Ngocehleave → 🚩\n"
                else:md+="╠ ◈ Ngocehleave → 🏳\n"
                if fitur["ngocehinvite"] == True: md+="╠ ◈ Ngocehinvite →🚩\n"
                else:md+="╠ ◈ Ngocehinvite → 🏳\n"
                if fitur["ngocehread"] == True: md+="╠ ◈ Ngocehread → 🚩\n"
                else:md+="╠ ◈ Ngocehread → 🏳\n"
                if fitur["ngocehjoin"] == True: md+="╠ ◈ Ngocehjoin → 🚩\n"
                else:md+="╠ ◈ Ngocehjoin → 🏳\n"
                if fitur["ngocehkick"] == True: md+="╠ ◈ Ngocehkick → 🚩\n"
                else:md+="╠ ◈ Ngocehkick → 🏳\n"
                if fitur["ngocehQR"] == True: md+="╠ ◈ NgocehQR → 🚩\n╚════════════════════\n"
                else:md+="╠ ◈ NgocehQR → 🏳\n╚════════════════════\n"
                c2.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                c2.sendMessage(msg)
                c2.sendText(msg.to,"Hayuu Akrab Sama Creatornya... Baik Kok Dia Gak Gigit...")

            elif msg.text.lower() == 'Ban/status':
                md = ""
                if ban["bancontact"] == True: md+="╔════════════════════\n╠ 🏴  Bancontact → 🚩\n"
                else:md+="╔════════════════════\n╠ 🏴 Bancontact → 🏳\n"
                if ban["bangambar"] == True: md+="╠ 🏴 Bangambar → 🚩\n"
                else:md+="╠ 🏴 Bangambar→ 🏳\n"
                if ban["banlink"] == True: md+="╠ 🏴 Banlink → 🚩\n"
                else:md+="╠ 🏴 Banlink→ 🏳\n"
                if ban["banvideo"] == True: md+="╠ 🏴 Banvideo → 🚩\n"
                else:md+="╠ 🏴 Banvideo → 🏳\n"
                if ban["bansticker"] == True: md+="╠ 🏴 Bansticker →🚩\n"
                else:md+="╠ 🏴 Bansticker → 🏳\n"
                if ban["banaudio"] == True: md+="╠ 🏴 Banaudio → 🚩\n╚════════════════════\n"
                else:md+="╠ 🏴 Banaudio → 🏳\n╚════════════════════\n"
                c2.sendText(msg.to,mad)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                c2.sendMessage(msg)
                c2.sendText(msg.to,"Hayuu Akrab Sama Creatornya... Baik Kok Dia Gak Gigit...")

            elif msg.text.lower() == 'Anti/status':
                md = ""
                if anti["anticontact"] == True: md+="╔════════════════════\n╠ 🚫 Anticontact → 🚩\n"
                else:md+="╔════════════════════\n╠ 🚫 Anticontact → 🏳\n"
                if anti["antilink"] == True: md+="╠ 🚫 Antilink → 🚩\n"
                else:md+="╠ 🚫 Antilink → 🏳\n"
                if anti["antigambar"] == True: md+="╠ 🚫 Antigambar → 🚩\n"
                else:md+="╠ 🚫 Antigambar → 🏳\n"
                if anti["antisticker"] == True: md+="╠ 🚫 Antisticker → 🚩\n"
                else:md+="╠ 🚫 Antisticker → 🏳\n"
                if anti["antiaudio"] == True: md+="╠ 🚫 Antiaudio →🚩\n"
                else:md+="╠ 🚫 Antiaudio → 🏳\n"
                if anti["antivideo"] == True: md+="╠ 🚫 Antivideo → 🚩\n╚════════════════════\n"
                else:md+="╠ 🚫 Antivideo → 🏳\n╚════════════════════\n"
                c2.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                c2.sendMessage(msg)
                c2.sendText(msg.to,"Hayuu Akrab Sama Creatornya... Baik Kok Dia Gak Gigit...")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                 if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
                if msg.from_ in admin:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Mid Send Contact Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Cek Mid Send Contact Off")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Auto Join off","Auto join:off","join off"]:
                if msg.from_ in admin or staff:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                if msg.from_ in admin or staff:
                    try:
                         strnum = msg.text.replace("Gcancel:","")
                         if strnum == "off":
                             wait["autoCancel"]["on"] = False
                             if wait["lang"] == "JP":
                                 cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                 cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])

#--------------------------------------------------------
#[ Auto Ngoceh Gak Jelas ]
            if fitur["autongoceh"] == True:
                lips = ["Kuntul","Apansi lu eyang subur","Bacot nih tukang colay","Yg benerr? Lu kan boong mulu... ","Monyet kok ngirim pesan yak?","Idihhh berukk napaa tuh?","Jangan percaya dia tukang boong","Jan mao sama dia.. mandi aja kaga pernah","Jan deketin dia begoo... dia kang sange.. ","Hmmm...","Lah lu Ngapaa semvak","Apaan... Bhak :v","Lah mulai dah boongnya kluar"]
                dblenk = random.choice(lips)
                blenk.sendText(msg.to,"{___[ Auto Ngoceh ]___}\n"+dblenk)
#[ Sambut Orang Join ]
        if op.type == 17:
            if fitur["sambutjoin"] == True:
        	    cl.sendMessage(op.param1,"Waduhh..."+cl.getContact(op.param2).displayName+" "+str(oceh["pesankick"]))
#[ Ngoceh Kalo Ada Yg Invite ]
        if op.type == 13:
            if fitur["ngocehinvite"] == True:
        	    cl.sendMessage(op.param1,"Waduhh..."+cl.getContact(op.param2).displayName+" "+str(oceh["pesankick"]))
#[ Ngoceh Kalo Ada yg Leave ]
        if op.type == 15:
            if fitur["ngocehleave"] == True:
        	    cl.sendMessage(op.param1,"Ett sob..."+cl.getContact(op.param2).displayName+" "+str(oceh["pesancancel"]))
#[ Ngoceh Pas Baru Join ]
        if op.type == 16:
            if fitur["ngocehjoin"] == True:
        	    cl.sendMessage(op.param1,"Ett sob..."+cl.getContact(op.param2).displayName+" "+str(oceh["pesancancel"]))
#[ Ngoceh Saat Ada Yg Kick ]
        if op.type == 19:
            if fitur["ngocehkick"] == True:
        	    cl.sendMessage(op.param1,"Waduhh..."+cl.getContact(op.param2).displayName+" "+str(oceh["pesankick"]))
#[ Ngoceh Saat Ada Yg Cancel Invite ]
        if op.type == 32:
            if fitur["ngocehcancel"] == True:
        	    cl.sendMessage(op.param1,"Ett sob..."+cl.getContact(op.param2).displayName+" "+str(oceh["pesancancel"]))
#[ Ngoceh Saat Ada Yg Ubah QR ]
        if op.type == 11:
            if fitur["ngocehQR"] == True:
                cname = cl.getContact(op.param2).displayName
                blenk.sendText(op.param1,cname + str(oceh["pesanqr"]))
		#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in team:
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).updateGroup(G)
        #------Open QR Kick finish-----#
        #------Open QR Kick start------#
        if op.type == 10:
            if wait["linkprotect"] == True:
                if op.param2 not in team:
                    G = blenk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    blenk.kickoutFromGroup(op.param1,[op.param2])
                    blenk.updateGroup(G)
        if op.type == 19:
            if team in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
#------------------------------------------------[ SelfBot ]
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ in admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
#-------------------------------------[ INVITE ]
            if msg.contentType == 13:
            	if wait["invite"] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                             break
                         elif invite in wait["blacklist"]:
                             c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                             c2.sendText(msg.to,"Unban: " + invite)
                             break                             
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 c2.findAndAddContactsByMid(target)
                                 c2.inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite: \n➡" + _name)
                                 wait["invite"] = False
                                 break                              
                             except:             
                                      c2.sendText(msg.to,"Error")
                                      wait["invite"] = False
                                      break
#---------------------------------------[ Add Staff ]
            	if private["addstaff"] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                             break
                         elif invite in wait["blacklist"]:
                             c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                             c2.sendText(msg.to,"Unban: " + invite)
                             break                             
                         else:
                             targets.append(invite)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Admin LipsBOT Success Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add by contact executed"
                else:
                    cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed")
#---------------------------------------[ Remove Staff ]
            	if private["dellstaff"] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                             break
                         elif invite in wait["blacklist"]:
                             c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                             c2.sendText(msg.to,"Unban: " + invite)
                             break                             
                         else:
                             targets.append(invite)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Success Remove Admin LipsBOT.... ")
                            except:
                                pass
                    print "[Command]Staff remove by contact executed"
                else:
                    cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed ")
#---------------------------------------[ Add Admin ]
            	if private["addadmin"] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                             break
                         elif invite in wait["blacklist"]:
                             c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                             c2.sendText(msg.to,"Unban: " + invite)
                             break                             
                         else:
                             targets.append(invite)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin LipsBOT Success Ditambahkan")
                            except:
                                pass
                    print "[Command] Admin add by contact executed"
                else:
                    cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed")
#---------------------------------------[ Remove Admin ]
            	if private["delladmin"] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                             break
                         elif invite in wait["blacklist"]:
                             c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                             c2.sendText(msg.to,"Unban: " + invite)
                             break                             
                         else:
                             targets.append(invite)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Success Remove Admin LipsBOT.... ")
                            except:
                                pass
                    print "[Command] Admin remove by contact executed"
                else:
                    cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed ")
#-----------------------------------------
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = c2.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        c2.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = c2.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = c2.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        c2.sendText(msg.to,"=======[displayName]=======\n" + contact.displayName + "\=========[mid]========\n" + msg.contentMetadata["mid"] + "\n=======[statusMessage]=======:\n" + contact.statusMessage + "\n=======[pictureStatus]=======\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n=======[coverURL]=======\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "========[URL]=========\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#-----------------------------------------------[ Help Command ] 
            elif msg.text in ["help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage) #ada
            elif msg.text in ["Bot/help","bot/help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,bot)
                else:
                    cl.sendText(msg.to,bot)
            elif msg.text in ["Protect/help","protect"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,plotek)
                else:
                    cl.sendText(msg.to,plotek) #ada
            elif msg.text in ["Ban/help","ban/help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,banmode)
                else:
                    cl.sendText(msg.to,banmode) #ada
            elif msg.text in ["Anti/help","anti/help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,antimode)
                else:
                    cl.sendText(msg.to,antimode) #ada
            elif msg.text in ["Pesan/help","pesan/help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,pesen)
                else:
                    cl.sendText(msg.to,pesen) #ada
#-----------------------------------------------[ Mix Command ] 
#Hapus Pesan Biar Gak Loadchat
            elif msg.text == "2Remove/pesan":
            	if msg.from_ in admin or staff:
                    c2.removeAllMessages(op.param2)
            elif msg.text == "3Remove/pesan":
            	if msg.from_ in admin or staff:
                    c3.removeAllMessages(op.param2)
            elif msg.text == "4Remove/pesan":
            	if msg.from_ in admin or staff:
                    c4.removeAllMessages(op.param2)
            elif msg.text == "5Remove/pesan":
            	if msg.from_ in admin or staff:
                    c5.removeAllMessages(op.param2)
            elif msg.text == "6Remove/pesan":
            	if msg.from_ in admin or staff:
                    c6.removeAllMessages(op.param2)
            elif msg.text == "Remove/pesan":
                c2.sendText(msg.to,"Wait boss....")
                c2.removeAllMessages(op.param2)
                c3.removeAllMessages(op.param2)
                c4.removeAllMessages(op.param2)
                c5.removeAllMessages(op.param2)
                c6.removeAllMessages(op.param2)
                c2.sendText(msg.to, "Clearr bosss")
            elif msg.text == "Kedapkedip: ":
                txt = msg.text.replace("Kedapkedip: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            elif msg.text == "Clone group":
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                lips = cl.getGroup(msg.to)
                deblenk = str(lips.name)
                path = "http://dl.profile.line-cdn.net/" + lips.pictureStatus
                blenks = path
                cl.createGroup(deblenk, blenks, mi_d)
                cl.sendText(msg.to,"Success Clone Group....")
            else:
                cl.sendText(msg.to,"Pleasee Use Command Cloning.....")
            elif msg.text in ["Ginfo","Group info","ginfo","Grup info","grup info","Group info"]:
                group = cl.getGroup(msg.to)
                try:
                    gCreator = group.creator.displayName
                except:
                    gCreator = "Error"
                md = "[[____[ Nama Grup ]____]]\n" + group.name + "\n\n[[____[ ID Grup ]___]]\n" + group.id + "\n\n[[____[ Pembuat Grup ]____]]\n" + gCreator + "\n\n[[___[ Link Gambar Grup ]__]]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                else: md += "\n\nKode Url : Diblokir"
                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                cl.sendText(msg.to,md)
            elif msg.text == "My/Cloning group":
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                lips = cl.getGroup(msg.to)
                deblenk = str(lips.name)
                cl.createGroup(deblenk, mi_d)
                cl.sendText(msg.to,"Success Clone Group....")
            elif msg.text == "My/Recover":
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.createGroup("Recover", mi_d)
                cl.sendText(msg.to,"Success recover")
            else:
                cl.sendText(msg.to,"Waduhh Gabisa Bang... Fixed Dong... Kan jago :v")
            elif msg.text == "My/Buat group: ":
                LipsD3BL3NK = msg.text.replace("Buat group: ","")
                MyName = LipsD3BL3NK
                cl.createGroup(MyName)
                cl.sendText(msg.to,"Success buat grup")
                cl.inviteIntoGroup(op.param1,[team])
            else:
                cl.sendText(msg.to,"Waduhh Gabisa Bang... Fixed Dong... Kan jago :v")
            elif msg.text == "My/Group image":
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            if msg.text in ["My/Mentionall"]:
                if msg.from_ in admin or staff:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                     mention(msg.to, nama)
                  if jml > 100 and jml < 200:
                     for i in range(0, 99):
                         nm1 += [nama[i]]
                     mention(msg.to, nm1)
                     for j in range(100, len(nama)-1):
                         nm2 += [nama[j]]
                     mention(msg.to, nm2)
                  if jml > 200  and jml < 500:
                     for i in range(0, 99):
                         nm1 += [nama[i]]
                     mention(msg.to, nm1)
                     for j in range(100, 199):
                         nm2 += [nama[j]]
                     mention(msg.to, nm2)
                     for k in range(200, 299):
                         nm3 += [nama[k]]
                     mention(msg.to, nm3)
                     for l in range(300, 399):
                         nm4 += [nama[l]]
                     mention(msg.to, nm4)
                     for m in range(400, len(nama)-1):
                         nm5 += [nama[m]]
                     mention(msg.to, nm5)
                  if jml > 500:
                     cl.sendText(msg.to, "Anggotanya 500+ waha")
                     print "Terlalu Banyak Mem 500+"
                 cnt = Message()
                 cnt.text = "Jumlah member:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
            elif msg.text == "My/name: ":
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 20000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)
            elif msg.text == "My/bio: ":
            	if msg.from_ in admin:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 20000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.sendText(msg.to,"Sebentar boss kita laksanakan..."
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio Menjadi :\n" + string +"\n Telah Succes Boss...")
            elif msg.text == "My/Gname: ":
                if msg.from_ in admin or staff:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        group.name = msg.text.replace("Gname: ","")
                        cl.updateGroup(group)
                    else:
                        cl.sendText(msg.to,"Tidak Dapat Mengubah Nama Grup")
            elif "My/Spam: " in msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                  txt = msg.text.split(" ")
                  jmlh = int(txt[2])
                  teks = msg.text.replace("My/Spam: "+str(txt[1])+" "+str(jmlh)+" ","")
                  tulisan = jmlh * (teks+"\n")
                  if txt[1] == "on":
                      if jmlh <= 100000:
                         for x in range(jmlh):
                             cl.sendText(msg.to, teks)
                      else:
                         cl.sendText(msg.to, "Out of Range!")
                  elif txt[1] == "off":
                      if jmlh <= 100000:
                          cl.sendText(msg.to, tulisan)
                      else:
                          cl.sendText(msg.to, "Out Of Range!")
            elif msg.text == "My/Spammed: ":
                if msg.from_ in admin or staff:
                   alip = msg.text.replace("Spammed: ","")
                   lips = oceh["pesanspam"]
                   blenk=cl.getAllContactIds()
                   blenk=alip
                   while(blenk)
                      cl.sendMessage(msg.to,str(lips))
            elif msg.text in ["Gidlist"]:
                if msg.from_ in admin or staff:
                    gid = cl.getGroupIdsJoined()
                    gid = c2.getGroupIdsJoined()
                    gid = c6.getGroupIdsJoined()
                    gid = c5.getGroupIdsJoined()
                    gid = c6.getGroupIdsJoined()
                    gid = c7.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                        h += "[%s]:%s\n" % (c2.getGroup(i).name,i)
                        h += "[%s]:%s\n" % (c3.getGroup(i).name,i)
                        h += "[%s]:%s\n" % (c4.getGroup(i).name,i)
                        h += "[%s]:%s\n" % (c5.getGroup(i).name,i)
                        h += "[%s]:%s\n" % (c6.getGroup(i).name,i)
                        cl.sendText(msg.to,h)
                        c2.sendText(msg.to,h)
                        c3.sendText(msg.to,h)
                        c4.sendText(msg.to,h)
                        c5.sendText(msg.to,h)
                        c6.sendText(msg.to,h)
            elif msg.text == "My/Undangke: ":
                if msg.from_ in admin:
                    gid = msg.text.replace("Undangke: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                      try:
                          cl.findAndAddContactsByMid(msg.from_)
                          c2.findAndAddContactsByMid(msg.from_)
                          c3.findAndAddContactsByMid(msg.from_)
                          c4.findAndAddContactsByMid(msg.from_)
                          c5.findAndAddContactsByMid(msg.from_)
                          c6.findAndAddContactsByMid(msg.from_)
                          cl.inviteIntoGroup(gid,[msg.from_])
                          c2.inviteIntoGroup(gid,[msg.from_])
                          c3.inviteIntoGroup(gid,[msg.from_])
                          c4.inviteIntoGroup(gid,[msg.from_])
                          c5.inviteIntoGroup(gid,[msg.from_])
                          c6.inviteIntoGroup(gid,[msg.from_])
#-----------------------------------------------
            elif msg.text in "Butuh asisten" in msg.text:
                if msg.from_ in admin or staff:
                    G = cl.getGroup(msg.to)
                    ginfo = blenk.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = blenk.reissueGroupTicket(msg.to)
                    c2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    c3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    c4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    c5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    c6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    blenk.updateGroup(G)
                    print "kicker ok"
                    G.preventJoinByTicket(G)
                    blenk.updateGroup(G)
                    cn2=c2.getProfile().displayName
                    cn3=c3.getProfile().displayName
                    cn4=c4.getProfile().displayName
                    cn5=c5.getProfile().displayName
                    cn6=c6.getProfile().displayName
                    c2.sendText(msg.to,"Saya "+ cn2 + " mewakili semua siap melayanii boss... \n\n Betul gakk nihh semua?... Pada setuju kan?")
                    c3.sendText(msg.to, "Yap Right... Ane "+cn3+ " Alreadqy Alwayss...")
                    c4.sebdText(msg.to, "Betull boss... Gw "+cn4+" Stuju boss...")
                    c5.sendText(msg.to, "Bener Syekalih... I am "+cn5+" Setujuu Syekalihh...")
                    c6.sendText(msg.to, "Nah.. Saya "+cn6+" Setujuu...")
#-----------------------------------------------[ Bot Leave Group ]
            elif msg.text in ["Leave all","leave all","Out all","out all"] or "Good joblah dah break dulu sono" in msg.text:
                if msg.toType == 2:
                    ginfo = blenk.getGroup(msg.to)
                    try:
                        c2.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                        c2.leaveGroup(msg.to)
                        c3.leaveGroup(msg.to)
                        c4.leaveGroup(msg.to)
                        c5.leaveGroup(msg.to)
                        c6.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Out dulu all"] or "out dulu all" in msg.text:
                if msg.toType == 2:
                    ginfo = blenk.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to, "Bye.... Thanks For Time.... ")
                        cl.leaveGroup(msg.to)
                        c2.sendText(msg.to, "Duhh Owner Out.... Kita Sbagai Asisten Ikut Out Dong Yee.... ")
                        c3.sendText(msg.to, "Iyaa nihh yaa.... ")
                        c4.sendText(msg.to, "Ywdh yee... Byee all...")
                        c5.sendText(msg.to, "Makasih yaaa udh buat kenangan... Walaupun gak berhaga haha... ")
                        c6.sendText(msg.to, "Akhir kata... Kurang lebihnya mohon maaf... \n\n Wabillahi taufiq wal hidayah... wassalamu'alaikum warahmatullahi.... wabarokaaaatuuhh.. :v")
                        c2.leaveGroup(msg.to)
                        c3.leaveGroup(msg.to)
                        c4.leaveGroup(msg.to)
                        c5.leaveGroup(msg.to)
                        c6.leaveGroup(msg.to)
                        blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                    except:
                        pass
            elif msg.text in ["2/leave","2/out"] or "Assiten2 silahkan break" in msg.text:
                if msg.toType == 2:
                    ginfo = blenk.getGroup(msg.to)
                    try:
                        c2.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                        c2.leaveGroup(msg.to)
                        blenk.sendText(msg.to, "Baguslah Temen Team Gw Break....")
                    except:
                        pass
            elif msg.text in ["3/leave","3/out"] or "Assiten3 silahkan break" in msg.text:
                if msg.toType == 2:
                    ginfo = blenk.getGroup(msg.to)
                    try:
                        c3.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                        c3.leaveGroup(msg.to)
                        blenk.sendText(msg.to, "Baguslah Temen Team Gw Break.... ")
                    except:
                        pass
            elif msg.text in ["4/leave","4/out"] or "Assiten4 silahkan break" in msg.text:
                if msg.toType == 2:
                    ginfo = blenk.getGroup(msg.to)
                    try:
                        c4.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                        c4.leaveGroup(msg.to)
                        blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                    except:
                        pass
            elif msg.text in ["5/leave","5/out"] or "Assiten5 silahkan break" in msg.text:
                if msg.toType == 2:
                    ginfo = blenk.getGroup(msg.to)
                    try:
                        c5.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                        c5.leaveGroup(msg.to)
                        blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                    except:
                        pass
            elif msg.text in ["6/leave","6/out"] or "Assiten6 silahkan break" in msg.text:
                if msg.toType == 2:
                    ginfo = blenk.getGroup(msg.to)
                    try:
                        c6.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                        c6.leaveGroup(msg.to)
                        blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                    except:
                        pass
#------------------------------------------------[ Command With Mention ]
            elif "My/Getinfo " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"◈ Nama\n" + contact.displayName + "\n◈ Mid\n" + contact.mid + "\n◈ Bio\n" + contact.statusMessage + "\n◈ Link Profile Picture: http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n◈ Link Cover: " + str(cu))
                except:
                    cl.sendText(msg.to,"◈ Nama\n" + contact.displayName + "\n◈ Mid\n" + contact.mid + "\n◈ Bio\n" + contact.statusMessage + "\n◈ Profile Picture\n" + str(cu))
           elif "My/Getname " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    cl.sendText(msg.to,"◈ Namanya : " + contact.displayName )
                except:
                    cl.sendText(msg.to,"◈ Namanya : " + contact.displayName )
            elif "My/Getbio " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    cl.sendText(msg.to,"______[ Bionya ]_____\n " + contact.displayName+"\n_________________" )
                except:
                    cl.sendText(msg.to,"______[ Bionya ]_____\n " + contact.displayName+"\n_________________" )
            elif "My/Getcover " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    lipss=str(cu)
                    cl.sendImageWithUrl(msg.to,lipss)
                except:
                    lipss=str(cu)
                    cl.sendImageWithUrl(msg.to,lipss)
            elif "My/Getvidcover " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    lipss=str(cu)
                    cl.sendVideoWithUrl(msg.to,lipss)
                except:
                    lipss=str(cu)
                    cl.sendVideoWithUrl(msg.to,lipss)
            elif "My/Getpp " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    cl.sendImageWithUrl(msg.to,lipss)
                except:
                    lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    cl.sendImageWithUrl(msg.to,lipss)
            elif "My/Getvidpp " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    cl.sendVideoWithUrl(msg.to,lipss)
                except:
                    lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    cl.sendVideoWithUrl(msg.to,lipss)
            elif "My/Getmid " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    cl.sendText(msg.to,"◈ Midnya : " + contact.mid )
                except:
                    cl.sendText(msg.to,"◈ Midnya : " + contact.mid )
#------------------------------------------------[ Command Clone ]
            elif "Clone/all " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    c2.cloneContactProfile(key1)
                    c3.cloneContactProfile(key1)
                    c4.cloneContactProfile(key1)
                    c5.cloneContactProfile(key1)
                    c6.cloneContactProfile(key1)
                    c2.sendText(msg.to,"Success Clone... ")
                except:
                    c2.cloneContactProfile(key1)
                    c3.cloneContactProfile(key1)
                    c4.cloneContactProfile(key1)
                    c5.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
            elif "My/Clone " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    cl.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
                except:
                    cl.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
            elif "2/clone " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    c2.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
                except:
                    c2.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
            elif "3/clone " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    c3.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
                except:
                    c3.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
            elif "4/clone " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    c4.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
                except:
                    c4.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
            elif "5/clone " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    c5.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
                except:
                    c5.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
            elif "6/clone " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                try:
                    c6.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
                except:
                    c6.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
#------------------------------------------------[ Command For URL ]
            elif msg.text == "My/Getvideo":
                blenk=msg.text.replace("Getvideo: ","")
                cl.sendVideoWithURL(msg.to,blenk)
            elif msg.text == "My/Getaudio":
                blenk=msg.text.replace("Getaudio: ","")
                cl.sendAudioWithURL(msg.to,blenk)
            elif msg.text == "My/Getimage: ":
                blenk=msg.text.replace("Getimage: ","")
                cl.sendImageWithURL(msg.to,blenk)
#------------------------------------------------[ Command Kicker ]
            elif msg.text in ["Clean","Endgrup","Ratakan"]:
                if msg.from_ in admin or staff:
                  gs = cl.getGroup(msg.to)
                  gs = c2.getGroup(msg.to)
                  gs = c3.getGroup(msg.to)
                  gs = c4.getGroup(msg.to)
                  gs = c5.getGroup(msg.to)
                  gs = c6.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                      if _name in g.displayName:
                         targets.append(g.mid)
                  if targets == []:
                      sendMessage(msg.to,"user does not exist")
                      pass
                  else:
                      for target in targets:                            
                        if target not in team:
                          try:
                              klist=[cl]
                              kicker=random.choice(klist)
                              kicker.kickoutFromGroup(msg.to,[target])
                              print (msg.to,[g.mid])
                          except:
                              cl.sendText(msg.to,"Sukses Bosqu")

#------------------------------------------------[ Command Work With Mid]
            elif "My/Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "My/Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.inviteIntoGroup(msg.to,[midd])
            elif "My/Contact: " in msg.text:
            	alip = msg.text.replace("Contact: ","")
                msg.contentType = 13
                msg.contentMetadata = {'mid': alip}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Success Get Contact From Mid")
            elif "My/Clone: " in msg.text:
            	alip = msg.text.replace("Contact: ","")
                msg.contentType = 13
                msg.contentMetadata = {'mid': alip}
                cl.cloneContactProfile(msg)
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Success Clone Contact From Mid")
            elif "My/Cloning: " in msg.text:
            	alip = msg.text.replace("Contact: ","")
                msg.contentType = 13
                msg.contentMetadata = {'mid': alip}
                cl.cloneContactProfile(alip)
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Success Cloning Contact From Mid")
#------------------------------------------------[ Command Ban ]
            elif "My/Ban " in msg.text:
                if msg.from_ in admin or msg.from_ in staff:
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
            elif "My/Unban " in msg.text:
                if msg.from_ in admin or msg.from_ in staff:
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
            elif msg.text in ["Clear ban"]:
               if msg.from_ in admin or msg.from_ in staff:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
            elif msg.text in ["Ban"]:
               if msg.from_ in admin or msg.from_ in staff:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim Kontaknya")
            elif msg.text in ["Unban"]:
               if msg.from_ in admin or msg.from_ in staff:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim Kontaknya")
            elif msg.text in ["Banlist"]:
               if msg.from_ in admin or msg.from_ in staff:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "n____________________\n====🏴 Blacklist 🏴====\n____________________"
                    for mi_d in wait["blacklist"]:
                        mc += "🗣  " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Banlist mid","banlist mid"]:
                if msg.from_ in admin or msg.from_ in staff:
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
            elif msg.text in ["Sikat ban","Cuci ban"]:
                if msg.from_ in admin or msg.from_ in staff:
                  if msg.toType == 2:
                      group = cl.getGroup(msg.to)
                      gMembMids = [contact.mid for contact in group.members]
                      matched_list = []
                      for tag in wait["blacklist"]:
                          matched_list+=filter(lambda str: str == tag, gMembMids)
                      if matched_list == []:
                          cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                          return
                      for jj in matched_list:
                          try:
                              cl.kickoutFromGroup(msg.to,[jj])
                              print (msg.to,[jj])
                          except:
                              pass
#------------------------------------------------[ Command Setting Pesan ]
            elif "Comment set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Comment set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Comment"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif "Pesanqr set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesanqr set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesanQR"] = c
                        cl.sendText(msg.to,"Ini telah diubah menjadi: \n\n" + c)
            elif msg.text in ["Pesanqr","pesanqr"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Maenin QR: \n\n" + str(oceh["pesanqr"]))
            elif "Pesansambut set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesansambut set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesansambut"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesansambut","pesansambut"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Join: \n\n" + str(oceh["pesansambut"]))
            elif "Pesanleave set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesanleave set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesanleave"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesanleave","pesanleave"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Ada Yg Leave: \n\n" + str(oceh["pesanleave"]))
            elif "Pesancancel set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesancancel set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesancancel"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesancancel","pesancancel"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Cancel Invite: \n\n" + str(oceh["pesancancel"]))
            elif "Pesankick set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesankick set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesankick"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesankick","pesankick"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Kick: \n\n" + str(oceh["pesankick"]))
            elif "Pesanspam set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesanspam set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesanspam"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesanspam","pesanspam"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Menjalankan Spam: \n\n" + str(oceh["pesanspam"]))
            elif "Pesanjoin set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesanjoin set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesanjoin"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesanjoin","pesanjoin"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Join: \n\n" + str(oceh["pesanjoin"]))
            elif "Pesanlike set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesanlike set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesanlike"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesanlike","pesanlike"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Menjalankan Autolike: \n\n" + str(oceh["pesanlike"]))
            elif "Pesantag set: " == msg.text:
                if msg.from_ in admin or msg.from_ in staff:
                    c = msg.text.replace("Pesantag set: ","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                    else:
                        oceh["pesantag"] = c
                        cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Pesanjoin","pesanjoin"]:
                cl.sendText(msg.to,"Berikut Settingan Pesan Saat Di Tag: \n\n" + str(oceh["pesantag"]))

#------------------------------------------------[ Creator / Owner Command ]
#____________________________
#----------------[ Staff Add / Dell ]

            elif "Admin add " in msg.text:
                if msg.from_ in owner:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Added to the staff list")
                        except:
                            pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Ini Command Buat Owner Ganteng.... :v ")
                    cl.sendText(msg.to,"Owner pea ini yg bisaa......")
            elif "Admin dell " in msg.text:
                if msg.from_ in owner:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Remove to the admin list")
                        except:
                            pass
                    print "[Command] Admin remove executed"
                else:
                    cl.sendText(msg.to,"Ini Command Buat Owner Ganteng.... :v ")
                    cl.sendText(msg.to,"Owner pea ini yg bisaa......")
            elif msg.text in ["Adminlist mid","Adminlist mid"]:
                if msg.from_ in admin or msg.from_ in staff:
                  if msg.toType == 2:
                      group = cl.getGroup(msg.to)
                      gMembMids = [contact.mid for contact in group.members]
                      matched_list = []
                      for tag in admin:
                          matched_list+=filter(lambda str: str == tag, gMembMids)
                      cocoa = ""
                      for mm in matched_list:
                          cocoa += mm + "\n"
                      cl.sendText(msg.to,cocoa + "")
#----------------[ Staff Add / Dell / List ]
            elif "Staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')                                                                                                                gs = cl.getGroup(msg.to)
                    gs = c2.getGroup(msg.to)
                    gs = c3.getGroup(msg.to)
                    gs = c4.getGroup(msg.to)
                    gs = c5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:                                                                                                                                               for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "Staff dell @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff del @","")
                    _nametarget = _name.rstrip('  ')
                    gs = c6.getGroup(msg.to)
                    gs = c2.getGroup(msg.to)
                    gs = c3.getGroup(msg.to)
                    gs = c4.getGroup(msg.to)
                    gs = c5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Stafflist mid","Stafflist mid"]:
                if msg.from_ in admin or msg.from_ in staff:
                  if msg.toType == 2:
                      group = cl.getGroup(msg.to)
                      gMembMids = [contact.mid for contact in group.members]
                      matched_list = []
                      for tag in staff:
                          matched_list+=filter(lambda str: str == tag, gMembMids)
                      cocoa = ""
                      for mm in matched_list:
                          cocoa += mm + "\n"
                      cl.sendText(msg.to,cocoa + "")
#------------------------------------------------[ Script Remote ]
#----------------------------------------------------------------------
#------------------------------ [ UNDANG ADMIN ]
           elif "Undangadmin on" in msg.text or "undangadmin on" in msg.text:
               if msg.from_ in admin or msg.from_ in staff:
                  if wait["undangadmin"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Auto Undang Admin Ke Grup On")
                     else:
                         cl.sendText(msg.to,"done")
                  else:
                     wait["undangadmin"] = True
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Auto Undang Admin Ke Grup On")
                     else:
                         cl.sendText(msg.to,"done")
            elif msg.text in ["Undangadmin off","undangadmin off","Lips/undangadmin/off"]:
                if msg.from_ in admin or msg.from_ in staff:
                   if fitur["undangadmin"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Auto Undang Admin Ke Grup Off")
                      else:
                          cl.sendText(msg.to,"done")
                   else:
                      fitur["undangadmin"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Auto Undang Admin Ke Grup Off")
                      else:
                          cl.sendText(msg.to,"done")
#------------------------------ [ SEND CONTACT ON qMODE ]
            elif msg.text in ["Ban on","ban on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban on","unban add"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["addadmin on","Addadmin on"]:
                private["addadmin"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["addstaff on","Addstaff on"]:
                private["addstaff"] = True
                cl.sendText(msg.to,"Send Contact")
#------------------------------ [ SEND CONTACT OFF MODE ]
            elif msg.text in ["Ban off","ban off"]:
                wait["wblacklist"] = False
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban off","unban adff"]:
                wait["dblacklist"] = False
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["addadmin off","Addadmin off"]:
                private["addadmin"] = False
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["addstaff off","Addstaff off"]:
                private["addstaff"] = False
                cl.sendText(msg.to,"Send Contact")
#------------------------------ [ ON MODE PROTECT ]
            elif msg.text in ["Protect on","protect on"]:
                if msg.from_ in admin or staff :
                   if protect["protect"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success....")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["protect"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success....")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Joinprotect on","joinprotect on"]:
                if msg.from_ in admin or staff:
                   if protect["joinprotect"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["joinprotect"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already...")
            elif msg.text in ["Linkprotect on","linkprotect on"]:
                if msg.from_ in admin or staff:
                   if protect["linkprotect"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["linkprotect"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Cancelprotect on","cancelprotect on"]:
                if msg.from_ in admin or staff:
                   if protect["cancelprotect"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["cancelprotect"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Joinprotect on","joinprotect on"]:
                if msg.from_ in admin or staff:
                   if protect["inviteprotect"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["inviteprotect"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Kickbanlist on","kickbanlist on"]:
                if msg.from_ in admin or staff:
                   if protect["kickbanlist"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["kickbanlist"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
#------------------------------ [ OFF MODE PROTECT ]
            elif msg.text in ["Protect off","protect off"]:
                if msg.from_ in admin or staff:
                   if protect["protect"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["protect"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Joinprotect off","joinprotect off"]:
                if msg.from_ in admin or staff:
                   if protect["joinprotect"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Already")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["joinprotect"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Already")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Linkprotect off","linkprotect off"]:
                if msg.from_ in admin or staff:
                   if protect["linkprotect"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["linkprotect"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Cancelprotect off","cancelprotect off"]:
                if msg.from_ in admin or staff:
                   if protect["cancelprotect"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          c2.sendText(msg.to,"Already")
                   else:
                      protect["cancelprotect"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Joinprotect off","joinprotect off"]:
                if msg.from_ in admin or staff:
                   if protect["inviteprotect"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["inviteprotect"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Kickbanlist off","kickbanlist off"]:
                if msg.from_ in admin or staff:
                   if protect["kickbanlist"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      protect["kickbanlist"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
#------------------------------ [ ON MODE FITUR ]
            elif msg.text in ["respontag on","Respontag on"]:
                if msg.from_ in admin or staff:
                   if fitur["respontag"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["respontag"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["sambutjoin on","Sambutjoin on"]:
                if msg.from_ in admin or staff:
                   if fitur["sambutjoin"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["sambutjoin"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Autongoceh on","autongoceh on"]:
                if msg.from_ in admin or staff:
                   if fitur["autongoceh"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["autongoceh"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Ngocehjoin on","ngocehjoin on"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehjoin"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehjoin"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Ngocehinvite on","ngocehinvite on"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehinvite"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehinvite"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["ngocehkick on","Ngocehkick on"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehkick"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehkick"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Ngocehleave on","ngocehleave on"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehleave"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehleave"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.t,"cRespontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Ngocehcancel on","ngocehcancel on"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehcancel"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehcancel"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["ngocehread on","Ngocehread on"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehread"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehread"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["NgocehQR on","ngocehQR on"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehQR"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehQR"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
#------------------------------ [ OFF MODE FITUR ]
            elif msg.text in ["respontag off","Respontag off"]:
                if msg.from_ in admin or staff:
                   if fitur["respontag"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["respontag"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["sambutjoin off","Sambutjoin off"]:
                if msg.from_ in admin or staff:
                   if fitur["sambutjoin"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["sambutjoin"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["Autongoceh off","autongoceh off"]:
                if msg.from_ in admin or staff:
                   if fitur["autongoceh"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["autongoceh"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["Ngocehjoin off","ngocehjoin off"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehjoin"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["ngocehjoin"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["Ngocehinvite off","ngocehinvite off"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehinvite"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["ngocehinvite"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Respontag Aktif")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["ngocehkick off","Ngocehkick off"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehkick"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["ngocehkick"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Ngocehleave off","ngocehleave off"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehleave"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["ngocehleave"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["Ngocehcancel off","ngocehcancel off"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehcancel"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["ngocehcancel"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["ngocehread off","Ngocehread off"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehread"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
                   else:
                      fitur["ngocehread"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Success...")
            elif msg.text in ["NgocehQR off","ngocehQR off"]:
                if msg.from_ in admin or staff:
                   if fitur["ngocehQR"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Respontag Sedang Aktif")
                   else:
                      fitur["ngocehQR"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
#------------------------------ [ ON MODE ANTI ]
            elif msg.text in ["anticontact on","Anticontact on"]:
                if msg.from_ in admin or staff:
                   if anti["anticontact"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success....")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["anticontact"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success....")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antigambar on","antigambar on"]:
                if msg.from_ in admin or staff:
                   if anti["antigambar"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antigambar"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already...")
            elif msg.text in ["Antilink on","antilink on"]:
                if msg.from_ in admin or staff:
                   if anti["antilink"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antilink"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antisticker on","antisticker on"]:
                if msg.from_ in admin or staff:
                   if anti["antisticker"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antisticker"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antivideo on","antivideo on"]:
                if msg.from_ in admin or staff:
                   if anti["antivideo"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antivideo"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antiaudio on","antiaudio on"]:
                if msg.from_ in admin or staff:
                   if anti["antiaudio"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antiaudio"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
#------------------------------ [ OFF MODE ANTI ]
            elif msg.text in ["anticontact off","Anticontact off"]:
                if msg.from_ in admin or staff:
                   if anti["anticontact"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success....")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["anticontact"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success....")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antigambar off","antigambar off"]:
                if msg.from_ in admin or staff:
                   if anti["antigambar"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antigambar"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already...")
            elif msg.text in ["Antilink off","antilink off"]:
                if msg.from_ in admin or staff:
                   if anti["antilink"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antilink"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antisticker off","antisticker off"]:
                if msg.from_ in admin or staff:
                   if anti["antisticker"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antisticker"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Success...")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antivideo off","antivideo off"]:
                if msg.from_ in admin or staff:
                   if anti["antivideo"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antivideo"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
            elif msg.text in ["Antiaudio off","antiaudio off"]:
                if msg.from_ in admin or staff:
                   if anti["antiaudio"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
                   else:
                      anti["antiaudio"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah")
                      else:
                          cl.sendText(msg.to,"Already")
#------------------------------ [ ON MODE BAN ]
            elif msg.text in ["Bangambar on","bangambar on"]:
                if msg.from_ in admin or staff:
                   if ban["bangambar"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
                   else:
                      ban["bangambar"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Bancontact on","bancontact on"]:
                if msg.from_ in admin or staff:
                   if ban["bancontact"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
                   else:
                      ban["bancontact"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Banvideo on","banvideo on"]:
                if msg.from_ in admin or staff:
                   if ban["banvideo"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
                  else:
                      ban["banvideo"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Banlink on","banlink on"]:
                if msg.from_ in admin or staff:
                   if ban["banlink"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
                   else:
                      ban["banlink"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Bansticker on","bansticker on"]:
                if msg.from_ in admin or staff:
                   if ban["bansticker"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
                   else:
                      ban["basticker"] = True
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
            elif msg.text in ["Banaudio on","banaudio on"]:
                if msg.from_ in admin or staff:
                   if ban["banaudio"] == True:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah Aktif")
                      else:
                          cl.sendText(msg.to,"Sedang Aktif")
                    else:
                       ban["banaudio"] = True
                       if wait["lang"] == "JP":
                           c2.sendText(msg.to,"Sudah Aktif")
                       else:
                           cl.sendText(msg.to,"Sedang Aktif")
#------------------------------ [ OFF MODE BAN ]
            elif msg.text in ["Bangambar off","bangambar off"]:
                if msg.from_ in admin or staff:
                   if ban["bangambar"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
                   else:
                      ban["bangambar"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
            elif msg.text in ["Bancontact off","bancontact off"]:
                if msg.from_ in admin or staff:
                   if ban["bancontact"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
                   else:
                      ban["bancontact"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
            elif msg.text in ["Banvideo off","banvideo off"]:
                if msg.from_ in admin or staff:
                   if ban["banvideo"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
                  else:
                      ban["banvideo"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
            elif msg.text in ["Banlink off","banlink off"]:
                if msg.from_ in admin or staff:
                   if ban["banlink"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
                   else:
                      ban["banlink"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
            elif msg.text in ["Bansticker off","bansticker off"]:
                if msg.from_ in admin or staff:
                   if ban["bansticker"] == False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
                   else:
                      ban["basticker"] = False
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
            elif msg.text in ["Banaudio off","banaudio off"]:
                if msg.from_ in admin or staff:
                   if ban["banaudio"] a== False:
                      if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Sudah off")
                      else:
                          cl.sendText(msg.to,"Sedang off")
                    else:
                       ban["banaudio"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Success...")
                       else:
                           cl.sendText(msg.to,"Already")
#------------------------------------------------ [ Protect ALL COMMAND ]
            elif msg.text in ["allprotect on","Allprotect on","Hard mode"]:
           	 if msg.from_ in admin or staff:
                   if protect["inviteprotect"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectInvite Sedang Aktif")
                       else:
                           cl.sendText(msg.to,"ProtectInvite Sudah Aktif")
                   else:
                       protect["inviteprotect"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectInvite Aktif")
                       else:
                       	cl.sendText(msg.to,"Telah Aktif")
                    if protect["joinprotect"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectInvite Sedang Aktif")
                       else:
                           cl.sendText(msg.to,"ProtectInvite Sudah Aktif")
                    else:
                       protect["joinprotect"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectInvite Aktif")
                    if protect["cancelprotect"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectCancel Sedang Aktif")
                       else:
                           cl.sendText(msg.to,"ProtectCancel Sudah Aktif")
                    else:
                       protect["cancelprotect"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectCancel Aktif")
                    if protect["protect"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Sedang Aktif")
                       else:
                           cl.sendText(msg.to,"Protect Sudah Aktif")
                    else:
                       protect["protect"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Aktif")
                       else:
                           cl.sendText(msg.to,"Protect Sudah Aktif")
                    if protect["linkprotect"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQR Sedang Aktif")
                       else:
                           cl.sendText(msg.to,"Protect Sudah Aktif")
                    else:
                       protect["linkprotect"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQR Aktif")
                       else:
                           cl.sendText(msg.to,"ProtectQR Sudah Aktif")
            elif msg.text in ["allprotect off","Allprotect off","Easy mode"]:
           	 if msg.from_ in admin or staff:
                   if protect["inviteprotect"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectInvite Sedang off")
                       else:
                           cl.sendText(msg.to,"ProtectInvite Sudah off")
                   else:
                       protect["inviteprotect"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectInvite off")
                       else:
                       	cl.sendText(msg.to,"Telah off")
                    if protect["joinprotect"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protectjoin off")
                       else:
                           cl.sendText(msg.to,"ProtectInvite Sudah off")
                    else:
                       protect["joinprotect"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectInvite off")
                    if protect["cancelprotect"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectCancel Sedang off")
                       else:
                           cl.sendText(msg.to,"ProtectCancel Sudah off")
                    else:
                       protect["cancelprotect"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectCancel off")
                    if protect["protect"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Sedang off")
                       else:
                           cl.sendText(msg.to,"Protect Sudah off")
                    else:
                       protect["protect"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect off")
                       else:
                           cl.sendText(msg.to,"Protect Sudah off")
                    if protect["linkprotect"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQR Sedang off")
                       else:
                           cl.sendText(msg.to,"Protect Sudah off")
                    else:
                       protect["linkprotect"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQR off")
                       else:
                           cl.sendText(msg.to,"ProtectQR Sudah off")
#--------------------------------------------------------------------------------- 
#------------------------------------------------[ Un SelfBot ]
        if op.type == 26:
            msg = op.message
            if msg.from_ in wait["blacklist"] or if private["botoff"] == True:
                c2.sendMessage(msg.to, "Maaf tidak bisa menggunakan command... mungkin command bot dalam keadaan off atau anda terdaftar di blacklist")
            else:
#-------------------------------------[ INVITE ]
                if msg.contentType == 13:
               	if wait["invite"] == True:
                       _name = msg.contentMetadata["displayName"]
                       invite = msg.contentMetadata["mid"]
                       groups = cl.getGroup(msg.to)
                       pending = groups.invitee
                       targets = []
                       for s in groups.members:
                           if _name in s.displayName:
                               c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                               break
                           elif invite in wait["blacklist"]:
                               c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                               c2.sendText(msg.to,"Unban: " + invite)
                               break                             
                           else:
                               targets.append(invite)
                       if targets == []:
                           pass
                       else:
                           for target in targets:
                               try:
                                   c2.findAndAddContactsByMid(target)
                                   c2.inviteIntoGroup(msg.to,[target])
                                   random.choice(KAC).sendText(msg.to,"Invite: \n➡" + _name)
                                   wait["invite"] = False
                                   break                              
                               except:             
                                        c2.sendText(msg.to,"Error")
                                        wait["invite"] = False
                                        break
#---------------------------------------[ Add Staff ]
                	if private["addstaff"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                                break
                            elif invite in wait["blacklist"]:
                                c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                                c2.sendText(msg.to,"Unban: " + invite)
                                break                             
                            else:
                                targets.append(invite)
                       if targets == []:
                           cl.sendText(msg.to,"Contact not found")
                           ki.sendText(msg.to,"Contact not found")
                       else:
                           for target in targets:
                               try:
                                   staff.append(target)
                                   cl.sendText(msg.to,"Admin LipsBOT Success Ditambahkan")
                               except:
                                   pass
                       print "[Command]Staff add by contact executed"
                    else:
                       cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed")
#---------------------------------------[ Remove Staff ]
                	if private["dellstaff"] == True:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                                 break
                             elif invite in wait["blacklist"]:
                                 c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                                 c2.sendText(msg.to,"Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                        if targets == []:
                            cl.sendText(msg.to,"Contact not found")
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    staff.remove(target)
                                    cl.sendText(msg.to,"Success Remove Admin LipsBOT.... ")
                                except:
                                    pass
                        print "[Command]Staff remove by contact executed"
                    else:
                        cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed ")
#---------------------------------------[ Add Admin ]
                	if private["addadmin"] == True:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                                 break
                             elif invite in wait["blacklist"]:
                                 c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                                 c2.sendText(msg.to,"Unban: " + invite)
                                 break                             
                             else:
                                  targets.append(invite)
                        if targets == []:
                            cl.sendText(msg.to,"Contact not found")
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    admin.append(target)
                                    cl.sendText(msg.to,"Admin LipsBOT Success Ditambahkan")
                                except:
                                    pass
                        print "[Command] Admin add by contact executed"
                    else:
                        cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed")
#---------------------------------------[ Remove Admin ]
                	if private["delladmin"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                c2.sendText(msg.to,"~ " + _name + " Berada DiGrup Ini")
                                break
                            elif invite in wait["blacklist"]:
                                c2.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                                c2.sendText(msg.to,"Unban: " + invite)
                                break                             
                            else:
                                 targets.append(invite)
                        if targets == []:
                            cl.sendText(msg.to,"Contact not found")
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    admin.remove(target)
                                    cl.sendText(msg.to,"Success Remove Admin LipsBOT.... ")
                                except:
                                    pass
                        print "[Command] Admin remove by contact executed"
                    else:
                        cl.sendText(msg.to,"Gabisa Bang... Fixxed Dong Bang... Kan Jagoo Fixed ")
#-----------------------------------------
                if msg.contentType == 13:
                    if wait["wblack"] == True:
                        if msg.contentMetadata["mid"] in wait["commentBlack"]:
                            c2.sendText(msg.to,"sudah masuk daftar hitam")
                            wait["wblack"] = False
                        else:
                            wait["commentBlack"][msg.contentMetadata["mid"]] = True
                            wait["wblack"] = False
                            c2.sendText(msg.to,"Itu tidak berkomentar")
                    elif wait["dblack"] == True:
                        if msg.contentMetadata["mid"] in wait["commentBlack"]:
                            del wait["commentBlack"][msg.contentMetadata["mid"]]
                            c2.sendText(msg.to,"Done")
                            wait["dblack"] = False
                        else:
                            wait["dblack"] = False
                            c2.sendText(msg.to,"Tidak ada dalam daftar hitam")
                    elif wait["wblacklist"] == True:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            c2.sendText(msg.to,"sudah masuk daftar hitam")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            c2.sendText(msg.to,"Done")
                    elif wait["dblacklist"] == True:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            del wait["blacklist"][msg.contentMetadata["mid"]]
                            c2.sendText(msg.to,"Done")
                            wait["dblacklist"] = False
                        else:
                            wait["dblacklist"] = False
                            c2.sendText(msg.to,"Done")
                    elif wait["contact"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = c2.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            c2.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                        else:
                            contact = c2.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = c2.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            c2.sendText(msg.to,"=======[displayName]=======\n" + contact.displayName + "\=========[mid]========\n" + msg.contentMetadata["mid"] + "\n=======[statusMessage]=======:\n" + contact.statusMessage + "\n=======[pictureStatus]=======\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n=======[coverURL]=======\n" + str(cu))
                elif msg.contentType == 16:
                    if wait["timeline"] == True:
                        msg.contentType = 0
                        if wait["lang"] == "JP":
                            msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                        else:
                            msg.text = "========[URL]=========\n" + msg.contentMetadata["postEndUrl"]
                        c2.sendText(msg.to,msg.text)
                elif msg.text is None:
                    return
#-----------------------------------------------[ Help Command ] 
                elif msg.text in ["help","Help"]:
                    if wait["lang"] == "JP":
                        c2.sendText(msg.to,helpMessage)
                    else:
                        c2.sendText(msg.to,helpMessage)
                elif msg.text in ["Bot/help","bot/help"]:
                    if wait["lang"] == "JP":
                        c2.sendText(msg.to,bot)
                    else:
                        c2.sendText(msg.to,bot)
                elif msg.text in ["Protect/help","protect"]:
                    if wait["lang"] == "JP":
                        c2.sendText(msg.to,plotek)
                    else:
                        c2.sendText(msg.to,plotek)
                elif msg.text in ["Ban/help","ban/help"]:
                    if wait["lang"] == "JP":
                        c2.sendText(msg.to,banmode)
                    else:
                        c2.sendText(msg.to,banmode)
                elif msg.text in ["Anti/help","anti/help"]:
                    if wait["lang"] == "JP":
                        c2.sendText(msg.to,antimode)
                    else:
                        c2.sendText(msg.to,antimode)
                elif msg.text in ["Pesan/help","pesan/help"]:
                    if wait["lang"] == "JP":
                        c2.sendText(msg.to,pesen)
                    else:
                        c2.sendText(msg.to,pesen)
#-----------------------------------------------[ Mix Command ] 
                elif "gift" or "Gift" in msg.text:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                                             'PRDTYPE': 'THEME',
                                                             'MSGTPL': '5'}
                    msg.text = None
                    cl.sendMessage(msg)
                elif msg.text in ["Creator","creator"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': owner}
                    random.choice(KAC).sendMessage(msg)
                elif msg.text in ["mid","Mid"]:
                    c2.sendMessage(msg.to, msg.from_)
                elif msg.text in ["Crash","crash"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': alipdeblenkgansbangetduhhh}
                    random.choice(KAC).sendMessage(msg)
                elif msg.text in ["Me","me"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg.from_}
                    random.choice(KAC).sendMessage(msg)
                elif msg.text in ["Contact/bot"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid2}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid3}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid4}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid5}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid6}
                    cl.sendMessage(msg)
                elif msg.text == "2Remove/pesan":
                	if msg.from_ in admin or staff:
                        c2.removeAllMessages(op.param2)
                elif msg.text == "3Remove/pesan":
                	if msg.from_ in admin or staff:
                        c3.removeAllMessages(op.param2)
                elif msg.text == "4Remove/pesan":
                	if msg.from_ in admin or staff:
                        c4.removeAllMessages(op.param2)
                elif msg.text == "5Remove/pesan":
                	if msg.from_ in admin or staff:
                        c5.removeAllMessages(op.param2)
                elif msg.text == "6Remove/pesan":
                	if msg.from_ in admin or staff:
                        c6.removeAllMessages(op.param2)
                elif msg.text == "Remove/pesan":
                    c2.removeAllMessages(op.param2)
                    c2.removeAllMessages(op.param2)
                    c3.removeAllMessages(op.param2)
                    c4.removeAllMessages(op.param2)
                    c5.removeAllMessages(op.param2)
                    c6.removeAllMessages(op.param2)
                elif msg.text == "Kedapkedip: ":
                    txt = msg.text.replace("Kedapkedip: ", "")
                    cl.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"
                elif msg.text == "Clone group":
                    thisgroup = cl.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    lips = cl.getGroup(msg.to)
                    deblenk = str(lips.name)
                    path = "http://dl.profile.line-cdn.net/" + lips.pictureStatus
                    blenks = path
                    cl.createGroup(deblenk, blenks, mi_d)
                    cl.sendText(msg.to,"Success Clone Group....")
                else:
                    cl.sendText(msg.to,"Pleasee Use Command Cloning.....")
                elif msg.text in ["Ginfo","Group info","ginfo","Grup info","grup info","Group info"]:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[[____[ Nama Grup ]____]]\n" + group.name + "\n\n[[____[ ID Grup ]___]]\n" + group.id + "\n\n[[____[ Pembuat Grup ]____]]\n" + gCreator + "\n\n[[___[ Link Gambar Grup ]__]]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
                elif msg.text == "Cloning group":
                    thisgroup = cl.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    lips = cl.getGroup(msg.to)
                    deblenk = str(lips.name)
                    cl.createGroup(deblenk, mi_d)
                    cl.sendText(msg.to,"Success Clone Group....")
                elif msg.text == "Recover":
                    thisgroup = cl.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    cl.createGroup("Recover", mi_d)
                    cl.sendText(msg.to,"Success recover")
                else:
                    cl.sendText(msg.to,"Waduhh Gabisa Bang... Fixed Dong... Kan jago :v")
                elif msg.text == "Buat group: ":
                    LipsD3BL3NK = msg.text.replace("Buat group: ","")
                    MyName = LipsD3BL3NK
                    cl.createGroup(MyName)
                    cl.sendText(msg.to,"Success buat grup")
                else:
                    cl.sendText(msg.to,"Waduhh Gabisa Bang... Fixed Dong... Kan jago :v")
                elif msg.text == "Group image":
                    group = cl.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(msg.to,path)
                if msg.text in ["Mentionall"]:
                    if msg.from_ in admin or staff:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        mention(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        mention(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        mention(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        mention(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        mention(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        mention(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        mention(msg.to, nm5)
                    if jml > 500:
                        cl.sendText(msg.to, "Anggotanya 500+ waha")
                        print "Terlalu Banyak Mem 500+"
                    cnt = Message()
                    cnt.text = "Jumlah member:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    cl.sendMessage(cnt)
                elif
                elif msg.text == "Myname: ":
                    string = msg.text.replace("Myname: ","")
                    if len(string.decode('utf-8')) <= 20000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Update Bio" + string)
                elif
                elif msg.text == "Mybio: ":
                	if msg.from_ in admin:
                    string = msg.text.replace("Mybio: ","")
                    if len(string.decode('utf-8')) <= 20000:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.sendText(msg.to,"Sebentar boss kita laksanakan..."
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Update Bio Menjadi :\n" + string +"\n Telah Succes Boss...")
                elif msg.text == "Gname: ":
                    if msg.from_ in admin or staff:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            group.name = msg.text.replace("Gname: ","")
                            cl.updateGroup(group)
                        else:
                            cl.sendText(msg.to,"Tidak Dapat Mengubah Nama Grup")
                elif "Spam: " in msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                      txt = msg.text.split(" ")
                      jmlh = int(txt[2])
                      teks = msg.text.replace("Spam: "+str(txt[1])+" "+str(jmlh)+" ","")
                      tulisan = jmlh * (teks+"\n")
                      if txt[1] == "on":
                          if jmlh <= 100000:
                             for x in range(jmlh):
                                 cl.sendText(msg.to, teks)
                          else:
                             cl.sendText(msg.to, "Out of Range!")
                      elif txt[1] == "off":
                          if jmlh <= 100000:
                              cl.sendText(msg.to, tulisan)
                          else:
                              cl.sendText(msg.to, "Out Of Range!")
                elif msg.text == "Spammed: ":
                    if msg.from_ in admin or staff:
                       alip = msg.text.replace("Spammed: ","")
                       lips = oceh["pesanspam"]
                       blenk=cl.getAllContactIds()
                       blenk=alip
                       while(blenk)
                          cl.sendMessage(msg.to,lips)
                elif msg.text in ["Gidlist"]:
                    if msg.from_ in admin or staff:
                        gid = cl.getGroupIdsJoined()
                        gid = c2.getGroupIdsJoined()
                        gid = c6.getGroupIdsJoined()
                        gid = c5.getGroupIdsJoined()
                        gid = c6.getGroupIdsJoined()
                        gid = c7.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                            h += "[%s]:%s\n" % (c2.getGroup(i).name,i)
                            h += "[%s]:%s\n" % (c3.getGroup(i).name,i)
                            h += "[%s]:%s\n" % (c4.getGroup(i).name,i)
                            h += "[%s]:%s\n" % (c5.getGroup(i).name,i)
                            h += "[%s]:%s\n" % (c6.getGroup(i).name,i)
                            cl.sendText(msg.to,h)
                            c2.sendText(msg.to,h)
                            c3.sendText(msg.to,h)
                            c4.sendText(msg.to,h)
                            c5.sendText(msg.to,h)
                           c6.sendText(msg.to,h)

                elif msg.text == "Undangke: ":
                    if msg.from_ in admin:
                        gid = msg.text.replace("Undangke: ","")
                        if gid == "":
                            cl.sendText(msg.to,"Invalid group id")
                        else:
                          try:
                              cl.findAndAddContactsByMid(msg.from_)
                              c2.findAndAddContactsByMid(msg.from_)
                              c3.findAndAddContactsByMid(msg.from_)
                              c4.findAndAddContactsByMid(msg.from_)
                              c5.findAndAddContactsByMid(msg.from_)
                              c6.findAndAddContactsByMid(msg.from_)
                              cl.inviteIntoGroup(gid,[msg.from_])
                              c2.inviteIntoGroup(gid,[msg.from_])
                              c3.inviteIntoGroup(gid,[msg.from_])
                              c4.inviteIntoGroup(gid,[msg.from_])
                              c5.inviteIntoGroup(gid,[msg.from_])
                              c6.inviteIntoGroup(gid,[msg.from_])
#-----------------------------------------------
                elif msg.text in "Butuh asisten" in msg.text:
                    if msg.from_ in admin or staff:
                        G = cl.getGroup(msg.to)
                        ginfo = blenk.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = blenk.reissueGroupTicket(msg.to)
                        c2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        c3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        c4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        c5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        c6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        blenk.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        blenk.updateGroup(G)
                        cn2=c2.getProfile().displayName
                        cn3=c3.getProfile().displayName
                        cn4=c4.getProfile().displayName
                        cn5=c5.getProfile().displayName
                        cn6=c6.getProfile().displayName
                        c2.sendText(msg.to,"Saya "+ cn2 + " mewakili semua siap melayanii boss... \n\n Betul gakk nihh semua?... Pada setuju kan?")
                        c3.sendText(msg.to, "Yap Right... Ane "+cn3+ " Alreadqy Alwayss...")
                        c4.sebdText(msg.to, "Betull boss... Gw "+cn4+" Stuju boss...")
                        c5.sendText(msg.to, "Bener Syekalih... I am "+cn5+" Setujuu Syekalihh...")
                        c6.sendText(msg.to, "Nah.. Saya "+cn6+" Setujuu...")
#-----------------------------------------------[ Bot Leave Group ]
                elif msg.text in ["Leave all","leave all","Out all","out all"] or "Good joblah dah break dulu sono" in msg.text:
                    if msg.toType == 2:
                        ginfo = blenk.getGroup(msg.to)
                        try:
                            c2.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                            c2.leaveGroup(msg.to)
                            c3.leaveGroup(msg.to)
                            c4.leaveGroup(msg.to)
                            c5.leaveGroup(msg.to)
                            c6.leaveGroup(msg.to)
                        except:
                            pass
                elif msg.text in ["Out dulu all"] or "out dulu all" in msg.text:
                    if msg.toType == 2:
                        ginfo = blenk.getGroup(msg.to)
                        try:
                            cl.sendText(msg.to, "Bye.... Thanks For Time.... ")
                            cl.leaveGroup(msg.to)
                            c2.sendText(msg.to, "Duhh Owner Out.... Kita Sbagai Asisten Ikut Out Dong Yee.... ")
                            c3.sendText(msg.to, "Iyaa nihh yaa.... ")
                            c4.sendText(msg.to, "Ywdh yee... Byee all...")
                            c5.sendText(msg.to, "Makasih yaaa udh buat kenangan... Walaupun gak berhaga haha... ")
                            c6.sendText(msg.to, "Akhir kata... Kurang lebihnya mohon maaf... \n\n Wabillahi taufiq wal hidayah... wassalamu'alaikum warahmatullahi.... wabarokaaaatuuhh.. :v")
                            c2.leaveGroup(msg.to)
                            c3.leaveGroup(msg.to)
                            c4.leaveGroup(msg.to)
                            c5.leaveGroup(msg.to)
                            c6.leaveGroup(msg.to)
                            blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                        except:
                            pass
                elif msg.text in ["2/leave","2/out"] or "Assiten2 silahkan break" in msg.text:
                    if msg.toType == 2:
                        ginfo = blenk.getGroup(msg.to)
                        try:
                            c2.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                            c2.leaveGroup(msg.to)
                            blenk.sendText(msg.to, "Baguslah Temen Team Gw Break....")
                       except:
                            pass
                elif msg.text in ["3/leave","3/out"] or "Assiten3 silahkan break" in msg.text:
                    if msg.toType == 2:
                        ginfo = blenk.getGroup(msg.to)
                        try:
                            c3.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                            c3.leaveGroup(msg.to)
                            blenk.sendText(msg.to, "Baguslah Temen Team Gw Break.... ")
                        except:
                            pass
                elif msg.text in ["4/leave","4/out"] or "Assiten4 silahkan break" in msg.text:
                    if msg.toType == 2:
                        ginfo = blenk.getGroup(msg.to)
                        try:
                            c4.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                            c4.leaveGroup(msg.to)
                            blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                       except:
                            pass
                elif msg.text in ["5/leave","5/out"] or "Assiten5 silahkan break" in msg.text:
                    if msg.toType == 2:
                        ginfo = blenk.getGroup(msg.to)
                        try:
                            c5.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                            c5.leaveGroup(msg.to)
                            blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                        except:
                            pass
                elif msg.text in ["6/leave","6/out"] or "Assiten6 silahkan break" in msg.text:
                    if msg.toType == 2:
                        ginfo = blenk.getGroup(msg.to)
                        try:
                            c6.sendText(msg.to, "Bye boss... Nnti kalo butuh panggil aja lgi")
                            c6.leaveGroup(msg.to)
                            blenk.sendText(msg.to, "Baguslah Temen Team Gw Break")
                        except:
                            pass
#------------------------------------------------[ Command With Mention ]
                elif "Getinfo " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    try:
                        cl.sendText(msg.to,"◈ Nama\n" + contact.displayName + "\n◈ Mid\n" + contact.mid + "\n◈ Bio\n" + contact.statusMessage + "\n◈ Link Profile Picture: http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n◈ Link Cover: " + str(cu))
                    except:
                        cl.sendText(msg.to,"◈ Nama\n" + contact.displayName + "\n◈ Mid\n" + contact.mid + "\n◈ Bio\n" + contact.statusMessage + "\n◈ Profile Picture\n" + str(cu))
                elif "Getname " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        cl.sendText(msg.to,"◈ Namanya : " + contact.displayName )
                    except:
                        cl.sendText(msg.to,"◈ Namanya : " + contact.displayName )
                elif "Getbio " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        cl.sendText(msg.to,"______[ Bionya ]_____\n " + contact.displayName+"\n_________________" )
                    except:
                        cl.sendText(msg.to,"______[ Bionya ]_____\n " + contact.displayName+"\n_________________" )
                elif "Getcover " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    try:
                        lipss=str(cu)
                        cl.sendImageWithUrl(msg.to,lipss)
                    except:
                        lipss=str(cu)
                        cl.sendImageWithUrl(msg.to,lipss)
                elif "Getvidcover " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    cu = cl.channel.getCover(key1)
                    try:
                        lipss=str(cu)
                        cl.sendVideoWithUrl(msg.to,lipss)
                    except:
                        lipss=str(cu)
                        cl.sendVideoWithUrl(msg.to,lipss)
                elif "Getpp " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithUrl(msg.to,lipss)
                    except:
                        lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithUrl(msg.to,lipss)
                elif "Getvidpp " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendVideoWithUrl(msg.to,lipss)
                    except:
                        lipss="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendVideoWithUrl(msg.to,lipss)
                elif "Getmid " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        cl.sendText(msg.to,"◈ Midnya : " + contact.mid )
                    except:
                        cl.sendText(msg.to,"◈ Midnya : " + contact.mid )
#------------------------------------------------[ Command Clone ]
                elif "Clone/all " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        c2.cloneContactProfile(key1)
                        c3.cloneContactProfile(key1)
                        c4.cloneContactProfile(key1)
                        c5.cloneContactProfile(key1)
                        c6.cloneContactProfile(key1)
                        c2.sendText(msg.to,"Success Clone... ")
                    except:
                        c2.cloneContactProfile(key1)
                        c3.cloneContactProfile(key1)
                        c4.cloneContactProfile(key1)
                        c5.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                elif "Clone " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        cl.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                    except:
                        cl.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                elif "2/clone " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        c2.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                    except:
                        c2.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                elif "3/clone " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        c3.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                    except:
                    c3.cloneContactProfile(key1)
                    cl.sendText(msg.to,"Success Clone... ")
                elif "4/clone " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        c4.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                    except:
                        c4.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                elif "5/clone " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        c5.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                    except:
                        c5.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                elif "6/clone " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        c6.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
                    except:
                        c6.cloneContactProfile(key1)
                        cl.sendText(msg.to,"Success Clone... ")
#------------------------------------------------[ Command For URL ]
                elif msg.text == "Getvideo":
                    blenk=msg.text.replace("Getvideo: ","")
                    cl.sendVideoWithURL(msg.to,blenk)
                elif msg.text == "Getaudio":
                    blenk=msg.text.replace("Getaudio: ","")
                    cl.sendAudioWithURL(msg.to,blenk)
                elif msg.text == "Getimage: ":
                    blenk=msg.text.replace("Getimage: ","")
                    cl.sendImageWithURL(msg.to,blenk)
#------------------------------------------------[ Command Kicker ]
                elif msg.text in ["Clean","Endgrup","Ratakan"]:
                    if msg.from_ in admin or staff:
                        gs = cl.getGroup(msg.to)
                        gs = c2.getGroup(msg.to)
                        gs = c3.getGroup(msg.to)
                        gs = c4.getGroup(msg.to)
                        gs = c5.getGroup(msg.to)
                        gs = c6.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                        if targets == []:
                             c2.sendMessage(msg.to,"user does not exist")
                             pass
                        else:
                             for target in targets:                            
                                 if not target in Bots:
                                 try:
                                     klist=[cl]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(msg.to,[target])
                                     print (msg.to,[g.mid])
                                 except:
                                     cl.sendText(msg.to,"Sukses Bosqu")

#------------------------------------------------[ Command Work With Mid]
                elif "Kick: " in msg.text:
                    midd = msg.text.replace("Kick: ","")
                    cl.kickoutFromGroup(msg.to,[midd])
                elif "Invite: " in msg.text:
                    midd = msg.text.replace("Invite: ","")
                    cl.inviteIntoGroup(msg.to,[midd])
                elif "Contact: " in msg.text:
                	alip = msg.text.replace("Contact: ","")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': alip}
                    cl.sendMessage(msg)
                    cl.sendText(msg.to,"Success Get Contact From Mid")
                elif "Clone: " in msg.text:
                	alip = msg.text.replace("Contact: ","")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': alip}
                    cl.cloneContactProfile(msg)
                    cl.sendMessage(msg)
                    cl.sendText(msg.to,"Success Clone Contact From Mid")
                elif "Cloning: " in msg.text:
                	alip = msg.text.replace("Contact: ","")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': alip}
                    cl.cloneContactProfile(alip)
                    cl.sendMessage(msg)
                    cl.sendText(msg.to,"Success Cloning Contact From Mid")
#------------------------------------------------[ Command Ban ]
                elif "Ban " in msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
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
                elif "Unban " in msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
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
                elif msg.text in ["Clear ban"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        wait["blacklist"] = {}
                        cl.sendText(msg.to,"clear")
                elif msg.text in ["Ban"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        wait["wblacklist"] = True
                        cl.sendText(msg.to,"Kirim Kontaknya")
                elif msg.text in ["Unban"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        wait["dblacklist"] = True
                        cl.sendText(msg.to,"Kirim Kontaknya")
                elif
                elif msg.text in ["Banlist"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        if wait["blacklist"] == {}:
                            cl.sendText(msg.to,"Tidak Ada Blacklist")
                        else:
                            cl.sendText(msg.to,"Daftar Banlist􏿿")
                            mc = "n____________________\n====🏴 Blacklist 🏴====\n____________________"
                            for mi_d in wait["blacklist"]:
                                mc += "🗣  " + cl.getContact(mi_d).displayName + " \n"
                            cl.sendText(msg.to, mc + "")
                elif
                elif msg.text in ["Banlist mid","banlist mid"]:
                    if msg.from_ in admin or msg.from_ in staff:
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
                elif msg.text in ["Sikat ban","Cuci ban"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                            return
                        for jj in matched_list:
                            try:
                                cl.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
#------------------------------------------------[ Ngeloncong Command ]
                elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
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
                elif "Ngeloncong " in msg.text:
                    if msg.from_ in owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
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
                                        cl.sendMessageWithMention(msg.to,target)
                                        break
                                    except:
                                        cl.sendText(msg.to,"...")
                                        break
                elif "Ngeloncong: " in msg.text:
                        cmd = msg.text.replace("Ngeloncong: ","")
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
                        elif "add: " in cmd:
                            target0 = msg.text.replace("Mimic: add: ","")
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
                                        cl.sendMessageWithMention(msg.to,target)
                                        break
                                    except:
                                        cl.sendText(msg.to,"...")
                                        break
                        elif "del: " in cmd:
                            target0 = msg.text.replace("Mimic: del: ","")
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
                                        cl.sendMessageWithMention(msg.to,target)
                                        break
                                    except:
                                        cl.sendText(msg.to,"...")
                                        break
                        elif cmd == "list":
                            if mimic["target"] == {}:
                                cl.sendText(msg.to,"No target")
                            else:
                                lst = "<<List Target>>"
                                total = len(mimic["target"])
                                for a in mimic["target"]:
                                    if mimic["target"][a] == True:
                                        stat = "On"
                                    else:
                                        stat = "Off"
                                    lst += "\n-> " + cl.getContact(a).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal: " + total)q
#------------------------------------------------[ Command Setting Pesan ]
                elif "Comment set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Comment set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            wait["comment"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Comment"]:
                    cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
                elif "Pesanqr set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesanqr set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesanQR"] = c
                            cl.sendText(msg.to,"Ini telah diubah menjadi: \n\n" + c)
                elif msg.text in ["Pesanqr","pesanqr"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Maenin QR: \n\n" + str(oceh["pesanqr"]))
                elif "Pesansambut set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesansambut set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesansambut"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesansambut","pesansambut"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Join: \n\n" + str(oceh["pesansambut"]))
                elif "Pesanleave set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesanleave set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesanleave"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesanleave","pesanleave"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Ada Yg Leave: \n\n" + str(oceh["pesanleave"]))
                elif "Pesancancel set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesancancel set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesancancel"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesancancel","pesancancel"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Cancel Invite: \n\n" + str(oceh["pesancancel"]))
                elif "Pesankick set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesankick set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesankick"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesankick","pesankick"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Kick: \n\n" + str(oceh["pesankick"]))
                elif "Pesanspam set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesanspam set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesanspam"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesanspam","pesanspam"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Menjalankan Spam: \n\n" + str(oceh["pesanspam"]))
                elif "Pesanjoin set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesanjoin set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesanjoin"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesanjoin","pesanjoin"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Join: \n\n" + str(oceh["pesanjoin"]))
                elif "Pesanlike set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesanlike set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesanlike"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesanlike","pesanlike"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Menjalankan Autolike: \n\n" + str(oceh["pesanlike"]))
                elif "Pesantag set: " == msg.text:
                    if msg.from_ in admin or msg.from_ in staff:
                        c = msg.text.replace("Pesantag set: ","")
                        if c in [""," ","\n",None]:
                            cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                        else:
                            oceh["pesantag"] = c
                            cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
                elif msg.text in ["Pesanjoin","pesanjoin"]:
                    cl.sendText(msg.to,"Berikut Settingan Pesan Saat Di Tag: \n\n" + str(oceh["pesantag"]))

#------------------------------------------------[ Creator / Owner Command ]
#____________________________
#----------------[ Staff Add / Dell ]

                elif "Admin add " in msg.text:
                    if msg.from_ in owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                        print "[Command]Staff add executed"
                    else:
                        cl.sendText(msg.to,"Ini Command Buat Owner Ganteng.... :v ")
                        cl.sendText(msg.to,"Owner pea ini yg bisaa......")
                elif "Admin dell " in msg.text:
                    if msg.from_ in owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Remove to the admin list")
                            except:
                                pass
                        print "[Command] Admin remove executed"
                    else:
                        cl.sendText(msg.to,"Ini Command Buat Owner Ganteng.... :v ")
                        cl.sendText(msg.to,"Owner pea ini yg bisaa......")
                elif msg.text in ["Adminlist mid","Adminlist mid"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in admin:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            cocoa = ""
                            for mm in matched_list:
                                cocoa += mm + "\n"
                            cl.sendText(msg.to,cocoa + "")
#----------------[ Staff Add / Dell / List ]
                elif
                elif "/Staff add @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff add executing"
                        _name = msg.text.replace("/Staff add @","")
                        _nametarget = _name.rstrip('  ')                                                                                                                gs = cl.getGroup(msg.to)
                        gs = c2.getGroup(msg.to)
                        gs = c3.getGroup(msg.to)
                        gs = c4.getGroup(msg.to)
                        gs = c5.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:                                                                                                                                               for target in targets:
                                try:
                                    staff.append(target)
                                    cl.sendText(msg.to,"Added to the staff list")
                                 except:
                                    pass
                        print "[Command]Staff add executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                elif "Staff dell @" in msg.text:
                    if msg.from_ in admin:
                        print "[Command]Staff remove executing"
                        _name = msg.text.replace("Staff del @","")
                        _nametarget = _name.rstrip('  ')
                        gs = c6.getGroup(msg.to)
                        gs = c2.getGroup(msg.to)
                        gs = c3.getGroup(msg.to)
                        gs = c4.getGroup(msg.to)
                        gs = c5.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                       else:
                           for target in targets:
                               try:
                                    staff.remove(target)
                                    cl.sendText(msg.to,"Removed to the staff list")
                                except:
                                    pass
                        print "[Command]Staff remove executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                elif msg.text in ["Stafflist mid","Stafflist mid"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in staff:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            cocoa = ""
                            for mm in matched_list:
                                cocoa += mm + "\n"
                            cl.sendText(msg.to,cocoa + "")
#------------------------------------------------[ Script Remote ]
#----------------------------------------------------------------------
#------------------------------ [ UNDANG ADMIN ]
               elif "Undangadmin on" in msg.text or "undangadmin on" in msg.text:
                   if msg.from_ in admin or msg.from_ in staff:
                       if wait["undangadmin"] == True:
                           if wait["lang"] == "JP":
                               cl.sendText(msg.to,"Auto Undang Admin Ke Grup On")
                           else:
                               cl.sendText(msg.to,"done")
                       else:
                          wait["undangadmin"] = True
                           if wait["lang"] == "JP":
                               cl.sendText(msg.to,"Auto Undang Admin Ke Grup On")
                           else:
                               cl.sendText(msg.to,"done")
                elif msg.text in ["Undangadmin off","undangadmin off","Lips/undangadmin/off"]:
                    if msg.from_ in admin or msg.from_ in staff:
                        if fitur["undangadmin"] == False:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Auto Undang Admin Ke Grup Off")
                            else:
                                cl.sendText(msg.to,"done")
                        else:
                           fitur["undangadmin"] = False
                           if wait["lang"] == "JP":
                              cl.sendText(msg.to,"Auto Undang Admin Ke Grup Off")
                          else:
                              cl.sendText(msg.to,"done")
#------------------------------ [ SEND CONTACT ON qMODE ]
                elif msg.text in ["Ban on","ban on"]:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact")
                elif msg.text in ["Unban on","unban add"]:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact")
                elif msg.text in ["addadmin on","Addadmin on"]:
                    wait["addadmin"] = True
                    cl.sendText(msg.to,"Send Contact")
                elif msg.text in ["addstaff on","Addstaff on"]:
                    wait["addstaff"] = True
                    cl.sendText(msg.to,"Send Contact")
#------------------------------ [ SEND CONTACT OFF MODE ]
                elif msg.text in ["Ban off","ban off"]:
                    wait["wblacklist"] = False
                    cl.sendText(msg.to,"Send Contact")
                elif msg.text in ["Unban off","unban adff"]:
                    wait["dblacklist"] = False
                    cl.sendText(msg.to,"Send Contact")
                elif msg.text in ["addadmin off","Addadmin off"]:
                    wait["addadmin"] = False
                    cl.sendText(msg.to,"Send Contact")
                elif msg.text in ["addstaff off","Addstaff off"]:
                    wait["addstaff"] = False
                    cl.sendText(msg.to,"Send Contact")
#------------------------------ [ ON MODE PROTECT ]
                elif msg.text in ["Protect on","protect on"]:
                    if msg.from_ in admin or staff :
                        if protect["protect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                           protect["protect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")

                elif msg.text in ["Joinprotect on","joinprotect on"]:
                    if msg.from_ in admin or staff:
                        if protect["joinprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                             else:
                                c2.sendText(msg.to,"Already")
                         else:
                            protect["joinprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already...")

                elif msg.text in ["Linkprotect on","linkprotect on"]:
                    if msg.from_ in admin or staff:
                        if protect["linkprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["linkprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Cancelprotect on","cancelprotect on"]:
                    if msg.from_ in admin or staff:
                        if protect["cancelprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["cancelprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["inviteprotect on","Inviteprotect on"]:
                    if msg.from_ in admin or staff:
                        if protect["inviteprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["inviteprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Kickbanlist on","kickbanlist on"]:
                    if msg.from_ in admin or staff:
                        if protect["kickbanlist"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["kickbanlist"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
#------------------------------ [ OFF MODE PROTECT ]
                elif msg.text in ["Protect off","protect off"]:
                    if msg.from_ in admin or staff:
                        if protect["protect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["protect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Joinprotect off","joinprotect off"]:
                    if msg.from_ in admin or staff:
                        if protect["joinprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Already")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["joinprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Already")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Linkprotect off","linkprotect off"]:
                    if msg.from_ in admin or staff:
                        if protect["linkprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["linkprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Cancelprotect off","cancelprotect off"]:
                    if msg.from_ in admin or staff:
                        if protect["cancelprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["cancelprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["inviteprotect off","Inviteprotect off"]:
                    if msg.from_ in admin or staff:
                        if protect["inviteprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["inviteprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Kickbanlist off","kickbanlist off"]:
                    if msg.from_ in admin or staff:
                        if protect["kickbanlist"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["kickbanlist"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
#------------------------------ [ ON MODE FITUR ]
                elif msg.text in ["respontag on","Respontag on"]:
                    if msg.from_ in admin or staff:
                        if fitur["respontag"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["respontag"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["sambutjoin on","Sambutjoin on"]:
                    if msg.from_ in admin or staff:
                        if fitur["sambutjoin"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Already")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["sambutjoin"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Already")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["autongoceh on","Autongoceh on"]:
                    if msg.from_ in admin or staff:
                        if fitur["autongoceh"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["autongoceh"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Ngocehjoin on","ngocehjoin on"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehjoin"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehjoin"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Ngocehinvite on","ngocehinvite on"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehinvite"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehinvite"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehkick on","Ngocehkick on"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehkick"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehkick"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehleave on","Ngocehleave on"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehleave"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehleave"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehcancel on","Ngocehcancel on"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehcancel"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehcancel"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehread on","Ngocehread on"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehread"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehread"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehQR on","NgocehQR on"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehQR"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehQR"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
#------------------------------ [ OFF MODE FITUR ]
                elif msg.text in ["respontag off","Respontag off"]:
                    if msg.from_ in admin or staff:
                        if fitur["respontag"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["respontag"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["sambutjoin off","Sambutjoin off"]:
                    if msg.from_ in admin or staff:
                        if fitur["sambutjoin"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Already")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["sambutjoin"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Already")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["autongoceh off","Autongoceh off"]:
                    if msg.from_ in admin or staff:
                        if fitur["autongoceh"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["autongoceh"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Ngocehjoin off","ngocehjoin off"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehjoin"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehjoin"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Ngocehinvite off","ngocehinvite off"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehinvite"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehinvite"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehkick off","Ngocehkick off"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehkick"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehkick"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehleave off","Ngocehleave off"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehleave"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehleave"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehcancel off","Ngocehcancel off"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehcancel"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehcancel"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehread off","Ngocehread off"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehread"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehread"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["ngocehQR off","NgocehQR off"]:
                    if msg.from_ in admin or staff:
                        if fitur["ngocehQR"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            fitur["ngocehQR"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")

#------------------------------ [ ON MODE ANTI ]
                elif msg.text in ["anticontact on","Anticontact on"]:
                    if msg.from_ in admin or staff:
                        if anti["anticontact"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["anticontact"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antigambar on","antigambar on"]:
                    if msg.from_ in admin or staff:
                        if anti["antigambar"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antigambar"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already...")
                elif msg.text in ["Antilink on","antilink on"]:
                    if msg.from_ in admin or staff:
                        if anti["antilink"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antilink"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antisticker on","antisticker on"]:
                    if msg.from_ in admin or staff:
                        if anti["antisticker"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antisticker"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antivideo on","antivideo on"]:
                    if msg.from_ in admin or staff:
                        if anti["antivideo"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antivideo"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antiaudio on","antiaudio on"]:
                    if msg.from_ in admin or staff:
                        if anti["antiaudio"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antiaudio"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
#------------------------------ [ OFF MODE ANTI ]
                elif msg.text in ["anticontact off","Anticontact off"]:
                    if msg.from_ in admin or staff:
                        if anti["anticontact"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["anticontact"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antigambar off","antigambar off"]:
                    if msg.from_ in admin or staff:
                        if anti["antigambar"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antigambar"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already...")
                elif msg.text in ["Antilink off","antilink off"]:
                    if msg.from_ in admin or staff:
                        if anti["antilink"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antilink"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antisticker off","antisticker off"]:
                    if msg.from_ in admin or staff:
                        if anti["antisticker"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antisticker"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antivideo off","antivideo off"]:
                    if msg.from_ in admin or staff:
                        if anti["antivideo"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antivideo"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                elif msg.text in ["Antiaudio off","antiaudio off"]:
                    if msg.from_ in admin or staff:
                        if anti["antiaudio"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antiaudio"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
#------------------------------ [ ON MODE BAN ]
                elif msg.text in ["Bangambar on","bangambar on"]:
                    if msg.from_ in admin or staff:
                        if ban["bangambar"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bangambar"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Bancontact on","bancontact on"]:
                    if msg.from_ in admin or staff:
                        if ban["bancontact"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bancontact"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Banvideo on","banvideo on"]:
                    if msg.from_ in admin or staff:
                        if ban["banvideo"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banvideo"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Banlink on","banlink on"]:
                    if msg.from_ in admin or staff:
                        if ban["banlink"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banlink"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Bansticker on","bansticker on"]:
                    if msg.from_ in admin or staff:
                        if ban["bansticker"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["basticker"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Banaudio on","banaudio on"]:
                    if msg.from_ in admin or staff:
                        if ban["banaudio"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banaudio"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
#------------------------------ [ OFF MODE BAN ]
                elif msg.text in ["Bangambar off","bangambar off"]:
                    if msg.from_ in admin or staff:
                        if ban["bangambar"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bangambar"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Bancontact off","bancontact off"]:
                    if msg.from_ in admin or staff:
                        if ban["bancontact"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bancontact"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Banvideo off","banvideo off"]:
                    if msg.from_ in admin or staff:
                        if ban["banvideo"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banvideo"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Banlink off","banlink off"]:
                    if msg.from_ in admin or staff:
                        if ban["banlink"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banlink"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Bansticker on","bansticker off"]:
                    if msg.from_ in admin or staff:
                        if ban["bansticker"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["basticker"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                elif msg.text in ["Banaudio off","banaudio off"]:
                    if msg.from_ in admin or staff:
                        if ban["banaudio"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banaudio"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
#------------------------------------------------ [ Protect ALL COMMAND ]
                elif msg.text in ["All/anti on","all/anti on"]:
                    if msg.from_ in admin or staff:
                        if anti["anticontact"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["anticontact"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antigambar"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antigambar"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already...")
                        if anti["antilink"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antilink"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antisticker"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antisticker"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antivideo"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antivideo"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antiaudio"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antiaudio"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                                
               elif msg.text in ["All/ban on","all/ban on"]:
                    if msg.from_ in admin or staff:
                        if ban["bangambar"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bangambar"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["bancontact"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bancontact"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["banvideo"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banvideo"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["banlink"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banlink"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["bansticker"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["basticker"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["banaudio"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banaudio"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")

                elif msg.text in ["All/fitur on","all/fitur on"]:
                    if msg.from_ in admin or staff:
                        if fitur["respontag"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Respontag Sudah")
                            else:
                                c2.sendText(msg.to,"Respontag Already")
                        else:
                            fitur["respontag"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Respontag Sudah")
                            else:
                                c2.sendText(msg.to,"Respontag Already")
                        if fitur["sambutjoin"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sambut join Already")
                            else:
                                c2.sendText(msg.to,"Sambut join Already")
                        else:
                            fitur["sambutjoin"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sambut join Already")
                            else:
                                c2.sendText(msg.to,"Sambut join Already")
                        if fitur["autongoceh"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Auto ngoceh Sudah")
                            else:
                                c2.sendText(msg.to,"Auto ngoceh Already")
                        else:
                            fitur["autongoceh"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Auto ngoceh Sudah")
                            else:
                                c2.sendText(msg.to,"Auto ngoceh Already")
                        if fitur["ngocehjoin"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh join Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh join Already")
                        else:
                            fitur["ngocehjoin"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh join Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh join Already")
                        if fitur["ngocehinvite"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Invite Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Invite Already")
                        else:
                            fitur["ngocehinvite"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Invite Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Invite Already")
                        if fitur["ngocehkick"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Kick Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh kick Already")
                        else:
                            fitur["ngocehkick"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh kickSudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh kick Already")
                        if fitur["ngocehleave"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        else:
                            fitur["ngocehleave"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        if fitur["ngocehcancel"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        else:
                            fitur["ngocehcancel"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        if fitur["ngocehread"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh read Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh read Already")
                        else:
                            fitur["ngocehread"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Read Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Read Already")
                        if fitur["ngocehQR"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh QR Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh QR Already")
                        else:
                            fitur["ngocehQR"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh QR Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh QR Already")

                elif msg.text in ["All/protect on","all/protect on"]:
                    if msg.from_ in admin or staff :
                        if protect["protect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                           protect["protect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["joinprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                             else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["joinprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already...")
                        if protect["linkprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["linkprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["cancelprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["cancelprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["inviteprotect"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["inviteprotect"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["kickbanlist"] == True:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["kickbanlist"] = True
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")

#------------------------------------------------ [ Protect ALL COMMAND ]
                elif msg.text in ["All/anti off","all/anti off"]:
                    if msg.from_ in admin or staff:
                        if anti["anticontact"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["anticontact"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antigambar"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antigambar"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already...")
                        if anti["antilink"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antilink"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antisticker"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antisticker"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antivideo"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antivideo"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        if anti["antiaudio"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            anti["antiaudio"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                                
               elif msg.text in ["All/ban off","all/ban off"]:
                    if msg.from_ in admin or staff:
                        if ban["bangambar"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bangambar"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["bancontact"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["bancontact"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["banvideo"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banvideo"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["banlink"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banlink"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["bansticker"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["basticker"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        if ban["banaudio"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")
                        else:
                            ban["banaudio"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah Aktif")
                            else:
                                c2.sendText(msg.to,"Sedang Aktif")

                elif msg.text in ["All/fitur off","all/fitur off"]:
                    if msg.from_ in admin or staff:
                        if fitur["respontag"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Respontag Sudah")
                            else:
                                c2.sendText(msg.to,"Respontag Already")
                        else:
                            fitur["respontag"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Respontag Sudah")
                            else:
                                c2.sendText(msg.to,"Respontag Already")
                        if fitur["sambutjoin"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sambut join Already")
                            else:
                                c2.sendText(msg.to,"Sambut join Already")
                        else:
                            fitur["sambutjoin"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sambut join Already")
                            else:
                                c2.sendText(msg.to,"Sambut join Already")
                        if fitur["autongoceh"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Auto ngoceh Sudah")
                            else:
                                c2.sendText(msg.to,"Auto ngoceh Already")
                        else:
                            fitur["autongoceh"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Auto ngoceh Sudah")
                            else:
                                c2.sendText(msg.to,"Auto ngoceh Already")
                        if fitur["ngocehjoin"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh join Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh join Already")
                        else:
                            fitur["ngocehjoin"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh join Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh join Already")
                        if fitur["ngocehinvite"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Invite Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Invite Already")
                        else:
                            fitur["ngocehinvite"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Invite Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Invite Already")
                        if fitur["ngocehkick"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Kick Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh kick Already")
                        else:
                            fitur["ngocehkick"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh kickSudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh kick Already")
                        if fitur["ngocehleave"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        else:
                            fitur["ngocehleave"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        if fitur["ngocehcancel"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        else:
                            fitur["ngocehcancel"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Leave Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Leave Already")
                        if fitur["ngocehread"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh read Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh read Already")
                        else:
                            fitur["ngocehread"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh Read Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh Read Already")
                        if fitur["ngocehQR"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh QR Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh QR Already")
                        else:
                            fitur["ngocehQR"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Ngoceh QR Sudah")
                            else:
                                c2.sendText(msg.to,"Ngoceh QR Already")

                elif msg.text in ["All/protect off","all/protect off"]:
                    if msg.from_ in admin or staff :
                        if protect["protect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                           protect["protect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success....")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["joinprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                             else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["joinprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already...")
                        if protect["linkprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["linkprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Success...")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["cancelprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["cancelprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["inviteprotect"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["inviteprotect"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        if protect["kickbanlist"] == False:
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
                        else:
                            protect["kickbanlist"] = False
                            if wait["lang"] == "JP":
                                c2.sendText(msg.to,"Sudah")
                            else:
                                c2.sendText(msg.to,"Already")
#--------------------------------------------------------------------------------- 
                elif "Id" == msg.text:
                    key = msg.to
                    cl.sendText(msg.to, key)
#----------------------------------------------------------------------------
#--------------------------------- TRANSLATE --------------------------------
                elif
                elif "Tr/inggris: " in msg.text:
                    txt = msg.text.replace("Tr/inggris: ","")
                    try:
                        gs = goslate.Goslate()
                        trs = gs.translate(txt,'en')
                        cl.sendText(msg.to,trs)
                        print '[Command] Translate EN'
                    except:
                       cl.sendText(msg.to,'Error.')
                elif
                elif "Tr/indonesia:" in msg.text:
                    txt = msg.text.replace("Tr/indonesia:","")
                    try:
                        gs = goslate.Goslate()
                        trs = gs.translate(txt,'id')
                        cl.sendText(msg.to,trs)
                        print '[Command] Translate ID'
                    except:
                        cl.sendText(msg.to,'Erorr.')
#=============================================

                elif "Youtube: " in msg.text:
                    query = msg.text.replace("Youtube: ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url    = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r    = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&List' not in a['href']:
                                  cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
                elif "Yt:" in msg.text.lower():
                    if msg.toType == 2:
                        query = msg.text.split(":")
                        try:
                             if len(query) == 3:
                                isi = yt(query[2])
                                hasil = isi[int(query[1])-1]
                                cl.sendText(msg.to, hasil)
                             else:
                                isi = yt(query[1])
                                cl.sendText(msg.to, isi[0])
                        except Exception as e:
                             cl.sendText(msg.to, str(e))
#----------- .Maenan -----------#
                elif "Siapa " in msg.text:
                    tanya = msg.text.replace("Siapa ","")
                    jawab = ("Setan","Jin iprit","Manusia","Orang laen","Orang gila","Pejabat","Presiden","Supermen","Betmen","Kak Seto","Awkarin","Yang lek","Papah Setnov")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)
                elif "Apakah " in msg.text:
                    tanya = msg.text.replace("Apakah ","")
                    jawab = ("Ya","Tidak","Bisa Jadi","Gak Mungkin","Sangat")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)
                elif "Love " in msg.text:
                    tanya = msg.text.replace("Love ","")
                    jawab = ("5%","10%","15%","20%","25%","30%","35%","40%","45%","50%","55%","60%","65%","70%","75%","80%","85%","90%","95","100%")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)
                elif "Rating " in msg.text:
                    tanya = msg.text.replace("Rating ","")
                    jawab = ("5%","10%","15%","20%","25%","30%","35%","40%","45%","50%","55%","60%","65%","70%","75%","80%","85%","90%","95","100%")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)
                elif "Profesi " in msg.text:
                    tanya = msg.text.replace("Profesi ","")
                    jawab = ("Mulung","Presiden","Mucikari","PSK","Mentri","Pejabat","Kang Parkir","Pembantu","Nganggur","Pelacur","Maling sendal","Maling jemuran","Maling motor","Maling hati aku","Maling hati kamu","Kang Siomay","Kang Baso","Kang Batagor","Ojek Online","Keamanan Jaringan","Security Cyber","Progammer","Designer","Ngebutik","Kuli Proyek","Satpam warteg","Satpam komplek","Satpam kuburan","Satpam hati aku","Satpam hati kamu")
                    jawaban = random.choice(jawab)
                    cl.sendText(msg.to,jawaban)
#------------ Maenan -----------#
#------------ music ------------#
                elif "Music: " in msg.text.lower():
                    songname = msg.text.lower().replace("Music: ","")
                    params = {"songname":" songname"}
                    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        cl.sendMessage(msg.to, song[4])
			#------------ music -------------#
                elif "Play: " in msg.text.lower():
                    songname = msg.text.lower().replace("Play: ","")
                    params = {"songname":" songname"}
                    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        cl.sendAudioWithURL(msg.to, song[4])
#-----------------------[ Download Tools ]
                elif "Unduh/yt: " in msg.text:
                    idyt = msg.text.replace("Unduh/yt","")
                    r=requests.get("http://wahidganteng.ga/process/api/b4cca9d55df60a67bab576b92d890de9/youtube-downloader?url="+idyt)
                    data=r.text
                    data=json.loads(data)
                    judul = data['title']
                    b = ""
                    for a in data.get('data', []):
                        b += "Judul: %s\n%s\n%s\n%s\n\n" % (judul,a['type'],a['link'],a['size'])
                    c2.sendText(msg.to,b)
#==================================================
                elif '.lyric ' in msg.text.lower():
                    try:
                        songname = msg.text.lower().replace('.lyric ','')
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            cl.sendText(msg.to, hasil)
                    except Exception as wak:
                            cl.sendText(msg.to, str(wak))
                elif msg.text == "Wikipedia:":
                    try:
                        wiki = msg.text.replace("Wikipedia: ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=1)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        cl.sendText(msg.to, pesan)
                    except:
                            try:
                                 pesan="Over Text Limit! Please Click link\n"
                                 pesan+=wikipedia.page(wiki).url
                                 cl.sendText(msg.to, pesan)
                            except Exception as e:
                                 cl.sendText(msg.to, str(e))
                elif msg.text.lower() == 'Restart':
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
                elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
                elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
                elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                elif '.instagram ' in msg.text.lower():
                    try:
                        instagram = msg.text.lower().replace(".instagram ","")
                        html = requests.get('https://www.instagram.com/' + instagram + '/?')
                        soup = BeautifulSoup(html.text, 'html5lib')
                        data = soup.find_all('meta', attrs={'property':'og:description'})
                        text = data[0].get('content').split()
                        data1 = soup.find_all('meta', attrs={'property':'og:image'})
                        text1 = data1[0].get('content').split()
                        user = "Name: " + text[-2] + "\n"
                        user1 = "Username: " + text[-1] + "\n"
                        followers = "Followers: " + text[0] + "\n"
                        following = "Following: " + text[2] + "\n"
                        post = "Post: " + text[4] + "\n"
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        detail = "========INSTAGRAM INFO USER========\n"
                        details = "\n========INSTAGRAM INFO USER========"
                        cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                        cl.sendImageWithURL(msg.to, text1[0])
                    except Exception as njer:
                    	cl.sendText(msg.to, str(njer))
                elif 'music ' in msg.text.lower():
                    try:
                        songname = msg.text.lower().replace('music ','')
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'This is Your Music\n'
                            hasil += 'Judul : ' + song[0]
                            hasil += '\nDurasi : ' + song[1]
                            hasil += '\nLink Download : ' + song[4]
                            cl.sendText(msg.to, hasil)
                            cl.sendText(msg.to, "Please Wait for audio...")
                            cl.sendAudioWithURL(msg.to, song[4])
                    except Exception as njer:
                        cl.sendText(msg.to, str(njer))
                elif msg.text in ["Cancel"]:
                    if msg.toType == 2:
                        X = blenk.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            blenk.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"No one is inviting。")
                            else:
                                cl.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            #------------ finish -------------#
                elif msg.text in ["Link on","QR on","Url on"]:
                    if msg.toType == 2:
                        X = c2.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        blenk.updateGroup(X)
                        if wait["lang"] == "JP":
                            c2.sendText(msg.to,"done")
                        else:
                            c2.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            c2.sendText(msg.to,"Can not be used outside the group")
                        else:
                            c2.sendText(msg.to,"Not for use less than group")
                elif msg.text in ["Link off","Url off","QR off"]:
                    if msg.toType == 2:
                        X = c2.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        blenk.updateGroup(X)
                        if wait["lang"] == "JP":
                            c2.sendText(msg.to,"done")
                        else:
                            c2.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            c2.sendText(msg.to,"Can not be used outside the group")
                        else:
                            c2.sendText(msg.to,"Not for use less than group")
                elif msg.text in ["Gurl"]:
                    if msg.from_ in admin or staff:
                        if msg.toType == 2:
                            x = cl.getGroup(msg.to)
                            if x.preventJoinByTicket == True:
                                x.preventJoinByTicket = False
                                cl.updateGroup(x)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendText(msg.to,"Nih link grupnya: line://ti/g/" + gurl)
                            else:
                                if wait["lang"] == "JP":
                                     cl.sendText(msg.to,"Can't be used outside the group")
                                else:
                                     cl.sendText(msg.to,"Not for use less than group")
#------------------------------------------------[ Operation Ban & Anti Mode]
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["anticontact"] == True:
                        c2.kickDariGroup(ruang,[msg.from_])
            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["bancontact"] == True:
                        gs = blenk.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            blenk.sendText(msg.to,"Tidak DiTemukan")
                        else:
                            for target in targets:
                                try:
                                     wait["blacklist"][target] = True
                                     f=codecs.open('st2__b.json','w','utf-8')
                                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                     blenk.sendText(msg.to,"Berhasil")
                                except:
                                     blenk.sendText(msg.to,"Error")
            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["antigambar"] == True:
                        c2.kickDariGroup(ruang,[msg.from_])
            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["bangambar"] == True:
                        gs = blenk.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            blenk.sendText(msg.to,"Tidak DiTemukan")
                        else:
                            for target in targets:
                                try:
                                     wait["blacklist"][target] = True
                                     f=codecs.open('st2__b.json','w','utf-8')
                                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                     blenk.sendText(msg.to,"Berhasil")
                                except:
                                     blenk.sendText(msg.to,"Error")
            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["antilink"] == True:
                        c2.kickDariGroup(ruang,[msg.from_])
            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["banlink"] == True:
                        gs = blenk.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            blenk.sendText(msg.to,"Tidak DiTemukan")
                        else:
                            for target in targets:
                                try:
                                     wait["blacklist"][target] = True
                                     f=codecs.open('st2__b.json','w','utf-8')
                                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                     blenk.sendText(msg.to,"Berhasil")
                                except:
                                     blenk.sendText(msg.to,"Error")            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["antiaudio"] == True:
                        c2.kickoutFromGroup(ruang,[msg.from_])
            if msg.contentType == 13:
                if msg.from_ not in team:
                    if ban["banaudio"] == True:
                        gs = blenk.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            blenk.sendText(msg.to,"Tidak DiTemukan")
                        else:
                            for target in targets:
                                try:
                                     wait["blacklist"][target] = True
                                     f=codecs.open('st2__b.json','w','utf-8')
                                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                     blenk.sendText(msg.to,"Berhasil")
                                except:
                                     blenk.sendText(msg.to,"Error")
            if msg.contentType == 7:
                if msg.from_ not in team:
                    if ban["antisticker"] == True:
                        c2.kickoutFromGroup(op.param1,[msg.from_])
            if msg.contentType == 7:
                if msg.from_ not in team:
                    if ban["bansticker"] == True:
                        gs = blenk.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            blenk.sendText(msg.to,"Tidak DiTemukan")
                        else:
                            for target in targets:
                                try:
                                     wait["blacklist"][target] = True
                                     f=codecs.open('st2__b.json','w','utf-8')
                                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                     blenk.sendText(msg.to,"Berhasil")
                                except:
                                     blenk.sendText(msg.to,"Error")
            if msg.contentType == 2:
                if msg.from_ not in team:
                    if ban["antivideo"] == True:
                        blenk.kickoutFromGroup(op.param1,[msg.from_])
            if msg.contentType == 2:
                if msg.from_ not in team:
                    if ban["banvideo"] == True:
                        gs = blenk.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            blenk.sendText(msg.to,"Tidak DiTemukan")
                        else:
                            for target in targets:
                                try:
                                     wait["blacklist"][target] = True
                                     f=codecs.open('st2__b.json','w','utf-8')
                                     json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                     blenk.sendText(msg.to,"Berhasil")
                                except:
                                     blenk.sendText(msg.to,"Error")
#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n╠" + Nama
                        wait2['ROM'][op.param1][op.param2] = "╠" + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


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

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"],likeType=1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],oceh["pesanlike"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
          c2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          c2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
          c3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          c3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
          c4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
          c4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
          c5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
          c5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],str(oceh["pesanlike"]))
          c6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
          c6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likeme():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in admin:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
                    c2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    c2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
                    c3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    c3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
                    c4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    c4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
                    c5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    c5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
                    c6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    c6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By D3BL3NK |\n line://ti/p/~deblip_")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"

def autolike():
     for zx in range(0,20):
         hasil = cl.activity(limit=20)
         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
             try:    
                 cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                 cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],oceh["pesanlike"])
                 print "DiLike"
             except:
                     pass
          else:
                 print "Sudah DiLike"
              time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
         hasil = c2.activity(limit=20)
         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
             try:    
                 c2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                 c2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],oceh["pesanlike"])
                 print "DiLike"
             except:
                     pass
          else:
                 print "Sudah DiLike"
              time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
         hasil = c3.activity(limit=20)
         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
             try:    
                 c3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                 c3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],oceh["pesanlike"])
                 print "DiLike"
             except:
                     pass
          else:
                 print "Sudah DiLike"
              time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
         hasil = c4.activity(limit=20)
         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
             try:    
                 c4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                 c4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],oceh["pesanlike"])
                 print "DiLike"
             except:
                     pass
          else:
                 print "Sudah DiLike"
              time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
         hasil = c5.activity(limit=20)
         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
             try:    
                 c5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                 c5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],oceh["pesanlike"])
                 print "DiLike"
             except:
                     pass
          else:
                 print "Sudah DiLike"
              time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
         hasil = c6.activity(limit=20)
         if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
             try:    
                 c6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                 c6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],oceh["pesanlike"])
                 print "DiLike"
             except:
                     pass
          else:
                 print "Sudah DiLike"
              time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

#def tolike():
#     for zx in range(0,50):
#        hasil = cl.activity(limit=1000)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#          try:    
#            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            print "Like"
#            print "Like"
#            print "Like"
#          except:
#            pass
#        else:
#            print "Already Liked"
#     time.sleep(600)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
