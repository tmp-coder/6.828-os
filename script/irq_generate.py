def seg_gate(i):
    print("void irq{}();".format(i))
    print("SETGATE(idt[IRQ_OFFSET+{}], 0, GD_KT, irq{}, 3);".format(i,i))

for i in range(16):
    seg_gate(i)

for i in range(16):
    print("TRAPHANDLER_NOEC(irq{}, {})".format(i,32 + i))