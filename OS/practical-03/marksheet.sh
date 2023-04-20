RED="\e[31m"
BLUE_COLOR="\e[34m"
GREEN="\e[32m"
DEFAULT="\e[0m"

read -p "enter name: " name
read -p "enter enrollment no.: " enrollment_no 

read -p "marks of subject 1: " sub1
read -p "marks of subject 2: " sub2
read -p "marks of subject 3: " sub3

total=$(($sub1 + $sub2 + $sub3))
average=$(($total/3))

echo "result of" $BLUE_COLOR$name$DEFAULT "with enrollment number" $BLUE_COLOR$enrollment_no$DEFAULT
echo -e "you scored total of" $BLUE_COLOR$total$DEFAULT "and averaged" $BLUE_COLOR$average$DEFAULT



if (($sub1 > 100 || $sub2 > 100 || $sub3 > 100))
then
    echo -e "${RED}you entered wrong marks!${DEFAULT}"
fii 


if (($sub1 < 35 || $sub2 < 35 || $sub3 < 35))
then
    echo -e "best of work! for next time. ${RED}you failed!${DEFAULT}"
elif (($average == 100))
then
    echo -e "you passed with ${GREEN}distinction!${DEFAULT}"
elif (($average > 60))
then
    echo "you passed with first class!"
elif (($average > 35))
then
    echo "you passed with second class!"
fi


