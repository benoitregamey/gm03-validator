// prevent the default behavior of web browser when dragging and droping files over DOM
['dragleave', 'drop', 'dragenter', 'dragover'].forEach(function (evt) {
    document.addEventListener(evt, function (e) {
        e.preventDefault();
    }, false);
});

// Deal dragiing over effect
$(".drop-area").on('dragenter', function (e) {
    $(".drop-area").css("outline-width", "1px");
});

$(".drop-area").on('dragleave', function (e) {
    $(".drop-area").css("outline-width", "0px");
});

var test;

// Function to upload files to the server
$(".drop-area").on('drop', function (e) {
    e.preventDefault();

    $(".drop-area").css("outline-width", "0px");

    const fileList = e.originalEvent.dataTransfer.files; // the files to be uploaded
    if (fileList.length == 0) {
        return false;
    }

    // we use XMLHttpRequest here instead of fetch, because with the former we can easily implement progress and speed.
    const xhr = new XMLHttpRequest();
    xhr.open('post', '/upload', true);

    // show uploading progress
    xhr.upload.onprogress = function (event) {
        if (event.lengthComputable) {
            // update progress
            let percent = Math.floor(event.loaded / event.total * 100);
            $('.progress').removeClass("d-none");
            $('.progress-bar').css('width', percent + "%");
            if (percent === 100){
                $('.progress-bar').text("Validating metadata...");

            } else {
                $('.progress-bar').text(percent + "%");
            }
        }
    };

    xhr.onload = function() {
        if (xhr.status != 200) { // analyze HTTP status of the response
            alert(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
        } else { // show the result

            setTimeout(function(){
                $("#drop-area").css("height", "0");
                $("#drop-area").css("opacity", "0");
                read_md_results(JSON.parse(xhr.response));
              }, 500);

        }
    };

    // send files to server
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    const fd = new FormData();
    for (let file of fileList) {
        fd.append('files', file);
    }

    xhr.send(fd);
});

function read_md_results(results) {

    for (let i = 0; i < results.length; i++) {

        $("#md-results").append(
            `<div class="row mx-1 mx-sm-2 mx-md-5 my-3 align-items-center flex-nowrap md-result">
                <div class="col-8 col-sm-4 overflow-hidden">
                    <p class="text-muted my-0 text-nowrap"></p>
                </div>
                <div class="col-sm-6 d-none d-sm-block overflow-hidden">
                    <p class="text-muted my-0 text-nowrap"></p>
                </div>
                <div class="col-4 col-sm-2 overflow-hidden" style="min-width:100px">
                    <p class="text-right my-0 text-nowrap"></p>
                </div>
            </div>`
        )   

        $("#md-results .md-result").last().children().children("p").eq(0).text(results[i].uuid);
        $("#md-results .md-result").last().children().children("p").eq(1).text(results[i].title);

        if (results[i].valid === "yes"){
            $("#md-results .md-result").last().addClass("md-valid")
            $("#md-results .md-result").last().children().children("p").eq(2).html(
                '<i class="fa-solid fa-check"></i>&nbsp;valid'
            );
        } else {
            $("#md-results .md-result").last().addClass("md-notvalid")
            $("#md-results .md-result").last().children().children("p").eq(2).html(
                '<i class="fa-solid fa-xmark"></i>&nbsp;not valid'
            );
        }
      }
  }