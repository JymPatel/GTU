ssasit@ssasit-Veriton-Series:~$ pwd
/home/ssasit
ssasit@ssasit-Veriton-Series:~$ cd 210*/OS
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ clear
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ pwd
/home/ssasit/210760107022/OS
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ who
ssasit   tty7         2023-03-15 10:15 (:0)
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ who --help
Usage: who [OPTION]... [ FILE | ARG1 ARG2 ]
Print information about users who are currently logged in.

  -a, --all         same as -b -d --login -p -r -t -T -u
  -b, --boot        time of last system boot
  -d, --dead        print dead processes
  -H, --heading     print line of column headings
      --ips         print ips instead of hostnames. with --lookup,
                    canonicalizes based on stored IP, if available,
                    rather than stored hostname
  -l, --login       print system login processes
      --lookup      attempt to canonicalize hostnames via DNS
  -m                only hostname and user associated with stdin
  -p, --process     print active processes spawned by init
  -q, --count       all login names and number of users logged on
  -r, --runlevel    print current runlevel
  -s, --short       print only name, line, and time (default)
  -t, --time        print last system clock change
  -T, -w, --mesg    add user's message status as +, - or ?
  -u, --users       list users logged in
      --message     same as -T
      --writable    same as -T
      --help     display this help and exit
      --version  output version information and exit

If FILE is not specified, use /var/run/utmp.  /var/log/wtmp as FILE is common.
If ARG1 ARG2 given, -m presumed: 'am i' or 'mom likes' are usual.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/who>
or available locally via: info '(coreutils) who invocation'
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ who -l
LOGIN    tty1         2023-03-15 10:15              1329 id=tty1
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ who -b
         system boot  2011-01-01 17:31
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ who -H
NAME     LINE         TIME             COMMENT
ssasit   tty7         2023-03-15 10:15 (:0)
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ who -q
ssasit
# users=1
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ who -a
           system boot  2011-01-01 17:31
           run-level 5  2023-03-15 10:15
LOGIN      tty1         2023-03-15 10:15              1329 id=tty1
ssasit   + tty7         2023-03-15 10:15  old         1464 (:0)
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ whoami
ssasit
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ whoami -h
whoami: invalid option -- 'h'
Try 'whoami --help' for more information.
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ whoami --help
Usage: whoami [OPTION]...
Print the user name associated with the current effective user ID.
Same as id -un.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/whoami>
or available locally via: info '(coreutils) whoami invocation'
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ whoami --version
whoami (GNU coreutils) 8.25
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Richard Mlynarik.
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ uname'
> ^C
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ uname
Linux
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ uname -s
Linux
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ uname -n
ssasit-Veriton-Series
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ uname -v
#50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ uname -m
x86_64
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ uname -o
GNU/Linux
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ passwd
Changing password for ssasit.
(current) UNIX password: 
Enter new UNIX password: 
Retype new UNIX password: 
Password unchanged
Enter new UNIX password: 
Retype new UNIX password: 
You must choose a longer password
Enter new UNIX password: 
Retype new UNIX password: 
Bad: new and old password are too similar
passwd: Authentication token manipulation error
passwd: password unchanged
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ ls
hello(2).txt  hello(3).txt  hello.txt  screenshots  untitled.doc
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ mkdir assignments
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ mkdir -p assignments/some/screenshots/today
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ ls assignments/some/screenshots/today
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cd  assignments/some/screenshots/today
ssasit@ssasit-Veriton-Series:~/210760107022/OS/assignments/some/screenshots/today$ cd ../../../../
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ ls
assignments  hello(2).txt  hello(3).txt  hello.txt  screenshots  untitled.doc
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ mkdir -m folder
mkdir: missing operand
Try 'mkdir --help' for more information.
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ mkdir folder
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ ls
assignments  folder  hello(2).txt  hello(3).txt  hello.txt  screenshots  untitled.doc
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ rmdir folder
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ rmdir assignments
rmdir: failed to remove 'assignments': Directory not empty
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ rmdir -p assignments
rmdir: failed to remove 'assignments': Directory not empty
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ rmdir -p assignments/some/screenshots/today
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ ls
hello(2).txt  hello(3).txt  hello.txt  screenshots  untitled.doc



ssasit@ssasit-Veriton-Series:~$ cd 2107*/OS
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ ls
commands.sh  hello(2).txt  hello(3).txt  hello.txt  screenshots  untitled.doc
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ wc -l hello.txt
1 hello.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ wc hello.txt
 1  2 14 hello.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ wc ../readme.md
 10  87 626 ../readme.md
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ wc -L ../readme.md
364 ../readme.md
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ wc -c ../readme.md
626 ../readme.md
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ wc -w ../readme.md
87 ../readme.md
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ wc -l ../readme.md
10 ../readme.md
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ link hello.txt null.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ ls
commands.sh   hello(3).txt  null.txt     untitled.doc
hello(2).txt  hello.txt     screenshots
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cat null.txt
hello, world!
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ echo "good morning!" >> hello.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cat null.txthello, world!
good morning!
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ rm hello.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cat null.txt
hello, world!
good morning!
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cat hello.txt
cat: hello.txt: No such file or directory
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cat > hello.txt
hello, world!
^C
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cat null.txt
hello, world!
good morning!
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ echo "good evening!" >> hello.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ cat null.txthello, world!
good morning!
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ 

