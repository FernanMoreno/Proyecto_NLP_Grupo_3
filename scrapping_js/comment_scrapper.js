const puppeteer = require('puppeteer');
const fs = require('fs');

class CommentScraper {
    constructor(page) {
        this.page = page
        this.todosLosComentarios = [];
        this.numScrollInVideo = 15
    }

    async cerrarNavegador() {
        await this.page.close();
    }

    async scrollDown() {
        await this.page.evaluate(async () => {
            window.scrollBy(0, window.innerHeight);
        });
    }

    async recopilarComentarios(videos) {
        for (let i = 0; i < videos.length; i++) {
            await this.page.goto(videos[i]);
            const video = videos[i];
            
            this.cerrarModal(this.page)
            
            for (let j = 0; j < this.numScrollInVideo; j++) {
                await this.scrollDown();
                await new Promise(resolve => setTimeout(resolve, 1000));
            }

            try{
                await this.page.waitForSelector('#comments');

                const comentarios = await this.page.evaluate(() => {
                    const comentarios = [];
                    const content = document.querySelector('#comments #contents');
                    const contentLength = content.children.length - 1;
                    const currentUrl = window.location.href;

                    for (let k = 0; k < contentLength; k++) {
                        const contentElement = content.children[k];
                        const img_autor = contentElement.querySelector('#author-thumbnail #img')?.src || 'vacio';
                        const link_autor = contentElement.querySelector('#header-author h3')?.childNodes[1]?.href || 'vacio';
                        const autorComment = contentElement.querySelector('#author-text span')?.innerText || 'vacio';
                        const textComment = contentElement.querySelector('#content-text')?.innerText || 'vacio';
                        const link_video = currentUrl

                        let comentario = {
                            'img_autor':img_autor,
                            'link_autor':link_autor,
                            'autor': autorComment,
                            'comentario': textComment,
                            'link_video' : link_video
                        };
                        comentarios.push(comentario);
                    }
                    return comentarios;
                });

                this.todosLosComentarios.push({ 'link-video': video, 'comentarios': comentarios });
                // this.mostrarComentarios();
                console.log('Se han analizado ' + this.todosLosComentarios.length + ' videos');
                await new Promise(resolve => setTimeout(resolve, 1000));
            } catch (error)  {
                console.log(`No se pudo encontrar el elemento #comments en el video ${video}. Continuando con el siguiente video.`);
            }
                   
                
        }
        return this.todosLosComentarios
    }

    
    
    mostrarComentarios() {
        for (let elemento of this.todosLosComentarios) {
            console.log(`Comentarios para el video: ${elemento['link-video']}`);
            for (let comentario of elemento['comentarios']) {
                console.log(comentario);
            }
        }
        console.log('Se han analizado ' + this.todosLosComentarios.length + ' videos');
        return this.todosLosComentarios
    }


    async cerrarModal(page) {
        const modalSelector = '#dialog';
        try {
            await page.waitForSelector(modalSelector, { visible: true, timeout: 5000 }); //iempo de espera máximo
            const modalElement = await page.$(modalSelector);
            if (modalElement) {
                const closeButtonSelector = '.yt-spec-button-shape-next--filled';
                const closeButton = await modalElement.$(closeButtonSelector);
                if (closeButton) {
                    await closeButton.click();
                }
            }
        } catch (error) {
            // console.log('No se encontró el modal o no era visible en esta página.');
        }
    }
}

module.exports = CommentScraper;
