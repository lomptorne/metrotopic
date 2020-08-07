// Zip Apending handling
function urlToPromise(url) {
    return new Promise(function(resolve, reject) {
        JSZipUtils.getBinaryContent(url, function (err, data) {
            if(err) {
                reject(err);
            } 
            else {
                resolve(data);
            }
        });
    });
}

// Error handling
window.onerror = function (msg, url, line, columnNo, error) {   
    alert("Sorry, hashtag not found, try again !")
    location.reload()
 } 

$(document).ready(function() {

    // Setting Globals vars
    var urlList = [];
    var hashtag;
    var imgNbr;
    let url;
    var mydata;
    var infinite;
    
    // On button click submit the form
    $( "#dlbtn" ).click(function() {
        
        // Setting scoped variables
        event.preventDefault();
        document.getElementById("loader").style.visibility = "visible";
        document.getElementById("dlbtn").disabled = true;

        // Hashtag and image number formating
        hashtag = document.getElementById("id_Hashtag").value;
        hashtag =hashtag.replace(/[^A-Za-z]/g, "");  
        hashtag = hashtag.toLowerCase();
        hashtag = hashtag.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
        imgNbr = parseInt(document.getElementById("id_Image_numbers").value);
        if(imgNbr > 500){imgNbr = 500}
        url = `https://www.instagram.com/explore/tags/${hashtag}/?__a=1`;

        //Set a delay before ajax freeze the page due to async false
        setTimeout(function() {

            // Ajax request for the images urls
            $.ajax({
                url: url,
                async: false,
                dataType: 'json',
                success: function (json) {mydata = json}
            });

            // Get the urls nodes
            jsonDump = mydata.graphql.hashtag.edge_hashtag_to_media

            // Append urls to an array
            for (var i = 0; i < jsonDump.edges.length; i++) { 
                urlList.push(jsonDump.edges[i].node.display_url);
            }

            // Get the numbers of urls
            var urlLength = urlList.length

            // If the number of urls is not enough query others pages for more
            if(urlLength >= 50){
                while(urlLength < imgNbr ){

                    // Get the url of the next page via end_cursor
                    var urlNext = url + "&max_id=" + mydata.graphql.hashtag.edge_hashtag_to_media.page_info.end_cursor

                    // New ajax request
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

                    // Security against infinite loop
                    if (infinite === 10) { break; }
                }

            }

            // Make the urlist the correct number the user querying
            if (urlLength > imgNbr) {
                accuration = urlLength- imgNbr
                for (var i = 0; i < accuration; i++) { 
                urlList.pop()
                }
            }

            // Launch the zip function
            second()
        }, 10);
        


    });

    // Ziping function
    function second (callback) {

        // Set variables
        var zip = new JSZip();
        filename = hashtag

        // Get all the urls data 
        for (var i = 0; i < urlList.length; i++) { 
            var url = urlList[i];
            var filename = `${i}.png`;
            zip.file(filename, urlToPromise(url), {binary:true});
        }

        // generate the zip with all the files
        zip.generateAsync({type:"blob"}, function updateCallback(metadata) {
            var msg = "progression : " + metadata.percent.toFixed(2) + " %";
            if(metadata.currentFile) {
                msg += ", current file = " + metadata.currentFile;
            }
            showMessage(msg);
            updatePercent(metadata.percent|0);
        })
        .then(function callback(blob) {

            // reload frontend
            document.getElementById("loader").style.visibility = "hidden";
            document.getElementById("dlbtn").disabled = false;
            saveAs(blob, `${hashtag}`);
            showMessage("done !");
            location.reload();
            
        }, function (e) {
            showError(e);
        });
    }

});

