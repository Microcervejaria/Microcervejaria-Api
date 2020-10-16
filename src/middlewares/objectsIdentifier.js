
objectsIdentifier = (req, res, next) => {
    const db = require('../db.json')
    if (req.method == "POST" || req.method == "PUT"){
        req.body['id'] = ++db[req.url.substr(1)].length
        console.log(req.body['id'])
    }
    next();
}

module.exports = objectsIdentifier;
