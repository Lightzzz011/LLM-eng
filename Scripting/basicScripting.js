function cleanText(t) {
  return t.toLowerCase().trim();
}

const texts = ["Hello", "WORLD"];
const result = texts.map(cleanText);

console.log(result);
