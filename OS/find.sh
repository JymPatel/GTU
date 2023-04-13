# FILE
ssasit@ssasit-Veriton-Series:~/210760107022/OS$ find *.txt
hello(2).txt
hello(3).txt
hello.txt
null.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -newer ../hello.txt
.
./table-sort.txt
./sort.txt
./numeric-sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ file -user ssasit
file: invalid option -- 'u'
Usage: file [-bcEhikLlNnprsvzZ0] [--apple] [--extension] [--mime-encoding] [--mime-type]
            [-e testname] [-F separator] [-f namefile] [-m magicfiles] file ...
       file -C [-m magicfiles]
       file [--help]
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ file --user ssasit
file: unrecognized option '--user'
Usage: file [-bcEhikLlNnprsvzZ0] [--apple] [--extension] [--mime-encoding] [--mime-type]
            [-e testname] [-F separator] [-f namefile] [-m magicfiles] file ...
       file -C [-m magicfiles]
       file [--help]
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find --user ssasit
find: unknown predicate `--user'
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -user ssasit
.
./table-sort.txt
./sort.txt
./numeric-sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size +6
.
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size +7
.
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size +8
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size +5
.
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size -5
./table-sort.txt
./sort.txt
./numeric-sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size -4
./table-sort.txt
./sort.txt
./numeric-sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size -7
./table-sort.txt
./sort.txt
./numeric-sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -size -2
./table-sort.txt
./sort.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -empty
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ touch empty.txt
ssasit@ssasit-Veriton-Series:~/210760107022/OS/lab$ find -empty
./empty.txt