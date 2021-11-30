function togglePasswordVisibility(elementId)
{
    const x = document.getElementById(elementId);
    if(x.type === "password"){
        x.type ="text";
    }
    else{
        x.type = "password";
    }
}