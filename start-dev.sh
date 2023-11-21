# Inicia el servidor Node.js en segundo plano
cd backend

cd api_comment_analyzer/api_scrapping

node index.js &

# Espera un momento para que el servidor Node.js se inicie (ajusta según sea necesario)
sleep 2

cd ..

# cd api_comment_analyzer

# Inicia el servidor FastAPI en segundo plano
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Espera un momento para que el servidor FastAPI se inicie (ajusta según sea necesario)
sleep 2

cd ..

cd database
 
node main.js  &

cd ../../

sleep 2

# Cambia al directorio de Angular (debes ajustar la ruta)
cd frontend

# Inicia el servidor de desarrollo de Angular en segundo plano
ng serve &

# Vuelve al directorio principal si es necesario
cd ..

# Informa que los servidores se han iniciado
echo "Servidores Node.js, FastAPI y Angular en ejecución."


## Debes posicionarte en el archivo raiz del proyecto, escribir este comando en la tarminal y ejecutarlo
# chmod +x start-dev.sh && ./start-dev.sh