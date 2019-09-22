
def generate(line):
    is_trap =0
    dpl =0
    if line =='T_SYSCALL':
        is_trap = 1
        dpl = 3
    ans = line.split("_")
    print("void "+ans[1]+"();")
    line2 = "SETGATE(idt["+line +"],"+str(is_trap)+",GD_KT,"+ans[1]+","+str(dpl)+");"
    print(line2)
    # print("SETGATE(idt["+line +"],"+str(is_trap)+",GD_KT,"+ans[1]+","+dpl+");")


while True:

    words = str(input())
    # print(words)
    try:
        line = words.split(" ")[1]
        # print(line)
        if line[0] =='T' and line[1] =='_':
            generate(line)
    except Exception :
        pass