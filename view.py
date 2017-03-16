#!/usr/bin/python3

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#:set fileformat=unix
#!!!!!!!!!!!!!!!!!!!!!!!!!!!

'''
*Michal Chorobik 0937145
*CIS 2750 Assignment2
*mchorobi@uofguelph.mail.ca
*February 19, 2017
'''

if __name__ == "__main__":

    import sys
    import glob
    import os
    import curses

def writeFile(pos,user,stream):#{

    #os.chdir("./messages/")
    fileName=stream+"StreamUsers.txt"
    list=[]

    with open(fileName,'r') as f:
       for line in f:
           list.append(line)

    file = open(fileName,'w')
    for line in list:
        if user in line:
            line=user+" "+str(pos)+"\n"
        file.write(line)
    file.close()

#}

def main(var,var2,var3):#{

    lastRead=0
    lastPost=0
    userName = sys.argv[1]

    if var=="0":
        os.chdir("./messages/")
    list=[]

    for file in glob.glob("*StreamUsers.txt"):
        with open(file,'r') as f:
           for line in f:
              for word in line.split():
                  if word==userName:
                      file = file[:-15]
                      list.append(file)

    if not list:
        print("This user is not in any streams")
        sys.exit()

    print(" ".join(list) ,"all ")

    if var=="0":
        pas=0
        while pas==0:
            choice = input()
            for x in range(len(list)):
                if choice == list[x]:
                    pas=1
                if choice == "all":
                    pas=1
            if pas==0:
                print("This is not a possible option")
    else:
        choice=var

    if var2=="1":
        pas=0
        while pas==0:
            choice = input()
            for x in range(len(list)):
                if choice == list[x]:
                    pas=1
                if choice == "all":
                    pas=1
            if pas==0:
                print("This is not a possible option")

    if choice!="all":
        #finding the last read line
        file=choice+"StreamUsers.txt"
        with open(file,'r') as f:
           for line in f:
               line.strip()
               line=line.rstrip('\n')
               if userName in line:
                    viewLine=line.split()
        viewLine=viewLine[1]

        messageList=[]
        file=choice+"StreamData.txt"
        with open(file,'r') as f:
           for line in f:
               for word in line.split():
                   messageList.append(word)

    #curses
    mypad_pos = 0
    screen=curses.initscr()
    screen=curses.newpad(1000,80)
    screen.addstr(23,0," Page Up   Page Down   O-order toggle   M-mark all   S-stream  C-check for new")
    screen.refresh(mypad_pos, 0, 0, 0, 23, 200)

    count=0
    dateList=[]
    senderList=[]
    oldLine=0
    nextLoop=0
    authorLine=""

    if var3=="1":
        if choice == "all":
            for i in range(len(list)):
                file=list[i]+"Stream.txt"
                with open(file,'r') as f:
                   for line in f:
                       line.strip()
                       line=line.rstrip('\n')

                       if nextLoop==1:
                          senderList.append(authorLine+" "+line)
                          senderList.sort()
                          nextLoop=0

                       if "Sender" in line:
                           nextLoop=1
                           authorLine=line[8:]

            newLine=""
            for x in range(len(senderList)):
                for i in range(len(list)):
                    file=list[i]+"Stream.txt"
                    with open(file,'r') as f:
                       for line in f:
                           line.strip()
                           line=line.rstrip('\n')
                           if "Sender" in line:
                              authorLine=line[8:]
                              ok=0
                           if ok==1:
                              screen.addstr(count,0,line)
                              count+=1

                           newLine= authorLine+" "+line
                           if senderList[x] in newLine:
                               if count==23:
                                   screen.addstr(count,0,"                                                                               ")
                               screen.addstr(count,0,str(oldLine))
                               count+=1
                               if count==23:
                                   screen.addstr(count,0,"                                                                               ")
                               screen.addstr(count,0,str(line))
                               count+=1
                               ok=1
                           oldLine=line
        else:
            file=choice+"Stream.txt"
            with open(file,'r') as f:
               for line in f:
                   line.strip()
                   line=line.rstrip('\n')

                   if nextLoop==1:
                      senderList.append(authorLine+" "+line)
                      senderList.sort()
                      nextLoop=0

                   if "Sender" in line:
                       nextLoop=1
                       authorLine=line[8:]

            newLine=""
            for x in range(len(senderList)):
                    file=choice+"Stream.txt"
                    with open(file,'r') as f:
                       for line in f:
                           line.strip()
                           line=line.rstrip('\n')
                           if "Sender" in line:
                              authorLine=line[8:]
                              ok=0
                           if ok==1:
                              if count==23:
                                  screen.addstr(count,0,"                                                                               ")
                              screen.addstr(count,0,line)
                              count+=1

                           newLine= authorLine+" "+line
                           if senderList[x] in newLine:
                               if count==23:
                                   screen.addstr(count,0,"                                                                               ")
                               screen.addstr(count,0,str(oldLine))
                               count+=1
                               if count==23:
                                   screen.addstr(count,0,"                                                                               ")
                               screen.addstr(count,0,str(line))
                               count+=1
                               ok=1
                           oldLine=line
    elif choice=="all":
        for i in range(len(list)):
            file=list[i]+"Stream.txt"
            with open(file,'r') as f:
               for line in f:
                   line.strip()
                   line=line.rstrip('\n')
                   if "Date" in line:
                       dateList.append(line[-4:]+line[-16:-14]+line[-13:-11]+line[-10:-8]+line[-7:-5])
                       sorted(dateList, key=int)
        newLine=""
        for x in range(len(dateList)):
            for i in range(len(list)):
                file=list[i]+"Stream.txt"
                with open(file,'r') as f:
                   for line in f:
                       line.strip()
                       line=line.rstrip('\n')
                       if "Sender" in line:
                          ok=0
                       if ok==1:
                          if count==23:
                              screen.addstr(count,0,"                                                                               ")
                          screen.addstr(count,0,line)
                          count+=1

                       newLine=line[-4:]+line[-16:-14]+line[-13:-11]+line[-10:-8]+line[-7:-5]
                       if dateList[x] in newLine:
                           if count==23:
                               screen.addstr(count,0,"                                                                               ")
                           screen.addstr(count,0,str(oldLine))
                           count+=1
                           if count==23:
                              screen.addstr(count,0,"                                                                               ")
                           screen.addstr(count,0,str(line))
                           count+=1
                           ok=1
                       oldLine=line
    else:
        file=choice+"Stream.txt"
        with open(file,'r') as f:
           for line in f:
               line.strip()
               line=line.rstrip('\n')
               if count==23:
                   screen.addstr(count,0,"                                                                               ")
               screen.addstr(count,0,line)
               count+=1

        #here i move the text down to the last read line of that us
        mypad_pos = mypad_pos + int(viewLine)

        #here i add 23 to the seen lines because as its printed you can see all 23 lines at first
        if int(viewLine)!=0:
            mypad_pos=mypad_pos+1
        viewLine = 24 + int(viewLine)
        prev=0
        for pos in messageList:
            if int(pos)>int(viewLine):
                    lastPost=prev
                    break
            prev=pos
        #print(lastPost)

    screen.refresh(mypad_pos, 0, 0, 0, 22, 200)

    if choice!="all":
        if viewLine==int(messageList[-1]):
                if int(messageList[-1])<22:
                    screen.addstr(22,0,"no messages left")

    if count<23:
         screen.addstr(23,0,"                  ^Go Up To See The Previously Read Messages^                                   ")
         #screen.addstr(23,0,"                                                                               ")
    screen.refresh(mypad_pos, 0, 0, 0, 22, 200)

    cmd=2
    while cmd != -123 :
        cmd=screen.getch();
        #print(cmd)
        if  cmd == 113:
            curses.nocbreak()
            curses.echo()
            curses.endwin()
            break
        if  cmd == 66:
            mypad_pos += 1
            if choice!="all":
                viewLine = 1 + int(viewLine)

                for pos in messageList:
                    if int(pos)>int(viewLine):
                        if int(prev)<int(viewLine):
                            lastPost=prev
                            break
                    prev=pos
            screen.refresh(mypad_pos, 0, 0, 0, 22, 200)
        elif cmd == 65:
            mypad_pos -= 1
            screen.refresh(mypad_pos, 0, 0, 0, 22, 200)
        elif (cmd == 109 or cmd == 77):#m
            if choice!="all":
                lastPost=int(messageList[-1])
        elif (cmd == 99 or cmd == 67):#c
            curses.endwin()
            main(choice,"0","0")
            break
        elif (cmd == 115 or cmd == 83):#s
            curses.endwin()
            main(choice,"1","0")
            break
        elif (cmd == 111 or cmd == 79):#o
            curses.endwin()
            if var3 == "1":
                main(choice,"0","0")
            else:
                main(choice,"0","1")
            break

    if choice!="all":
        if lastPost==0:
            lastPost=int(messageList[-1])
        writeFile(lastPost,userName,choice)
    return 0;
    #}

main("0","0","0")
