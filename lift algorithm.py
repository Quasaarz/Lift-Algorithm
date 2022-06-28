import time
i = -4 
def lift(a,b):
       global i
       print("Lift is at", i,"th Floor")
       while i > a:
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
                            i-=1
                            print(i)
                            time.sleep(0.5)
                            if i-1 ==  b or i == b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   break
                                   
                     while i<b:
                            print("moving up")
                            i+=1
                            print(i)
                            time.sleep(0.5)
                            if i+1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   break
                     if i ==b:
                            print("Door opening")
                            time.sleep(1)
                            print("Floor Reached")
                            time.sleep(0.5)
                            print("Door closing")
                            break
       while i == a:
              print(i)
              print("Door Opening")
              time.sleep(1)
              print("Door Closing")
              while i > b:
                     print("Going down")
                     i-=1
                     print(i)
                     time.sleep(0.5)
                     if i-1 ==  b or i == b:
                            i=b
                            print(i)
                            print("Door opening")
                            time.sleep(1)
                            print("Floor Reached")
                            time.sleep(0.5)
                            print("Door closing")
                            break
                            
              while i<b:
                     print("moving up")
                     i+=1
                     print(i)
                     time.sleep(0.5)
                     if i+1 ==  b:
                            i=b
                            print(i)
                            print("Door opening")
                            time.sleep(1)
                            print("Floor Reached")
                            time.sleep(0.5)
                            print("Door closing")
                            break
              if i ==b:
                     print("Door opening")
                     time.sleep(1)
                     print("Floor Reached")
                     time.sleep(0.5)
                     print("Door closing")
                     break
              elif i-1 == a:
                     i = a
                     print(i)
                     print("Door Opening")
                     time.sleep(1)
                     print("Door Closing")
                     while i > b:
                            print("Going down")
                            i-=1
                            print(i)
                            time.sleep(0.5)
                            if i-1 ==  b or i == b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   break
                                   
                     while i<b:
                            print("moving up")
                            i+=1
                            print(i)
                            time.sleep(0.5)
                            if i+1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   break
                     if i ==b:
                            print("Door opening")
                            time.sleep(1)
                            print("Floor Reached")
                            time.sleep(0.5)
                            print("Door closing")
                            break
              
       while i < a:
              i+=1
              print(i)
              time.sleep(0.5)
              if i+1 == a:
                     i=a
                     print(i)
                     print("Door Opening")
                     time.sleep(1)
                     print("Door Closing")
                     while i > b:
                            print("Going down")
                            i-=1
                            print(i)
                            time.sleep(0.5)
                            if i-1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   break
                     if i ==b:
                            print("Door opening")
                            time.sleep(1)
                            print("Floor Reached")
                            time.sleep(0.5)
                            print("Door closing")
                            break
                            
                            
                                   
                     while i<b:
                            print("moving up")
                            i+=1
                            print(i)
                            time.sleep(0.5)
                            if i+1 ==  b:
                                   i=b
                                   print(i)
                                   print("Door opening")
                                   time.sleep(1)
                                   print("Floor Reached")
                                   time.sleep(0.5)
                                   print("Door closing")
                                   break
                            
                            
              
while True:
       print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       c = int(input("Enter your current floor"))
       d = int(input("enter your destination floor(lobby is 0 and parking areas mention with a negative number counting down from the lobby(eg. If you want to go to P2 you type -3 if lobby is at P5))"))
       print(c, ",", d)
       print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
       if c!=d and c<=51 and c >= -4 and d<= 51 and d>=-4:
              lift(c, d)
       else:
              print("??")
