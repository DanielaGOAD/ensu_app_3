import streamlit as st
import pandas as pd
import gdown

# --- Grupo 1: Percepción de inseguridad por tipo de lugar ---
percepcion_lugares = {
    "BP1_1": "En la ciudad",
    "BP1_2_01": "En su casa",
    "BP1_2_02": "En su lugar de trabajo",
    "BP1_2_03": "En la calle",
    "BP1_2_04": "En la escuela o universidad",
    "BP1_2_05": "En el mercado",
    "BP1_2_06": "En centros comerciales",
    "BP1_2_07": "En bancos",
    "BP1_2_08": "En cajeros automáticos o en vía pública",
    "BP1_2_09": "En el transporte público",
    "BP1_2_10": "En su automóvil",
    "BP1_2_11": "En carreteras o caminos",
    "BP1_2_12": "En parques o áreas verdes"
}

# --- Grupo 2: Cambios de hábitos por temor a la delincuencia ---
cambios_habitos = {
    "BP1_5_1": "Cambiar sus hábitos respecto a llevar cosas de valor por temor a sufrir algún delito",
    "BP1_5_2": "Cambiar sus hábitos respecto a caminar por los alrededores de su vivienda, pasadas las ocho de la noche, por temor a sufrir algún delito",
    "BP1_5_3": "Cambiar sus hábitos respecto a visitar a parientes o amigos(as) por temor a sufrir algún delito",
    "BP1_5_4": "Cambiar sus hábitos respecto a permitir que los (las) menores de edad que viven en el hogar salgan solos(as) por temor a sufrir algún delito",
    "BP1_5_5": "Cambiar sus hábitos respecto a otra situación por temor a sufrir algún delito"
}

# --- Grupo 3: Efectividad de autoridades 2024–2025 ---
efectividad_autoridades_2024_2025 = {
    "BP1_8_1": "Policía Preventiva Municipal",
    "BP1_8_2": "Policía Estatal",
    "BP1_8_3": "Policía Federal / Guardia Nacional",
    "BP1_8_4": "Ejército",
    "BP1_8_5": "Fuerza Aérea Mexicana",
    "BP1_8_6": "Marina"
}

# --- Grupo 4: Efectividad de autoridades 2021–2023 ---
efectividad_autoridades_2021_2023 = {
    "BP1_8_1": "Policía Preventiva Municipal",
    "BP1_8_2": "Policía Estatal",
    "BP1_8_3": "Policía Federal / Guardia Nacional",
    "BP1_8_4": "Ejército",
    "BP1_8_6": "Marina"
}

# --- 🆕 Grupo 5: Expectativas sobre delincuencia ---
expectativas_delincuencia = {
    "BP1_3": "Expectativas sobre delincuencia"
}

# --- 🆕 Grupo 6: Efectividad del gobierno para resolver problemas ---
efectividad_gobierno = {
    "BP3_2": "Efectividad del gobierno para resolver problemas"
}

# --- 🆕 Grupo 7: Problemas que enfrenta la ciudad
otro_problema = {
    "BP3_1_01": "Fallas y fugas en el suministro de agua potable",
    "BP3_1_02": "Deficiencias en la red pública de drenaje",
    "BP3_1_03": "Coladeras tapadas por acumulación de desechos",
    "BP3_1_04": "Falta de tratamiento de aguas residuales",
    "BP3_1_05": "Alumbrado público insuficiente",
    "BP3_1_06": "Ineficiencia en el servicio de limpia y recolección de basura",
    "BP3_1_07": "Mercados y centrales de abasto en mal estado",
    "BP3_1_08": "Calles y avenidas con embotellamientos frecuentes",
    "BP3_1_09": "Problemas de salud derivados del manejo inadecuado de los rastros",
    "BP3_1_10": "Baches en calles y avenidas",
    "BP3_1_11": "Parques y jardines descuidados",
    "BP3_1_12": "Delincuencia (robos, extorsiones, secuestros, fraudes, etcétera)",
    "BP3_1_13": "Servicio de transporte público deficiente",
    "BP3_1_14": "Hospitales saturados o con servicio deficiente",
    "BP3_1_15": "Otro",
    "BP3_1_16": "Ninguno"
}

