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
    var guess = document.getElementById(answer).getAttribute('innerHTML');
    if (guess == aircraftTrue) {
        document.getElementById(answer).style.backgroundColor = "green";
        correct_guesses++;
        document.getElementById("score").innerHTML = correct_guesses + "/" + image_index;
        $("#next_plane").fadeIn();
    } else {
        document.getElementById(answer).style.backgroundColor = 'red';
        document.getElementById("score").innerHTML = correct_guesses + "/" + image_index;
        for (var i=0; i < document.getElementsByTagName('button').length; i++) {
            if (document.getElementsByTagName('button')[i].innerHTML == aircraftTrue) {
                document.getElementsByTagName('button')[i].style.backgroundColor = 'green';
                $("#next_plane").fadeIn();
            };
        };
    };
    for (var i=0; i < document.getElementsByClassName("answer_button").length; i++) {
            document.getElementsByClassName("answer_button")[i].disabled = true;
        };
}

function nextPlane() {
    image_index++;
    document.getElementById('image').src = "static/images/" + images[image_index];
    var aircraftTrue = images[image_index].split('_')[0];
    var planeTypes = [... new Set(images.filter(function(x) {
        if (x.split('_')[0] === aircraftTrue) {
            return false;
        } else {
            return true;
        }
    }).map(function(x, i, a) {
        return x.split('_')[0];
    }))];

    var aircraftFalse = shuffleArray(planeTypes).slice(0,3);
    var choices = shuffleArray(aircraftFalse.concat(aircraftTrue));
    var answer1 = choices[0];
    var answer2 = choices[1];
    var answer3 = choices[2];
    var answer4 = choices[3];

    document.getElementById('answer-1').innerHTML = answer1;
    document.getElementById('answer-2').innerHTML = answer2;
    document.getElementById('answer-3').innerHTML = answer3;
    document.getElementById('answer-4').innerHTML = answer4;

    for (var i=0; i < document.getElementsByClassName("answer_button").length; i++) {
        document.getElementsByClassName("answer_button")[i].disabled = false;
        document.getElementsByClassName("answer_button")[i].style.backgroundColor = "";
    };

    document.getElementById("score").innerHTML = correct_guesses + "/" + image_index;
}