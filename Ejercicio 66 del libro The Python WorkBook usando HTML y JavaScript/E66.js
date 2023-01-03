var grades =
{
    "A+": 4,
    "A": 4,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0
};

var grader = document.getElementById("grade");
document.addEventListener("keydown", write);

var resultado = document.getElementById("resultado")
var resultadof = document.getElementById("resultadof")
var x = 0;
var counter = 0;
function write(evento)
{   
    var grade = grader.value;
    
    if (evento.keyCode == 13)
    {   
        for (g in grades)
        {
            if (grade == g)
            {
                x=x+grades[g]    
            }
        }
        counter=counter+1
        resultado.innerHTML+="The grade entered is: "+grade+"<br/>"
        if (grade == 0)
        {
            resultadof.innerHTML="The average of grades entered is "+parseFloat(x/(counter-1))
        }      
    }
}

