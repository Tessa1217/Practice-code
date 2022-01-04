infile = open("sales.txt", "r+")
line = infile.readline().strip()
sum = 0
count = 0
while line != "":
    print(line)
    s = int(line)
    sum += s
    count += 1
    line = infile.readline().strip()

infile.write("\n" + "총매출: " + str(sum) + "원" + "\n")
infile.write("평균 일매출: " + str(sum/count) + "원")

infile.close()

