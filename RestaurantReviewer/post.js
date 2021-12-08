function sendText()
{
    $.ajax
    (
        {
            type: "POST",
            url: "http://127.0.0.1:5000/json",
            dataType:"json",
            data: 
            {               
               parsedText,
            },
            success: function(backEndModelJSONOutput)
            {
               output = backEndModelJSONOutput.hyperPartisan;
               alert(output);
            },
            error: function() {
                alert('error sending parsed text');
            }     
        }
    );
}
sendText();