import locale

PICKJSON = 0
SAVEOUT = 1
FIRST_RESULT = 2
PREVIEW = 3
INPUT_PATTERN = 4
CHOOSE_DATA_FILE = 5
SEE_PATTERN = 6
TYPE_PATTERN = 7
CHOOSE_FILE = 8
CONVERT = 9

STR = {
    "pt_BR": {
        0 : "Escolha um arquivo qualquer no formato json...",
        1 : "Salvar conversão como...",
        2 : "Primeiro item de json identificado no arquivo de entrada:",
        3 : "Pré-visualizar o efeito da aplicação do padrão sobre os dados:",
        4 : "Entre com um padrão para traduzir os dados:",
        5 : "Abra um arquivo que contenha os dados que deseja converter. Aqui você verá o primeiro registro da lista de dados...",
        6 : "Aqui você verá a conversão do primeiro registro para o padrão que você digitou. (e.g. MyData(1))",
        7 : "Digite aqui um padrão para a conversão dos dados, use o símbolo # como escopo de declaração de variáveis. (e.g. MyData(#id#))",
        8 : "Abra um Arquivo",
        9 : "Converter",
    },
    "default": {
        0 : "Pick any file with json extension...",
        1 : "Save converted data as...",
        2 : "First identified json item on file input:",
        3 : "Preview the effect of applying the pattern on the data:",
        4 : "Input a string pattern to translate the whole dataset:",
        5 : "Open a file that contains the data you want to convert. Here you will see the first register of the dataset...",
        6 : "Here you will see the first register conversion to the pattern you input. (e.g. MyData(1))",
        7 : "Type here a pattern to convert the data, use the # symbol as a scope of variable declaration. (e.g. MyData(#id#))",
        8 : "Choose a File",
        9 : "Convert",
    },
}

LANG = locale.getdefaultlocale()[0]
SYSLANG = LANG if LANG in STR else "default"

def get(resID:int) -> str:
    return STR[SYSLANG][resID]
