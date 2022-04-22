from datetime import datetime
from concurrent import futures

import pandas as pd
from pandas import DataFrame
import pandas_datareader.data as web
import os
def download_stock(stock):
	""" try to query the iex for a stock, if failed note with print """
	cache = False
	if os.path.exists('./data/'+stock+'_data.csv') and cache: 
		return 
	try:
		print(stock)
		stock_df = web.DataReader(stock,'yahoo', start_time, now_time)
		stock_df['Name'] = stock
		output_name = './data/' + stock + '_data.csv'
		stock_df.to_csv(output_name)
	except:
		bad_names.append(stock)
		print('bad: %s' % (stock))

if __name__ == '__main__':

	""" set the download window """
	now_time = datetime.now()
	start_time = datetime(now_time.year - 1, now_time.month , now_time.day)

	""" list of s_anp_p companies """
	s_and_p = ['MMM','AOS','ABT','ABBV','ABMD','ACN','ATVI','ADM','ADBE','ADP','AAP','AES','AFL','A','AIG','APD','AKAM','ALK',
	'ALB','ARE','ALGN','ALLE','LNT','ALL','GOOGL','GOOG','MO','AMZN','AMCR','AMD','AEE','AAL','AEP','AXP','AMT','AWK','AMP','ABC',
	'AME','AMGN','APH','ADI','ANSS','ANTM','AON','APA','AAPL','AMAT','APTV','ANET','AIZ','T','ATO','ADSK','AZO','AVB','AVY','BKR',
	'BLL','BAC','BBWI','BAX','BDX','WRB','BRK-B','BBY','BIO','TECH','BIIB','BLK','BK','BA','BKNG','BWA','BXP','BSX','BMY','AVGO','BR',
	'BRO','BF-B','CHRW','CDNS','CZR','CPT','CPB','COF','CAH','KMX','CCL','CARR','CTLT','CAT','CBRE','CDW','CE','CNC','CNP','CDAY','CERN',
	'CF','CRL','SCHW','CHTR','CVX','CMG','CB','CHD','CI','CINF','CTAS','CSCO','C','CFG','CTXS','CLX','CME','CMS','KO','CTSH','CL','CMCSA',
	'CMA','CAG','COP','ED','STZ','CEG','COO','CPRT','GLW','CTVA','COST','CTRA','CCI','CSX','CMI','CVS','DHI','DHR','DRI','DVA','DE','DAL',
	'XRAY','DVN','DXCM','FANG','DLR','DFS','DISH','DIS','DG','DLTR','D','DPZ','DOV','DOW','DTE','DUK','DRE','DD','DXC','EMN','ETN','EBAY',
	'ECL','EIX','EW','EA','EMR','ENPH','ETR','EOG','EPAM','EFX','EQIX','EQR','ESS','EL','ETSY','RE','EVRG','ES','EXC','EXPE','EXPD','EXR',
	'XOM','FFIV','FDS','FAST','FRT','FDX','FITB','FRC','FE','FIS','FISV','FLT','FMC','F','FTNT','FTV','FBHS','FOXA','FOX','BEN','FCX','AJG',
	'GRMN','IT','GE','GNRC','GD','GIS','GPC','GILD','GL','GPN','GM','GS','GWW','HAL','HIG','HAS','HCA','PEAK','HSIC','HSY','HES','HPE','HLT',
	'HOLX','HD','HON','HRL','HST','HWM','HPQ','HUM','HII','HBAN','IEX','IDXX','ITW','ILMN','INCY','IR','INTC','ICE','IBM','IP','IPG','IFF','INTU',
	'ISRG','IVZ','IPGP','IQV','IRM','JBHT','JKHY','J','JNJ','JCI','JPM','JNPR','K','KEY','KEYS','KMB','KIM','KMI','KLAC','KHC','KR','LHX','LH','LRCX',
	'LW','LVS','LDOS','LEN','LLY','LNC','LIN','LYV','LKQ','LMT','L','LOW','LUMN','LYB','MTB','MRO','MPC','MKTX','MAR','MMC','MLM','MAS','MA','MTCH',
	'MKC','MCD','MCK','MDT','MRK','FB','MET','MTD','MGM','MCHP','MU','MSFT','MAA','MRNA','MHK','MOH','TAP','MDLZ','MPWR','MNST','MCO','MS','MOS','MSI',
	'MSCI','NDAQ','NTAP','NFLX','NWL','NEM','NWSA','NWS','NEE','NLSN','NKE','NI','NDSN','NSC','NTRS','NOC','NLOK','NCLH','NRG','NUE','NVDA','NVR','NXPI',
	'ORLY','OXY','ODFL','OMC','OKE','ORCL','OGN','OTIS','PCAR','PKG','PARA','PH','PAYX','PAYC','PYPL','PENN','PNR','PEP','PKI','PFE','PM','PSX','PNW',
	'PXD','PNC','POOL','PPG','PPL','PFG','PG','PGR','PLD','PRU','PEG','PTC','PSA','PHM','PVH','QRVO','PWR','QCOM','DGX','RL','RJF','RTX','O','REG',
	'REGN','RF','RSG','RMD','RHI','ROK','ROL','ROP','ROST','RCL','SPGI','CRM','SBAC','SLB','STX','SEE','SRE','NOW','SHW','SBNY','SPG','SWKS','SJM',
	'SNA','SEDG','SO','LUV','SWK','SBUX','STT','STE','SYK','SIVB','SYF','SNPS','SYY','TMUS','TROW','TTWO','TPR','TGT','TEL','TDY','TFX','TER','TSLA',
	'TXN','TXT','TMO','TJX','TSCO','TT','TDG','TRV','TRMB','TFC','TWTR','TYL','TSN','USB','UDR','ULTA','UAA','UA','UNP','UAL','UNH','UPS','URI','UHS',
	'VLO','VTR','VRSN','VRSK','VZ','VRTX','VFC','VTRS','V','VNO','VMC','WAB','WMT', 'WBA','WBD','WM','WAT','WEC','WFC','WELL','WST','WDC','WRK','WY','WHR',
	'WMB','WTW','WYNN','XEL','XYL','YUM','ZBRA','ZBH','ZION','ZTS']
		
	bad_names =[] #to keep track of failed queries

	"""here we use the concurrent.futures module's ThreadPoolExecutor
		to speed up the downloads buy doing them in parallel 
		as opposed to sequentially """

	#set the maximum thread number
	max_workers = 50

	workers = min(max_workers, len(s_and_p)) #in case a smaller number of stocks than threads was passed in
	with futures.ThreadPoolExecutor(workers) as executor:
		res = executor.map(download_stock, s_and_p)

	
	""" Save failed queries to a text file to retry """
	if len(bad_names) > 0:
		with open('failed_queries.txt','w') as outfile:
			for name in bad_names:
				outfile.write(name+'\n')

	df = pd.DataFrame(pd.read_csv('./data/MMM_data.csv')['Date'])
	for ticker in s_and_p:
		sub = pd.read_csv('./data/' +ticker+'_data.csv')[['Date', 'Close']]
		sub = sub.set_axis(['Date', ticker], axis=1, inplace=False)
		df = df.merge(sub, on='Date', how='left')

	# df = df.set_axis(s_and_p, axis=1, inplace=False)
	df.to_csv('sp500_data.csv', index=False)
