

window.addEventListener("load", function(){
    var checkbox  = document.getElementById('{{form.toggle_pw.id}}');
    var x = document.getElementById('{{form.password.id}}');
    checkbox.addEventListener('change', function() {
        if(this.checked) {
            x.type = 'text';
        } else {
            x.type = 'password';
        }
    });
});



