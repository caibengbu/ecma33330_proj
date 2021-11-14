from .download_cps import download_cps
from .blsdata_retrieve import retrieve_bls
from .match_extract import extract_all
from .match_merge import match_all
from .match_flow import flow_all
from .match_sa import seasonal_adjust
from .three_state import three_state
from .draw_plots import plot_all
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", required=True,help="starting month, format: YYYYDD, e.g. 201201")
    parser.add_argument("--end", required=True,help="ending month, format: YYYYDD, e.g. 201201")
    parser.add_argument("--dir", required=False,help="The unit of speed used for exported statistics. (ms/kmh/mph)")
    args = parser.parse_args()
    START_DATE = args.start
    END_DATE = args.end

    if args.dir is None:
        DIR = "."
    else:
        DIR = args.dir
    
    download_cps(START_DATE,END_DATE,DIR)
    retrieve_bls(START_DATE,END_DATE,DIR)
    extract_all(START_DATE,END_DATE,DIR)
    match_all(START_DATE,END_DATE,DIR)
    
    df = flow_all(START_DATE,END_DATE,DIR)
    df_sa = seasonal_adjust(df)

    three_state(df_sa,DIR)
    plot_all(START_DATE,END_DATE,DIR)



    