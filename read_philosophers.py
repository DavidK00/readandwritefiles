def main():
    #open file
    infile = open('philosophers.txt', 'r')
    #read the file
    #file_contents = infile.read()
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')
    line4 = infile.readline().rstrip('\n')

    #display file conents
    #print(file_contents)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
main()