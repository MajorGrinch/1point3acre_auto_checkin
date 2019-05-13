import requests
from bs4 import BeautifulSoup
import re

mainpage_url = 'https://www.1point3acres.com/bbs/'
login_action_url = 'https://www.1point3acres.com/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

# checkin_btn_patt = re.compile(r'<a[\s]*(.*?)</a>')
sess = requests.Session()


data = {'username':'anonymous_test', 'quickforward':'yes', 'handlekey':'ls', 'password': '1fdfd3038cc7b73e5bfa7addf8ac65cf'}
rsp = sess.post(login_action_url, data=data)
rsp = sess.get('https://www.1point3acres.com/bbs/./')
bsObj = BeautifulSoup(rsp.text, features="lxml")
checkin_a_tag = bsObj.findAll("a", {'onclick' : re.compile(r"showWindow\('dsu.*")} )[0]
print(checkin_a_tag)
