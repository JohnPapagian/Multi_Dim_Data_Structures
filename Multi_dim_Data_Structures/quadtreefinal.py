import datetime

#from math import sqrt

class Position():
     def __init__(self, x=0.0, y=0.0):
       self.x=x
       self.y=y




class Node():
    def __init__(self, pos):
       self.pos=pos
       self.data=[]




class Quadtree():
    def __init__(self):  #top,bot == positions

        self.top=None
        self.bot=None
        self.n=[]
        self.parent=None
        self.SW=None
        self.SE=None
        self.NW=None
        self.NE=None




    def add(self, node):
        if(node):


            if(self.inBound(node.pos)):

                if(self.SW==None and self.SE==None and self.NW==None and self.NE==None):
                    if(len(self.n)<3):

                        self.n.append(node)
                        return
                    else:


                        self.subdivide()

                        self.add(node)
                        return


                if(self.SW.inBound(node.pos)):

                    self.SW.add(node)
                    return

                if(self.NW.inBound(node.pos)):


                    self.NW.add(node)
                    return

                if(self.SE.inBound(node.pos)):

                    self.SE.add(node)
                    return


                if(self.NE.inBound(node.pos)):

                    self.NE.add(node)
                    return

        return

    def inBound(self, p):

        if(p.x >= self.bot.x and p.x <= self.top.x and p.y <= self.top.y and p.y >= self.bot.y):

             return True

        return False

    def subdivide(self):

        self.SW=Quadtree()
        self.SW.top=Position((self.top.x+self.bot.x)/2, (self.bot.y+self.top.y)/2)
        self.SW.bot=Position(self.bot.x, self.bot.y)
        self.SW.parent=self
        self.NW=Quadtree()
        self.NW.top=Position((self.top.x+self.bot.x)/2, self.top.y)
        self.NW.bot=Position(self.bot.x, (self.bot.y+self.top.y)/2)

        self.NW.parent=self

        self.SE=Quadtree()
        self.SE.top=Position(self.top.x, (self.top.y+self.top.x)/2)
        self.SE.bot=Position((self.top.x+self.bot.x)/2,  self.bot.y)
        self.SE.parent=self
        pos=Position(self.top.x, self.top.y)

        pos1=Position((self.top.x+self.bot.x)/2, (self.top.y+self.bot.y)/2)
        self.NE=Quadtree()
        self.NE.top=Position(self.top.x, self.top.y)
        self.NE.bot=Position((self.top.x+self.bot.x)/2, (self.top.y+self.bot.y)/2)
        self.NE.parent=self

        for i in self.n:
            if(self.SW.inBound(i.pos)):
                self.SW.n.append(i)
                continue
            if(self.NW.inBound(i.pos)):
                self.NW.n.append(i)
                continue
            if(self.NE.inBound(i.pos)):


                self.NE.n.append(i)
                continue
            if(self.SE.inBound(i.pos)):

                self.SE.n.append(i)


        del self.n
        return





    def search(self, p):

        if(self.inBound(p)):

            if(self.SW==None or self.SE==None or self.NW==None or self.NE==None):
                for i in self.n:
                    if(p.x==i.pos.x and p.y==i.pos.y):

                        return i

                return None




            if(self.SW.inBound(p)):
                return self.SW.search(p)


            if(self.NW.inBound(p)):
                return self.NW.search(p)


            if(self.SE.inBound(p)):
                 return    self.SE.search(p)


            if(self.NE.inBound(p)):
                return self.NE.search(p)

        return None

    def edit(self):

        pos1=Position(0,0)
        node=Node(pos1)

        print("Which node would you like to change\n")
        x=input()
        y=input()
        pos=Position()
        pos.x=float(x)
        pos.y=float(y)
        data=[]
        data.append(str(input("Edit the data: ")))

        start=datetime.datetime.now()

        node=root.search(pos)
        node.data=data
        root.delete(pos)
        root.add(node)

        end=datetime.datetime.now()



        print("I did that in:",(float)((end-start))

        return
    def delete(self, p):



        if(self.inBound(p)):

           if(self.SW==None or self.SE==None or self.NW==None or self.NE==None):

               i=0
               g=len(self.n)
               for i in range (len(self.n)):
                   if(self.n[i].pos.x==p.x and self.n[i].pos.y==p.y):
                       del self.n[i]
                       break;

               return



           else:

               if(self.SW.inBound(p)):
                   self.SW.delete(p)

                   return

               if(self.NW.inBound(p)):
                   self.NW.delete(p)
                   return
               if(self.SE.inBound(p)):
                   self.SE.delete(p)

                   return
               if(self.NE.inBound(p)):
                   self.NE.delete(p)
                   return


        return
    def printree(self):
        if(self.SW==None and self.SE==None and self.NW==None and self.NE==None):
            for i in range(len(self.n)):
                print(self.n[i].data)
            return
        else:

            self.SW.printree()
            self.SE.printree()
            self.NW.printree()
            self.NE.printree()
        return
    def searchNN(self, pos, neighors, k):


        if((self.top.x>=pos.x-5) and (self.top.y>=pos.y-5) and (self.bot.x<=pos.x+5) and (self.bot.y<=pos.y+5)):


            if(self.SW==None and self.SE==None and self.NW==None and self.NE==None):

                for i in range(len(self.n)):
                    if(abs(self.n[i].pos.x-pos.x)<=5 and abs(self.n[i].pos.y-pos.y)<=5):
                        neighors.append(self.n[i])


                if(len(neighors)>k):
                    neighors.sort(key=lambda x: ((x.pos.x - pos.x)**2+(x.pos.y - pos.y)**2))

                    while(len(neighors)>k):
                        del neighors[-1]



            else:
                if(self.SW):

                    self.SW.searchNN(pos, neighors,k)
                if(self.NW):

                    self.NW.searchNN(pos, neighors,k)
                if(self.SE):

                    self.SE.searchNN(pos, neighors,k)
                if(self.NE):

                    self.NE.searchNN(pos, neighors,k)
                return
        else:

            return
root=Quadtree()

root.bot=Position(40.0,0.0)
root.top=Position(60.0,20.0)



with open("data66.txt",'r',encoding='utf8',errors='ignore') as f:
    for line in f:
        data=[i for i in line.split('  ')] #SPLIT LINE
        pos=Position(x=0.0,y=0.0)
        node=Node(pos)
        data[0].strip(' ')
        data[1].strip(' ')
        try:
            node.pos.x=float(data[0][:9])
            node.pos.y=float(data[1][:9])

            node.data.insert(0,data[2][:25])
            node.data.insert(1,data[3][:20])

            root.add(node)


        except ValueError:
            pass

while(1):
    try:
        print("\n  MENU\n  What do you want to do?\n")
        print("Press 1 to search\nPress 2 to see the tree\
        \nPress 3 to edit node\nPress 4 to delete\nPress 5 for nearest neigbor\
        \nPress 6 else to exit")
        c=int(input())
        if(c==1):        #SEARCH
            print("What do you want to search for?")
            x=input()
            y=input()
            pos=Position()
            pos.x=float(x)
            pos.y=float(y)

            start=datetime.datetime.now()
            if(root.search(pos)!= None):
                end=datetime.datetime.now()
                print("I did that in:",(end-start))

                print(root.search(pos).data)
        elif(c==2): #PrintTree
                print("\n\nΤΑ ΔΗΜΟΣΙΑ WIFI ΣΤΗΝ ΕΛΛΑΔΑ ΕΊΝΑΙ:\n")
                print("Latitude  -- Longtitude  --  Περιγραφή  --  Δήμος\n")
                start=datetime.datetime.now()
                root.printree()
                end=datetime.datetime.now()
                print("I did that in:",(end-start))
        elif(c==3):
            root.edit()
        elif(c==4):
                print("Which node would you like to delete\n")
                pos=Position()
                x=input()
                y=input()
                pos.x=float(x)
                pos.y=float(y)


                start=datetime.datetime.now()
                root.delete(pos)
                end=datetime.datetime.now()


                print("I did that in:",(end-start))
        elif(c==5):
            print("which is the node you want the nearest neighors?")
            x=input()
            y=input()
            pos=Position()
            pos.x=float(x)
            pos.y=float(y)
            neighors=[]
            print("How many neighors would you like\n")
            k=input()


            start=datetime.datetime.now()
            root.searchNN(pos, neighors,int(k))
            end=datetime.datetime.now()



            print("I did that in:",(end-start))
            for i in range(len(neighors)):
                print(neighors[i].data,neighors[i].pos.x,neighors[i].pos.y)
            a1=((float(x)-neighors[0].pos.x)*111000)
            if((a1)<0):
                h="North"
            else:
                h="South"
            a2=(float(y)-neighors[0].pos.y)*111000
            if((a2)<0):
                p="East"
            else:
                p="West"

            a1=abs(a1)
            a2=abs(a2)
            print("I did that in:",(end-start))
            print("\nThe nearest station in located","{0:.2f}".format(a1),"\
meters",h,"{0:.2f}".format(a2),"meters",p,"\n PRESS ENTER TO RETURN TO MENU\n")
            k=input()
        elif(c==6):
            print("SESSION COMPLETED")
            break
    except:
        pass
