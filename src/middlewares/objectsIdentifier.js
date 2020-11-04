const { values } = require('.');

objectsIdentifier = (req, res, next) => {
    const db = require('../db.json')
    if ((req.method == "POST" || req.method == "PUT") && (req.path == '/receitas' || req.path == '/receita')){
        db.receitas.map((value) => {
            if(value.id == req.body.nome && req.method == 'POST') {
                res.status(400).json({erro: "Já existe uma receita com esse nome"});
            }
        })
        console.log("ENTROU?");
        req.body['id'] = req.body['nome'];
    }
    next();
}

module.exports = objectsIdentifier;
