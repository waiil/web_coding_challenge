function dislike(id){
}

function like(id){
    url = $("#"+id+".like").attr("url")
    $.get(url+"?id="+id, function(response){
        $("#"+id+".like").parent().parent().parent().remove()
    })
}