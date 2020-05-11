var el = document.createElement('div');
el.className = "video-container marker";
el.id = marker.properties.id + "-element";
el.setAttribute("onclick","playvideo(" + marker.properties.id + ", [" + marker.geometry.coordinates + "], '" + marker.properties.title + "');");

var loader_v = document.createElement('div');
loader_v.className = 'lds-ripple';
loader_v.style = "width:100px; height:100px; position:absolute;"
el.appendChild(loader_v);

var video_v = document.createElement('video');
video_v.id = marker.properties.id;
video_v.style = "width:100%; height:100%; border-radius:10px;"
video_v.src = marker.properties.videofile;
video_v.href = "/feed/v/" + marker.properties.id;
video_v.loop = "true";
video_v.className = '';
el.appendChild(video_v);

// var video_shadow = document.createElement("div");
// video_shadow.className = "video-overlay"
// video_shadow.style = "bottom:0; left:0; width:100%; height:100%; border-radius:10px; background: linear-gradient(180deg, rgba(0, 0, 0, 0) 36.98%, rgba(0, 0, 0, 0.21) 52.08%, #121212 98.44%);"
// el.appendChild(video_shadow);

{/* <svg width="414" height="624" viewBox="0 0 414 624" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="414" height="104" fill="#FF0000" fill-opacity="0.37"/>
<rect y="104" width="414" height="104" fill="#FF6B00" fill-opacity="0.56"/>
<rect y="208" width="414" height="104" fill="#FFE600" fill-opacity="0.56"/>
<rect y="312" width="414" height="104" fill="#24FF00" fill-opacity="0.47"/>
<rect y="416" width="414" height="104" fill="#0075FF" fill-opacity="0.47"/>
<rect y="520" width="414" height="104" fill="#0500FF" fill-opacity="0.47"/>
</svg> */}


var rainbow_layer = document.createElement('div');
rainbow_layer.style = "position:absolute; width: 100%; height: 100%;  top:0; border-radius: 10px;";
el.appendChild(rainbow_layer)

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
el.appendChild(video_progress_bar_div)

video_progress_bar = document.createElement("span");
video_progress_bar.id = "progressbar" + marker.properties.id;
video_progress_bar_div.appendChild(video_progress_bar)

var video_title = document.createElement("p");
video_title.innerHTML = marker.properties.title;
video_title.style = "position: absolute; bottom: 8px; left:7px; position:absolute; color:#fff; font-weight:bold"
el.appendChild(video_title);

var video_author = document.createElement("p");
video_author.innerHTML = marker.properties.author;
video_author.style = "bottom: -10px; left:7px; position:absolute; color:#fff;"
el.appendChild(video_author);
