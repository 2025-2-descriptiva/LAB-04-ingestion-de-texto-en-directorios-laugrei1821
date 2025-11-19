# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

import os
import zipfile
import pandas as pd


def pregunta_01():

    # 1 Descomprimir archivo zip
   
    input_zip_path = "files/input.zip"
    extract_path = "files/input"

    if not os.path.exists(extract_path):
        with zipfile.ZipFile(input_zip_path, "r") as zip_ref:
            zip_ref.extractall("files/")

    # 2 leer archivos y crear DataFrames

    def load_split(split_name):
        base_path = os.path.join("files/input", split_name)

        rows = []

        for sentiment in ["negative", "positive", "neutral"]:
            sentiment_path = os.path.join(base_path, sentiment)

            if not os.path.exists(sentiment_path):
                continue

            for filename in os.listdir(sentiment_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(sentiment_path, filename)

                    with open(file_path, "r", encoding="utf-8") as f:
                        text = f.read().strip()

                    rows.append({
                        "phrase": text,
                        "target": sentiment
                    })

        return pd.DataFrame(rows)


    # 3 Cargar train y test

    train_df = load_split("train")
    test_df = load_split("test")


    # 4 Crear carpeta de salida (output)

    output_path = "files/output"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

 
    # 5 Guardar CSVs

    train_df.to_csv(os.path.join(output_path, "train_dataset.csv"), index=False)
    test_df.to_csv(os.path.join(output_path, "test_dataset.csv"), index=False)
    
    return train_df, test_df