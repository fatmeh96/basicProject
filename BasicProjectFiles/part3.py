res=open('result.txt','w')
def func1(file_path):
    with open('result.txt', 'w+') as s:
        s.write("The encrypt text is:\n")
        with open('file.txt', 'r') as f:
            for line in f:
                s.write(line)
        s.write("The decrypt text is:\n")
        with open('file2.txt', 'r') as f2:
            for line2 in f2:
                s.write(line2)
func1(res)