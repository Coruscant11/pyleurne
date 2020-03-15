let username = document.getElementById('userNameID').innerHTML;
let roomID = window.location.href.substring(window.location.href.lastIndexOf('/') + 1 );
let socket = io();


/* Nettoie la div liste des utilisateurs connectés a la room */
function clearUsersList() {
    let userlist = document.getElementById('userlist');
    let users = document.getElementsByClassName('user');

    while(users[0]) {
        users[0].parentNode.removeChild(users[0]);
    }
}

/* Ajoute dynamiquement une div contenant un user à la liste */
function addUserOnUsersList(username, imgPath) {

    /* Création des éléments */
    let userList = document.getElementById('userlist');
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

/** ----------- BOUTONS ------------ **/
function onClickCreateRoomButton() {
    alert('create');
}

function onClickJoinRoomButton() {
    alert('join');
}

function onClickAddVideoButton() {
    let videoRequestUrl = document.getElementById('addVideoText').value;
    socket.emit('videoAddRequest', {'username': username, 'room': roomID, 'videoURL': videoRequestUrl })
}
/** ------    FIN BOUTONS          ----------- */



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
socket.on('clear', (message) => {
    console.log("SERVEUR : " + message);
    clearUsersList()
});

/** Ordre d'ajout d'utilisateur **/
socket.on('appendUser', (username, imgPath) => {
    addUserOnUsersList(username, imgPath);
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
