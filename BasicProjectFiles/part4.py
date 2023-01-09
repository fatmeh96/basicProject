def lines_Number(file_path):
    with open('result.txt','r') as res:
        count=0
        for line in res:
            count+=1
    print(f"The number of lines in result file is: {count}")
lines_Number('result.txt')
def longest_words(file_path):
    with open('result.txt','r') as res:
        str1=""
        count=0
        for line in res:
            count+=1
            for letter in line:
                if letter.isalpha() or letter == " " or letter == '\n':
                    str1+=letter
        str1 = str1.split()
        max_length = 0
        max_word = ""
        for i in range(len(str1)):
            if len(str1[i]) > max_length:
                max_length = len(str1[i])
                max_word = str1[i]
        l = []
        for i in str1:
            if len(i) == max_length:
                l.append(i)
    print(f"The list of longest words in the file are: {l}")

    #printing each word in the list as the lines number
    decrypt_lines=encrypt_lines=1
    count-=(decrypt_lines+encrypt_lines)
    lines=int(count/2)
    for i in l:
        print((i+" ")*lines)

longest_words('result.txt')

#printing a pattern:
ll=[2,1,2]
flag=True
k=True
while(flag==True):
    for i in ll:
        if i==2 and k==True:
            print("*     *")
            print("*     *")
            print(" *   *")
            continue
        if i==1:
            print("   *")
            k = False
            continue
        if i==2 and k==False:
            print(" *   *")
            print("*     *")
            print("*     *")
            flag=False






