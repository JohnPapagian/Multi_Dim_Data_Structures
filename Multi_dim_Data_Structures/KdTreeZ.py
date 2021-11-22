import sys
import datetime

def add(a,b,d):                               #PAPAGIANNOPOULOS
    val=b.d%2 # calc dimension with depth     #DIMITROPOYLOS
    b.par=a
    if(b.data[val]>a.data[val]):

        if(a.right==None):
            a.right=b

        else:
            a=a.right
            b.d+=1
            add(a,b,d)

        return


    if(b.data[val]<=a.data[val]):
        if(a.left==None):
            a.left=b
        else:
            a=a.left
            b.d+=1
            add(a,b,d)
    return



def FindMax(top,val,array,flag): #val=dimension #///////////////////////////////////////
    if(top.data[val]>array.data[val]): #if bigger than max->its new max
        array.data=top.data.copy()
    if(top.left or top.right):
        if (flag==0):
            if(top.right):
                root=root.right
                return FindMax(top,val,array,1)

        else: #flag==1
            if(top.right): #CHECK RIGHT
                x1=FindMax(top.right,val,array,0)
                if(top.left): #CHECK LEFT
                    x2=FindMax(top.left,val,array,0)
                    if(x1.data[val]>x2.data[val]): #COMPARE RESULTS AND GET BEST
                        return x1
                    else:
                        return x2
            else:
                x2=FindMax(top.left,val,array,0)
                return x2
    else: #no children
        return array



def FindMin(top,val,array,flag): #val=dimension array:keeps min node
    if(top):
        if(top.data[val]<array.data[val]):
            array.data=top.data.copy()
        if(top.left or top.right):
            if (flag==0):
                if(top.left):
                    return FindMin(top.left,val,array,1)

            else: #flag==1
                if(top.right): #CHECK RIGHT
                    x1=FindMin(top.right,val,array,0) #flag is 0 again
                    if(top.left): #CHECK LEFT
                        x2=FindMin(top.left,val,array,0)
                        if(x1.data[val]<x2.data[val]): #COMPARE RESULTS AND GET BEST
                            return x1
                        else:
                            return x2
                    else:
                        return x1
                else:
                    x2=FindMin(top.left,val,array,0)
                    return x2
        else:
            return array



def PrintTree(root): #///////////////////////////////////////#//////////////////
    if(root):
         PrintTree(root.left)
         print(root.data)
         PrintTree(root.right)
         return


def Edit(old,p,new): #old=node p=old point new=new poin
    x=Search(root,old,0)
    temp.data=x.data.copy()
    pos=[]
    pos.insert(0,temp.data[0])
    pos.insert(1,temp.data[1])
    Delete(pos,root,0)
    temp.data[p]=new
    #print(temp.data)
    #print("\n\n",root.data,temp.data,"\n")
    temp.d=0
    add(root,temp,0)
    #check=[]
    #check.insert(0,temp.data[0])
    #check.insert(1,temp.data[1])
    #x=Search(root,check,0)
    #print(x.data)

    return

def Search(root,tar,d): #///////////////////////////////////////#///////////////

    if(root):
        val=d%2   #calc dimension
        if(tar[0]==root.data[0] and tar[1]==root.data[1]):
            return root

        if(tar[val]>root.data[val]):

            if(root.right):
                root=root.right
                d+=1
                return Search(root,tar,d)

            else:
                print("Can't go right,Target not found")
                return root
        else:

            if(root.left):
                root=root.left
                d+=1
                return Search(root,tar,d)

            else:
                print("Can't go left,Target not found")
                return root


