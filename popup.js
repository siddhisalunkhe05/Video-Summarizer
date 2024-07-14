document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('summaryForm');
    var summaryDiv = document.getElementById('summary');
    var loadingSpinner = document.createElement('div');
    loadingSpinner.className = 'loading-spinner';
    loadingSpinner.innerHTML = '<div class="spinner"></div>';

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var videoId = document.getElementById('videoId').value;
        summaryDiv.innerHTML = ''; 


        summaryDiv.appendChild(loadingSpinner);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://localhost:5000/', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var summary = xhr.responseText;

                summaryDiv.removeChild(loadingSpinner);

                summaryDiv.innerText = summary;
            }
        };
        xhr.send('video_id=' + encodeURIComponent(videoId));
    });
});

