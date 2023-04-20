read -p "enter number to get fabonacci series upto that number: " number

number1=0
number2=1
for ((i = 0; i < number; i++))
do
    echo "${number2} "
    number2=$((number1 + number2))
    number1=$((number2 - number1))
done