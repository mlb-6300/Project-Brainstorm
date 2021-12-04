function load(){
    var uuid = document.getElementById('uuid').value;
    $.post('/load', {id : uuid});
}