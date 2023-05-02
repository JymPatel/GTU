while true
do
echo "MENU
1. Display calendar of current month
2. Display today’s date and time
3. Display usernames those are currently logged in the system
4. Display your terminal number
5. Exit"
read -p "select option: " i
case $i in
1) cal ;;
2) date ;;
3) who;;
4) tty ;;
5) exit ;;
*) echo “enter valid input” ;;
esac
done