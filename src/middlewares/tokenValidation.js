module.exports = (req, res, next) => {
    console.log(req.headers.authorization)
    if(req.headers.authorization == 'cervejaria') {
        next();
    }
    else {
        res.json({ erro: 'Token não encontrado.'});
    }
}