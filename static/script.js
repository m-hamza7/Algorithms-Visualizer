document.addEventListener('DOMContentLoaded', () => {
  const resultText = document.querySelector('.processing-result');

  if (resultText) {
    const text = resultText.innerHTML.trim();
    resultText.innerHTML = '';
    let i = 0;

    function type() {
      if (i < text.length) {
        resultText.innerHTML += text[i];
        i++;
        setTimeout(type, 50); // Typing speed
      }
    }

    type();
  }
});
