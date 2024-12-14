//!----------Declarar una constante para usar express---------
const express = require ('express');
const app  = express();


//?-----------Usar la constante app para usar los metodos de express-------
app.use(express.json());

//?-----------Usar el metodo get para hacer una peticion de tipo get-------
app.get('/api/:res',(request,response)=>{
    const parametro = request.params.res;
    response.send('Esto es una api de node con el parametro '+parametro);
});

//?-----------Declarar el puerto que escucha----------------
const puerto = process.env.port || 8080;
app.listen(puerto,()=> console.log(`Escuchando en puerto ${puerto}`));