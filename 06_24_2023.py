import os
os.system("cls")

#-------------------------------------------R1-----------------------------------------------
"""
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(set(sample_list))
print(sample_set)
"""
#-------------------------------------------R2-----------------------------------------------
"""
set1 = (10, 20, 30, 40, 50)
set2 = {30, 40, 50, 60, 70}
print(set2.intersection(set(set1)))
"""
#-------------------------------------------R3-----------------------------------------------
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))
"""
#-------------------------------------------R4-----------------------------------------------
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dct = {}

for i in range(len(keys)):
    dct[keys[i]] = values[i]
print(dct)
"""
#-------------------------------------------R5-----------------------------------------------
"""
sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])
"""
#-------------------------------------------R6-----------------------------------------------
"""
sampleDict = {'a': 100, 'b': 200, 'c': 300}
sampleDict = list(sampleDict.items())

for i in sampleDict:
    if i[1] == 200:
        print("bor")
        exit()
print("yo'q")
"""
#-------------------------------------------R7-----------------------------------------------
"""
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sampleDict["location"] = sampleDict["city"]
print(sampleDict)
"""
#-------------------------------------------R8-----------------------------------------------
"""
lst = [
     [1, 'Jean Castro', 'V'],
     [2, 'Lula Powell', 'V'],
     [3, 'Brian Howell', 'VI'],
     [4, 'Lynne Foster', 'VI'],
     [5, 'Zachary Simon', 'VII']
]
dct = {}
for i in lst:
    dct[i[0]] = [i[1], i[2]]
    print(dct[i[0]])
print()
"""
#-------------------------------------------R9-----------------------------------------------
"""
user = {   
    "login": "kalit2000",
    "password": "qwerty",
    "name": "Dildora",
    "age": 18    
}
print(user)

print("\t"*5, "c")
user["status"] = "active"  #"inactive"
print(user)

print("\t"*5, "d")
user["age"] += 1
print(user)

print("\t"*5, "e")
adress = {
    "city": "Tashkent",
    "street": "Sugdiona",
    "house": 690
}
user["adress"] = (adress)
print(user)

print("\t"*5, "f")
login = input("Login kiriting: ")
password = input("Password kiriting: ")
if user["login"] == login and user["password"] == password:
    print("Ism ->", user["name"] ,"\nYosh ->" , user["age"])
    print("City ->",user["adress"]["city"],"\nStreet ->",user["adress"]["street"],"\nHouse ->", user["adress"]["house"])

print("\t"*5, "g")
user.pop("status")
print(user)

print("\t"*5, "h")
kir = False
for i in user:
    if i == "status":
        kir = True
print("Status kaliti bor" if kir else "Status kaliti yo'q")

print("\t"*5, "i")
user.popitem()
print(user)

print("\t"*5, "j")
foods = {
    "osh": 20000,
    "burger": 15000,
    "manti": 6000,
    "norin": 21000,
    "pizza": 45000
}
print(foods)

print("\t"*5, "k")
print(foods[max(foods, key=foods.get)])

print("\t"*5, "l")
nomi = input("Taom nomini kiriting: ")
for i in foods:
    if i == nomi:
        print(foods[i],"so'm")
        break
    
print("\t"*5, "m")
while True:
    soz = input("Taom nomini kiriting: ")
    if soz == "tamom" or soz == "TAMOM":
        break
    narx = int(input("Narxni kiriting: "))
    foods[soz] = narx
    print()
foods = list(foods.items())

for i in range(len(foods)):
    for i in range(1, len(foods)):
        if foods[i-1][1] > foods[i][1]:
            temp = foods[i-1]
            foods[i-1] = foods[i]
            foods[i] = temp
print(dict(foods))
"""
#------------------------------------------R13-----------------------------------------------
"""
son = input("listga son kiriting: ").split()
for i in range(len(son)):
    son[i] = int(son[i])
print(son)

for i in range(-1, -len(son)-1, -1):
    if son[i] < 9:
        son[i] += 1
        break
    elif son[i] == 9:
        son[i] = 0
        if i == -len(son):        
            son.insert(0, 1)
            break
        if son[i-1] < 9:
            son[i-1] += 1
            break
print(son)
"""
##########################################################################################
########################################### Amaliyot #####################################

