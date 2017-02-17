My first Library!!

# python3-Gpio-library

simple library to read and write gpio state
 
pins use BCM values 

## use

    import gpiostate
    
    ###export### (must be root)
    
    gpiostate.export(pin) # pin must be exported to read or write 
    
    ###read state###
    gpiostate.read(pin)
    print(gpiostate.state)
    
    ###write state###(must be root)
    gpiostate.write(pin, stateW) # stateW [on/off]
    
    ###write on###(must be root)
    gpiostate.write(pin, on)
 
    ###write off###(must be root)
    gpiostate.write(pin, off)
    
    ###flip state###(must be root)
    gpiostate.flip(pin)  
    
## need to add

    unexport