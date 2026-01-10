const apiUrl = "/api";  // sets the base URL for API requests
const motorUrl = ":5001/api";  // sets the base URL for motor control requests

// Function to send POST request with movement direction
function sendMove(direction) {  
    fetch(motorUrl + 'move', { 
        method: 'POST',  
        headers: {'Content-Type': 'application/json'},  
        body: JSON.stringify({direction})  
    });
}

// Function to send POST request with sound URL to be played
function sendSound(url) {  
    fetch(apiUrl + '/play', {  
        method: 'POST',  
        headers: {'Content-Type': 'application/json'},  
        body: JSON.stringify({url})  
    });
}

// Function to send POST request with text to be spoken
async function sendText(text) {  
    const response = await fetch(apiUrl + "/speak", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    console.log("Robot tank says:", data.message);
}

// Function to send POST request to stop any playing sound
function stopSound() {
    fetch(apiUrl + '/stop', { method: 'POST' });
}

// When the play button is pressed, send the link to be played
document.getElementById('playSound').onclick = () => { 
    const url = document.getElementById('soundUrl').value;  
    if(url) {
        sendSound(url)
    };
};

// When the stop button is pressed, stop the sound
document.getElementById('stopSound').onclick = () => stopSound();

// When the send message button is pressed, send the text to AI
document.getElementById('sendMsg').onclick = () => {
    const text = document.getElementById('aiChat').value;
    if(text) {
        sendText(text);
    }
};

// Add touch support for movement buttons
const buttons = [
    {id: 'up', direction: 'up'},
    {id: 'down', direction: 'down'},
    {id: 'left', direction: 'left'},
    {id: 'right', direction: 'right'}
];

// Attach touch and mouse event listeners to each button
buttons.forEach(btnInfo => {
    const btn = document.getElementById(btnInfo.id);
    btn.onmousedown = btn.ontouchstart = () => sendMove(btnInfo.direction);
    btn.onmouseup = btn.ontouchend = () => sendMove('stop');
});

// Map keys to directions for keyboard control
const keys = {
    'arrowup': 'up',
    'arrowdown': 'down',
    'arrowleft': 'left',
    'arrowright': 'right'
};

// Handle keyboard events for movement
window.addEventListener('keydown', e => {
    const dir = keys[e.key.toLowerCase()];
    if (dir) sendMove(dir);
});

// Stop movement on key release
window.addEventListener('keyup', e => {
    const dir = keys[e.key.toLowerCase()];
    if (dir) sendMove('stop');
});