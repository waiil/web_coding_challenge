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

function remove_f(id){
    url = $("#"+id+".dislike").attr("url")
    $.get(url+"?remove_f=1&id="+id, function(response){
        $("#"+id+".dislike").parent().parent().parent().remove()
    })
}