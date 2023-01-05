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
        for line in res:
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
longest_words('result.txt')