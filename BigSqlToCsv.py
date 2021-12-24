import regex as re
import time

##thekey will sepfrom
key = "INSERT INTO `user_exam_question` VALUES ("
start = time.time()
##openSQLfile
with open("D:\\doroos_user_exam_question.sql", encoding = "utf-8")as file:
    ## openTarget file
    with open("D:\\final_v13.csv",  "a", encoding = "utf-8")as f: 
        ## BIGloop inSQL file lineby line
        for i in range(100000000000):
            try:
                line = next(file)
                ## if the line is query
                if key in line:
                    print("yes {}".format(i) )
                    
                    ## drop the key
                    line = line.replace(key, "")
                    
                    ##drop the lineend
                    line = line.replace(");", "")
                    
                    ## if franch words correct it
                    franc = list(set(re.findall("(\w+\\\\')", line)))
                    if franc :
                        for m in franc:
                            line = line.replace(m, m.replace("'", "*"))   
                    
                    ## split the lines
                    lines = line.split("),(")
                    for query_i in range(len(lines)):
                        
                        ##remove any "," between ''
                        pats = re.findall("\'(.*?)\'", lines[query_i])
                        if pats:
                            for M in pats:
                                lines[query_i] = lines[query_i].replace(M, M.replace(",", "_"))
                        
                        ## add the line to the newfile
                        f.write(lines[query_i]); f.write("\n")

            ## if no more lines stop
            except StopIteration:
                print("no more")
                break        

##print the time                  
end = time.time()
tim = (end - start)/60
print("the proccess finished after {}h: {}m".format(tim//60, tim%60))
   
   
###*************************************************************************##
###*************************************************************************##
###*************************************************************************##


line = head[-1]

line = line.split("),(")


import pandas as pd
import numpy as np

test = pd.read_csv("D:\\res_v12.csv")
test[test["grade_name"].isnull()].count()[0]
test.iloc[306113, :]
test.info()
test.describe()
test.head()

k = []
with open("D:\\test.text", "r", encoding = "utf-8") as te:
    for i in range(5612124):
        
        g = next(te)
        if (i == 5602123)or (i == 5602124) or (i == 5602125):
            print(i+1)
            k.append(g)




key = "INSERT INTO `user_exam_question` VALUES ("
with open("D:\\test.txt", "r", encoding = "utf-8") as te:
    line = te.read()
    data = line.split(key)[1]
    line = data.replace(");", "")
    
    

lines = line.split("),(")
for q in range(len(lines)):
    h = re.findall("\'(.*?)\'", lines[q])
    if h:
        for M in h:
            lines[q] = lines[q].replace(M, M.replace(",", "_"))
            
for i in range(len(lines)):
    if "que" in lines[i]:
        print(i)

fran = "1437,223,'اسئلة وتمارين',1,'ASSESSMENT',1,'INTERACTIVE',410402,26038,'Lis ce document puis choisis la bonne réponse: Moi, c\'est Emmanuelle, j\'ai 17 ans. Ma voisine s\'appelle Lorine, elle est née le 3/5/2004, elle est sociable, elle adore le basket et l\'anglais. Et ma copine de classe s\'appelle Laura, elle n\'aime pas lire, elle préfère la musique et le tennis comme moi. Laura déteste ……….',3,'Almentor',104,' مادة اللغة الفرنسية',1,'Secondary 1 Subjects'"

fff = fran.replace("\\\'", "\\*")
tes_fran = re.findall("(\w+\'\w+)", fran)

lines = re.findall("\((.*?)\)\,", line) 

test_again = lines[1345]
franc = list(set(re.findall("(\w+\\\\')", line)))

for i in tes_fran:
    i = i.replace("'", "*")
tes_fran[0].replace("'", "*")