# --- 🆕 Grupo 8: Conocimiento de programas de prevención ---
conocimiento_programas = {
    "BP3_2A": "Conoce programas de prevención contra la violencia/delincuencia"
}
# --- Mapeo de códigos de ciudad a nombres ---
mapeo_ciudades = {
    1: "AGUASCALIENTES",
    2: "MEXICALI",
    3: "TIJUANA",
    4: "LA PAZ",
    5: "SAN FRANCISCO DE CAMPECHE",
    6: "SALTILLO",
    7: "LA LAGUNA",
    8: "PIEDRAS NEGRAS",
    9: "COLIMA",
    10: "MANZANILLO",
    11: "TUXTLA GUTIERREZ",
    12: "TAPACHULA",
    13: "CHIHUAHUA",
    14: "CIUDAD JUAREZ",
    19: "DURANGO",
    20: "LEON DE LOS ALDAMA",
    21: "ACAPULCO DE JUAREZ",
    22: "CHILPANCINGO DE LOS BRAVO",
    23: "PACHUCA DE SOTO",
    25: "PUERTO VALLARTA",
    26: "TOLUCA DE LERDO",
    27: "ECATEPEC DE MORELOS",
    28: "CIUDAD NEZAHUALCOYOTL",
    29: "MORELIA",
    30: "URUAPAN",
    31: "LAZARO CARDENAS",
    32: "CUERNAVACA",
    33: "TEPIC",
    35: "OAXACA DE JUAREZ",
    36: "HEROICA PUEBLA DE ZARAGOZA",
    37: "QUERETARO",
    38: "CANCUN",
    39: "SAN LUIS POTOSI",
    40: "CULIACAN ROSALES",
    41: "MAZATLAN",
    42: "LOS MOCHIS",
    43: "HERMOSILLO",
    44: "NOGALES",
    45: "VILLAHERMOSA",
    46: "TAMPICO",
    47: "REYNOSA",
    48: "NUEVO LAREDO",
    49: "TLAXCALA DE XICOHTENCATL",
    50: "VERACRUZ",
    51: "COATZACOALCOS",
    52: "MERIDA",
    53: "ZACATECAS",
    54: "FRESNILLO",
    55: "LOS CABOS",
    56: "CIUDAD DEL CARMEN",
    57: "GUANAJUATO",
    58: "IXTAPA-ZIHUATANEJO",
    59: "GUADALAJARA",
    60: "TONALA",
    61: "TLAJOMULCO DE ZUNIGA",
    62: "SAN PEDRO TLAQUEPAQUE",
    63: "ZAPOPAN",
    64: "MONTERREY",
    65: "SAN PEDRO GARZA GARCIA",
    66: "APODACA",
    67: "GUADALUPE",
    68: "GENERAL ESCOBEDO",
    69: "SAN NICOLAS DE LOS GARZA",
    70: "SANTA CATARINA",
    71: "AZCAPOTZALCO",
    72: "COYOACAN",
    73: "CUAJIMALPA DE MORELOS",
    74: "GUSTAVO A. MADERO",
    75: "IZTACALCO",
    76: "IZTAPALAPA",
    77: "LA MAGDALENA CONTRERAS",
    78: "MILPA ALTA",
    79: "ALVARO OBREGON",
    80: "TLAHUAC",
    81: "TLALPAN",
    82: "XOCHIMILCO",
    83: "BENITO JUAREZ",
    84: "CUAUHTEMOC",
    85: "MIGUEL HIDALGO",
    86: "VENUSTIANO CARRANZA",
    87: "TLALNEPANTLA DE BAZ",
    88: "NAUCALPAN DE JUAREZ",
    89: "CUAUTITLAN IZCALLI",
    90: "ATIZAPAN DE ZARAGOZA",
    91: "CHIMALHUACAN",
    92: "IRAPUATO",
    93: "CHETUMAL",
    94: "CIUDAD OBREGON",
    95: "CIUDAD VICTORIA",
    96: "XALAPA"
}

