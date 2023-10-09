[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Identification

* Title: ITA-ICEA Data Science Challenge - Previsão de ELDT

* Authors:

    * Pedro Teles

    * Marcel Zanetti

* Date: October 2023

# Folder Contents

* `data/original_files`: This directory houses the original Parquet files employed in the study. These files were obtained from the ICEA API and saved here to prevent redundant API requests and streamline the development process. Additionally, you'll find a file named `idsc_dataset.xlsx` in this folder, which contains the features of the test dataset.

* `data/feature_engineering`: Contains the Parquet files necessary for the feature engineering process. This includes the METAR scores extracted from OpenAI's API and the data generated by the `01_fetch_clean_data.py` script.

* `data/modelling`: Contains the Parquet files needed for the modeling process. This includes the data produced by the 02_feature_engineering.py script. Specifically, it comprises the data used for both model training and testing.

* `utils.py`: This file contains functions utilized by other scripts in this project.

* `01_fetch_clean_data.py`: This script is employed to fetch data from the API and perform cleaning operations. It generates a Parquet file named `clean_data.parquet` containing the cleaned data.

* `02_openai_metar.py`: This script is responsible for fetching METAR scores from OpenAI's API. Caution is advised when running this script due to the potential for a high number of API calls, which could result in substantial costs. The output is stored in a Parquet file named `metar_llm_scores.parquet`.

* `03_feature_engineering.py`: This script carries out the feature engineering process. It generates two Parquet files: `train_df.parquet` and `test_df.parquet`. It's essential to run this code twice, once for training data and once for test data.

* `04_modelling.py`: This script is used for training models and evaluating their performance. It produces a CSV file containing model predictions. Additionally, it implements a hyperparameter tuning process for the LightGBM model. The output file is named `submission_lightgbm.csv`.

# Data Availability Statement

All the parquet files used to suport the findings of this study have been deposited in the `data` folder. However, by uncommenting the code in the `01_fetch_clean_data.py` script, the data can be fetched directly from the API.

# Computational Requirements

- Python 3.10.4

    - aiofiles==0.6.0
    - asyncio==stdlib
    - calendar==stdlib
    - python-dotenv==1.0.0
    - duckdb==0.8.1
    - fancyimpute==0.7.0
    - geopy==2.4.0
    - json==2.0.9
    - lightgbm==3.3.2
    - metar==1.4
    - numpy==1.24.4
    - openai==0.27.2
    - pandas==1.5.2
    - pickle==stdlib
    - pyproj==3.6.1
    - re==2.2.1
    - requests==2.31.0
    - sklearn==1.1.1
    - tqdm==4.65.0
    - typing==stdlib

The code was last run on a 4 core 11th Gen Intel Core i7-1165G7 laptop, with Windows version 11, 16 GB of RAM, and 512GB of SSD. Computation took several hours.

# Instructions

Start by verifying that Python is installed on your system. Additionally, confirm that the folder containing your Python scripts serves as your current working directory. Futhermore, a `requirements.txt` file is provided to facilitate the installation of the necessary packages.

Moreover, if you intend to access data from the API and retrieve METAR scores via OpenAI's API, ensure you have an `.env` file within the same folder as your Python scripts. This `.env` file should contain the necessary keys for the OpenAI API (`OPENAI_API_KEY`) and the ICEA API (`API_TOKEN`). If you don't want to provide these keys, you can use the Parquet files provided in the `data` folder.

Finally, execute the code in the following order:

1. `01_fetch_clean_data.py`

2. `02_openai_metar.py` (optional)

3. `03_feature_engineering.py`

4. `04_modelling.py`

No further action is needed on the replicator’s part.

By this stage, you should find a `submission_lightgbm.csv` file that contains predictions for the test dataset. This file is located in the same directory as your Python scripts. Additionally, the intermediary files can be accessed through the `data` folder.

