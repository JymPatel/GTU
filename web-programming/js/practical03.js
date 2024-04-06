document.getElementById("only-form").addEventListener("submit", (event) => {
    event.preventDefault()

    var  dateElement = document.getElementById("birthdate");

    var birthdate = new Date(dateElement.value);
    var today = new Date();

    birthdate.setHours(0, 0, 0, 0);
    today.setHours(0, 0, 0, 0);

    var nextBirthday = birthdate;
    nextBirthday.setFullYear(today.getFullYear())

    if (nextBirthday.getTime() < today.getTime()) {
        nextBirthday.setFullYear(nextBirthday.getFullYear() + 1);
    }

    var oneDay = 1000 * 60 * 60 * 24;
    var daysUntilBirthday = Math.ceil((birthdate.getTime() - today.getTime()) / oneDay);

    document.getElementById("result").innerText = `${daysUntilBirthday} Days to your next birthday.`

})
