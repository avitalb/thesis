import pandas as pd 

def final_merge(geocoded,ethn,new_name):

    df1 = pd.read_csv(geocoded)
    df2 = pd.read_csv(ethn)

    final_df = pd.merge(df1,df2[["est_ethnicity",'StateVoterID']],on='StateVoterID', how='outer')
    final_df.to_csv(new_name)

if __name__ == '__main__':
    geocoded_2017 = "results/2017_vouchers_voter_file_merged_geocoded.csv"
    added_ethnicity_2017 = "results/2017_vouchers_voter_file_ethnicity.csv"
    geocoded_2019 = "results/2019_vouchers_voter_file_merged_geocoded.csv"
    added_ethnicity_2019 = "results/2019_vouchers_voter_file_ethnicity.csv"

    final_2019_name = "results/2019_vouchers_voter_file_all_cols.csv"
    final_2017_name = "results/2017_vouchers_voter_file_all_cols.csv"

    final_merge(geocoded_2019,added_ethnicity_2019,final_2019_name)
    final_merge(geocoded_2017,added_ethnicity_2017,final_2017_name)

    final_merge("results/2019_cash_merged_geocoded.csv","results/2019_cash_ethnicity.csv","results/2019_cash_all_cols.csv")
    final_merge("results/2017_cash_merged_geocoded.csv","results/2017_cash_ethnicity.csv","results/2017_cash_all_cols.csv")
