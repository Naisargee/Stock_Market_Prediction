#### Calculate Coreltion between diff global markets and display it ####
#### Calculate Coreltion between diff company and global markets and display it ####

from datafetch2 import *
from datetime import date



################################################ BSE WITH MARKETS,MCX,INR VALUE #####################################################################
print()
print()

print("Corelations : ")
print("BSE and CNX_Nifty : ",numpy.correlate(cnx_profit,bse_profit,"value")/len(cnx_profit))
print("BSE and NASDAQ : ",numpy.correlate(nasdaq_profit,bse_profit,"value")/len(nasdaq_profit))
print("BSE and Hang_Seng : ",numpy.correlate(hang_profit,bse_profit,"value")/len(hang_profit))
print("BSE and GDAXI : ",numpy.correlate(gdaxi_profit,bse_profit,"value")/len(gdaxi))
print("BSE and FTSE : ",numpy.correlate(ftse_profit,bse_profit,"value")/len(ftse))
print("BSE and AXJO : ",numpy.correlate(axjo_profit,bse_profit,"value")/len(axjo))
print("BSE and INR market vector : ",numpy.correlate(inr_profit,bse_profit,"value")/len(axjo))
print("BSE and MCX : ",numpy.correlate(mcx_profit,bse_profit[(mcx_date-base_date).days-1:],"value")/len(axjo))


################################################ TATASTEEL AND DIFF MARKES ##########################################################################

print()
print()


print("Corelations Of TATASTEEL : ")
print("TataSteel and CNX_Nifty : ",numpy.correlate(cnx_profit,tata_profit,"value")/len(cnx_profit))
print("TataSteel and BSE : ",numpy.correlate(bse_profit,tata_profit,"value")/len(bse_profit))
print("TataSteel and NASDAQ : ",numpy.correlate(nasdaq_profit,tata_profit,"value")/len(nasdaq_profit))
print("TataSteel and Hang_Seng : ",numpy.correlate(hang_profit,tata_profit,"value")/len(hang_profit))
print("TataSteel and GDAXI : ",numpy.correlate(gdaxi_profit,tata_profit,"value")/len(gdaxi))
print("TataSteel and FTSE : ",numpy.correlate(ftse_profit,tata_profit,"value")/len(ftse))
print("TataSteel and AXJO : ",numpy.correlate(axjo_profit,tata_profit,"value")/len(axjo))
#Volume=tata['Volume'].pct_change(peridos=1)
#print(len(tata_profit),len(tata['Volume_change']))
print("TataSteel and Volume : ",numpy.correlate(volume_change_tata,tata_profit)/len(tata_profit))




################################################# RELCAP AND DIFF MARKES ################################################################################
print()
print()

print("Corelations : ")
print("RelCapital and CNX_Nifty : ",numpy.correlate(cnx_profit,relcapital_profit,"value")/len(cnx_profit))
print("RelCapital and BSE : ",numpy.correlate(bse_profit,relcapital_profit,"value")/len(bse_profit))
print("RelCapital and NASDAQ : ",numpy.correlate(nasdaq_profit,relcapital_profit,"value")/len(nasdaq_profit))
print("RelCapital and Hang_Seng : ",numpy.correlate(hang_profit,relcapital_profit,"value")/len(hang_profit))
print("RelCapital and GDAXI : ",numpy.correlate(gdaxi_profit,relcapital_profit,"value")/len(gdaxi))
print("RelCapital and FTSE : ",numpy.correlate(ftse_profit,relcapital_profit,"value")/len(ftse))
print("RelCapital and AXJO : ",numpy.correlate(axjo_profit,relcapital_profit,"value")/len(axjo))


################################################## LICHFL AND DIFF MARKES ###############################################################################
print()
print()

print("Corelations : ")
print("LICHFL and CNX_Nifty : ",numpy.correlate(cnx_profit,lichfl_profit,"value")/len(cnx_profit))
print("LICHFL and BSE : ",numpy.correlate(bse_profit,lichfl_profit,"value")/len(bse_profit))
print("LICHFL and NASDAQ : ",numpy.correlate(nasdaq_profit,lichfl_profit,"value")/len(nasdaq_profit))
print("LICHFL and Hang_Seng : ",numpy.correlate(hang_profit,lichfl_profit,"value")/len(hang_profit))
print("LICHFL and GDAXI : ",numpy.correlate(gdaxi_profit,lichfl_profit,"value")/len(gdaxi))
print("LICHFL and FTSE : ",numpy.correlate(ftse_profit,lichfl_profit,"value")/len(ftse))
print("LICHFL and AXJO : ",numpy.correlate(axjo_profit,lichfl_profit,"value")/len(axjo))


