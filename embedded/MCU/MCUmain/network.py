def Do_Connect():
    import network
    wlanconnect = network.WLAN(network.STA_IF)
    wlanconnect.active(True)
    if not wlanconnect.isconnected():
        print('connecting to network...')
        wlanconnect.connect('networkco', '12345678')
        while not wlanconnect.isconnected():
            print("connecting....")
            pass
    print('success! network config:', wlanconnect.ifconfig())
    return wlanconnect
def Do_Creatwlansever(name,password):
    import network
    wlansever = network.WLAN(network.AP_IF)
    wlansever.active(True)
    wlansever.config(essid=name,authmode=3,password=password)
    return wlansever
def Do_Release(wlansever,wlanconnect):
    wlansever.active(False)
    wlanconnect .active(False)