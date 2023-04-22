// Get all buttons
const buttons = document.querySelectorAll('.btn');
const delete_btn = document.querySelector('.delete');
const clear_btn = document.querySelector('.clear');
const space_btn = document.querySelector('.space');

// Area where text will be written
const textarea = document.querySelector('textarea');

// Contains the text to write
let chars = [];

// Listener for each letter buttons on click
buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        var confirmation = confirm("You have entered letter " + btn.innerText + " is that correct?");
        if(confirmation){
            textarea.value += btn.innerText;
            chars = textarea.value.split('');
        }
    });
    // makeBlink(btn);
});

delete_btn.addEventListener('click', () => {
    var confirmation = confirm("You have entered DELETE is that correct?");
    if(confirmation){
        chars.pop();
        textarea.value = chars.join('');
    }
});
// makeBlink(delete_btn);

space_btn.addEventListener('click', () => {
    var confirmation = confirm("You have entered SPACE is that correct?");
    if(confirmation){
        chars.push(' ');
        textarea.value = chars.join('');
    }
});
// makeBlink(space_btn);

clear_btn.addEventListener('click', () => {
    var confirmation = confirm("You have entered CLEAR is that correct?");
    if(confirmation){
        chars = [];
        textarea.value = chars.join('');
    }
});
makeBlink(clear_btn);

// Make the button blink given the frequency in the HTML element
function makeBlink(element){
    setInterval(() => {
        element.style.visibility = (element.style.visibility == 'hidden' ? '' : 'hidden');
    }, element.getAttribute("freq"));
}

// To test the fetch on the Flask webserver
setInterval(() => {
    fetch("http://127.0.0.1:5555/GETdata")
        .then(function (response) {
            return response.json();
        }).then(function (response) {
            // console.log('GET response:');
            // console.log(response.greeting);
            textarea.value = response.textfield;
        });
}, 5000);
