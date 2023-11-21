const express = require('express');
const mysql = require('mysql');
const cors = require('cors'); // Importa el paquete CORS
const app =express()

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors()); //
require('dotenv').config();


const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE,
  port: process.env.DB_PORT,
  charset: process.env.DB_CHARSET
});


// Conectar a la base de datos
connection.connect((err) => {
    if (err) {
      console.error('Error al conectar a la base de datos:', err.message);
    } else {
      console.log('Conexión exitosa a la base de datos MySQL');
    }
  });



  app.get('/datos', (req, res) => {
    // Realizar la consulta a la base de datos
    connection.query('SELECT * FROM comentarios', (err, results) => {
      if (err) {
        console.error('Error al ejecutar la consulta:', err.message);
        res.status(500).send('Error interno del servidor');
      } else {
        console.log('Resultados de la consulta:', results);
        res.json(results); // Enviar los resultados como respuesta en formato JSON
      }
    });
  });




  app.post('/insertar-datos', (req, res) => {

     // Verificar si req.body y req.body.comentarios existen
    // if (!req.body || !req.body.comentarios) {
    //     return res.status(400).json({ error: 'Datos de comentarios no proporcionados correctamente.' });
    // }

    const comentarios = req.body;
  
    // Suponiendo que tu tabla se llama 'comentarios'
    const tablaComentarios = 'comentarios';
  
    // Construir la consulta de inserción
    const consultaInsercion = 'INSERT INTO ?? ( comentario, nombre_usuario, foto_usuario, link_usuario, url_video, sentimiento) VALUES ?';
  
    // Preparar los valores para la inserción
    const valoresInsercion = comentarios.map(comentario => {
      return [ comentario.comentario, comentario.nombre_usuario, comentario.foto_usuario, comentario.link_usuario, comentario.url_video, comentario.sentimiento];
    });

    console.log(valoresInsercion)
  
    // Ejecutar la consulta de inserción
    connection.query(consultaInsercion, [tablaComentarios, valoresInsercion], (error, resultados, campos) => {
      if (error) {
        console.error(`Error al insertar comentarios: ${error.message}`);
        res.status(500).json({ error: 'Error al insertar comentarios en la base de datos.' });
      } else {
        console.log(`Comentarios insertados con éxito. Filas afectadas: ${resultados.affectedRows}`);
        res.status(200).json({ message: 'Comentarios insertados con éxito.' });
      }
    });
  });



// Puerto en el que escucha el servidor
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Servidor en ejecución en http://localhost:${PORT}`);
});