  //posts tweet
  function getParameterByName(name,url) {
    if (!url){
        url = window.location.href;
    }
    name = name.replace(/[\[\]]/g,"\\$&");
    var regex = new RegExp("[?&]") + name + "(=([^&#]*)|&|#|$)",
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g,""));
}
$(document).ready(function(){
    console.log("working");

    var query = getParameterByName('q')
    var tweetlist = [];


    function parseTweets(){
        if (tweetlist==0){
            $(".user-info").text("No projects found you serched.");
            $(".post-text").text("No ideations produced yet!");

        } else{
            // tweet exist, parse&display them
         $.each(tweetlist,function(key,value){
                
            var tweetkey = key;
            var tweetcontent = value.content;
            var tweetUser = value.user;
            $(".user-info").append( tweetUser );
            $(".post-text").append(tweetcontent);
            
         })
        }
        
    }
    $.ajax({
        url:"/api/tweet",
        data:{
            "q": query
        },
        method:"GET",
        success: function(data){
            //console.log(data)
            tweetlist = data
            parseTweets()
         
        },
        error: function(data){
            console.log("error")
            console.log(data)
        }
    })


});