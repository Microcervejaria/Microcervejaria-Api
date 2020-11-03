const requestValidations = (req, res) => {
    console.log("TENTOU ENTRAR");
    // const parametros_receitas = ['nome', 'descricao', 'tempoMedio', 'quantidadeLitros', 'Ingredientes', 'aquecimento', 'brassagem', 'fervura']
    function checkEquals(array1, array2) {
        return (array1.sort().toString() == array2.sort().toString())
    } 

    function sendResponse(req, res, params, successMessage, failMessage) {
        console.log(params);
        console.log(Object.keys(req.body));

        if(checkEquals(params, Object.keys(req.body))){
            res.status(200).json({ message: successMessage });
        }
        else {
            res.status(400).json({ erro: failMessage });
        }
    }

    if (req.method === "POST") {
        if(req.originalUrl == '/receitas') {
            const parametros_receita = [ 'id', 'nome', 'descricao', 'tempoMedio', 'quantidadeLitros', 'Ingredientes', 'aquecimento', 'brassagem', 'fervura' ];
            sendResponse(req, res, parametros_receita, 'Receita cadastrada com sucesso.', 'Não foi possível adicionar a receita.')
        }
        if(req.originalUrl == '/iniciar') {
            const parametros_iniciar = [ 'id', 'nomeReceita' ];
            sendResponse(req, res, parametros_iniciar, 'Receita iniciada com sucesso.', 'Receita não encontrada.')
        }
        if(req.originalUrl == '/limpeza') {
            const parametros_limpeza = ['nomeReceita'];
            sendResponse(req, res, parametros_limpeza, 'Limpeza iniciada.', 'Alguma coisa deu errada.')
        }
    }
    else if (req.method == "PUT") {
        if(req.originalUrl == '/receita') {
            const parametros_receita = [ 'id', 'nome', 'descricao', 'tempoMedio', 'quantidadeLitros', 'Ingredientes', 'aquecimento', 'brassagem', 'fervura' ];
            sendResponse(req, res, parametros_receita, 'Receita atualizada com sucesso.', 'Não foi possível atualizar a receita.')
        }
        else if(req.originalUrl == '/processo') {
            const parametros_receita = [ 'id', 'processo', 'tempoAtual', 'etapas', 'tempoRestante', 'temperaturaAtual' ];
            sendResponse(req, res, parametros_receita, 'Processo atualizado com sucesso.', 'Não foi possível atualizar a receita.')
        }
    }
    else {
        res.jsonp({
            body: res.locals.data
        })
    }
}

module.exports = requestValidations;