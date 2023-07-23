class Kamanda():
    def __init__(self,nomi,count,trener,capitan):
        self.nomi = nomi
        self.soni = count
        self.murabbiy = trener
        self.sardor = capitan
        
    def show(self,yangi_ka):
        pass
    
teams = list()
son = int(input('Nechta kamanda kiritasiz: '))
for i in range(son):
    ob = Kamanda(input('Nomi: '),int(input('Soni: ')),input('Murabbiy: '),input('Sardor: '))
    teams.append('\n'+ob.nomi+' '+str(ob.soni)+' '+ob.murabbiy+' '+ob.sardor)
teams.sort()
print(*teams)