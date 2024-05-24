class team:
    def __init__(self,country):
        self.country=country
        self.played=0
        self.wins=0
        self.loss=0
        self.goalscr=0
        self.goalfcd=0
        self.gd=0
        self.draw=0
        self.points=0
    def print(self):
        print(self.country,"MP:" ,self.played,"W:",self.wins,"D:",self.draw,"L:",self.loss,"GF:",self.goalscr,"GA:",self.goalfcd,"GD:",self.gd,"P:",self.points)
    def total_points(self):
        self.points=self.wins*3+self.draw
        self.gd=self.goalscr-self.goalfcd
        
class group:
    def __init__(self,name):
        self.name=name
        self.members=[]
    def add_member(self,member):
        self.members.append(member)
    def display(self):
        print(self.name , self.members)
    def matches(self):
        for i in range(3):
            for j in range(i+1,4):
                match(self.members[i],self.members[j])
    def points_table(self):
        dict1={}
        for i in self.members:
            for j in objs:
                j.total_points()
                if j.country==i:
                    dict1[j]=[j.points,j.gd,j.goalscr]
        ranked=sorted(dict1.values())
        for i in range(len(ranked)-1,-1,-1):
            for key in dict1.keys():
                if dict1[key]==ranked[i]:
                    key.print()
                    if i in [3,2]:
                        ro16.add_team(key.country)
                
                    

class ro16:
    def __init__(self):
        self.next_round=[]
        self.half1=[]
        self.half2=[]
    def add_team(self,team):
        self.next_round.append(team)
    def make_half(self):
        for i in range(len(self.next_round)):
            if i in [0,3,4,7,8,11,12,15]:
                self.half1.append(self.next_round[i])
            else:
                self.half2.append(self.next_round[i])
class qf:
    def __init__(self):
        self.half1=[]
        self.half2=[]

class sf:
    def __init__(self):
        self.half1=[]
        self.half2=[]

class thirdplace:
    def __init__(self):
        self.half3=[]
        self.third=[]
        self.loser=[]

class final:
    def __init__(self):
        self.finalists=[]
        self.winner=[]
        self.runnerup=[]
                
            
def match(team1,team2):
        print(team1," VS ",team2)
        g1=int(input("Enter goals scored by first team:  "))
        g2=int(input("Enter goals scored by second team: "))
        for i in objs:
             if i.country==team1:
                i.played+=1
                i.goalscr+=g1
                i.goalfcd+=g2
                if g1>g2:
                    i.wins+=1
                elif g1<g2:
                    i.loss+=1
                else:
                    i.draw+=1
             elif i.country==team2:
                i.played+=1
                i.goalscr+=g2
                i.goalfcd+=g1
                if g2>g1:
                    i.wins+=1
                elif g2<g1:
                    i.loss+=1
                else:
                    i.draw+=1

def fixtures(l1,l2):
        for i in range(0,len(l1)-1,2):
            print(l1[i]," VS ",l1[i+1])
            g1=int(input("Enter goals scored by first team: "))
            g2=int(input("Enter goals scored by second team: "))
            if g1>g2:
                print(l1[i]," advances")
                l2.append(l1[i])
            elif g2>g1:
                print(l1[i+1]," advances")
                l2.append(l1[i+1])
            else :
                g3=int(input("Enter penalties scored by first team: "))
                g4=int(input("Enter penalties scored by second team: "))
                if g3>g4:
                     print(l1[i]," advances")
                     l2.append(l1[i])
                elif g4>g3:
                     print(l1[i+1]," advances")
                     l2.append(l1[i+1])

def loser(l1,l2,l3):
    for i in l1:
        if i not in l2:
            l3.append(i)

#main
objs=[]
for i in range(32):
    name=input("Enter name of country: ")
    objs.append(team(name))
groups=[]
for i in range(8):
    name=input("Enter group name: ")
    groups.append(group(name))
    for j in range(4):
        a=input("Enter country to add in group: ")
        groups[i].add_member(a)
ro16=ro16()
qf=qf()
sf=sf()
thirdpl=thirdplace()
final=final()
for i in groups:
    i.display()
    i.matches()
    i.points_table()
ro16.make_half()
print("ROUND OF 16 BEGINS") 
fixtures(ro16.half1,qf.half1)
fixtures(ro16.half2,qf.half2)
print("QUARTER FINAL BEGINS")
fixtures(qf.half1,sf.half1)
fixtures(qf.half2,sf.half2)
print("SEMI FINAL BEGINS")
fixtures(sf.half1,final.finalists)
fixtures(sf.half2,final.finalists)
loser(sf.half1,final.finalists,thirdpl.half3)
loser(sf.half2,final.finalists,thirdpl.half3)
print("THIRD PLACE PLAYOFF")
fixtures(thirdpl.half3,thirdpl.third)
print(thirdpl.third[0]," is the 2nd runner up")
print("FINAL BEGINS ")
fixtures(final.finalists,final.winner)
print("Congratulations, ",final.winner[0],"for winning the world cup")
loser(final.finalists,final.winner,final.runnerup)
print(final.runnerup[0]," is the 1st runner up")

