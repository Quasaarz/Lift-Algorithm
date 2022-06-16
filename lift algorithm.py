import time
i = -4 
def lift(a,b):
       while i >a:
              print(i)
              i-=1
              time.sleep(0.5)
              if i-1 == a:
                     i = a
                     print(i)
                     print("Door Opening")
                     time.sleep(1)
                     print("Door Closing")
                     while i > b:
                            print("Going down")
                            print(i)
                            i-=1
                            time.sleep(0.5)
                            if i-1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   
                     while i<b:
                            print("moving up")
                            print(i)
                            i+=1
                            time.sleep(0.5)
                            if i+1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   
              
       while i < a:
              print(i)
              i+=1
              time.sleep(0.5)
              if i+1 == a:
                     i=a
                     print(i)
                     print("Door Opening")
                     time.sleep(1)
                     print("Door Closing")
                     while i > b:
                            print("Going down")
                            print(i)
                            i-=1
                            time.sleep(0.5)
                            if i-1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   
                     while i<b:
                            print("moving up")
                            print(i)
                            i+=1
                            time.sleep(0.5)
                            if i+1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
     
       
              
while True:
       print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       c = int(input("Enter your current floor"))
       d = int(input("enter your destination floor(lobby is 0 and parking areas mention with a negative number counting down from the lobby(eg. If you want to go to P2 you type -3 if lobby is at P5))"))
       print(c, ",", d)
       print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       if c!=d:
              lift(c, d)
       else:
              print("??")
