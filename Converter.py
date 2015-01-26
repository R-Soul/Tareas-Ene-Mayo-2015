'''
Made by:

Luis Arzola - A01186956
'''

import re
conv = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"o",25:"p",26:"q",27:"r",28:"s",29:"t"}
inve = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26,"r":27,"s":28,"t":29}

#############################
#####DECIMAL TO NEW BASE#####
#############################

def tonew(num,nbase):
    tot = ""
    while int(num) >= int(nbase):
        tot += conv[int(int(num) % int(nbase))]
        num = int(num) // int(nbase)
    tot += str(num)
    return tot[::-1].upper()
    

#############################
#######BASE TO DECIMAL#######
#############################

def todec(num,base):
    num2 = str(num)[::-1]
    power = -1
    tot = 0
    for number in num2:
        power += 1
        tot += int(int(inve[number]) * (int(base)**power))
    return tot

#############################
####INPUT AND VALIDATIONS####
#############################
def convert():
    print("Welcome to the magical number converter. (Patent pending)\nTransform numbers from binary to hexadecimal, or to any base you wish.")

    while True:
        base = input("\nWhich is the base of the number to convert? (2-30) ")
        while True:
            if base.isnumeric() == False:
                base = input("Invalid input, please try again. ")
            elif  int(base) <= 1 or int(base) > 30:
                 base = input("Invalid input, please try again. ")
            else:
                break
                
        if int(base) > 10:
            inv = re.compile('[^0-9a-' + conv[int(base)-1] + ']')
        else:
            inv = re.compile('[^0-' + conv[int(base)-1] + ']')

        num = str(input("\nPlease input the number. (No decimal support) ")).lower()
        while True:
            val = re.findall(inv,num)
            if len(val) > 0:
                num = input("Invalid input, please try again. ")
            elif num == "":
                num = input("Invalid input, please try again. ")
            else:
                break
                   
        nbase = str(input("\nWhich is the new base you want? (2-30) "))
        while True:
            if nbase.isnumeric() == False:
                nbase = input("Invalid input, please try again. ")
            elif  int(nbase) <= 1 or int(nbase) > 30:
                 nbase = input("Invalid input, please try again. ")
            else:
                break
            
        ####USER VERIFICATION###
        fin = input('\nConvert "%s" from base %s to base %s? (Y/N) ' % (num.upper(),base,nbase)).lower()
        while fin not in ["y","n"]:
            fin = input("Invalid input, please try again. ")
        if fin == "y":
            break
    
#############################
######CHECK CASE TO USE######
#############################

    if int(base) == int(nbase):
        print("\nI suppose you know you asked me to do basically nothing.\nYour number stays on %s. \nRegardless, thank you for choosing the magical number converter." % (num))
    elif int(base) == 10:
        print("\nThe new number is %s.\nThank you for choosing the magical number converter." % (tonew(num,nbase)))
    elif int(nbase) == 10:
        print("\nThe new number is %s.\nThank you for choosing the magical number converter." % (todec(num,base)))
    else:
        print("\nThe new number is %s.\nThank you for choosing the magical number converter." % (tonew(todec(num,base),nbase)))

if __name__ == "__main__":
    convert()


