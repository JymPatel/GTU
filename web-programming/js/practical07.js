const imageUrls = [
  "https://avatars.githubusercontent.com/u/93824505?v=4",
  "https://avatars.githubusercontent.com/u/11620230?s=200&v=4",
  "https://avatars.githubusercontent.com/u/102582123?v=4",
];

let currentIndex = 0;
const imageElement = document.getElementById("image");

function changeImage() {
  imageElement.src = imageUrls[currentIndex];

  currentIndex = (currentIndex + 1) % imageUrls.length;

  setTimeout(changeImage, 1);
}

changeImage();
