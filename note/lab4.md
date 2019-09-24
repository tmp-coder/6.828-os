there is a bug about SYSCALL, set this as a interrupt rather than a trap,becouse JOS disabled all interrupts when enter kernel from user mode.


# ex13

bug : if use sys_page_map in ipc, i dont know why!!