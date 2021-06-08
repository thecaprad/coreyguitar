// This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player1,
    player2,
    player3,
    player4,
    player5,
    player6,
    player7,
    player8,
    player9;

var playersArr = [player1, player2, player3, player4, player5, player6, player7, player8, player9];

// YouTube function — onYouTubeIframeAPIReady.
function onYouTubeIframeAPIReady() {
    playersArr.forEach(function(player, index) {
        playersArr[index] = new YT.Player(('player-' + index), {
            origin: 'https://www.coreyguitar.com',
            events: {
                'onReady': onPlayerReady
            }
        })
    });
}

function onPlayerReady() {
}

function pauseVideo(){
    playersArr[0].pauseVideo();
    playersArr[1].pauseVideo();
    playersArr[2].pauseVideo();
    playersArr[3].pauseVideo();
    playersArr[4].pauseVideo();
    playersArr[5].pauseVideo();
    playersArr[6].pauseVideo();
    playersArr[7].pauseVideo();
    playersArr[8].pauseVideo();
}
