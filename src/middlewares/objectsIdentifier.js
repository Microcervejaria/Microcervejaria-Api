const { values } = require('.');

objectsIdentifier = (req, res, next) => {
    const db = require('../db.json')
    if ((req.method == "POST" || req.method == "PUT") && (req.originalUrl == '/receitas' || req.originalUrl == '/receita')){
        db.receitas.map((value) => {
            if(value.id == req.body.nome) {
                res.status(400).json({erro: "Já existe uma receita com esse nome"});
            }
        })
        req.body['id'] = req.body['nome'];
    }
    next();
}

module.exports = objectsIdentifier;
