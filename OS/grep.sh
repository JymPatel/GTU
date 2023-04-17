ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -c duplicates.txt
^C
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep gg duplicates.txt
egg
egg
Egg
egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -c gg duplicates.txt
4
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep gg *.txt
duplicates.txt:egg
duplicates.txt:egg
duplicates.txt:Egg
duplicates.txt:egg
sort.txt:egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -c gg *.txt
duplicates.txt:4
empty.txt:0
numeric-sort.txt:0
sort.txt:1
table-sort.txt:0
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -h gg *.txt
egg
egg
Egg
egg
egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -l gg *.txt
duplicates.txt
sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -l Egg *.txt
duplicates.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -li Egg *.txt
duplicates.txt
sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -i Egg *.txt
duplicates.txt:egg
duplicates.txt:egg
duplicates.txt:Egg
duplicates.txt:egg
sort.txt:egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -n Egg *.txt
duplicates.txt:9:Egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -v Egg duplicates.txt
hello
world
world

dog
cat
egg
egg
dino
1
99
45
3456
234
214
214
214
214
32
342


1
45

214
214
1
6
234


dog
cat

egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -c gg duplicates.txt
4
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -cw gg duplicates.txt
0
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -w gg duplicates.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -o gg duplicates.txt
gg
gg
gg
gg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -io gg duplicates.txt
gg
gg
gg
gg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -io eg duplicates.txt
eg
eg
Eg
eg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -o eg duplicates.txt
eg
eg
eg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -ic Egg duplicates.txt
4
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -ic Egg duplicates.txt
4
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -io Egg *.txt
duplicates.txt:egg
duplicates.txt:egg
duplicates.txt:Egg
duplicates.txt:egg
sort.txt:egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ grep -ic Egg *.txt
duplicates.txt:4
empty.txt:0
numeric-sort.txt:0
sort.txt:1
table-sort.txt:0