#-------------------------------------------1-masala--------------------------------------
"""
tple = [(1,2),(2,3),(3,4)]
print(tple)
for i in range(len(tple)):
    tple[i] = list(tple[i])
print(tple)
"""
#-------------------------------------------2-masala--------------------------------------
"""
tple = [(1,2),(2,3),(4,5)]
print(tple)
for i in range(len(tple)):
    tple[i] = sum(tple[i])
print(tple)
"""
#-------------------------------------------3-masala--------------------------------------
"""
dct = {1: 10, 2: 20, 3:30, 4: 45, 5: 25}
print(dct)              #qiymati kichik va kattalarni o'chirilish kerak
value = list(dct.values())
for i in dct:
    if dct[i] == min(value):
        min_key = i
    if dct[i] == max(value):
        max_key = i
dct.pop(min_key)
dct.pop(max_key)

print(dct)
"""
#-------------------------------------------4-masala--------------------------------------
"""
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {9:90, 7:70}
dict1 |= dict2 | dict3
print(dict1)
"""
#-------------------------------------------5-masala--------------------------------------
"""
dct = {'data1':100,'data2':-54,'data3':247}
value = list(dct.values())
print(sum(value),"yig'indisi")
"""
#-----------------------------------------------------------------------------------------
#-----------------------------------------  masala  --------------------------------------
"""
Data = [{
  "model": "RDX",
  "year": 2009
}, {
  "model": "LS",
  "year": 2000
}, {
  "model": "GLK-Class",
  "year": 2010
}, {
  "model": "Express 1500",
  "year": 2005
}, {
  "model": "LR2",
  "year": 2008
}, {
  "model": "XF",
  "year": 2012
}, {
  "model": "MR2",
  "year": 2005
}, {
  "model": "Malibu",
  "year": 2007
}, {
  "model": "M-Class",
  "year": 2010
}, {
  "model": "Routan",
  "year": 2011
}]

#Yuqorida keltirilgan ma'lumotlarni yili bo'yicha o'sish tartibida saralab chiqaring

                    #1-yechim
Data.sort(key=lambda k : k['year'])
print(Data)
                    #2-yechim
for i in range(1, len(Data)):
    if Data[i-1]["year"] > Data[i]["year"]:
        temp = Data[i]
        Data[i] = Data[i-1]
        Data[i-1] = temp
print(Data)
"""
        
