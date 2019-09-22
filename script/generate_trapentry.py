
err_code = {
    8,10,11,12,13,14,17
}


def generate(line,trapno):
    
    name = line.split("_")[1]
    num = line
    if trapno in err_code:
        print("TRAPHANDLER("+name+", "+num+")")
    else:
        print("TRAPHANDLER_NOEC("+name+", "+num+")")

import re
while True:

    words = str(input())
    # print(words)
    try:
        line = words.split(" ")[1]
        # print("wordrs = ",words)
        
        # print(line)
        if line[0] =='T' and line[1] =='_':

            m = re.search(r"[0-9]+",words)
            generate(line,int(m.group()))
            # print(num)
    except Exception :
        pass