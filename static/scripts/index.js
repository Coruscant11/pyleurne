function onClickCreateRoomButton() {
    alert('create');
}

function onClickJoinRoomButton() {
    alert('join');
}

function onClickAddVideoButton() {
    console.log('onClickAddVideoButton...');
}

let socket = io();

socket.on('reponse', (message) => {
    console.log(message);
});

socket.on('join', (message) => {
    console.log("Un nouvel utilisateur a rejoint la room.")
})


socket.emit('join', { 'username': document.getElementById('userNameID').innerHTML,
                        'room': window.location.href.substring(window.location.href.lastIndexOf('/') + 1 )});


/*
function updateUserList() {
    let url = window.location.href + "/population";


    $.getJSON(url).done((data) => {
        let parsedJSON = $.parseJSON(data);

        console.log(parsedJSON.values);
    })
}*/
