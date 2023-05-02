read -p "enter number to get factorial: " number

product=1

if (($number < 0))
then
    echo "can't get factorial of negative values."
    exit
fi

for i in $(seq 1 1 $number)
do
    product=$((product * i))
done

echo "${number}! = ${product}"