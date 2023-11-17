// // const observador = new MutationObserver((mutationList)=>{
// //     mutationList.forEach((mutation)=>{
// //         if(mutation.addedNodes.length){
// //             console.log('añadido', mutation.addedNodes[0])
// //         }
// //     });
// // });

// // //indicar el target que deseamos observar

// // const target = document.querySelector('.clase')
// // const observerOptions = {
// //     attributes :true,
// //     childList: true, // para ver si se agrego o elimino algo del DOM
// //     subtree:false,
// // }

// // observador.observe(target, observerOptions)



// class ObservadorDOM {
//     constructor(selector) {
//       this.target = document.querySelector(selector);
      
//       if (!this.target) {
//         console.error(`No se encontró ningún elemento con el selector: ${selector}`);
//         return;
//       }
      
//       this.observador = new MutationObserver((mutationList) => {
//         mutationList.forEach((mutation) => {
//           if (mutation.addedNodes.length) {
//             console.log('Añadido:', mutation.addedNodes[0]);
//           }
//         });
//       });
  
//       this.configuracionObservador = {
//         attributes: true,
//         childList: true,
//         subtree: false,
//       };
  
//       this.iniciarObservacion();
//     }



  
//     iniciarObservacion() {
//       this.observador.observe(this.target, this.configuracionObservador);
//       console.log(`Observando cambios en el elemento con el selector: ${this.target}`);
//     }
  
//     detenerObservacion() {
//       this.observador.disconnect();
//       console.log(`Observación detenida para el elemento con el selector: ${this.target}`);
//     }
//   }


// module.exports = ObservadorDOM;
