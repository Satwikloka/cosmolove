  //posts tweet
  function getParameterByName(name,url) {
    if (!url){
        url = window.location.href;
    }
    name = name.replace(/[\[\]]/g,"\\$&");
    var regex = new RegExp("[?&]") + name + "(=([^&#]*)|&|#|$)",
        results = regex.match(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g,""));
}
$(document).ready(function(){
    

    var query = getParameterByName('q')
    var tweetlist = [];

    function attachTweet(value,prepend){
        var tweetcontent = value.content;
        var tweetuser = value.user;
        
        var tweetdate = value.timestamp;
        $(".user-info").append($( tweetuser) );
        $(".post-text").append($(tweetcontent));
        $(".span").append($(tweetdate));
        

    }


    function parseTweets(){
        if (tweetlist==0){
            $(".user-info").text("No projects found you serched.");
            $(".post-text").text("No ideations produced yet!");

        } else{
            // tweet exist, parse&display them
         $.each(tweetlist,function(key,value){
            var tweetkey = key;
            attachTweet(value)

            
                
            

            
         })
        }
        
    }
    function fetchTweets(){
        console.log("fetching...")
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

    }
    fetchTweets()
    

    $(".tweet-form").submit(function(event){
        event.preventDefault()
        var this_ = $(this)
        
        //console.log(event)
        //console.log()

        var formData = this_.serialize()
        $.ajax({
            url:"/api/tweet/create",
            data:formData,
            method:"POST",
            success: function(data){
                attachTweet(data)
                //console.log(data)
                //fetchTweets()
                //tweetlist = data
                //parseTweets()
             
            },
            error: function(data){
                console.log("error")
                console.log(data.statusText)
                console.log(data.status)
            }
        })

        
    })


});