def Delete(tar,top,d):   #tar=target node #///////////////////////////////////////

    if(top):
        while not (tar[0]==top.data[0] and tar[1]==top.data[1]):
            val=d%2   #calc dimension
            if(tar[val]>top.data[val]):
                top=top.right     #GO RIGHT
                d+=1
                return Delete(tar,top,d)

            else:
                top=top.left        #GO LEFT
                d+=1
                return Delete(tar,top,d)
    else:
        return

    val=top.d%2

    if not (top.left or top.right):
        if (top.par):
             if(top.par.left==top):
                 top.par.left=None

             else:
                 top.par.right=None

             top=None
             flag=False
             return

    elif(top.right):
        array=Tree()
        array.data.insert(0,999999999)
        array.data.insert(1,999999999)
        found=FindMin(top.right,val,array,val)
        top.data=found.data.copy()

        list=[]
        list.insert(0,found.data[0])
        list.insert(1,found.data[1])
        Delete(list,top.right,d)

    elif(top.left):
        array=Tree()
        array.data.insert(0,0)
        array.data.insert(1,0)
        found=FindMax(top.left,val,array,val)
        top.data=found.data.copy()

        list=[]
        list.insert(0,found.data[0])
        list.insert(1,found.data[1])
        Delete(list,top.left,d) #delete the diadoxos


#///////////////////////////////////////////////////////////////////////////////
def NNSearch(top,tar,val,best,cut,f):#///////////////////////////////////////

    d=(val-1)%2#//////////////////////////

    if(top.par and (top.left or top.right)):

        if(best<((cut*cut)) and best<(top.par.data[d]-tar[d])**2): #PRUNING
            return f

    x=(((top.data[0]-tar[0])**2)+((top.data[1]-tar[1])**2))

    if(best==9999):
        cut=tar[d]-top.data[d]              #cut is difference to tar in cutting dimension
    else:                                   #its not a box in the first run
        cut=tar[d]-top.par.data[d]
    d=val%2#//////////////////////////////////


    if(x<best):
        best=x
        f=top


    if(not top.left and not top.right): #if no children return
        return f


    if(tar[d]>=top.data[d]): #RIGHT->LEFT

         if(top.right):                #RIGHT SUTREE
             RES1=NNSearch(top.right,tar,val+1,best,cut,f)
             r1=(((RES1.data[0]-tar[0])**2)+((RES1.data[1]-tar[1])**2))

         if(top.left):                 #LEFT SUBTREE

             if not(top.right):
                 RES2=NNSearch(top.left,tar,val+1,best,cut,f)
                 r2=(((RES2.data[0]-tar[0])**2)+((RES2.data[1]-tar[1])**2))

                 return RES2 #RES IS BETTER OR EQUAL TO FORMER BEST

             else:
                 RES2=NNSearch(top.left,tar,val+1,r1,cut,RES1)        #otan kaleseis tin apo katw thes to apotelesma tis apo panw mesa
                 r2=(((RES2.data[0]-tar[0])**2)+((RES2.data[1]-tar[1])**2))

                 return RES2        #RES IS BETTER OR EQUAL TO FORMER BEST

         else:
             if(r1<best):
                 f=RES1
             return f
            #PANTA THA EKTELEITAI 1 APO TA 2 DEN BLEKONTAI GENIKA MONO H SEIRA ALLAZEI


    else: #LEFT=>RIGHT

        if(top.left):

            RES1=NNSearch(top.left,tar,val+1,best,cut,f)
            r1=((RES1.data[0]-tar[0])**2+(RES1.data[1]-tar[1])**2)

        if(top.right):
            if not(top.left):
                RES2=NNSearch(top.right,tar,val+1,best,cut,f)
                r2=(((RES2.data[0]-tar[0])**2)+((RES2.data[1]-tar[1])**2))

                return RES2     #RES IS BETTER OR EQUAL TO FORMER BEST

            else:
                RES2=NNSearch(top.right,tar,val+1,r1,cut,RES1)
                r2=(((RES2.data[0]-tar[0])**2)+((RES2.data[1]-tar[1])**2))

                return RES2       #RES IS BETTER OR EQUAL TO FORMER BEST

        else:
                return RES1         #RES IS BETTER OR EQUAL TO FORMER BEST


