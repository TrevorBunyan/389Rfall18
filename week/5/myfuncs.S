section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov r8, rdi   ;moves the string pointer to r8
        mov rcx, rdx  ;sets counter to string length

  setValue: 
        mov byte [r8], sil    ;sets the char being pointed to equal to val
        inc r8        ;moves the pointer by one
        loop setValue ;loops until string length is reached


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov r8, rdi  ;moves *dst parameter to r8
        mov r9, rsi  ;moves *src parameter to r9
        mov rcx, rdx ;moves string lengths parameter to counter

  copy:
        mov r10b, byte [r9] ;copies over one character from the string
        mov byte [r8], r10b ;inserts the char
        inc r8        ;increments dst pointer
        inc r9        ;increments src pointer
        loop copy     ;loops until all chars have been copied

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
