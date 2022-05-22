

import akshare as ak
import pandas as pd

"""
获取行业名单《东方财富-行业板块》（接口: stock_board_industry_name_em）
货物行业成份股《东方财富-成份股》（接口: stock_board_industry_cons_em）
"""

data = pd.DataFrame(columns=['板块名称','代码','名称','ROE','自由现金流','营业收益率','税后净利润'])

stock_board_industry_name_em_df = ak.stock_board_industry_name_em() #获取行业名单
for index,row in stock_board_industry_name_em_df.iterrows():
    #print(row["板块名称"])
    stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol=row["板块名称"]) #获取行业成份股
    for subindex,subrow in stock_board_industry_cons_em_df.iterrows():
        #print(subrow["名称"])
        stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol=subrow["代码"]) #获取股票基本面
        #为四大基本面指标赋值
        ROE = stock_financial_analysis_indicator_df.iloc[0,:]["净资产收益率(%)"]
        FCF = stock_financial_analysis_indicator_df.iloc[0,:]["每股经营性现金流(元)"]
        OPE = stock_financial_analysis_indicator_df.iloc[0,:]["主营业务利润率(%)"]
        SM = stock_financial_analysis_indicator_df.iloc[0,:]["销售净利率(%)"]
        #将数据append到字典中
        data = data.append({'板块名称':row["板块名称"],'代码':subrow["代码"],'名称':subrow["名称"],'ROE':ROE,'自由现金流':FCF,'营业收益率':OPE,'税后净利润':SM}, ignore_index=True)

print(data)

#输出excel
data.to_excel("./six_indicators.xls", index=False)




