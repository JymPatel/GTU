read -p "enter number to get it's multiplication table: " number
read -p "enter number of rows to print: " rows

for ((i = 1; i <= rows; i++))
do
    echo "${number} x ${i} = $((i * number))"
done