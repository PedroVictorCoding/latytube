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

var video_shadow = document.createElement("div");
video_shadow.className = "video-overlay"
video_shadow.style = "bottom:0; left:0; width:100%; height:100%; border-radius:10px; background: linear-gradient(180deg, rgba(0, 0, 0, 0) 36.98%, rgba(0, 0, 0, 0.21) 52.08%, #121212 98.44%);"
marker_video_id.appendChild(video_shadow);

video_progress_bar_div = document.createElement('div')
video_progress_bar_div.id = "custom-seekbar"
marker_video_id.appendChild(video_progress_bar_div)

video_progress_bar = document.createElement("span");
video_progress_bar.id = "progressbar" + marker.properties.id;
video_progress_bar.className = "shadow-lg"
video_progress_bar.style = "background:#fff"
video_progress_bar_div.appendChild(video_progress_bar)

var video_title = document.createElement("p");
video_title.innerHTML = marker.properties.title;
video_title.style = "position: absolute; bottom: 8px; left:7px; position:absolute; color:#fff; font-weight:bold"
marker_video_id.appendChild(video_title);

var video_author = document.createElement("p");
video_author.innerHTML = marker.properties.author;
video_author.style = "bottom: -10px; left:7px; position:absolute; color:#fff;"
marker_video_id.appendChild(video_author);
