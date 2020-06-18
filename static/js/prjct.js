

$(document).ready(function(){
    $("#exampleFormControlInput1").blur(function(){

    var x = $("#exampleFormControlInput1").val();

    if(x.length<1)
    {
        $("#emailHelp1").show();
        return false;
    }
    else{
        $("#emailHelp1").hide();
        return false;
    }

    });
});


$(document).ready(function(){
    $("#exampleFormControlTextarea1").blur(function(){

    var x = $("#exampleFormControlTextarea1").val();

    if(x.length<1)
    {
        $("#emailHelp2").show();
        return false;
    }
    else{
        $("#emailHelp2").hide();
        return false;
    }

    });
});




$(document).ready(function(){

    $("#sendfb").click(function(){

    $("#feedbackinst").submit(function(){

            var x = $("#exampleFormControlInput1").val();

            sometext = "Thank You " + x + ",For Your Feedback."

            alert(sometext);


        });

    });

});


$(document).ready(function(){

    $("#urlsrchbt").click(function(){

    $("#urlsrch").submit();

    });

});



$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
});