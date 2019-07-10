import pynput,time

is_quit = False

charList = ['`','1','2','3','4','5','6','7','8','9','0','-','=','[',']','\\',';','\'',',','.','/']
KeyComb = []
for i in range(0, len(charList)):
    KeyComb.append({pynput.keyboard.Key.shift, pynput.keyboard.KeyCode(char=charList[i])})
    KeyComb.append({pynput.keyboard.Key.shift_r, pynput.keyboard.KeyCode(char=charList[i])})

spChar = [
    '~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','\"','<','>','?'
]
index =0
def on_press(key):
    global is_quit
    
    if any([key in comb for comb in KeyComb]) and not key in current:
        current.add(key)
        global index
        for index, comb in enumerate(KeyComb):
            if all(k in current for k in comb):
                if index == 0:
                    print("Char : %s" % spChar[0])
                else:
                    print("Char : %s" % spChar[(index//2)])
    else:
        print("{}".format(key))

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


# The currently active modifiers
current = set()

listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

##### MAIN Script #####
while True:
    time.sleep(0.00833)
    if is_quit:
        break