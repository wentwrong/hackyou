// temporary pure PoC 

var cliWindow = document.getElementById("console")
var cliForm = document.getElementById("command")
var cliInput = document.getElementById("cli_input")

function addCliOutput() {
    var newPreElement = document.createElement("pre"); 
    var outputLine = "$ " + document.getElementById("cli_input").value + "\nnot implemented yet...";
    var preText = document.createTextNode(outputLine); 
    newPreElement.appendChild(preText)
    document.getElementById("output").appendChild(newPreElement);
}

cliForm.onsubmit = function(e) {

    addCliOutput();
    
    cliInput.value = "";

    // autoscroll to bottom
    cliWindow.scrollTop = cliWindow.scrollHeight;

    e.preventDefault();
}