# --- Cargar datos desde múltiples archivos en Google Drive ---
@st.cache_data
def cargar_datos_base():
    file_ids = [
        "1VLMGozkGzj1eETDBAMQU296P2Z4r1wpY",# archivo original
        "1qktfndQFrzc-RRzJ6fF-vXNnGwttz6kD"                   # 🔁 ¡REEMPLAZA ESTO con el ID del nuevo CSV!
    ]

    columnas_necesarias = (
        ["ANIO", "TRIMESTRE", "CD", "NOM_CD", "FAC_SEL"]
        + list(percepcion_lugares.keys())
        + list(cambios_habitos.keys())
        + list(set(efectividad_autoridades_2024_2025.keys()) | set(efectividad_autoridades_2021_2023.keys()))
        + list(expectativas_delincuencia.keys())
        + list(efectividad_gobierno.keys())
        + list(otro_problema.keys())
        + list(conocimiento_programas.keys())
    )

    dtype_dict = {
        "ANIO": "int16",
        "TRIMESTRE": "int8",
        "CD": "category",
        "NOM_CD": "category",
        "FAC_SEL": "float32"
    }
    for col in columnas_necesarias:
        if col not in ["ANIO", "TRIMESTRE", "CD", "NOM_CD", "FAC_SEL"]:
            dtype_dict[col] = "Int8"

    dfs = []
    for file_id in file_ids:
        url = f"https://drive.google.com/uc?export=download&id={file_id}"  # ✅ sin espacios
        try:
            path = gdown.download(url, quiet=True, output=None)
            df_temp = pd.read_csv(
                path,
                encoding="latin1",
                usecols=columnas_necesarias,
                dtype=dtype_dict,
                low_memory=False
            )
            dfs.append(df_temp)
        except Exception as e:
            st.error(f"❌ Error al cargar el archivo con ID {file_id}: {e}")

    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        st.error("❗ No se pudo cargar ningún archivo desde Google Drive.")
        return pd.DataFrame(columns=columnas_necesarias)

# --- Cargar y preparar el DataFrame combinado ---
df = cargar_datos_base()

# Aseguramos que CD sea entero
df["CD"] = pd.to_numeric(df["CD"], errors="coerce").fillna(-1).astype(int)
df["NOMBRE_CIUDAD"] = df["CD"].map(mapeo_ciudades).fillna("Desconocido")
df["CD"] = df["CD"].astype(str)

# --- Resto de la interfaz y lógica (sin cambios) ---
st.title("📊 Histórico ENSU - Inseguridad, Hábitos, Expectativas y Efectividad de Autoridades")
st.markdown("""
Explora el **histórico trimestral (2016–2025)** sobre:
- 🏙️ Percepción de inseguridad por lugar
- 🚶‍♀️ Cambios de hábitos por temor a la delincuencia
- 👮‍♂️ Percepción de efectividad de autoridades
- 🔮 Expectativas sobre la delincuencia
- 🏛️ Efectividad del gobierno para resolver problemas
- 🚧 Problemas que enfrenta la ciudad
- 📢 Conocimiento de programas de prevención contra la violencia/delincuencia
""")

# --- Selección del tipo de indicador ---
tipo_variable = st.radio(
    "Selecciona el tipo de indicador:",
    [
        "Percepción de inseguridad",
        "Cambio de hábitos",
        "Efectividad de autoridades (2024 en delante)",
        "Efectividad de autoridades (2021–2023)",
        "Expectativas sobre delincuencia",
        "Efectividad del gobierno para resolver problemas",
        "Problemas que enfrenta la ciudad",
        "Conocimiento de programas de prevención contra la violencia/delincuencia"
    ]
)

