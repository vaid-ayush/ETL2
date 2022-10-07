import pandas as pd
import zipfile


def zipToDataframe():
    try:
        df = pd.read_table('01-decommercialresponsive_2021-01-05.tsv.gz', sep='\t', compression='gzip')
        df.columns = ['date_time', 'post_event_list',  'post_product_list',
                                 'post_page_event', 'page_url', 'exclude_hit']
        df = df.astype({"post_event_list": str})
        r_df = df[df['post_event_list'].str.contains("20113")]
        r_df_2 = r_df.filter(['post_event_list' , 'post_product_list'], axis=1)

# filtering data based on 20113 and dealerID and AdID
#         with open('out.txt', 'w') as f:
#             print(r_df_2.to_string(index= False), file=f)
        col_list = r_df_2["post_product_list"].values.tolist()
        res_list = []
        for val in col_list:
            val2 = val.split(",")
            for val3 in val2:
                val4 = val3.split(";")
                dealerID = val4[0]
                headID = val4[1]
                count = 1
                res_list.append([dealerID, headID, count])
        col = ["DealerID", "AdID", "Count"]
        result_1 = pd.DataFrame(res_list, columns = col)
        data = result_1.groupby(["DealerID", "AdID"]).Count.sum().reset_index()
        print(data)
        return True

    except FileNotFoundError:
        print("The file was not found")
        return False


zipToDataframe()
