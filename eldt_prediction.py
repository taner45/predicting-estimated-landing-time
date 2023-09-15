#%%
import pandas as pd
import dotenv
import os
from utils import FetchData, MetarExtender, MergeDataSets

dotenv.load_dotenv()

api_token = os.getenv("API_TOKEN")

#%%
start_date = "2022-06-01" # First Observation: 2022-06-01 
end_date = "2023-05-13" # Last Observation: 2023-05-13

fetcher = FetchData(api_token)

endpoints = [endpoint for endpoint in fetcher.ENDPOINTS if endpoint != "cat-62"]

# Uncomment to fetch data from API
##endpoints_data = {endpoint: fetcher.fetch_endpoint(endpoint, start_date, end_date) for endpoint in endpoints}
endpoints_data = {endpoint: pd.read_parquet(f"data/{endpoint}.parquet") for endpoint in endpoints}

# 'Troca de Cabeceira' (TC) is a runway change. For some reason, the API returns the runway code without the 'SB' prefix.
endpoints_data["tc-prev"]["aero"] = "SB" + endpoints_data["tc-prev"]["aero"]

endpoints_data["tc-real"]["aero"] = "SB" + endpoints_data["tc-real"]["aero"]

# TC-real has some useless columns
endpoints_data["tc-real"] = endpoints_data["tc-real"].drop(["nova_cabeceira", "antiga_cabeceira"], axis=1)
endpoints_data["tc-real"]["troca_real"] = 1

# The satellite data is returned in a different format than the other endpoints.
endpoints_data["satelite"] = endpoints_data["satelite"]\
    .rename(columns={"data": "hora"})\
    .drop("tamanho", axis=1)

endpoints_data["satelite"]["hora"] = pd.to_datetime(endpoints_data["satelite"]["hora"])

#%%
for key, value in endpoints_data.items():
    if key == "satelite":
        continue

    timestamp_column = "dt_dep" if key == "bimtra" else "hora"

    endpoints_data[key][timestamp_column] = pd.to_datetime(endpoints_data[key][timestamp_column], unit='ms')

#%%
merger = MergeDataSets(endpoints_data["bimtra"])\
    .merge_with_espera(endpoints_data["esperas"])\
    .merge_with_metaf(endpoints_data["metaf"])\
    .merge_with_metar(endpoints_data["metar"])\
    .merge_with_tc_prev(endpoints_data["tc-prev"])\
    .merge_with_tc_real(endpoints_data["tc-real"])\
    .merge_with_satelite(endpoints_data["satelite"])

final_df = merger.bimtra_df

final_df["troca_real"] = final_df["troca_real"].fillna(0)
# %%