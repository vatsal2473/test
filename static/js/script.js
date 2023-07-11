$(document).ready(function() {
    $('#alert-button').click(function() {
        $.ajax({
            url: '/alert_message',
            type: 'POST',
            data: JSON.stringify({ 'message': 'Hello, Flask!' }),
            contentType: 'application/json',
            success: function(response) {
                alert(response.message);
            },
            error: function(xhr, status, error) {
                console.log('Error:', error);
            }
        });
    });
});
