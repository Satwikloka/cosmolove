


  
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
    
    

    


        
        

        
                
        
    function parseTweets(){
        if (data.length == 0){

        }
    }    
    


    
    var count = 0;
    function fetchTweets(cnt){
        console.log("fetching...");
        $.ajax({
            url:"/api/tweet",
            data:{
                "q": query
            },
            method:"GET",
            success: function(data){
                
                
                if(data[cnt]){
                    var patch = '<div class="feeds-content"><div class="posts" id="tweet"><div class="post"><div class="user-avatar"><!--img src=--></div><div class="post-content"><div class="post-user-info"><h4 id="tweetuser" class="user-info">'+data[cnt]["user"]["username"]+'</h4><i class="fas fa-check-circle"></i><span class="span">@'+data[cnt]["user"]["last_name"]+'</span><h4 class="datetime">'+data[cnt]["timestamp"]+'ago</h4></div><p id="content" class="post-text">'+data[cnt]["content"]+'</p><div class="post-img"><!--img src= /--></div><div class="post-icons"><i class="far fa-comment"></i><i class="fas fa-retweet"></i><i class="far fa-heart"></i><i class="fas fa-share-alt"></i></div></div></div></div></div></div>';
                    document.getElementById("container").innerHTML = document.getElementById("container").innerHTML + patch;
                    document.getElementsByTagName("p").innerHTML = document.getElementsByTagName("p").innerHTML + patch;
                    document.getElementsByTagName("span").innerHTML = document.getElementsByTagName("span").innerHTML + patch;
                    document.getElementsByTagName("h4").innerHTML= document.getElementsByTagName("h4").innerHTML + patch;
                    count++;
                }

                
            },
            error: function(data){
                console.log("error")
                console.log(data)
            }
            
        })
    }
    //fetchTweets(count);
    setInterval(function(){fetchTweets(count);},1000);
    fetchTweets(data);
    console.log(data)

const tweetForm = document.getElementById("tweet-form")
    
        tweetForm.onsubmit(function(event){
           event.preventDefault()
            var this_ = $(this)
            //console.log(event) 
            alert("I am here");
            var formData = this_.serialize()

            $.ajax({
                url:"/api/tweetcreate",
                data: formData,
                method:"POST",
                success: function(data){
                   console.log(data) 
                   fetchTweets(data)
                },
            })
            
        })
        

    
    
    


});
