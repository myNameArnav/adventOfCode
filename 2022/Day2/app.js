// IT DONT WORK

// A, X ->   Rock      -> 1 point
// B, Y ->   Paper     -> 2 points
// C, Z ->   Scissors  -> 3 points

// Scissors -> Paper -> Rock -> Scissors
//    3          2        1        3

// won   -> 6
// draw  -> 3
// lost  -> 0

// 1 1 -> Draw
// 2 2 -> Draw
// 3 3 -> Draw
// 1 3 -> Win
// 2 1 -> Win
// 3 2 -> Win
// 1 2 -> Loss
// 2 3 -> Loss
// 3 1 -> Loss

// A Z 
// A Z
// C Y
// A X
// A X

let masterJSON = {
    "Rock": {
        "id": 1,
        "points": 1,
        "weakness": "Paper",
        "weaknessID": 2,
        "strength": "Scissors",
        "strengthID": 3
    },
    "Paper": {
        "id": 2,
        "points": 2,
        "weakness": "Scissors",
        "weaknessID": 3,
        "strength": "Rock",
        "strengthID": 1
    },
    "Scissors": {
        "id": 3,
        "points": 3,
        "weakness": "Rock",
        "weaknessID": 1,
        "strength": "Paper",
        "strengthID": 2
    }
}

const fs = require("fs");

// fs.readFile("input.txt", (err, data) =>{
//     if (err) throw err;

//     console.log(data.toString());
// });

data = "A Z"

let youChoose = data.substring(0,1)
let oppChoose = data.substring(2,3)
let points = 0

// Points based on what you choose
if (youChoose == "A")
    points += 1
else if (youChoose == "B")
    points += 2
else if (youChoose == "C")
    points += 3

// Points based on if you win loose or draw

LWD(youChoose, oppChoose)

console.log(youChoose, oppChoose, points);

function LWD(youChoose, oppChoose){

}