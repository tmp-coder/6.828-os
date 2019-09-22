# bug

1. ```
   (gdb) x /10x $esp
    0xeebfe000:     Cannot access memory at address 0xeebfe000
    ```
    // often caused by unmapping va

2. breakpoint
   set dpl = 3