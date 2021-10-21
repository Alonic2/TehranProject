import pytse_client as tse
import shutil
import pandas as pd
import fire
import warnings
warnings.filterwarnings("ignore",category=UserWarning)

def Stock(ID,Start,End):

    Start_year = int(str(Start)[6:10])
    Start_month = int(str(Start)[3:5])
    Start_day = int(str(Start)[0:2])

    End_year = int(str(End)[6:10])
    End_month = int(str(End)[3:5])
    End_day = int(str(End)[0:2])
    tse.download(symbols=str(ID), write_to_csv=True)


    Data = pd.read_csv(f"./tickers_data/{ID}.csv")
    Data2 = Data[Data.date.astype(str).str[0:4].astype(int)>Start_year]
    DataM1 = Data[Data.date.astype(str).str[0:4].astype(int)==Start_year]
    DataS = Data[Data.date.astype(str).str[0:4].astype(int)==Start_year]
    DataSS = DataS[DataS.date.astype(str).str[5:7].astype(int)==Start_month]
    Data0 = DataSS[DataS.date.astype(str).str[8:10].astype(int)>=Start_day]
    Data1 = DataM1[DataM1.date.astype(str).str[5:7].astype(int)>Start_month]
    Data2 = Data2[Data2.date.astype(str).str[0:4].astype(int)<End_year]
    DataFm1 = Data[Data.date.astype(str).str[0:4].astype(int) == End_year]
    Data3 = DataFm1[DataFm1.date.astype(str).str[5:7].astype(int) < End_month]
    DataFs1 = DataFm1[DataFm1.date.astype(str).str[5:7].astype(int) == End_month]
    Data4 = DataFs1[DataFs1.date.astype(str).str[8:10].astype(int) <= End_day]

    DataT = pd.concat([Data0,Data1,Data2,Data3,Data4])

    DataT.to_csv(f"{ID}.csv")
    shutil.rmtree("tickers_data")

if __name__ == '__main__':
    fire.Fire()