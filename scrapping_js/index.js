const express = require('express');
const puppeteer = require('puppeteer');
const CommentScraper = require('./comment_scrapper.js');
const YoutubeScraper = require('./search.js');
const bodyParser = require('body-parser');
const fs = require('fs');
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
    console.log(comentarios_data)
    await browser.close();
    res.json(comentarios_data);
    fs.writeFileSync('comentarios.json', JSON.stringify(comentarios_data, null, 2));
});



app.post('/api/search-and-scrap-videos', async (req, res) => {
    const { query } = req.body;

    if (!query) {
        return res.status(400).json({ error: 'Se requiere una consulta de búsqueda válida.' });
    }

    const browser = await puppeteer.launch({ headless: false, defaultViewport: null });
    const page = await browser.newPage();
    await page.goto('https://www.youtube.com');
    const youTubeScraper = new YoutubeScraper(page);
    // Realiza la búsqueda en YouTube
    const searchResults = await youTubeScraper.search(query);
    console.log('Se han cargado '+searchResults.length+' videos')
    const commentScraper = new CommentScraper(page);
    const comentarios_data = await commentScraper.recopilarComentarios(searchResults);
    await browser.close();
    res.json(comentarios_data);
    fs.writeFileSync('comentarios.json', JSON.stringify(comentarios_data, null, 2));
});


app.listen(port, () => {
    console.log(`La API está escuchando en el puerto ${port}`);
});



























// {
//     "urls": [
//         "https://www.youtube.com/watch?v=n1w3_gT3D0E",
//         "https://www.youtube.com/watch?v=79JygZ7DUqw"
//     ]
// }


// {
//     "query": 'politica'
// }