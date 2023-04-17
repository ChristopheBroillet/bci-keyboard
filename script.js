const buttons = document.querySelectorAll('.btn');
const textarea = document.querySelector('textarea');

const delete_btn = document.querySelector('.delete');
const clear_btn = document.querySelector('.clear');
const space_btn = document.querySelector('.space');

let chars = [];

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        textarea.value += btn.innerText;
        chars = textarea.value.split('');
    })
})

delete_btn.addEventListener('click', () => {
    chars.pop();
    textarea.value = chars.join('');
})

space_btn.addEventListener('click', () => {
    chars.push(' ');
    textarea.value = chars.join('');
})

clear_btn.addEventListener('click', () => {
    chars = [];
    textarea.value = chars.join('');
})