##########################################################################################
##########################################  Uy ishi  #####################################
"""
data = [
    {"full_name":"Eugene Elsmor","company":"Kazu","position":"Electrical Engineer","salary":"$4440.86"},
    {"full_name":"Joni Stredder","company":"JumpXS","position":"Environmental Tech","salary":"$870.05"},
    {"full_name":"Terri-jo Fulham","company":"Tagchat","position":"Assistant Media Planner","salary":"$1992.55"},
    {"full_name":"Priscilla Pandya","company":"Youopia","position":"Help Desk Operator","salary":"$3715.95"},
    {"full_name":"Wolfy Swanborough","company":"Topiclounge","position":"Recruiter","salary":"$1045.61"},
    {"full_name":"Raleigh Ratter","company":"Zoozzy","position":"Graphic Designer","salary":"$602.41"},
    {"full_name":"Anastasia Winward","company":"Avaveo","position":"Cost Accountant","salary":"$3641.42"},
    {"full_name":"Dorry Vasyunichev","company":"Fivebridge","position":"Junior Executive","salary":"$2035.05"},
    {"full_name":"Richy Cleft","company":"Jamia","position":"Sales Associate","salary":"$912.98"},
    {"full_name":"Zack Record","company":"Oyonder","position":"Social Worker","salary":"$2492.23"},
    {"full_name":"Lissy Newns","company":"Riffwire","position":"Developer II","salary":"$1177.79"},
    {"full_name":"Audrye Churchyard","company":"Photospace","position":"Environmental Tech","salary":"$4125.83"},
    {"full_name":"Timothy Seligson","company":"Riffpath","position":"Compensation Analyst","salary":"$1271.94"},
    {"full_name":"Brandie Rogeon","company":"Riffpath","position":"Analyst Programmer","salary":"$1911.09"},
    {"full_name":"Dane Rugg","company":"Twimm","position":"Associate Professor","salary":"$2200.72"},
    {"full_name":"Mick Jeduch","company":"Realblab","position":"Executive Secretary","salary":"$1154.20"},
    {"full_name":"Rowland Christofol","company":"Mycat","position":"Senior Cost Accountant","salary":"$1119.94"},
    {"full_name":"Sibella Abrahams","company":"Minyx","position":"Internal Auditor","salary":"$4023.25"},
    {"full_name":"Layne Thomel","company":"Centimia","position":"Research Associate","salary":"$4073.17"},
    {"full_name":"Demetris Clemenzi","company":"Tagopia","position":"Human Resources Manager","salary":"$1530.37"},
    {"full_name":"Kerstin Devon","company":"Katz","position":"Senior Quality Engineer","salary":"$1305.61"},
    {"full_name":"Brandon Burgwyn","company":"Mydeo","position":"Physical Therapy Assistant","salary":"$1325.58"},
    {"full_name":"Dyana Crosby","company":"BlogXS","position":"Payment Adjustment Coordinator","salary":"$1501.54"},
    {"full_name":"Harald Voller","company":"Riffpedia","position":"Accountant I","salary":"$4397.60"},
    {"full_name":"Nollie Phipard-Shears","company":"Aimbo","position":"Legal Assistant","salary":"$3172.57"},
    {"full_name":"Gaynor Dannohl","company":"Leexo","position":"Administrative Assistant II","salary":"$3035.89"},
    {"full_name":"Tome Bensen","company":"Yamia","position":"Assistant Professor","salary":"$3677.10"},
    {"full_name":"Jessey Anshell","company":"Bubblemix","position":"Registered Nurse","salary":"$2782.66"},
    {"full_name":"Valentijn Melbury","company":"Bluejam","position":"Statistician I","salary":"$1308.43"},
    {"full_name":"Rochelle Andrejevic","company":"Rhyzio","position":"VP Product Management","salary":"$1734.61"}
]
"""
#-------------------------------------------1-masala--------------------------------------
"""
max = float(data[0]["salary"][1:])
index = 0
for i in range(1, len(data)):
    if float(data[i]["salary"][1:]) > max:
        max = float(data[i]["salary"][1:])
        index = i
print("NAME:",data[index]["full_name"])
print("COMPANY NAME:",data[index]["company"])
print("JOB POSITION:",data[index]["position"])
print("SALARY:",data[index]["salary"])
"""
#-------------------------------------------2-masala--------------------------------------
"""
for i in range(len(data)):  #sortlash
    for i in range(1, len(data)):
        if float(data[i-1]["salary"][1:]) < float(data[i]["salary"][1:]):
            temp = data[i]
            data[i] = data[i-1]
            data[i-1] = temp

for i in range(5):
    print(f"\t\t\t\t{i+1}-top ishchi:")
    print("NAME:",data[i]["full_name"])
    print("COMPANY NAME:",data[i]["company"])
    print("JOB POSITION:",data[i]["position"])
    print("SALARY:",data[i]["salary"])
    print()
"""
#-------------------------------------------3-masala--------------------------------------
"""
min = float(data[0]["salary"][1:])
index = 0
for i in range(1, len(data)):
    if float(data[i]["salary"][1:]) < min:
        min = float(data[i]["salary"][1:])
        index = i
print("NAME:",data[index]["full_name"])
print("COMPANY NAME:",data[index]["company"])
print("JOB POSITION:",data[index]["position"])
print("SALARY:",data[index]["salary"])
"""
#-------------------------------------------4-masala--------------------------------------
"""
for i in range(len(data)):
    salary = float(data[i]["salary"][1:])
    if salary < 1000:
        print("NAME:",data[i]["full_name"])
        print("SALARY:", data[i]["salary"], "({:.2f}) yetishmaydi".format(1000-salary))
        print()
"""
#-------------------------------------------5-masala--------------------------------------
"""
for i in range(len(data)):
    salary = float(data[i]["salary"][1:])
    if salary < 1000:
        print("NAME:",data[i]["full_name"])
        print("SALARY: {:,.2f} ( {} eski maosh)".format(salary+1000, data[i]["salary"]))
        print()
"""
#-------------------------------------------6-masala--------------------------------------
"""
matn = "A personal computer (PC) is a multi-purpose microcomputer whose size, capabilities, and price make it feasible for individual use.[1] Personal computers are intended to be operated directly by an end user, rather than by a computer expert or technician. Unlike large, costly minicomputers and mainframes, time-sharing by many people at the same time is not used with personal computers. Primarily in the late 1970s and 1980s, the term home computer was also used."
index = matn.rfind("computer")
print(index)
"""