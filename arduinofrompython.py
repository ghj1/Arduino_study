from termios import XCASE
import serial 

opencr = serial.Serial(port= '/dev/ttyACM0', baudrate= 115200, timeout=1) # baudrate는 begin이랑 맞아야 한다. 

while True:
    number = input("Enter a number : ")  # serial 모니터의 입력하는 부분과 같음 
    opencr.write(bytes(number, 'utf-8'))
    x = opencr.readline()   #readline이 여러값을 받을 수 있다. 
    