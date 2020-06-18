var marker_video_id = document.createElement("div");
marker_video_id.id = marker.properties.id + "-marker"
marker_video_id.className = "video-container marker";

var video_box = document.createElement('div');
video_box.className = "video-container";
video_box.id = marker.properties.id + "-element";
video_box.setAttribute("onclick","playvideo(" + marker.properties.id + ", [" + marker.geometry.coordinates + "], '" + marker.properties.title + "');");
marker_video_id.appendChild(video_box);

var loader_v = document.createElement('div');
loader_v.className = 'lds-ripple';
loader_v.style = "width:100px; height:100px; position:absolute;"
video_box.appendChild(loader_v);

var video_v = document.createElement('video');
video_v.id = marker.properties.id;
video_v.style = "width:100%; height:100%; border-radius:10px;"
video_v.src = marker.properties.videofile;
video_v.href = "/feed/v/" + marker.properties.id;
video_v.loop = "true";
video_v.className = '';
video_box.appendChild(video_v);

var video_shadow = document.createElement("div");
video_shadow.className = "video-overlay"
video_shadow.style = "bottom:0; left:0; width:100%; height:100%; border-radius:10px; background: linear-gradient(180deg, rgba(0, 0, 0, 0) 36.98%, rgba(0, 0, 0, 0.21) 52.08%, #121212 98.44%);"
video_box.appendChild(video_shadow);

video_progress_bar_div = document.createElement('div')
video_progress_bar_div.id = "custom-seekbar"
video_box.appendChild(video_progress_bar_div)

video_progress_bar = document.createElement("span");
video_progress_bar.id = "progressbar" + marker.properties.id;
video_progress_bar.className = "shadow-lg"
video_progress_bar.style = "background:#fff"
video_progress_bar_div.appendChild(video_progress_bar)

var video_title = document.createElement("p");
video_title.innerHTML = marker.properties.title;
video_title.style = "position: absolute; bottom: 8px; left:7px; position:absolute; color:#fff; font-weight:bold"
video_box.appendChild(video_title);

var video_author = document.createElement("p");
video_author.innerHTML = marker.properties.author;
video_author.style = "bottom: -10px; left:7px; position:absolute; color:#fff;"
video_box.appendChild(video_author);

var hidden_deck_div = document.createElement("div");
hidden_deck_div.style = "max-width:22.5vw; max-height:80vh;";
marker_video_id.appendChild(hidden_deck_div);

var hidden_deck = document.createElement("div");
hidden_deck.style = "width:100%; height: 100%; position:absolute; top:0; left: 100%; border-radius: 10px; display:none; margin-left: 10px";
hidden_deck.id = marker.properties.id + "-hiddenDeck";
hidden_deck.className = "bg-dark";
hidden_deck_div.appendChild(hidden_deck);

var views_box = document.createElement("p");
views_box.id = marker.properties.id + "-views"
views_box.className = "btn btn-dark btn-lg";
views_box.style = "position: absolute; left: -100px; bottom: 50px;"
views_box.innerText = "👀 " + marker.properties.view_count;
hidden_deck.appendChild(views_box);

var likes_box = document.createElement("p");
likes_box.id = marker.properties.id + "-like"
likes_box.className = "btn btn-dark btn-lg";
likes_box.style = "position: absolute; left: -100px; bottom: 0;";
likes_box.innerText = "👍 " + marker.properties.like_count;
hidden_deck.appendChild(likes_box);

var exit_button = document.createElement("button");
exit_button.style = "position:absolute; right:0; margin-right: 2.5%; margin-top:10px";
exit_button.className = "btn btn-action";
exit_button.innerHTML = "Hide Video";
exit_button.setAttribute("onclick", "hideVideo(" + marker.properties.id + ")");
hidden_deck.appendChild(exit_button);

var comments_box = document.createElement("div");
comments_box.id = marker.properties.id + "-comments";
comments_box.style = "width:95%; height:85%; margin-left:2.5%; margin-top:12%; cursor: grab; cursor : -o-grab; cursor : -moz-grab; cursor : -webkit-grab; overflow-y: auto;"
comments_box.className = "rounded"
hidden_deck.appendChild(comments_box);

var create_comment = document.createElement("div");
create_comment.className = "input-group";
create_comment.style = "position:absolute; width:95%; margin-left: 2.5%; margin-right: 2.5%; bottom: 10px"
hidden_deck.appendChild(create_comment)

var comments_input = document.createElement("input");
comments_input.id = marker.properties.id + "-newcomment"
comments_input.style = "width:72.5%; position: absolute;  bottom: 5px;";
comments_input.className = "btn btn-lg text-left btn-outline-light";
comments_input.placeholder = "Comment";
comments_input.setAttribute("maxlength", "150")
create_comment.appendChild(comments_input);

var submit_comment = document.createElement("button");
submit_comment.id = marker.properties.id + "-newcommentsubmit"
submit_comment.innerHTML = "Send";
submit_comment.style = 'width: 22.5%; position: absolute; bottom: 5px; right:0';
submit_comment.className = "btn btn-lg btn-action text-white rounded";
create_comment.appendChild(submit_comment);

