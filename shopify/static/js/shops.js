function dislike(id){
    console.log("in dislike")
    url = $("#"+id+".dislike").attr("url")
    $.get(url+"?id="+id, function(response){
        $("#"+id+".like").parent().parent().parent().remove()
    })
}

function like(id){
    url = $("#"+id+".like").attr("url")
    $.get(url+"?id="+id, function(response){
        $("#"+id+".like").parent().parent().parent().remove()
    })
}