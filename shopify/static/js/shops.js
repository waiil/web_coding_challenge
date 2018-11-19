function dislike(id){
    url = $("#"+id+".dislike").attr("url")
    $.get(url+"?id="+id, function(response){
        $("#"+id+".like").parents().eq(2).remove()
    })
}


function like(id){
    url = $("#"+id+".like").attr("url")
    $.get(url+"?id="+id, function(response){
        $("#"+id+".like").parents().eq(2).remove()
    })
}

function remove_f(id){
    url = $("#"+id+".dislike").attr("url")
    $.get(url+"?remove_f=1&id="+id, function(response){
        $("#"+id+".dislike").parents().eq(2).remove()
    })
}