import csv
import os
# read striver sheet and isolate the names of programs

loc = "/home/aditya/go_workspace/src/github.com/aditya109/Grokking-The-Coding-Interview/02-striver-sheet"
if not os.path.isdir(loc):
    os.mkdir(loc)
with open('acp.csv') as csvfile:
    r = csv.reader(csvfile)
    rows = 0
    day = 0
    pno = 1
    day_path = loc
    for idx, row in enumerate(r):
        if idx != 0:
            if row[0] == "1":
                day += 1
                if day < 10:
                    day_path = os.path.join(loc, "day-0" + str(day))
                else:
                    day_path = os.path.join(loc, "day-" + str(day))
                pno = 1
                if not os.path.isdir(day_path):
                    os.mkdir(day_path)
                print("directory created at " + day_path)
            else:
                pno += 1
            words = row[1].lower().split(" ")
            filename = "0" + str(pno) + "-" + "-".join(words)
            dirpath = os.path.join(day_path, filename)
            os.mkdir(dirpath)
            with open(os.path.join(dirpath, "README.md"), 'w') as fp: pass
            rows += 1


# for row in df[['Problem Name', 'Q.No']]:
#     print(row)

# create similar directories

# create internal directories structures


