function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

function getAnswer(answer) {
    let guess = document.getElementById(answer).getAttribute('value');
    if (guess == aircraftTrue) {
        document.getElementById(answer).style.backgroundColor = "green";
        correct_guesses++;
        document.getElementById('next_plane').classList.toggle("show");
        document.getElementById("next_plane").disabled = false;
    } else {
        document.getElementById(answer).style.backgroundColor = 'red';
        for (var i=0; i < document.getElementsByTagName('button').length; i++) {
            if (document.getElementsByTagName('button')[i].value == aircraftTrue) {
                document.getElementsByTagName('button')[i].style.backgroundColor = 'green';
                document.getElementById('next_plane').classList.toggle("show"); 
                document.getElementById("next_plane").disabled = false;
            };
        };
    };
    for (var i=0; i < document.getElementsByClassName("answer_button").length; i++) {
            document.getElementsByClassName("answer_button")[i].disabled = true;
        };
}