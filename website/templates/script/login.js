$(document).ready(function(){
    
    var imgs = [ "img/1.svg", "img/2.svg", "img/3.svg", "img/4.svg", "img/5.svg" ];
    var currIn = -1;

    ranImg();

    function ranImg() {
        let prev; do{ 
            prev = currIn;
            currIn = Math.floor((Math.random()*imgs.length));
        }while (prev == currIn);

        $("#commodity").attr("src", imgs[currIn]);
    }

    $("#login-form").submit(function(event) {
        event.preventDefault();

        var email = $("#email").val();
        var password = $("#password").val();

        if (email === "" || password === "") {
            $("#form-message").text("Please fill in all fields.");
            return;
        }
        // Login logic
    });
    
});