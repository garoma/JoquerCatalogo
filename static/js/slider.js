document.addEventListener('DOMContentLoaded', () => {
  const slider = document.querySelector('.slider');
  if (!slider) return;

  const images = slider.querySelectorAll('img');
  const prevBtn = slider.querySelector('.prev');
  const nextBtn = slider.querySelector('.next');

  let currentIndex = 0;
  let zoomed = false;

  function showImage(index) {
    images.forEach((img, i) => {
      img.classList.toggle('active', i === index);
      img.classList.remove('zoomed');
    });
    zoomed = false;
  }

  showImage(currentIndex);

  prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    showImage(currentIndex);
  });

  nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
  });

  images.forEach(img => {
    img.addEventListener('click', () => {
      zoomed = !zoomed;
      if (zoomed) {
        img.classList.add('zoomed');
      } else {
        img.classList.remove('zoomed');
      }
    });
  });
});
