/*
    Function which create html elements and
    showing data like a posts
*/
const showData = (data) => {
  const mediaUrl = location.href + "media/";
  const contentBox = document.querySelector(".content__box");
  const showMuchButton = document.querySelector(".home__wrapper__button");

  for (const post of data) {
    // create and add content post
    const componentPostWrapper = document.createElement("div");
    componentPostWrapper.className = "component__post__wrapper";
    contentBox.insertBefore(componentPostWrapper, showMuchButton);

    // create and add img wrapper
    const componentPostImageWrapper = document.createElement("div");
    componentPostImageWrapper.className = "component__post__image__wrapper";
    componentPostWrapper.appendChild(componentPostImageWrapper);

    // create and add img
    const componentPostImage = document.createElement("img");
    componentPostImage.className = "component__post__image";
    componentPostImage.src = mediaUrl + post.fields.photo;
    componentPostImageWrapper.appendChild(componentPostImage);

    // create post rside
    const componentPostContentWrapper = document.createElement("div");
    componentPostContentWrapper.className = "component__post__content__wrapper";
    componentPostWrapper.appendChild(componentPostContentWrapper);

    // create and add h3.title
    const componentPostContentTitle = document.createElement("h3");
    componentPostContentTitle.className = "component__post__content__title";
    componentPostContentWrapper.appendChild(componentPostContentTitle);

    // create and add ahref title
    const aTitle = document.createElement("a");
    aTitle.href = location.href + "blog/" + post.fields.slug;
    aTitle.innerText = post.fields.title;
    componentPostContentTitle.appendChild(aTitle);

    // create and div intro
    const componentPostContentIntro = document.createElement("div");
    componentPostContentIntro.className = "component__post__content__intro";
    componentPostContentIntro.innerText = post.fields.content.slice(0, 255);
    componentPostContentWrapper.appendChild(componentPostContentIntro);

    // create and add a czytaj dalej
    const aRead = document.createElement("a");
    aRead.href = location.href + "blog/" + post.fields.slug;
    aRead.innerText = "\tCzytaj dalej...";
    componentPostContentIntro.appendChild(aRead);
  }
};

// variable reperesnted posts list length
let postsLen;

// first take data on load website
const takeData = (url) => {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const json_data = JSON.parse(data);
      postsLen = json_data.length;
      showData(json_data);
    });
};

// remove button show much when posts end
const removeButton = () => {
  const muchButton = document.querySelector(".home__button__show__much");
  muchButton.innerText = "Koniec";
};

// get csrf cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// set csrf token
const csrftoken = getCookie("csrftoken");
let headers = new Headers();
headers.append("X-CSRFToken", csrftoken);
headers.append("Content-Type", "application/json");

// take data to end posts list
const postData = (url) => {
  fetch(url, {
    method: "POST",
    credentials: "include",
    headers: headers,
    body: JSON.stringify({ postsLen: postsLen }),
  })
    .then((response) => response.json())
    .then((data) => {
      const json_data = JSON.parse(data);
      postsLen += json_data.length;
      console.log(json_data);
      if (json_data.length === 0) {
        removeButton();
      } else {
        showData(json_data);
      }
    });
};
