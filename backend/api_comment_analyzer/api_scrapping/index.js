const express = require('express');
const puppeteer = require('puppeteer');
const CommentScraper = require('./comment_scrapper.js');
const bodyParser = require('body-parser');
const app = express();

const port = 3000; // Puerto en el que la API estará en funcionamiento

app.use(bodyParser.json());

app.post('/api/scrap-comments', async (req, res) => {
    const { urls } = req.body;

    if (!urls || !Array.isArray(urls) || urls.length === 0) {
        return res.status(400).json({ error: 'Se requieren URLs de videos válidas.' });
    }
    
    const browser = await puppeteer.launch({ headless: false, defaultViewport: null });
    const page = await browser.newPage();
    await page.goto('https://www.youtube.com');
    const commentScraper = new CommentScraper(page);
    const comentarios_data = await commentScraper.recopilarComentarios(urls);
    await browser.close();
    res.json(comentarios_data);
});


app.listen(port, () => {
    console.log(`La API está escuchando en el puerto ${port}`);
});




















