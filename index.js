const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use('/reload', createProxyMiddleware({ target: 'http://localhost:3001', changeOrigin: true }));
app.listen(3000);
