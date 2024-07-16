// script.js
document.addEventListener('DOMContentLoaded', () => {
  const counters = [
    { id: 'clientCounter', target: 500 },
    { id: 'codeCounter', target: 1000 },
    { id: 'downloadCounter', target: 1500 },
    { id: 'subscriberCounter', target: 10000 }
  ];
  const duration = 2000; // Duration in milliseconds

  counters.forEach(counter => {
    let count = 0;
    const element = document.getElementById(counter.id);
    const increment = counter.target / (duration / 100); // Increment step

    function updateCounter() {
      if (count < counter.target) {
        count += increment;
        element.innerText = Math.ceil(count);
        setTimeout(updateCounter, 100); // Update every 100 milliseconds
      } else {
        element.innerText = counter.target; // Ensure the final value matches the target
      }
    }

    updateCounter();
  });
});