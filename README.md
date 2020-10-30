# Documentação da API

**Visualizar todas as receitas**


* **URL**

  /receitas

* **Headers**

  **authorization**: Token

* **Método**

  `GET`

* **Payload**

    None
  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** 
    ```json
    [{
        "nome": "string",
        "descricao": "string",
        "tempoMedio": "string",
        "quantidadeLitros": "number",
            "ingredientes": [{
		        "nome": "string",
		        "quantidade": "string",
 		        "unidadeMedida": "enum"
	        }],
        "aquecimento": {
            "temperatura": "number"
	    },
        "brassagem": [{
		    "tempo": "number",
		    "temperatura": "number"
        }],
        "fervura": {
            "tempoTotal": "number",
		    "ingredientes": [{
                "tempo": "number",
		        "nome": "string",
		        "quantidade": "string",
 		        "unidadeMedida": "enum"
		    }]
        }
    }]
    ```
 
* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`
----

**Adicionar receita**


* **URL**

  /receita

* **Headers**

  **authorization**: Token  
  **Content-Type**: 'application/json'

* **Método**

  `POST`
  
* **Payload**
    ```json
    {
        "nome": "string",
        "descricao": "string",
        "tempoMedio": "string",
        "quantidadeLitros": "number",
        "ingredientes": [{
            "nome": "string",
            "quantidade": "string",
            "unidadeMedida": "enum"
        }],
        "aquecimento": {
            "temperatura": "number"
        },
        "brassagem": [{
            "tempo": "number",
            "temperatura": "number"
        }],
        "fervura": {
            "tempoTotal": "number",
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }
    }
    ```

  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** `{ mensagem: "Receita cadastrada com sucesso." }`
 
* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 400 Bad Request  
    **Corpo:** `{ erro: "Não foi possível adicionar a receita" }`
    
  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`


----

**Visualizar receita específica**


* **URL**

  /receita/:receita.nome

* **Headers**

  **authorization**: Token

* **Método:**

  `GET`

* **Payload**

  None
  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** 
    ```json
    {
	    "nome": "string",
	    "descricao": "string",
	    "tempoMedio": "string",
	    "quantidadeLitros": "number",
	    "ingredientes": [{
		    "nome": "string",
		    "quantidade": "string",
 		    "unidadeMedida": "enum"
	    }],
	    "aquecimento": {
		    "temperatura": "number"
	    },
	    "brassagem": [{
		    "tempo": "number",
		    "temperatura": "number"
	    }],
	    "fervura": {
            "tempoTotal": "number",
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }
    }
    ```
 
* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 400 Bad Request  
    **Corpo:** `{ erro: "Receita não encontrada." }`

  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`


----

**Editar Receita**

    
* **URL**

  /receita

* **Headers**

  **authorization**: Token  
  **Content-Type**: 'application/json'

* **Método**

  `PUT`
  
* **Payload**
    ```json
    {
        "nome": "string",
        "descricao": "string",
        "tempoMedio": "string",
        "quantidadeLitros": "number",
        "ingredientes": [{
            "nome": "string",
            "quantidade": "string",
            "unidadeMedida": "enum"
        }],
        "aquecimento": {
            "temperatura": "number"
        },
        "brassagem": [{
            "tempo": "number",
            "temperatura": "number"
        }],
        "fervura": {
            "tempoTotal": "number",
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }
    }
    ```

  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** `{ mensagem: "Receita atualizada com sucesso." }`
 
* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 400 Bad Request  
    **Corpo:** `{ erro: "Não foi possível editar a receita" }`
    
  OU
  
    * **Status:** 500 Internal Server Error  
      **Corpo:** `{ erro: "Alguma coisa deu errada." }`

----    


**Visualizar processo atual**

* **URL**

  /processo

* **Headers**

  **authorization**: Token

* **Método**

  `GET`

* **Payload**

  None
  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** 
    ```json
    {
        "processo": "string",
        "etapas": [{
            "tempo": "number",
            "temperatura": "number",
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }],
        "tempoTotal": "number",
        "tempoAtual": "number",
        "tempoRestante": "number",
        "temperaturaAtual": "number"
    }

    ```
    **Exemplo aquecimento:** 
    ```json
     {
        "processo": "aquecimento",
        "etapas": [{
            "temperatura": "number"
        }],
        "tempoAtual": "number",
        "tempoRestante": "number",
        "temperaturaAtual": "number"
    }

    ```

    **Exemplo brassagem:** 
    ```json
    {
        "processo": "brassagem",
        "etapas": [{
            "tempo": "number",
            "temperatura": "number"
        }],
        "tempoAtual": "number",
        "tempoRestante": "number",
        "temperaturaAtual": "number"
    }

    ```

    **Exemplo Fervura:** 
    ```json
    {
        "processo": "fervura",
        "etapas": [{
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }],
        "tempoTotal": "number",
        "tempoAtual": "number",
        "tempoRestante": "number",
        "temperaturaAtual": "number"
    }
    ```



* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 400 Bad Request  
    **Corpo:** `{ erro: "Não existe processo em andamento." }`

  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`