# --- Diccionarios de opciones (igual que antes) ---
if tipo_variable == "Percepción de inseguridad":
    opciones = percepcion_lugares
elif tipo_variable == "Cambio de hábitos":
    opciones = cambios_habitos
elif tipo_variable == "Efectividad de autoridades (2024 en delante)":
    opciones = efectividad_autoridades_2024_2025
elif tipo_variable == "Efectividad de autoridades (2021–2023)":
    opciones = efectividad_autoridades_2021_2023
elif tipo_variable == "Expectativas sobre delincuencia":
    opciones = expectativas_delincuencia
elif tipo_variable == "Efectividad del gobierno para resolver problemas":
    opciones = efectividad_gobierno
elif tipo_variable == "Problemas que enfrenta la ciudad":
    opciones = otro_problema
else:
    opciones = conocimiento_programas

variable_sel = st.selectbox("Selecciona la variable:", list(opciones.values()))
nombres_ciudades = sorted(df[df["NOMBRE_CIUDAD"] != "Desconocido"]["NOMBRE_CIUDAD"].unique())
ciudad_sel = st.selectbox(
    "Selecciona la ciudad:",
    ["Estados Unidos Mexicanos"] + list(nombres_ciudades)
)

variable_col = [k for k, v in opciones.items() if v == variable_sel][0]

# --- Filtrado ---
df_filtrado = df.copy()
if ciudad_sel != "Estados Unidos Mexicanos":
    df_filtrado = df_filtrado[df_filtrado["NOMBRE_CIUDAD"] == ciudad_sel]

if tipo_variable == "Efectividad de autoridades (2024 en delante)":
    df_filtrado = df_filtrado[df_filtrado["ANIO"].isin([2024, 2025, 2026, 2027, 2028, 2029, 2030])]
elif tipo_variable == "Efectividad de autoridades (2021–2023)":
    df_filtrado = df_filtrado[df_filtrado["ANIO"].between(2021, 2023)]