#top=current node///////target=given node  #val=
#best=list of nn distances///////cut=distance to bounding square
#f=list of nn nodes
def KNNSearch(top,tar,val,best,cut,f): #///////////////////////////////////////

    d=(val-1)%2
    if(top.par and (top.left or top.right)):


        if(best[0]<cut*cut and best[0]<(top.par.data[d]-tar[d])**2):
            return f

    x=(((top.data[0]-tar[0])**2)+((top.data[1]-tar[1])**2))
    if(best[k]==9999):
        cut=tar[d]-top.data[d]              #cut is difference to tar in cutting dimension
    else:                                  #its not a box in the first run
        cut=tar[d]-top.par.data[d]
    d=val%2


    p=k
    while(p>=0 and x<best[p]):
        p-=1
    p+=1
    best.insert(p,x)
    f.insert(p,top)
    best.pop(k+1)
    f.pop(k+1)


    if(tar[d]>=top.data[d]):

         if(top.right):
             RES1=KNNSearch(top.right,tar,val+1,best,cut,f)
             if not(top.left):
                     return RES1



         if(top.left):
             RES2=KNNSearch(top.left,tar,val+1,best,cut,f)
             if not(top.right):
                         return RES2

             for i in range (0,k): #combine and get best final list from both subtrees
                x=(((RES1[i].data[0]-tar[0])**2)+((RES1[i].data[1]-tar[1])**2))
                y=(((RES2[i].data[0]-tar[0])**2)+((RES2[i].data[1]-tar[1])**2))
                if(x<y):
                    f[i]=RES1[i]
                else:
                    f[i]=RES2[i]

             return f                #return combined list

         else:
             return f
            #PANTA THA EKTELEITAI 1 APO TA 2 DEN BLEKONTAI GENIKA MONO H SEIRA ALLAZEI

    else:
        if(top.left):
            RES1=KNNSearch(top.left,tar,val+1,best,cut,f)
            if not(top.right):
                return RES1



        if(top.right):
                RES2=KNNSearch(top.right,tar,val+1,best,cut,f)
                if(top.left):

                    for i in range (0,k): #combine and get best final list from both subtrees
                        x=(((RES1[i].data[0]-tar[0])**2)+((RES1[i].data[1]-tar[1])**2))
                        y=(((RES2[i].data[0]-tar[0])**2)+((RES2[i].data[1]-tar[1])**2))
                        if(x<y):
                            f[i]=RES1[i]
                        else:
                            f[i]=RES2[i]

                        return f        #return combined list
                else:
                    return RES2


        else:
            return f




class Tree(object):
    def __init__(self):
        self.right=None
        self.left=None
        self.par=None
        self.data=[]
        self.d=0

root=Tree()
with open("data66.txt",'r',encoding='utf8',errors='ignore') as f:
    for line in f:
        data=[i for i in line.split('  ')] #SPLIT LINE
        temp=Tree()
        data[0].strip(' ')
        data[1].strip(' ')
        temp.data.insert(0,float(data[0][:8]))
        temp.data.insert(1,float(data[1][:8]))
        temp.data.insert(2,data[2][:25])
        temp.data.insert(3,data[3][:20])
        if(len(root.data)==0): #if no root become root
            root.data=temp.data
        else:
            add(root,temp,0) #root,what is added, depth

