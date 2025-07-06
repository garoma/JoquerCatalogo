from flask import Flask, render_template, abort, request

app = Flask(__name__)

# Dados estaticos dos produtos
produtos = [
    {
        "id": 1,
        "categoria": "Calca",
        "titulo": "Calça Skny",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: calcaskynclara",
        "imagens": ["foto3_0.jpeg", "foto3_1.jpeg", "OIP.jpg"],
        "capa": "foto3_0.jpeg"
    },
    {
        "id": 2,
        "categoria": "Calca",
        "titulo": "Calça Skny",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: calcaskynescura",
        "imagens": ["foto4_0.jpeg", "foto4_1.jpeg", "OIP.jpg"],
        "capa": "foto4_0.jpeg"
    },
    {
        "id": 3,
        "categoria": "Short",
        "titulo": "Short Meia Cocha",
        "preco": 25.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: shortmeiacochaclara",
        "imagens": ["foto1_0.jpeg", "foto1_1.jpeg", "OIP.jpg"],
        "capa": "foto1_0.jpeg"
    },
    {
        "id": 4,
        "categoria": "Short",
        "titulo": "Short Meia Cocha",
        "preco": 25.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: shortmeiacochaescura",
        "imagens": ["foto2_0.jpeg", "foto2_1.jpeg", "OIP.jpeg"],
        "capa": "foto2_0.jpeg"
    },
    {
        "id": 5,
        "categoria": "Calca",
        "titulo": "Calça Pantalona",
        "preco": 30.00,
        "tamanhos": "P, M, G e GG",
        "descricao": "Ref: calcapantalonaclara",
        "imagens": ["foto5_0.jpeg", "foto5_1.jpeg", "OIP.jpg"],
        "capa": "foto5_0.jpeg"
    },
    {
        "id": 6,
        "categoria": "Calca",
        "titulo": "Calça Pantalona",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: calcapntalonaescura",
        "imagens": ["foto6_0.jpeg", "foto6_1.jpeg", "OIP.jpg"],
        "capa": "foto6_0.jpeg"
    },
    {
        "id": 7,
        "categoria": "Short",
        "titulo": "Short Plinçado",
        "preco": 25.00,
        "tamanhos": "P, M, G e GG",
        "descricao": "Ref: shortplinçadoclaro",
        "imagens": ["foto7_0.jpeg", "foto7_1.jpeg", "OIP.jpg"],
        "capa": "foto7_0.jpeg"
    },
    {
        "id": 8,
        "categoria": "Calca",
        "titulo": "Calça Fler",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: calçaflerescura",
        "imagens": ["foto8_0.jpeg", "oto8_1.jpeg", "OIP.jpg"],
        "capa": "foto8_0.jpeg"
    },
    {
        "id": 9,
        "categoria": "Saia",
        "titulo": "Saia Gode",
        "preco": 32.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: saiagodeescura",
        "imagens": ["foto9_0.jpeg", "foto9_1.jpeg", "foto9_2.jpeg"],
        "capa": "foto9_0.jpeg"
    },
    {
        "id": 10,
        "categoria": "Saia",
        "titulo": "Saia Gode",
        "preco": 32.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: saiagodeclara",
        "imagens": ["foto10_0.jpeg", "foto10_1.jpeg", "foto10_2.jpeg"],
        "capa": "foto10_0.jpeg"
    },
    {
        "id": 11,
        "categoria": "Saia",
        "titulo": "Saia Botão Lateral",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: saiabotãolateralescura",
        "imagens": ["foto11_0.jpeg", "foto11_1.jpeg", "foto11_2.jpeg"],
        "capa": "foto11_0.jpeg"
    },
    {
        "id": 12,
        "categoria": "Saia",
        "titulo": "Saia Botão Lateral",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: saiabotãolateralclaro",
        "imagens": ["foto12_0.jpeg", "foto12_1.jpeg", "foto12_2.jpeg"],
        "capa": "foto12_0.jpeg"
    },
    {
        "id": 14,
        "categoria": "Calca",
        "titulo": "Calça WidLeg",
        "preco": 35.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: calcawidlegclara",
        "imagens": ["foto14_0.jpeg", "foto14_1.jpeg", "OIP.jpg"],
        "capa": "foto14_0.jpeg"
    },
    {
        "id": 15,
        "categoria": "Calca",
        "titulo": "Calça WidLeg",
        "preco": 35.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: calcawidlegescura",
        "imagens": ["foto15_0.jpeg", "foto15_1.jpeg", "OIP.jpg"],
        "capa": "foto15_0.jpeg"
    },
    {
        "id": 16,
        "categoria": "Saia",
        "titulo": "Mini Saia",
        "preco": 22.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: minisaiaclara",
        "imagens": ["foto16_0.jpeg", "foto16_1.jpeg", "foto16_2.jpeg"],
        "capa": "foto16_0.jpeg"
    },
    {
        "id": 17,
        "categoria": "Saia",
        "titulo": "Mini Saia",
        "preco": 22.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: minisaiaescura",
        "imagens": ["foto17_0.jpeg", "foto17_1.jpeg", "foto17_2.jpeg"],
        "capa": "foto17_0.jpeg"
    },
    {
        "id": 18,
        "categoria": "Jaqueta",
        "titulo": "Jaqueta",
        "preco": 32.00,
        "tamanhos": "P, M, G e GG",
        "descricao": "Ref: jaquetaescura",
        "imagens": ["foto18_0.jpeg", "foto18_1.jpeg", "OIP.jpg"],
        "capa": "foto18_0.jpeg"
    },
    {
        "id": 19,
        "categoria": "Jaqueta",
        "titulo": "Jaqueta",
        "preco": 32.00,
        "tamanhos": "P, M, G e GG",
        "descricao": "Ref: jaquetaclara",
        "imagens": ["foto19_0.jpeg", "foto19_1.jpeg", "OIP.jpg"],
        "capa": "foto19_0.jpeg"
    },
    {
        "id": 20,
        "categoria": "Saia",
        "titulo": "Mini Saia Cargo",
        "preco": 25.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: minisaiacargoclara",
        "imagens": ["foto20_0.jpeg", "foto20_1.jpeg", "OIP.jpg"],
        "capa": "foto20_0.jpeg"
    },
    {
        "id": 21,
        "categoria": "Saia",
        "titulo": "Mini Saia Cargo",
        "preco": 25.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: minisaiacargoescura",
        "imagens": ["foto21_0.jpeg", "foto21_1.jpeg", "OIP.jpg"],
        "capa": "foto21_0.jpeg"
    },

    {
        "id": 22,
        "categoria": "Saia",
        "titulo": "Saia Escura",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: saiaescura01",
        "imagens": ["foto22_0.jpeg", "OIP.jpg", "OIP.jpg"],
        "capa": "foto22_0.jpeg"
    },
    {
        "id": 23,
        "categoria": "Saia",
        "titulo": "Saia",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: saiaclara01",
        "imagens": ["foto23_0.jpeg", "OIP.jpg", "OIP.jpg"],
        "capa": "foto23_0.jpeg"
    },
    {
        "id": 24,
        "categoria": "Saia",
        "titulo": "Saia",
        "preco": 30.00,
        "tamanhos": "36 ao 46",
        "descricao": "Ref: saiaescura02",
        "imagens": ["foto24_0.jpeg", "OIP.jpg", "OIP.jpg"],
        "capa": "foto24_0.jpeg"
    },
]


@app.route('/')
def index():
    categoria = request.args.get('categoria')
    if categoria:
        produtos_filtrados = [p for p in produtos if p['categoria'].lower() == categoria.lower()]
    else:
        produtos_filtrados = produtos
    categorias = sorted(set(p['categoria'] for p in produtos))
    return render_template('index.html', produtos=produtos_filtrados, categorias=categorias, categoria_selecionada=categoria)

@app.route('/produto/<int:produto_id>')
def produto(produto_id):
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if not produto:
        abort(404)
    return render_template('produto.html', produto=produto)

if __name__ == '__main__':
    app.run(debug=True)