# --- Función calcular_porcentaje (igual que antes) ---
def calcular_porcentaje(df, col, tipo):
    # [Misma función que ya tienes, sin cambios]
    if tipo == "Conocimiento de programas de prevención contra la violencia/delincuencia":
        df_val = df[df[col].isin([1, 2, 9])].copy()
        if df_val.empty:
            return pd.DataFrame(columns=["ANIO", "TRIMESTRE", "PORCENTAJE"])
        df_val["PESO_SI"] = (df_val[col] == 1) * df_val["FAC_SEL"]
        resumen = df_val.groupby(["ANIO", "TRIMESTRE"]).agg(
            TOTAL_VALIDOS=('FAC_SEL', 'sum'),
            TOTAL_SI=('PESO_SI', 'sum')
        ).reset_index()
        resumen["PORCENTAJE"] = (100 * resumen["TOTAL_SI"] / resumen["TOTAL_VALIDOS"]).round(2)

    elif tipo == "Problemas que enfrenta la ciudad":
        df_val = df[df[col].isin([0, 1])].copy()
        if df_val.empty:
            return pd.DataFrame(columns=["ANIO", "TRIMESTRE", "PORCENTAJE"])
        df_val["PESO_SI"] = (df_val[col] == 1) * df_val["FAC_SEL"]
        resumen = df_val.groupby(["ANIO", "TRIMESTRE"]).agg(
            TOTAL_VALIDOS=('FAC_SEL', 'sum'),
            TOTAL_SI=('PESO_SI', 'sum')
        ).reset_index()
        resumen["PORCENTAJE"] = (100 * resumen["TOTAL_SI"] / resumen["TOTAL_VALIDOS"]).round(2)

    else:
        if tipo in ["Percepción de inseguridad", "Cambio de hábitos"]:
            df_val = df[df[col].isin([1, 2])].copy()
        else:
            df_val = df[df[col].isin([1, 2, 3, 4, 9])].copy()

        if df_val.empty:
            return pd.DataFrame(columns=["ANIO", "TRIMESTRE", "PORCENTAJE"])

        if tipo == "Percepción de inseguridad":
            df_val["PESO_SI"] = (df_val[col] == 2) * df_val["FAC_SEL"]
        elif tipo == "Cambio de hábitos":
            df_val["PESO_SI"] = (df_val[col] == 1) * df_val["FAC_SEL"]
        elif tipo in ["Efectividad de autoridades (2024 en delante)", "Efectividad de autoridades (2021–2023)", "Efectividad del gobierno para resolver problemas"]:
            df_val["PESO_SI"] = df_val[col].isin([1, 2]) * df_val["FAC_SEL"]
        elif tipo == "Expectativas sobre delincuencia":
            df_val["PESO_IGUAL"] = (df_val[col] == 3) * df_val["FAC_SEL"]
            df_val["PESO_EMPEORARA"] = (df_val[col] == 4) * df_val["FAC_SEL"]
        else:
            return pd.DataFrame()

        resumen = df_val.groupby(["ANIO", "TRIMESTRE"]).apply(
            lambda g: pd.Series({
                "TOTAL_VALIDOS": g["FAC_SEL"].sum(),
                "TOTAL_SI": g["PESO_SI"].sum() if "PESO_SI" in g else 0,
                "TOTAL_IGUAL": g["PESO_IGUAL"].sum() if "PESO_IGUAL" in g else 0,
                "TOTAL_EMPEORARA": g["PESO_EMPEORARA"].sum() if "PESO_EMPEORARA" in g else 0
            })
        ).reset_index()

        if "PESO_SI" in df_val:
            resumen["PORCENTAJE"] = (100 * resumen["TOTAL_SI"] / resumen["TOTAL_VALIDOS"]).round(2)
        else:
            resumen["PORCENTAJE"] = 0

        if tipo == "Expectativas sobre delincuencia":
            resumen["PORCENTAJE_IGUAL"] = (100 * resumen["TOTAL_IGUAL"] / resumen["TOTAL_VALIDOS"]).round(2)
            resumen["PORCENTAJE_EMPEORARA"] = (100 * resumen["TOTAL_EMPEORARA"] / resumen["TOTAL_VALIDOS"]).round(2)
            resumen["PORCENTAJE_TOTAL"] = (100 * (resumen["TOTAL_IGUAL"] + resumen["TOTAL_EMPEORARA"]) / resumen["TOTAL_VALIDOS"]).round(2)

    resumen["PERIODO"] = resumen["ANIO"].astype(str) + "-" + resumen["TRIMESTRE"].astype(str)
    return resumen.sort_values(["ANIO", "TRIMESTRE"])

# --- Mostrar resultados ---
resumen = calcular_porcentaje(df_filtrado, variable_col, tipo_variable)

if resumen.empty:
    st.warning(f"No hay datos válidos para '{variable_sel}' en la ciudad seleccionada.")
else:
    titulo = f"Histórico de {ciudad_sel}" if ciudad_sel != "Estados Unidos Mexicanos" else "Histórico nacional"
    st.subheader(f"{titulo} - {variable_sel}")

    if tipo_variable == "Expectativas sobre delincuencia":
        st.dataframe(resumen[["PERIODO", "PORCENTAJE_IGUAL", "PORCENTAJE_EMPEORARA", "PORCENTAJE_TOTAL"]])
        st.line_chart(resumen.set_index("PERIODO")[["PORCENTAJE_IGUAL", "PORCENTAJE_EMPEORARA"]])
    else:
        st.dataframe(resumen[["PERIODO", "PORCENTAJE"]])
        st.line_chart(resumen.set_index("PERIODO")["PORCENTAJE"])
