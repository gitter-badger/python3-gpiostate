My first Library!!

# python3-Gpio-library

simple library to read and write gpio state
 
pins use BCM values 

tested on raspberry piZero and pi2B, on raspbian and ubuntu core, but I thick it should work on any linux SBC with gpio

requirements{
     python3
}
## use

    import gpiostate 
    
    ###export###  (must be root) # pin must be exported to read or write
    
    gpiostate.export(pin, dir) #dir = direction in/out   

    ###unexport###
    
    gpiostate.unexport(pin)
    
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
    
 

  