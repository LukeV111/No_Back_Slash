ultimate_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>',',','@','[',']','^','_','`','{','|','}','~','1','2','3','4','5','6','7','8','9','0']

list_number_1 = 0
list_number_2 = 0


def scanning_list(): #Iterates over last letter - good!
    for number in range(91):
        print (ultimate_list[list_number_1]+ultimate_list[list_number_2]+ultimate_list[number])


while list_number_1 < 91:
    for list_number_2 in range(91):
        scanning_list() #This changes the last number. - WORKS
        list_number_2 = list_number_2 + 1 #This changes the middle number - WORKS
    list_number_1 = list_number_1 + 1 #This changes the first number - works!


#Something is tripping out with the ranges!

#creation()

#list_number_1 = list_number_1 + 1

#It's not restarting either "number" or 

#You need it to reach add and then stop, not go out of range.
