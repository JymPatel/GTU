ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq sort.txt | head 4
head: cannot open '4' for reading: No such file or directory
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq sort.txt | head -4
hello
world

dog
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq sort.txt | tail -4 | head -2
dog
cat