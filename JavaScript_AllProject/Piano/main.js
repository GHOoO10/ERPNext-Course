
const keys = document.querySelectorAll('.piano-key');
const sounds = {
    C: 'C.wav',
    'C#': 'note1.wav',
    D: 'note6.wav',
    'D#': 'note2.wav',
    E: 'note7.wav',
    F: 'note1.wav',
    'F#': 'note3.wav',
    G: 'note1.wav',
    'G#': 'note4.wav',
    A: 'note7.wav',
    'A#': 'note5.wav',
    B: 'note2.wav'
};


function playSound(note) {
    const audio = new Audio('sounds/' + sounds[note]);
    audio.play();
}


keys.forEach(key => {
    key.addEventListener('click', function() {
        const note = this.dataset.note;
        playSound(note);
    });
});
