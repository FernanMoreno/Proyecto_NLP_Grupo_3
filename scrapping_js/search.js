class YouTubeScraper {
    constructor(page) {
      this.page = page;
    }
  
    async search(tema) {
        // Selecciono el botón por su clase CSS
        const buttonSelector = '.yt-spec-button-shape-next--filled';
        // Espero a que el botón esté visible y sea interactuable
        await this.page.waitForSelector(buttonSelector, { visible: true });
        // Hago clic en el botón
        await this.page.click(buttonSelector);
        // Agrego una espera de un segundo usando setTimeout
        await new Promise(resolve => setTimeout(resolve, 1000)); 
        // selecciono el buscador por su id y escribo 
        await this.page.type('input#search', tema)
        // Agrego una espera de un segundo usando setTimeout
        await new Promise(resolve => setTimeout(resolve, 1000)); 
        // le doy click al boton de buscar
        await this.page.click('#search-icon-legacy')
        // Hago scroll varias veces para cargar mas videos
        for (let i = 0; i < 2; i++) { // Se puede ajustar el numero de veces que deseas hacer scroll
            await this.scrollDown();
            // Agrego una espera de un segundo entre cada scroll
            await new Promise(resolve => setTimeout(resolve, 1000));
        }

        const enlaces = await this.page.evaluate(()=>{
            const elements = document.querySelectorAll('.ytd-video-renderer #thumbnail')
            enlaces = []
            for (let element of elements){
                enlaces.push(element.href)
            }
            return enlaces
        });
        return enlaces
    }
  
    async scrollDown() {
        await this.page.evaluate(async () => {
            window.scrollBy(0, window.innerHeight);
        });
    }
  }

  module.exports = YouTubeScraper;