# SORT
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ cat sort.txt
hello
world

dog
cat
egg
dinossasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -c sort.txt
sort: sort.txt:3: disorder: 
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort sort.txt

cat
dino
dog
egg
hello
world
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ cat sort.txt
hello
world

dog
cat
egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -r sort.txt
world
hello
egg
dog
dino
cat
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -n numeric-sort.txt
1
32
45
99
214
234
342
3456
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort numeric-sort.txt
1
214
234
32
342
3456
45
99
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -nr numeric-sort.txt
3456
342
234
214
99
45
32
1
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -k 2n table-sort.txt
18 dev
1 parth
23 krushil
25 pratham
70 jay
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -k 2 table-sort.txt
18 dev
70 jay
23 krushil
1 parth
25 pratham
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -k 1 table-sort.txt
18 dev
1 parth
23 krushil
25 pratham
70 jay
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ sort -k 1n table-sort.txt
1 parth
18 dev
23 krushil
25 pratham
70 jay