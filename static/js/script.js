document.addEventListener('DOMContentLoaded', function () {
    const slider = document.getElementById('myRange');
    const imageMask = document.querySelector('.image-mask');

    if (slider && imageMask) {
        slider.addEventListener('input', function () {
            imageMask.style.width = this.value + '%';
        });
    }
});