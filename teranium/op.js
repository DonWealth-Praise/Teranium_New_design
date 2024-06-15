// let topIndex = 0;
// let bottomIndex = 0;
// const topSlides = document.querySelector('.top-slider .slides');
// const bottomSlides = document.querySelector('.bottom-slider .slides');
// const topImages = document.querySelectorAll('.top-slider .slides img');
// const bottomImages = document.querySelectorAll('.bottom-slider .slides img');
// const topTotalSlides = topImages.length;
// const bottomTotalSlides = bottomImages.length;

// function showNextTopSlide() {
//     topIndex = (topIndex + 1) % topTotalSlides;
//     const offset = -topIndex * 105; // 100px image width + 5px margin
//     topSlides.style.transform = `translateX(${offset}px)`;
// }

// function showNextBottomSlide() {
//     bottomIndex = (bottomIndex + 1) % bottomTotalSlides;
//     const offset = -bottomIndex * 105; // 100px image width + 5px margin
//     bottomSlides.style.transform = `translateX(${offset}px)`;
// }

// // Change images every 3 seconds
// setInterval(showNextTopSlide, 3000);
// setInterval(showNextBottomSlide, 3000);