# ex9

```asm
f010002f <relocated>:
relocated:

	# Clear the frame pointer register (EBP)
	# so that once we get into debugging C code,
	# stack backtraces will be terminated properly.
	movl	$0x0,%ebp			# nuke frame pointer
f010002f:	bd 00 00 00 00       	mov    $0x0,%ebp

	# Set the stack pointer
	movl	$(bootstacktop),%esp
f0100034:	bc 00 00 11 f0       	mov    $0xf0110000,%esp

	# now to C code
	call	i386_init
f0100039:	e8 68 00 00 00       	call   f01000a6 <i386_init>
```

# ex10

```asm
//kernel.asm line 75 -81
void
test_backtrace(int x)
{
f0100040:	55                   	push   %ebp // para 1
f0100041:	89 e5                	mov    %esp,%ebp
f0100043:	56                   	push   %esi // para 2
f0100044:	53                   	push   %ebx // para 3
```

4 : `x`,`ebp`,`esi`,`ebx`

# ex11

**stack**

```
+------------+   |
               | arg 2      |   \
               +------------+    >- previous function's stack frame
               | arg 1      |   /
               +------------+   |
               | ret %eip   |   /
               +============+   
               | saved %ebp |   \
        %ebp-> +------------+   |
               |            |   |
               |   local    |   \
               | variables, |    >- current function's stack frame
               |    etc.    |   /
               |            |   |
               |            |   |
        %esp-> +------------+   /
```

```c
int
mon_backtrace(int argc, char **argv, struct Trapframe *tf)
{
    // Your code here.ex11
    uint32_t * ebp = (uint32_t *)read_ebp();
    while(ebp !=0){
        cprintf("ebp %08x",ebp);
        uint32_t eip = ebp[1];
        cprintf("  eip %08x  args",eip);
        uint32_t *args = ebp+2;
        for(int i = 0 ; i<5 ; ++i)
            cprintf("  %08x",args[i]);
        cputchar('\n');
        ebp = (uint32_t *) ebp[0];
    }
    return 0;
}
```

# ex12 

boot loader boot kernel' s stab

see

```asm
=> 0x10000c:    movw   $0x1234,0x472

Breakpoint 1, 0x0010000c in ?? ()
(gdb) x /10s 0x105e3d
0x105e3d:       ""
0x105e3e:       "{standard input}"
0x105e4f:       "kern/entry.S"
0x105e5c:       "kern/entrypgdir.c"
0x105e6e:       "gcc2_compiled."
0x105e7d:       "int:t(0,1)=r(0,1);-2147483648;2147483647;"
0x105ea7:       "char:t(0,2)=r(0,2);0;127;"
0x105ec1:       "long int:t(0,3)=r(0,3);-2147483648;2147483647;"
0x105ef0:       "unsigned int:t(0,4)=r(0,4);0;4294967295;"
0x105f19:       "long unsigned int:t(0,5)=r(0,5);0;4294967295;"
```

**code : debuginfo**

```c
	// Your code here.

	stab_binsearch(stabs,&lline,&rline,N_SLINE,addr);
	if(lline <= rline)
		info->eip_line = stabs[lline].n_desc;
	else return -1;

```

**code : mon_backtrace**

```c
int
mon_backtrace(int argc, char **argv, struct Trapframe *tf)
{
    // Your code here.ex11
    uint32_t * ebp = (uint32_t *)read_ebp();
    while(ebp !=0){
        cprintf("ebp %08x",ebp);
        uint32_t eip = ebp[1];
        cprintf("  eip %08x  args",eip);
        uint32_t *args = ebp+2;
        for(int i = 0 ; i<5 ; ++i)
            cprintf("  %08x",args[i]);
        cputchar('\n');
        // for ex12
        struct Eipdebuginfo info;
        debuginfo_eip(eip,&info);
        cprintf("%s:%d: %.*s+%d\n",info.eip_file,info.eip_line,info.eip_fn_namelen,info.eip_fn_name,eip - info.eip_fn_addr);
        ebp = (uint32_t *) ebp[0];
    }
    return 0;
}
```