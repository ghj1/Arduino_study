import serial 

opencr = serial.Serial(port= '/dev/ttyACM0', baudrate= 115200, timeout=1) # baudrate는 begin이랑 맞아야 한다. 

while True:
    number = input("Enter a number : ")  # serial 모니터의 입력하는 부분과 같음 
    # opencr.write(bytes(number, 'utf-8'))
    # x = opencr.readline()   #readline이 여러값을 받을 수 있다. 

    if number == '1':
        key_01 = opencr.write(bytes(number, 'utf-8'))
        opencr.write(key_01)
    
    elif number == '2':
        key_02 = opencr.write(bytes(number, 'utf-8'))
        opencr.write(key_02)

    elif number == '3':
        key_03 = opencr.write(bytes(number, 'utf-8'))
        opencr.write(key_03)

    elif number == '4':
        key_04 = opencr.write(bytes(number, 'utf-8'))
        opencr.write(key_04)

    elif number == '5':
        key_05 = opencr.write(bytes(number, 'utf-8'))
        opencr.write(key_05)


    
    
