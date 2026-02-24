'use strict';

const P = 40;
const Tj = 150;
const Tamb = 40;

const Rjc = 2.2;
const Rcs = 0;

const Rsa = ((Tj - Tamb)/P) - (Rjc + Rcs);
const S = 800/Rsa

console.log(`Rsa: ${Math.ceil(Rsa)} °C/W`);
console.log(`Heat sink (S): ${Math.ceil(S)} cm2`);
