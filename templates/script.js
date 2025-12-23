const apiUrl = "/api";  // sets the base URL for API requests

function sendMove(direction) {  // defines a function to send movement commands
    fetch(apiUrl + '/move', {  // sends a POST request to /move url
        method: 'POST',  // sets HTTP method to POST
        headers: {'Content-Type': 'application/json'},  // tells the server the request body is JSON
        body: JSON.stringify({direction})  // sends the direction as JSON in the body
    });
}

function sendSound(url) {  // defines a function to send a sound URL
    fetch(apiUrl + '/play', {  // sends a POST request to /play
        method: 'POST',  // sets HTTP method to POST
        headers: {'Content-Type': 'application/json'},  // tells the server the request body is JSON
        body: JSON.stringify({url})  // sends the URL as JSON in the body
    });
}

function stopSound() {
    fetch(apiUrl + '/stop', { method: 'POST' });
}

document.getElementById('playSound').onclick = () => {  // binds the "playSound" button
    const url = document.getElementById('soundUrl').value;  // gets the value from the sound input field
    if(url) sendSound(url);  // if URL exists, send it to the backend
};

document.getElementById('stopSound').onclick = () => stopSound();  // binds the "stopSound" button to stop the audio

document.getElementById('up').addEventListener('mousedown', () => sendMove('stop'));
document.getElementById('up').addEventListener('mouseup', () => sendMove('stop'));

document.getElementById('down').addEventListener('mousedown', () => sendMove('down'));
document.getElementById('down').addEventListener('mouseup', () => sendMove('stop'));

document.getElementById('left').addEventListener('mousedown', () => sendMove('left'));
document.getElementById('left').addEventListener('mouseup', () => sendMove('stop'));

document.getElementById('right').addEventListener('mousedown', () => sendMove('right'));
document.getElementById('right').addEventListener('mouseup', () => sendMove('stop'));

const keys = {
    'arrowup': 'up', 'w': 'up',
    'arrowdown': 'down', 's': 'down',
    'arrowleft': 'left', 'a': 'left',
    'arrowright': 'right', 'd': 'right'
};

window.addEventListener('keydown', e => {
    const dir = keys[e.key.toLowerCase()];
    if (dir) sendMove(dir);
});

window.addEventListener('keyup', e => {
    const dir = keys[e.key.toLowerCase()];
    if (dir) sendMove('stop');
});

const buttons = [
    {id: 'up', direction: 'up'},
    {id: 'down', direction: 'down'},
    {id: 'left', direction: 'left'},
    {id: 'right', direction: 'right'}
];

buttons.forEach(btnInfo => {
    const btn = document.getElementById(btnInfo.id);
    // Start moving on press (mouse or touch)
    btn.onmousedown = btn.ontouchstart = () => sendMove(btnInfo.direction);
    // Stop moving on release (mouse or touch)
    btn.onmouseup = btn.ontouchend = () => sendMove('stop');
});