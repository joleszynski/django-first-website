const hamburger = document.querySelector(".hamburger");
const nav = document.querySelector(".menu");
const menu = document.querySelector(".menu__wrapper");

const handleClick = () => {
  //menu.classList.toggle("menu__wrapper--active");
  hamburger.classList.toggle("hamburger--active");
  nav.classList.toggle("menu--active");
};

hamburger.addEventListener("click", handleClick);

const path = location.pathname;
const activeElement = document.getElementById(path);
if (activeElement) {
  activeElement.className = "menu__click--active";
}
