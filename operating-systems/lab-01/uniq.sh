ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -u duplicates.txt
hello
world

dog
cat
egg
dino
1
99
45
3456
234
214
32
342
1
45

342
1
6
234
dog
cat

egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -d duplicates.txt


ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -u duplicates.txt
hello

dog
cat
dino
1
99
45
3456
234
32
342
1
45

1
6
234
dog
cat

egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -d duplicates.txt
world
egg
214

214

ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -D duplicates.txt
world
world
egg
egg
egg
214
214
214
214


214
214


ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -c duplicates.txt
      1 hello
      2 world
      1 
      1 dog
      1 cat
      3 egg
      1 dino
      1 1
      1 99
      1 45
      1 3456
      1 234
      4 214
      1 32
      1 342
      2 
      1 1
      1 45
      1 
      2 214
      1 1
      1 6
      1 234
      2 
      1 dog
      1 cat
      1 
      1 egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -c duplicates.txt
      1 hello
      2 world
      1 
      1 dog
      1 cat
      2 egg
      1 Egg
      1 dino
      1 1
      1 99
      1 45
      1 3456
      1 234
      4 214
      1 32
      1 342
      2 
      1 1
      1 45
      1 
      2 214
      1 1
      1 6
      1 234
      2 
      1 dog
      1 cat
      1 
      1 egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -i duplicates.txt
hello
world

dog
cat
egg
dino
1
99
45
3456
234
214
32
342

1
45

214
1
6
234

dog
cat

egg
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ uniq -ic duplicates.txt
      1 hello
      2 world
      1 
      1 dog
      1 cat
      3 egg
      1 dino
      1 1
      1 99
      1 45
      1 3456
      1 234
      4 214
      1 32
      1 342
      2 
      1 1
      1 45
      1 
      2 214
      1 1
      1 6
      1 234
      2 
      1 dog
      1 cat
      1 
      1 egg