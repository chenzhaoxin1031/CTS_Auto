import libtmux
from countfile import *
import subprocess
finish=Sleep(finish)

def start():
    server = libtmux.Server()
    session = server.find_where({ "session_name": "sts"})
    window = session.attached_window
    pane = window.split_window(attach=False)

def getip():
    childip=subprocess.Popen(['adb devices'],shell=True,stdout=subprocess.PIPE)
    devicestr=childip.read().decode(encoding="utf-8")
    ipstr=devicestr[25:43]
    return ipstr

def copy_media(ipstr):
    copyicmd="./copy_image.sh -s " + ipstr
    copymcmd="./copy_media.sh -s " + ipstr
    pane.send_keys(copyicmd)
    pand.send_keys(copymcmd)

def run_sts(ipstr):
    pane.send_keys('cd /home/sqa/VTS/r13/android-vts/tools')
    pane.send_keys('./vts-tradefed')
    run_sts_cmd="run vts -m VtsFirmwareBootHeaderVerification -s " + ipstr
    pane.send_keys(run_sts_cmd)

def retry_sts():
    pane.send_keys('run vts -m VtsFirmwareBootHeaderVerification -s 192.168.50.43:5555')

if __name__ == '__main__':
    start()
    run_sts()

    if finish == 1 and fail_num == 0:
        retry_sts()