while True:
    try: #MENU
        print("\n MENU\n What do you want to do?\
    (ALL COORDINATES NEED 5 DECIMALS/ 1,11 m accuracy)\n\n")
        #Print1Tree(root.right)
        print("Press 0 to add node\nPress 1 to search\nPress 2 to see the tree\
        \nPress 3 to edit node\nPress 4 to delete\nPress 5 for nearest neigbor\
        \nPress 6 for knn\nPress 7 to exit()")
        c=int(input())

        if(c==0):
            temp=Tree()
            print("Insert latitude:")
            x1=input()
            print("Insert longitude:")
            x2=input()
            print("Insert area")
            x3=input()
            print("Insert country")
            x4=input()
            temp.data.insert(0,float(x1[:8])) #READ FIRST PART OF LINE THAT IS THE 'AM'
            temp.data.insert(1,float(x2[:8]))
            temp.data.insert(2,x3[:25])
            temp.data.insert(3,x4[:20])
            print(temp.data)
            if(len(root.data)==0): #if no root become root
                root.data=temp.data
            else:
                add(root,temp,0) #root,what is added, depth
        if(c==1):        #SEARCH
            print("Which node are you searching for?")
            tar=[]
            x=input()
            y=input()
            tar.insert(0,float(x[:8]))
            tar.insert(1,float(y[:8]))

            start=datetime.datetime.now()
            x=Search(root,tar,0)
            end=datetime.datetime.now()

            print("I did that in:",(end-start))
            print(x.data)
            print("PRESS ENTER TO RETURN TO MENU\n")
            k=input()
        elif(c==2): #PrintTree
                print("\n\nEuropean train stations:\n")
                print("Latitude  -- Longtitude  --  Area  --  Country\n")

                start=datetime.datetime.now()
                PrintTree(root)
                end=datetime.datetime.now()

                print("I did that in:",(end-start))
                print("PRESS ENTER TO RETURN TO MENU\n")
                k=input()
        elif(c==3): #EDIT
            print("Which node would you like to change\n")
            tar=[]
            x=input()
            y=input()
            tar.insert(0,float(x[:8]))
            tar.insert(1,float(y[:8]))
            k=int(input("Change latitude(0),longitude(1),area(2) or country(3)? ")) #which value
            n=input("What will be the new value? ") #

            start=datetime.datetime.now()
            Edit(tar,k,n)
            end=datetime.datetime.now()

            print("I did that in:",(end-start))
            k=input()
        elif(c==4):
            print("Which node would you like to delete\n")
            tar=[]
            x=input()
            y=input()
            tar.insert(0,float(x[:8]))
            tar.insert(1,float(y[:8]))
            print("Im goint to delete",tar[0],tar[1])
            k=input()

            start=datetime.datetime.now()
            Delete(tar,root,0)
            end=datetime.datetime.now()

            print("I did that in:",(end-start))
            print("PRESS ENTER TO RETURN TO MENU\n")
            k=input()
        elif(c==5):
            print("Which point")
            tar=[]
            x=input()
            y=input()
            tar.insert(0,float(x[:8]))
            tar.insert(1,float(y[:8]))


            start=datetime.datetime.now()
            k=NNSearch(root,tar,0,9999,0,root)
            end=datetime.datetime.now()


            print("I did that in:",(end-start))
            print("DONE THE RESULTS ARE:\n")
            print(k.data)
            a1=((float(x)-k.data[0])*111000)
            if((a1)<0):
                h="North"
            else:
                h="South"
            a2=(float(y)-k.data[1])*111000
            if((a2)<0):
                p="East"
            else:
                p="West"

            a1=abs(a1)
            a2=abs(a2)

            print("\nThe station in located","{0:.2f}".format(a1),"\
meters",h,"{0:.2f}".format(a2),"meters",p,"\nPRESS ENTER TO RETURN TO MENU\n")
            k=input()

        elif(c==6):
            print("Which point")
            tar=[]
            x=input()
            y=input()
            tar.insert(0,float(x[:8]))
            tar.insert(1,float(y[:8]))
            print("How many neigbors are you looking for:")
            k=int(input())
            best=[]
            for i in range(k):
                best.insert(i,9999)
            f=[]
            for i in range(k):
                f.insert(i,root)
            print("GOIND FOR NEIGBORS\n")
            k-=1


            start=datetime.datetime.now()
            l=KNNSearch(root,tar,0,best,0,f)
            end=datetime.datetime.now()


            print("DONE THE RESULTS ARE:\n")
            print(i)
            for i in range(k+1):
                print(l[i].data)
            print("\nI did that in:",(end-start),"\n")
            a1=((float(x)-l[0].data[0])*111000)
            if((a1)<0):
                h="North"
            else:
                h="South"
            a2=(float(y)-l[0].data[1])*111000
            if((a2)<0):
                p="East"
            else:
                p="West"

            a1=abs(a1)
            a2=abs(a2)

            print("\nThe station in located","{0:.2f}".format(a1),"\
meters",h,"{0:.2f}".format(a2),"meters",p,"\nPRESS ENTER TO RETURN TO MENU\n")
            k=input()

        elif(c==7):
            print("\n\nSESSION COMPLETED\n\n")
            break

    except:
        print("Choose one of the functions given")
