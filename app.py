import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Maison Bags",
    page_icon="👜",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "bolsas.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1584917865442-de89df76afd3"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_FROTA = (
    "https://images.unsplash.com/"
    "photo-1594223274512-ad4803739b7c"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap'
);


/* =========================================================
FONTE
========================================================= */

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F8F5EF 0%,
            #F1ECE3 50%,
            #E8E0D4 100%
        );
}


/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #111111,
            #211E1A
        );

    border-right:
        1px solid #B99A5E;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-family: 'Playfair Display', serif;

    font-size: 31px;
    font-weight: 600;

    color: #D4B477 !important;

    margin-bottom: 5px;

    letter-spacing: 1px;
}

.logo-subtitle {
    font-size: 10px;
    font-weight: 600;

    color: #D8D0C1 !important;

    letter-spacing: 2px;
}


/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-family: 'Playfair Display', serif;

    font-size: 42px;
    font-weight: 600;

    color: #211E1A !important;

    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 16px;

    color: #6E665B !important;

    margin-bottom: 30px;
}


/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;

    height: 430px;
    width: 100%;

    border-radius: 4px;

    overflow: hidden;

    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 18px 40px rgba(0,0,0,0.18);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(15,15,15,0.94) 0%,
            rgba(15,15,15,0.75) 45%,
            rgba(15,15,15,0.10) 100%
        );
}

.hero-content {
    position: absolute;

    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 580px;
}

.hero-number {
    font-family: 'Playfair Display', serif;

    font-size: 70px;
    font-weight: 500;

    color: #D4B477 !important;

    line-height: 1;
}

.hero-title {
    font-family: 'Playfair Display', serif;

    font-size: 46px;
    font-weight: 600;

    color: #FFFFFF !important;

    margin-top: 12px;

    line-height: 1.1;
}

.hero-text {
    font-size: 17px;

    color: #F0ECE5 !important;

    margin-top: 20px;

    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 2px;

    background: #B99A5E;

    color: #FFFFFF !important;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 1px;
}


/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 3px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(185,154,94,0.35);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.07);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-family: 'Playfair Display', serif;

    font-size: 34px;
    font-weight: 600;

    color: #211E1A !important;

    margin-top: 10px;
}

.card-label {
    font-size: 12px;

    font-weight: 700;

    color: #776F64 !important;

    margin-top: 5px;

    letter-spacing: 1px;
}


/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #151515,
            #292621
        );

    border-radius: 3px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    font-family: 'Playfair Display', serif;

    color: #D4B477 !important;

    margin-top: 0;
}

.dark-card p {
    color: #E9E3D9 !important;

    line-height: 1.7;
}


/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.92);

    padding: 30px;

    border-radius: 3px;

    border:
        1px solid #C8B58D;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}


/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {
    color: #211E1A !important;

    opacity: 1 !important;

    font-size: 14px !important;

    font-weight: 700 !important;
}


/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #211E1A !important;

    -webkit-text-fill-color:
        #211E1A !important;

    border:
        1px solid #B9A77E !important;

    border-radius: 3px !important;

    font-size: 15px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border:
        2px solid #A3844D !important;

    box-shadow:
        0 0 0 3px rgba(163,132,77,0.12) !important;
}

input::placeholder,
textarea::placeholder {
    color: #81796D !important;

    opacity: 1 !important;
}


/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {
    background-color: #292722 !important;

    border:
        1px solid #B99A5E !important;

    border-radius: 3px !important;
}

