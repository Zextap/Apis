//!----------Declarar una constante para usar express---------
const express = require ('express');
const app  = express();


//?-----------Usar la constante app para usar los metodos de express-------
app.use(express.json());

//?-----------Usar el metodo get para hacer una peticion de tipo get-------
app.get ('/hola',(parametro,respuesta)=>{
    let res = {"mensaje" : "!Hola, mundo¡"};
    respuesta.send(res);
});

app.get('/hola/:res',(request,response)=>{ //request -> para recibir parametros | response -> para enviar el contenido 
    const parametro = request.params.res;
    let res = {"mensaje" : `Hola,${parametro}`};
    response.send(res);
});

//?-----------Declarar el puerto que escucha----------------
const puerto = process.env.port || 3000;
app.listen(puerto,()=> console.log(`Escuchando en puerto ${puerto}`));