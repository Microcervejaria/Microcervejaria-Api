const requestValidations = (req, res) => {
    console.log("Validando dados");
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
        const first_path = req.path.split("/")[1];
        if(req.originalUrl == '/receitas') {
            const parametros_receita = [ 'nome', 'descricao', 'tempoMedio', 'quantidadeLitros', 'ingredientes', 'aquecimento', 'brassagem', 'fervura' ];
            sendResponse(req, res, parametros_receita, 'Receita cadastrada com sucesso.', 'Não foi possível adicionar a receita.')
        }
        if(req.originalUrl == '/iniciar' || first_path == 'iniciar') {
            const parametros_iniciar = [ 'nomeReceita' ];
            sendResponse(req, res, parametros_iniciar, 'Receita iniciada com sucesso.', 'Receita não encontrada.')
        }
        if(req.originalUrl == '/limpeza', first_path == 'limpeza') {
            const parametros_limpeza = ['nomeReceita'];
            sendResponse(req, res, parametros_limpeza, 'Limpeza iniciada.', 'Alguma coisa deu errada.')
        }
    }
    else if (req.method == "PUT") {
        const first_path = req.path.split("/")[1];
        if(req.path == '/receitas' || first_path == 'receitas') {
            const parametros_receita = [ 'nome', 'descricao', 'tempoMedio', 'quantidadeLitros', 'ingredientes', 'aquecimento', 'brassagem', 'fervura' ];
            sendResponse(req, res, parametros_receita, 'Receita atualizada com sucesso.', 'Não foi possível atualizar a receita.')
        }
        else if(req.originalUrl == '/processo') {
            const parametros_receita = [ 'processo', 'tempoAtual', 'etapas', 'tempoRestante', 'temperaturaAtual' ];
            sendResponse(req, res, parametros_receita, 'Processo atualizado com sucesso.', 'Não foi possível atualizar o processo.')
        }
    }
    else {
        res.jsonp(res.locals.data)
    }
}

module.exports = requestValidations;