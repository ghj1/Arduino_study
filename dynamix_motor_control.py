import serial 

opencr = serial.Serial(port= '/dev/ttyACM0', baudrate= 115200, timeout=1) # baudrate는 begin이랑 맞아야 한다. 

while True:
    str = input("Enter a str : ")  
    opencr.write(bytes(str, 'utf-8'))
    value = opencr.readline()   
    print('Result: ', value)

    # if number == '1':
    #     key_01 = opencr.write(bytes(number, 'utf-8'))
    #     opencr.write(key_01)
    
    # elif number == '2':
    #     key_02 = opencr.write(bytes(number, 'utf-8'))
    #     opencr.write(key_02)

    # elif number == '3':
    #     key_03 = opencr.write(bytes(number, 'utf-8'))
    #     opencr.write(key_03)

    # elif number == '4':
    #     key_04 = opencr.write(bytes(number, 'utf-8'))
    #     opencr.write(key_04)

    # elif number == '5':
    #     key_05 = opencr.write(bytes(number, 'utf-8'))
    #     opencr.write(key_05)


    
    
