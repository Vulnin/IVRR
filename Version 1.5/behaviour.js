// interactive video prototype
// Author: Benjamin Fuchs
// University of Freiburg, Chair of Computer Architecture

 
 // this is just on cue changes 
 var videoElement = document.querySelector("video");
 var textTrack = videoElement.textTracks[0];
 
 // When cue value changes run your code
 textTrack.oncuechange = function(e) {
   var cue = this.activeCues[0];
   if(cue){
     //console.log(cue.text);
     setTimeout(function(){
       videoElement.pause();
       var answer = confirm("Möchten Sie nun zu der hier gestellten Frage weitergeleitet werden?");
       if (answer) {
         //if ("http" in cue.text) {
           window.open(cue.text);
         //} else {
           //window.open("https://" + cue.text);
         //}
       } else {
            videoElement.play();
       }
     },2500);
   }
 };

 