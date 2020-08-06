function urlToPromise(url) {
    return new Promise(function(resolve, reject) {
        JSZipUtils.getBinaryContent(url, function (err, data) {
            if(err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
}
window.onerror = function () {
    location.reload();
 }

$(document).ready(function() {
    var urlList = [];
    var hashtag;
    var imgNbr;
    let url;
    var mydata;
    var infinite;
    
    $( "#dlbtn" ).click(function() {
        event.preventDefault();
        document.getElementById("loader").style.visibility = "visible";
        document.getElementById("dlbtn").disabled = true;
        hashtag = document.getElementById("id_Hashtag").value;
        imgNbr = parseInt(document.getElementById("id_Image_numbers").value);
        url = `https://www.instagram.com/explore/tags/${hashtag}/?__a=1`;
        setTimeout(function() {
            $.ajax({
                url: url,
                async: false,
                dataType: 'json',
                success: function (json) {mydata = json}
            });

            jsonDump = mydata.graphql.hashtag.edge_hashtag_to_media

            for (var i = 0; i < jsonDump.edges.length; i++) { 
                urlList.push(jsonDump.edges[i].node.display_url);
            }

            var urlLength = urlList.length

            if(urlLength >= 50){
                while(urlLength < imgNbr ){
                    var urlNext = url + "&max_id=" + mydata.graphql.hashtag.edge_hashtag_to_media.page_info.end_cursor
                    $.ajax({
                        url: urlNext,
                        async: false,
                        dataType: 'json',
                        success: function (json) {mydata = json}
                    });

                    jsonDump = mydata.graphql.hashtag.edge_hashtag_to_media

                    for (var i = 0; i < jsonDump.edges.length; i++) { 
                        urlList.push(jsonDump.edges[i].node.display_url);
                    }

                    urlLength = urlList.length
                    infinite ++;
                    if (infinite === 10) { break; }
                }

            }

            if (urlLength > imgNbr) {
                accuration = urlLength- imgNbr
                for (var i = 0; i < accuration; i++) { 
                urlList.pop()
                }
            }
            second()
        }, 10);
        


    });

function second (callback) {


    
    var zip = new JSZip();
    filename = hashtag
    
    for (var i = 0; i < urlList.length; i++) { 
        var url = urlList[i];
        var filename = `${i}.png`;
        zip.file(filename, urlToPromise(url), {binary:true});
    }
    zip.generateAsync({type:"blob"}, function updateCallback(metadata) {
        var msg = "progression : " + metadata.percent.toFixed(2) + " %";
        if(metadata.currentFile) {
            msg += ", current file = " + metadata.currentFile;
        }
        showMessage(msg);
        updatePercent(metadata.percent|0);
    })
    .then(function callback(blob) {
        document.getElementById("loader").style.visibility = "hidden";
        document.getElementById("dlbtn").disabled = false;
        saveAs(blob, `${hashtag}`);

        showMessage("done !");
    }, function (e) {
        showError(e);
    });
}

});