----

**Visualizar processo específico**


* **URL**

  /processo/:processo.nome

* **Headers**

  **authorization**: Token

* **Método**

  `GET`

* **Data Params**

  None
  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** 
    ```json
    {
        "etapas": [{
            "tempo": "number",
            "temperatura": "number",
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }],
        "tempoTotal": "number",
        "tempoAtual": "number",
        "tempoRestante": "number"
    }

    ```
    **Exemplo aquecimento:** 
    ```json
    {
        "etapas": [{
            "temperatura": "number"
        }],
        "tempoAtual": "number",
        "tempoRestante": "number"
    }

    ```

    **Exemplo brassagem:** 
    ```json
    {
        "etapas": [{
            "tempo": "number",
            "temperatura": "number"
        }],
        "tempoAtual": "number",
        "tempoRestante": "number"
    }

    ```

    **Exemplo Fervura:** 
    ```json
    {
        "etapas": [{
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }],
        "tempoTotal": "number",
        "tempoAtual": "number",
        "tempoRestante": "number"
    }
    ```


* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 400 Bad Request  
    **Corpo:** `{ erro: "Processo não encontrado." }`

  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`
----

**Atualizar processo atual**

* **URL**

  /processo

* **Headers**

  **authorization**: Token

* **Método**

  `PUT`

* **Payload**
    ```json
    {
        "processo": "string",
        "etapas": [{
            "tempo": "number",
            "temperatura": "number",
            "ingredientes": [{
                "tempo": "number",
                "nome": "string",
                "quantidade": "string",
                "unidadeMedida": "enum"
            }]
        }],
        "tempoTotal": "number",
        "tempoAtual": "number",
        "temperaturaAtual": "number",
        "tempoRestante": "number"
    }

    ```

  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** `{ mensagem: Processo(objeto) }`
 
* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 400 Bad Request  
    **Corpo:** `{ erro: "Não foi possível atualizar o processo" }`
    
  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`

----

**Iniciar processo**


* **URL**

  /iniciar

* **Headers**

  **authorization**: Token  
  **Corpo-Type**: 'application/json'

* **Método**

  `POST`
  
* **Payload**
    ```json
    {
        "nomeReceita": "string"
    }

    ```

  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** `{ mensagem: "Receita iniciada com sucesso." }`
 
* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 400 Bad Request  
    **Corpo:** `{ erro: "Receita não encontrada." }`

  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`
----

**Iniciar limpeza**

* **URL**

  /limpeza

* **Headers**

  **authorization**: Token

* **Método**

  `POST`
  
* **Payload**
  
  None

  
* **Resposta de Sucesso**

  * **Status:** 200 OK  
    **Corpo:** `{ mensagem: "Limpeza iniciada." }`
 
* **Resposta de Erro**

  * **Status:** 401 Unauthorized  
    **Corpo:** `{ erro: "Token não encontrado." }`

  OU

  * **Status:** 500 Internal Server Error  
    **Corpo:** `{ erro: "Alguma coisa deu errada." }`
