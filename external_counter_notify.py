import os
import urllib.request
import stat
import sys


URL_COUNTER = "https://github.com/antonmedv/countdown/releases/download/v$RELEASE/countdown_linux_amd64 -O countdown"

def download_counter():
    path = os.getcwd() + "/" + "counter"
    urllib.request.urlretrieve(URL_COUNTER, filename=path)
    return path

def make_executable(counter_path):
    st = os.stat(counter_path)
    os.chmod(counter_path, st.st_mode | stat.S_IEXEC)

def move_to_user_place(counter_path):
    cpstr = 'echo %(pass)s | sudo  mv "%(from)s" "%(to)s"'
    os.system(cpstr % {'pass': 'userpassword', 'from': counter_path, 'to': '/usr/local/bin'})


def install_external_counter():
    counter_path = download_counter()
    make_executable(counter_path)
    move_to_user_place(counter_path)

def runner(minute):
    os.system("""counter %
    notify - send '% is over !' 'time to begin it over' - -icon = dialog - information""", minute)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        install_external_counter() if sys.argv[1] == 'install' else print('pass')
