
const jsonServer = require('json-server');
const server = jsonServer.create();
const middlewares = require('./middlewares');
const requestValidation = require('./middlewares/requestValidations');
const port = process.env.PORT || 3000;
const router = jsonServer.router(__dirname + '/db.json');
const routes = require(__dirname + '/routes.json');


router.db._.id = 'nome';

server.use(jsonServer.bodyParser);
server.use(jsonServer.rewriter(routes));
server.use(middlewares);

server.use(router);
router.render = requestValidation;
  
  

server.listen(port);