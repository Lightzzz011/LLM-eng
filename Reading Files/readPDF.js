import fs from "fs";
import pdf from "pdf-parse";

const dataBuffer = fs.readFileSync("file.pdf");
const pdfData = await pdf(dataBuffer);
console.log(pdfData.text);
