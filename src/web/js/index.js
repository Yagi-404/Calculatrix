// get the btn

const btn = document.getElementById('submit');

/* the actual calculator...
I'will (or if you want to) improve the "return result" system
Beacause 'alert' is a very ugly way to do it xD
*/


const historicDiv = document.querySelector('.historic');

btn.onclick = function() {
    const inputOpValueRaw = document.getElementById('input-op').value;
    let parsedValue = eval(inputOpValueRaw);
    // alert(parsedValue);
    if (inputOpValueRaw == false) { // more readable than !inputOpValueRaw
        alert("Please enter a value before submit");
    } else {
        historicDiv.innerHTML += "<br>" + inputOpValueRaw + "<br>" + "---------------------" + "<br>" + parsedValue + "<br>";
    }
};