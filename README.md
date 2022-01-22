# MiniRTU-Firmware
A pack of libraries for MiniRTU Board, such a GPIO library, ETH library, etc. 

  Usage of m-gpio library: 

    Firs you need to creade a library object

    miniRTU = mgpio()

    Then you can use the following function:
    1. For GPIO output .PIN( MiniRTU-Pin-Number ), it will return MiniRTU asigned Pin, for example Pin 1 on MiniRTU is Pin 4 on RP2040 MCU. 
    2. For Relay output .Relay( Relay-Number, Relay-State ).
    3. For Mosfet output .Mosfet( Mosfet-NO, Mosfet-State, PWM-Duty=0 (0-100%), PWM-Freq=50 ).
    
    Example:
    
    from m-gpio import mgpio
    from machine import SPI
    
    miniRTU = mgpio()
    
    Periphery = Pin(miniRTU.PIN(1), Pin.OUT)
    spi = SPI(1, miso=Pin(miniRTU.PIN(5)), sck=Pin(miniRTU.PIN(6)))
    
    miniRTU.Relay(1, 1)
    miniRTU.Relay(2, 0)
    
    miniRTU.Mosfet(1, 1)
    miniRTU.Mosfet(2, 1, 30)
    miniRTU.Mosfet(3, 1, 70, 1000)
