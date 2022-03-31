const express = require('express');
const app = express();
app.listen(3000, () => console.log('hello I hear you at 3000'));
app.use(express.static('public copy'));