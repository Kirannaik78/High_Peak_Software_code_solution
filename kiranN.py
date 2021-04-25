
n = 0
dic = {}
diff = 10**20
goodies = []
lis=[]
input_file = open("input.txt","r")
for line in input_file.readlines():
    if ":" in line:
        key, value = line.split(":")
        if value != '\n':
            dic[key] = int(value)
            lis.append(int(value))
n = dic['Number of employees']
del dic['Number of employees']
    
sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1]))
    
for i in range(len(sorted_dic) - n):
    if sorted_dic[list(sorted_dic)[i + n - 1]] - sorted_dic[list(sorted_dic)[i]] < diff:
        #print(list(sorted_dic)[i + n - 1], list(sorted_dic)[i])
        diff = sorted_dic[list(sorted_dic)[i + n - 1]] - sorted_dic[list(sorted_dic)[i]]
        goodies = []
        for j in range(i, i + n):
            line = list(sorted_dic)[j]
            line += ": "
            line += str(sorted_dic[list(sorted_dic)[j]])
            goodies.append(line)
           #print(goodies)
    
    #print(diff)
    #print(goodies)
    
output_file = open("output.txt", "w")
output_file.write("The goodies selected for distribution are: \n\n")
for line in goodies:
    output_file.write(line + "\n")
output_file.write("\nAnd the difference between the chosen goodie with highest " +
                      "price and the lowest price is " + str(diff))
                
input_file.close()
output_file.close()