[data-baseweb="select"] > div * {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {
    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {
    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {
    fill: #D4B477 !important;

    color: #D4B477 !important;
}

[data-baseweb="select"] > div:hover {
    border-color: #D4B477 !important;
}


/* =========================================================
MENU ABERTO DO SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #292722 !important;
}

[data-baseweb="menu"] {
    background-color: #292722 !important;
}

[role="option"] {
    background-color: #292722 !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #594A31 !important;

    color: #FFFFFF !important;
}


/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background:
        linear-gradient(
            135deg,
            #A3844D,
            #C3A66D
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 3px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 13px !important;

    font-weight: 700 !important;

    letter-spacing: 0.5px;

    box-shadow:
        0 8px 18px rgba(125,96,47,0.22);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background:
        linear-gradient(
            135deg,
            #806534,
            #A3844D
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 3px;

    overflow: hidden;

    border:
        1px solid #C8B58D;
}


/* =========================================================
RODAPÉ
========================================================= */

.footer {
    margin-top: 50px;

    text-align: center;

    color: #756B5D !important;

    font-size: 13px;

    font-weight: 600;

    letter-spacing: 0.5px;
}


/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 32px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Marca",
        "Modelo",
        "Ano",
        "Cor",
        "Placa",
        "Quilometragem",
        "Valor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:

            dados = pd.read_csv(ARQUIVO)

            return dados

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# Garantir colunas necessárias

colunas_necessarias = [
    "Marca",
    "Modelo",
    "Ano",
    "Cor",
    "Placa",
    "Quilometragem",
    "Valor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:

        df[coluna] = ""


# Converter valores

df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)

df["Quilometragem"] = pd.to_numeric(
    df["Quilometragem"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
👜 Maison Bags
</div>

<div class="logo-subtitle">
BOUTIQUE DE LUXO
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Início",
        "➕ Cadastrar Bolsa",
        "👜 Bolsas Cadastradas"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "Maison Bags • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Início":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Elegância.<br>
Em cada detalhe.
</div>

<div class="hero-text">
Descubra uma seleção especial de bolsas,
organizada em um único lugar.
<br>
Cadastre, consulte e acompanhe sua coleção
com praticidade e sofisticação.
</div>

<div class="hero-badge">
👜 COLLECTION PRIVÉE
</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
"""
<div class="page-title">
✨ Visão geral da coleção
</div>

<div class="page-subtitle">
Acompanhe suas bolsas e mantenha sua coleção organizada.
</div>
""",
        unsafe_allow_html=True
    )

    total_carros = len(df)

    valor_total = df["Valor"].sum()

    km_total = df["Quilometragem"].sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
👜
</div>

<div class="card-number">
{total_carros}
</div>

<div class="card-label">
BOLSAS CADASTRADAS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💎
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR TOTAL DA COLEÇÃO
</div>

</div>
""",
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
✨
</div>

<div class="card-number">
{km_total:,.0f}
</div>

<div class="card-label">
ITENS REGISTRADOS
</div>

</div>
""",
            unsafe_allow_html=True
        )


    st.markdown("<br>", unsafe_allow_html=True)


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✨ Elegância em cada detalhe
</h2>

<p>
A Maison Bags permite manter sua coleção
de bolsas organizada em um único lugar.
</p>

<p>
Cadastre, consulte, pesquise e acompanhe
suas peças de maneira moderna, simples
e sofisticada.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    with coluna2:

        st.image(
            IMAGEM_FROTA,
            use_container_width=True
        )


# =========================================================
# CADASTRAR BOLSA
# =========================================================

elif menu == "➕ Cadastrar Bolsa":

    st.markdown(
"""
<div class="page-title">
➕ Nova bolsa
</div>

<div class="page-subtitle">
Adicione uma nova peça à sua coleção.
</div>
""",
        unsafe_allow_html=True
    )


    with st.form(
        "cadastro_carro",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            marca = st.text_input(
                "🏷️ Marca"
            )

            modelo = st.text_input(
                "👜 Modelo"
            )

            ano = st.number_input(
                "📅 Ano da coleção",
                min_value=1900,
                max_value=2035,
                value=2024,
                step=1
            )

            cor = st.selectbox(
                "🎨 Cor",
                [
                    "Preto",
                    "Bege",
                    "Branco",
                    "Marrom",
                    "Cinza",
                    "Vermelho",
                    "Azul",
                    "Rosa",
                    "Verde",
                    "Dourado",
                    "Outro"
                ]
            )


        with col2:

            placa = st.text_input(
                "🔖 Código / Referência"
            )

            quilometragem = st.number_input(
                "📦 Quantidade",
                min_value=0,
                value=1,
                step=1
            )

            valor = st.number_input(
                "💎 Valor da Bolsa",
                min_value=0.0,
                value=0.0,
                step=1000.0
            )

            observacoes = st.text_area(
                "📝 Observações"
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR BOLSA"
        )


    if cadastrar:

        if (
            marca.strip()
            and modelo.strip()
            and placa.strip()
        ):

            novo_carro = pd.DataFrame(
                [{
                    "Marca": marca.strip(),
                    "Modelo": modelo.strip(),
                    "Ano": int(ano),
                    "Cor": cor,
                    "Placa": placa.strip().upper(),
                    "Quilometragem": int(quilometragem),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    novo_carro
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "👜 Bolsa cadastrada com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha Marca, Modelo e Código / Referência."
            )


# =========================================================
# BOLSAS CADASTRADAS
# =========================================================

elif menu == "👜 Bolsas Cadastradas":

    st.markdown(
"""
<div class="page-title">
👜 Minha coleção
</div>

<div class="page-subtitle">
Consulte e pesquise todas as bolsas cadastradas.
</div>
""",
        unsafe_allow_html=True
    )


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
👜 Nenhuma bolsa cadastrada
</h2>

<p>
Sua coleção ainda está vazia.
Cadastre sua primeira bolsa para começar.
</p>

</div>
""",
            unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar bolsa",
            placeholder="Digite marca, modelo, referência ou cor..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown("<br>", unsafe_allow_html=True)


        opcoes_carros = df.index.tolist()


        carro_excluir = st.selectbox(
            "🗑️ Selecione uma bolsa para excluir",
            options=opcoes_carros,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} "
                f"{df.loc[indice, 'Modelo']} - "
                f"{df.loc[indice, 'Placa']}"
        )


        if st.button(
            "🗑️ EXCLUIR BOLSA"
        ):

            df = df.drop(
                carro_excluir
            )

            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "👜 Bolsa excluída com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

👜 Maison Bags<br>
Elegância em cada detalhe

</div>
""",
    unsafe_allow_html=True
)
