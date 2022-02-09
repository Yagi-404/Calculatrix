// get the btn

const btn = document.getElementById('submit');

/* the actual calculator...
I'will (or if you want to) improve the "return result" system
Beacause 'alert' is a very ugly way to do it xD
*/

btn.onclick = function(notTooMuchCaheForChrome) {
    const inputOpValueRaw = document.getElementById('input-op').value;
    let parsedValue = eval(inputOpValueRaw);
    alert(parsedValue);
};