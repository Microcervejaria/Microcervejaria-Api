
objectsIdentifier = (req, res, next) => {
    if ((req.method == "POST" || req.method == "PUT") && (req.originalUrl == '/receitas' || req.originalUrl == '/receita')){
        const db = require('../db.json')
        req.body['id'] = db[req.url.substr(1)].length + 1
    }
    next();
}

module.exports = objectsIdentifier;
