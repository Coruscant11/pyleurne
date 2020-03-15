let username = document.getElementById('userNameID').innerHTML;
let roomID = window.location.href.substring(window.location.href.lastIndexOf('/') + 1 );

let userNumber;
let playlist = [];

let socket = io();
let ytbPlayer;

clearUsersList();
loadYoutubeAPI();

function loadYoutubeAPI() {
    let tag = document.createElement('script');

    tag.src = "https://www.youtube.com/iframe_api";
    let firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
}

function onYouTubeIframeAPIReady() {
    ytbPlayer = new YT.Player('player', {
        height: '100%',
        width: '100%',
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    emit('playerready', username)
}

var done = false;
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
    setTimeout(stopVideo, 6000);
        done = true;
    }
}

function stopVideo() {
    player.stopVideo();
}

function playVideo() {
    player.loadVideoById(playlist[0]);
}

/* Nettoie la div liste des utilisateurs connectés a la room */
function clearUsersList() {
    console.log("CLEAR_FUNC\n");
    let users = document.getElementsByClassName('user');
    userNumber = 0; 

    while(users[0]) {
        users[0].parentNode.removeChild(users[0]);
    }
}

/* Ajoute dynamiquement une div contenant un user à la liste */
function addUserOnUsersList(username, imgPath) {
    console.log("ADD_FUNC\n");
    /* Incrémentation et check nombre de users */

    userNumber += 1;
    isManyPeopleConnected();

    /* Création des éléments */
    let userList = document.getElementById('innerUserList');
    let div = document.createElement("div");
    let img = document.createElement("img");
    let p = document.createElement("p");
    

    /* On attribue leurs paramètres */
    div.className = "user";

    img.src = imgPath;
    img.className = 'userPic';

    p.id="userNameID";
    p.className = "userName";
    p.innerHTML = username;

    /* On ajoute a chaque parent leur enfants respectifs */
    div.appendChild(img);
    div.appendChild(p);
    userList.appendChild(div);

    console.log("APPENDED !");
}

/* Clear la playlist de la vidéo */
function clearVideoPlaylist() {
    console.log("CLEAR VIDEO");
    let users = document.getElementsByClassName('playlistVideo');

    while(users[0]) {
        users[0].parentNode.removeChild(users[0]);
    }

    playlist = [];
}


/* Ajoute une vidéo a la playlist */
function addVideoOnPlaylist(videoURL, videoID, user) {
    let playlistDiv = document.getElementById('innerPlaylist');
    let playlistVideoDiv = document.createElement('div');
    let imgThumbnail = document.createElement('img');

    let pVideoName = document.createElement('p');
    let spanVideoName = document.createElement('span')

    playlistVideoDiv.className = "playlistVideo";

    imgThumbnail.className = "videoThumbnail";
    imgThumbnail.src = `https://img.youtube.com/vi/${videoID}/0.jpg`;
    imgThumbnail.alt = 'Miniature';

    pVideoName.className = "videoInfos";
    spanVideoName.className = "videoName";
    spanVideoName.innerHTML = videoID;

    pVideoName.appendChild(spanVideoName);
    playlistVideoDiv.appendChild(imgThumbnail);
    playlistVideoDiv.appendChild(pVideoName);
    playlistDiv.appendChild(playlistVideoDiv);

    playlist.push(videoID)
}

/** ----------- BOUTONS ------------ **/
function onClickCreateRoomButton() {
    alert('create');
}

function onClickJoinRoomButton() {
    alert('join');
}

function onClickAddVideoButton() {
    let inputText = document.getElementById('addVideoText');
    let videoRequestUrl = inputText.value;
    socket.emit('videoAddRequest', {'username': username, 'room': roomID, 'videoURL': videoRequestUrl });

    inputText.value = ""

}
/** ------    FIN BOUTONS          ----------- */

/** ------      Connecté ça prends un s        ----------- */
function isManyPeopleConnected() {  
    if (userNumber > 1) {
        document.querySelector('#listTitle').innerHTML = 'Actuellement connectés:';
    }
}
/** ----------- PARTIE SOCKETS ------------ **/

/** Réponse random du serveur **/
socket.on('reponse', (message) => {
    console.log(message);
});

/** Message de confirmation de connexion à la room **/
socket.on('join', (message, username) => {
    console.log("MESSAGE SERVEUR -> " + message);
});

/** Demande de clear de la liste des utilisateurs par serveur **/
socket.on('clearuserlist', (message) => {
    console.log("SERVEUR : " + message);
    clearUsersList();
});

/** Demande de clear de la liste des utilisateurs par serveur **/
socket.on('clearplaylist', (message) => {
    console.log("SERVEUR : " + message);
    clearVideoPlaylist();
});

/** Ordre d'ajout d'utilisateur **/
socket.on('appendUser', (username, imgPath) => {
    addUserOnUsersList(username, imgPath);
});


socket.on('appendVideo', (videoUrl, videoID, callingUser) => {
    console.log(`\tVidéo reçue -> url[${videoUrl}], id[${videoID}], user[${callingUser}]`);
    addVideoOnPlaylist(videoUrl, videoID, callingUser);
});

socket.on('playvideo', (message) => {
    console.log("SERVER : " + message);
    playVideo();
});

socket.emit('join', { 'username': username, 'room': roomID }); // Connexion à la room

/** ------------------------------------- **/

/*
function updateUserList() {
    let url = window.location.href + "/population";


    $.getJSON(url).done((data) => {
        let parsedJSON = $.parseJSON(data);

        console.log(parsedJSON.values);
    })
}*/