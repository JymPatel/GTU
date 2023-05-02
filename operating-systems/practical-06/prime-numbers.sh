read -p "enter number to get prime numbers before it: " number

if (($number < 0))
then
    echo "can't get prime numbers of negative values."
    exit
fi

echo "prime numbers are:"
for i in $(seq 2 1 $number)
do
    is_prime=1
    for ((j = 2; j <= i/2; j++))
    do
        if ((i % j == 0))
        then
            is_prime=0
            break
        fi
    done
    if ((is_prime == 1))
    then
        echo $i
    fi
done