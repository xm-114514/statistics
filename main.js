const factorial = n => n === 0 ? 1 : Array.from({ length: n }, (_, i) => i + 1).reduce((a, b) => a * b, 1);

const nPr = (n, r) => {
  if (n < r) return 0; 
  return factorial(n) / factorial(n - r);
};
const nCr = (n, r) => {
  if (n < r) return 0;
  return factorial(n) / (factorial(r) * factorial(n - r));
};
const circularpermutation = n => n > 1 ? factorial(n-1) : false;
