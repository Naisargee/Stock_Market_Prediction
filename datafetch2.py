#### Featches data from downloaded CSV FIle And Save it into Data Frame ####
#### Also calculates % return on Adj_Close and profit ( up (1) and down(-1) of the day) ####



import csv
import numpy
import pandas
from datetime import date

base_date=date(2009,1,1)
end_date=date(2014,12,31)

## filename : csv file from where data is loaded remove_starting: remove few start data so that all stock fall in same range ##
def createDataFrame(filename,remove_starting):
	ans=pandas.DataFrame.from_csv("CSVs/"+filename)
	ans=ans.rename(columns= {'Adj Close':'AdjClose'})
	ans=ans.resample('D',how='mean')
	ans=ans.fillna(method='pad')
	ans['Return'] = ans['AdjClose'].pct_change(periods=1)
	ans['Volume_change']=ans['Volume'].pct_change(periods=1)
	ans['Profit']=numpy.where(ans['Return']>0,1,-1)
	ans=ans.ix[remove_starting:]
	return ans

tata=createDataFrame('tata.csv',2)					# yahoo_finance id : TATASTEEL6.BO
relcapital=createDataFrame('relcapital.csv',2)		# yahoo_finance id : RELCAPITAL.BO
lichfl=createDataFrame('lichfl.csv',2)				# yahoo_finance id : LICHSFIN.NS
nasdaq=createDataFrame('nasdaq.csv',1)				# yahoo_finance id : ^IXIC
hang_seng=createDataFrame('hang_seng.csv',1)		# yahoo_finance id : ^HSI
gdaxi=createDataFrame('gdaxi.csv',0)				# yahoo_finance id : ^GDAXI
ftse=createDataFrame('ftse.csv',2)					# yahoo_finance id : ^FTSE
axjo=createDataFrame('axjo.csv',1)					# yahoo_finance id : ^AXJO
bse=createDataFrame('bse.csv',1)					# yahoo_finance id : ^BSESN
cnx_nifty=createDataFrame('cnx_nifty.csv',2)		# yahoo_finance id : ^NSEI
inr=createDataFrame('inr.csv',1)					# yahoo_finance id : MarketVectors INR/USD ETN
mcx=createDataFrame('mcx.csv',1)					# yahoo_finance id : MCX.NS


mcx_date=date(2012,3,9)


