import fs from 'fs';

const text = fs.readFilesync("sample.txt","utf-8");
console.log(text);