function startListening(){

const recognition = new webkitSpeechRecognition();

recognition.onresult = function(event){

let text = event.results[0][0].transcript;

document.getElementById("output").innerText = text;

fetch("/command",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({text:text})
})

.then(res=>res.json())
.then(data=>{
document.getElementById("output").innerText = data.response;
});

}

recognition.start();

}