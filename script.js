let countries = [];
let current = null;
let points = 0;

fetch("country-list.json")
  .then(res => res.json())
  .then(data => {
    countries = data.filter(item => isEnglish(item.country) && isEnglish(item.capital));
    newQuestion();
  });

function isEnglish(str) {
  return /^[\x00-\x7F]*$/.test(str);
}

function newQuestion() {
  document.getElementById("feedback").textContent = '';
  document.getElementById("answer").value = '';
  current = countries[Math.floor(Math.random() * countries.length)];
  document.getElementById("question").textContent = `What is the capital of ${current.country}?`;
}

function checkAnswer() {
  const userInput = document.getElementById("answer").value.trim();
  if (!userInput) return;

  if (userInput.toLowerCase() === current.capital.toLowerCase()) {
    points += 2;
    document.getElementById("feedback").textContent = "✅ Correct! +2 points";
  } else if (similarity(userInput, current.capital) > 0.7) {
    points += 1;
    document.getElementById("feedback").textContent = `⚠️ Close! The correct answer is ${current.capital}. +1 point`;
  } else {
    document.getElementById("feedback").textContent = `❌ No! The correct answer is ${current.capital}.`;
  }
  document.getElementById("points").textContent = `Points: ${points}`;
}

function similarity(a, b) {
  let longer = a.length > b.length ? a : b;
  let shorter = a.length > b.length ? b : a;
  let same = 0;
  for (let i = 0; i < shorter.length; i++) {
    if (a[i] === b[i]) same++;
  }
  return same / longer.length;
}
