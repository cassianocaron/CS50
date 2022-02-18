// Wait until page is fully loaded
document.addEventListener('DOMContentLoaded', () => {

    // When correct answer is clicked, change color to green
    let correct = document.querySelector('.correct');
    correct.addEventListener('click', () => {
        correct.style.backgroundColor = '#00ff00';
        document.querySelector('#feedback1').innerHTML = 'Correct!';
    });

    // When any incorrect answer is clicked, change color to red
    let incorrect = document.querySelectorAll('.incorrect');
    incorrect.forEach(button => {
        button.addEventListener('click', () => {
            button.style.background = '#ff0000';
            document.querySelector('#feedback1').textContent = 'Incorrect';
        });
    });

    // Check free response submission
    document.querySelector('#check').addEventListener('click', () => {
        let input = document.querySelector('input');
        if (input.value === 'Koala' || input.value === 'koala') {
            input.style.backgroundColor = '#00ff00';
            document.querySelector('#feedback2').innerHTML = 'Correct!';
        } else {
            input.style.backgroundColor = '#ff0000';
            document.querySelector('#feedback2').innerHTML = 'Incorrect!';
        }
    });
});