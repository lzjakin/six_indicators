
"""
六大指标选股

指标1： 近五年ROE平均>15%；
ROE(股東權益報酬率) = 稅後淨利 / 股東權益
簡單說就是公司利用股東資金來賺錢的能力。 

指标2： 近五年每股自由現金流平均>0元 
每股自由現金流 = 自由現金流 / 公司發行在外流通股數
自由現金流代表公司在支付必要支出後所剩餘可以自由使用的錢，觀察此指標可以判斷公司的用錢能力 

指标3： 近五年營業利益率平均>10%
營業利益率 = 營業利益 / 營收
此項指標可以判斷公司是否依靠本業賺錢，可以補足僅看ROE指標的不足處。因為ROE指標的分子為稅後淨利，是包含公司業外損益的結果，因此當公司業外損益過高都會有所影響。 
除了希望公司主要依靠本業賺錢，也希望本業利潤夠高，因此將營業利益率設定為10%。 

指标4：近一年營業現金流對稅後淨利比平均>50%
如字面意思此指標 = 營業現金流 / 稅後淨利 
稅後淨利是扣除一切成本後的預估損益；而營業現金流則代表實際依靠營業收付現金的情況。因此若實際收到的錢(營業現金流)小於稅後淨利，這個時候就必須小心避開，或進一步實際觀察公司財報。 

指标5：現在董監持股比率>10%
我們會希望公司董事、監察人與股東站在同一條船上，所以當公司高層持有越多股票，代表與股東的利益越一致，公司經營不善的風險也會降低。
有些大型公司可能會另立其他投資公司的方式持股，整體來說持股還是高過10%，但這些股份不會顯示為董監事持有，這時此指標就會把這些公司篩選掉。 

指标6：現在董監質押比率<10%
質押就是以股票做為抵押品借錢。若質押比率高，可能代表董監事缺錢，或著借錢投資(不務正業)等，長期來說還是會擔心動公司歪腦筋。 


"""


import akshare as ak
import pandas as pd

"""
获取行业名单《东方财富-行业板块》（接口: stock_board_industry_name_em）
货物行业成份股《东方财富-成份股》（接口: stock_board_industry_cons_em）
"""

#data = pd.DataFrame(columns=['板块名称','代码','名称','ROE','自由现金流','营业收益率','税后净利润','股东持股比例','股东质押比率'])
data = pd.DataFrame(columns=['板块名称','代码','名称','ROE','自由现金流','营业收益率','税后净利润'])

stock_board_industry_name_em_df = ak.stock_board_industry_name_em()

for index,row in stock_board_industry_name_em_df.iterrows():
    print(row["板块名称"])
    print("---1--")
    #
    stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol=row["板块名称"])
    #stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol="有色金属")#test
    #print(stock_board_industry_cons_em_df)#test

    for subindex,subrow in stock_board_industry_cons_em_df.iterrows():
        #
        print(subrow["名称"])
        print("---2--")
        #
        stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol=subrow["代码"])
        #stock_financial_analysis_indicator_df = ak.stock_financial_analysis_indicator(symbol="000612")#test
        #print(stock_financial_analysis_indicator_df)#test
        
        #
        print(stock_financial_analysis_indicator_df)
        print("--3---")
        
        ROE = stock_financial_analysis_indicator_df.iloc[0,:]["净资产收益率(%)"]
        FCF = stock_financial_analysis_indicator_df.iloc[0,:]["每股经营性现金流(元)"]
        OPE = stock_financial_analysis_indicator_df.iloc[0,:]["主营业务利润率(%)"]
        SM = stock_financial_analysis_indicator_df.iloc[0,:]["销售净利率(%)"]
        print("--4---")
        
        #print(stock_financial_analysis_indicator_df)
        #

        #for index,row in stock_financial_analysis_indicator_df.iterrows():
        #    print(row['日期'],row['净资产收益率(%)'],row['每股经营性现金流(元)'])
    #

        #data = data.append({'板块名称':row["板块名称"],'代码':subrow["代码"],'名称':subrow["名称"]}, ignore_index=True)
        #data = data.append({'板块名称':row["板块名称"],'代码':subrow["代码"],'名称':subrow["名称"],'ROE':ROE,'自由现金流':FCF,'营业收益率':OPE,'税后净利润':SM,'股东持股比例','股东质押比率'}, ignore_index=True)
        data = data.append({'板块名称':row["板块名称"],'代码':subrow["代码"],'名称':subrow["名称"],'ROE':ROE,'自由现金流':FCF,'营业收益率':OPE,'税后净利润':SM}, ignore_index=True)
        print("--5---")
#

print(data)

#输出excel
data.to_excel("./six_indicators.xls", index=False)




