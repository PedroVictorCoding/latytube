var marker_video_id = document.createElement('div');
marker_video_id.className = "video-container marker";
marker_video_id.id = marker.properties.id + "-element";
marker_video_id.setAttribute("onclick","playvideo(" + marker.properties.id + ", [" + marker.geometry.coordinates + "], '" + marker.properties.title + "');");

var loader_v = document.createElement('div');
loader_v.className = 'lds-ripple';
loader_v.style = "width:100px; height:100px; position:absolute;"
marker_video_id.appendChild(loader_v);

var video_v = document.createElement('video');
video_v.id = marker.properties.id;
video_v.style = "width:100%; height:100%; border-radius:10px;"
video_v.src = marker.properties.videofile;
video_v.href = "/feed/v/" + marker.properties.id;
video_v.loop = "true";
video_v.className = '';
marker_video_id.appendChild(video_v);

var rainbow_layer = document.createElement('div');
rainbow_layer.style = "position:absolute; width: 100%; height: 100%;  top:0; border-radius: 10px;";
marker_video_id.appendChild(rainbow_layer)

var rainbow_red = document.createElement('div');
rainbow_red.style = "width: 100%; height: 16.6666666%; top:0; border-radius: 10px 10px 0 0; background-color: rgba(255,0,0,0.37);";
rainbow_layer.appendChild(rainbow_red);

var rainbow_orange = document.createElement('div');
rainbow_orange.style = "width: 100%; height: 16.6666666%; top:33.3333332%; background-color: rgba(255, 127, 0, 0.37);";
rainbow_layer.appendChild(rainbow_orange);

var rainbow_yellow = document.createElement('div');
rainbow_yellow.style = "width: 100%; height: 16.6666666%; top:49.9999998%; background-color: rgba(255, 255, 0, 0.37);";
rainbow_layer.appendChild(rainbow_yellow);

var rainbow_green = document.createElement('div');
rainbow_green.style = "width: 100%; height: 16.6666666%; top:66.6666664%; background-color: rgba(0, 255, 0, 0.37);";
rainbow_layer.appendChild(rainbow_green);

var rainbow_blue = document.createElement('div');
rainbow_blue.style = "width: 100%; height: 16.6666666%; top:83.333333%; background-color: rgba(0, 0, 255, 0.37);";
rainbow_layer.appendChild(rainbow_blue);

var rainbow_purple = document.createElement('div');
rainbow_purple.style = "width: 100%; height: 16.6666666%; top:99.9999996%; border-radius: 0 0 10px 10px; background-color: rgba(148, 0, 211, 0.37);";
rainbow_layer.appendChild(rainbow_purple);

video_progress_bar_div = document.createElement('div')
video_progress_bar_div.id = "custom-seekbar"
video_progress_bar_div.style = ""
marker_video_id.appendChild(video_progress_bar_div)

video_progress_bar = document.createElement("span");
video_progress_bar.id = "progressbar" + marker.properties.id;
video_progress_bar.style = "background: #fff"
video_progress_bar_div.appendChild(video_progress_bar)

var video_title = document.createElement("p");
video_title.innerHTML = marker.properties.title;
video_title.style = "position: absolute; bottom: 8px; left:7px; position:absolute; color:#fff; font-weight:bold"
marker_video_id.appendChild(video_title);

var video_author = document.createElement("p");
video_author.innerHTML = marker.properties.author;
video_author.style = "bottom: -10px; left:7px; position:absolute; color:#fff;"
marker_video_id.appendChild(video_author);
