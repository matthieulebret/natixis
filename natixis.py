import streamlit as st

import altair as alt
import plotly.express as px

import numpy as np
import pandas as pd
import datetime
import xlrd

from datetime import datetime
from dateutil.relativedelta import relativedelta

import html2text

import json
import lxml

# from st_aggrid import AgGrid


st.set_page_config('Natixis deals',layout='wide')

st.title('Natixis project finance deals')

### Infralogic data

# maxidf = pd.DataFrame()
#
# for i in [str(1),str(2),str(3)]:
#     file = 'transactions_'+i+'.json'
#     with open(file,encoding='utf-8') as data_file:
#         data = json.load(data_file)
#     nbdeals = len(data['transactions'])
#
#     id = [data['transactions'][i]['details']['id'] if not None else 'N/A' for i in range(nbdeals)]
#     name = [data['transactions'][i]['details']['name'] if not None else 'N/A' for i in range(nbdeals)]
#     region = [data['transactions'][i]['details']['regions'][0] if not None else 'N/A' for i in range(nbdeals)]
#     sector = [data['transactions'][i]['details']['sectors'][0] if not None else 'N/A' for i in range(nbdeals)]
#     currency = [data['transactions'][i]['details']['currency'] if not None else 'N/A' for i in range(nbdeals)]
#     fundings = [data['transactions'][i]['details']['fundings'] if not None else 'N/A' for i in range(nbdeals)]
#     countries = [data['transactions'][i]['details']['countries'][0]['name'] if not None else 'N/A' for i in range(nbdeals)]
#     states = [data['transactions'][i]['details']['countries'][0]['states'] if not None else 'N/A' for i in range(nbdeals)]
#     subsectors = [data['transactions'][i]['details']['subSectors'][0] if not None else 'N/A' for i in range(nbdeals)]
#     description = [data['transactions'][i]['details']['description'] if not None else 'N/A' for i in range(nbdeals)]
#     ratios = [data['transactions'][i]['details']['financeRatios'] if not None else 'N/A' for i in range(nbdeals)]
#     dominantregion = [data['transactions'][i]['details']['dominantRegion'] if not None else 'N/A' for i in range(nbdeals)]
#     dominantsector = [data['transactions'][i]['details']['dominantSector'] if not None else 'N/A' for i in range(nbdeals)]
#     dominantcountry = [data['transactions'][i]['details']['dominantCountry'] if not None else 'N/A' for i in range(nbdeals)]
#     transactiontype = [data['transactions'][i]['details']['transactionType'] if not None else 'N/A' for i in range(nbdeals)]
#     dominantsubsector = [data['transactions'][i]['details']['dominantSubSector'] if not None else 'N/A' for i in range(nbdeals)]
#     transactionstatus = [data['transactions'][i]['details']['transactionLifecycle']['transactionStatus'] if not None else 'N/A' for i in range(nbdeals)]
#     transactioncharacteristicsPPP = [data['transactions'][i]['details']['transactionCharacteristics']['PPP'] if not None else 'N/A' for i in range(nbdeals)]
#     transactioncharacteristicsutility = [data['transactions'][i]['details']['transactionCharacteristics']['utility'] if not None else 'N/A' for i in range(nbdeals)]
#
#
#     dealdict = {'id':id,'Name':name,'region':region,'sector':sector,'currency':currency,'fundings':fundings,'countries':countries,'states':states,'subsectors':subsectors,
#         'description':description,'ratios':ratios,'dominantRegion':dominantregion,'dominantsector':dominantsector,'dominantcountry':dominantcountry,
#         'transactiontype':transactiontype,'dominantsubsector':dominantsubsector,'transactionstatus':transactionstatus,
#         'PPP':transactioncharacteristicsPPP,'Utility':transactioncharacteristicsutility}
#
#     dealdf = pd.DataFrame(dealdict)
#
#     # df.to_excel('natixis_deals.xlsx')
#
#     name = []
#     type = []
#     tenor = []
#     amount = []
#     role = []
#     lenders = []
#     dateadded = []
#     allocation = []
#     estimatedAlloc = []
#     estimatedAllocUSD = []
#
#     ratings = []
#     retired = []
#     borrower = []
#     comments = []
#     monoline = []
#     debtclass = []
#     margininfo = []
#     marginvalue = []
#     facilitytype = []
#     maturity = []
#     lifecyclepoint = []
#     amountusd = []
#
#
#     for transaction in data['transactions']:
#         for tranche in transaction['details']['fundings']:
#             try:
#                 for lender in tranche['lenders']:
#                     try:
#                         name.append(transaction['details']['name'])
#                     except:
#                         name.append(None)
#                     try:
#                         type.append(tranche['type'])
#                     except:
#                         type.append(None)
#                     try:
#                         tenor.append(tranche['tenor'])
#                     except:
#                         tenor.append(None)
#                     try:
#                         amount.append(tranche['amount'])
#                     except:
#                         amount.append(None)
#                     try:
#                         role.append(lender['role'])
#                     except:
#                         role.append(None)
#                     try:
#                         lenders.append(lender['lender']['name'])
#                     except:
#                         lenders.append(None)
#                     try:
#                         dateadded.append(lender['dateAdded'])
#                     except:
#                         dateadded.append(None)
#                     try:
#                         allocation.append(lender['allocation'])
#                     except:
#                         allocation.append(None)
#                     try:
#                         estimatedAlloc.append(lender['estimatedAllocation'])
#                     except:
#                         estimatedAlloc.append(None)
#                     try:
#                         estimatedAllocUSD.append(lender['estimatedAllocationUSD'])
#                     except:
#                         estimatedAllocUSD.append(None)
#                     try:
#                         ratings.append(tranche['ratings'])
#                     except:
#                         ratings.append(None)
#                     try:
#                         borrower.append(tranche['borrower'])
#                     except:
#                         borrower.append(None)
#                     try:
#                         comments.append(tranche['comments'])
#                     except:
#                         comments.append(None)
#                     try:
#                         monoline.append(tranche['monoline'])
#                     except:
#                         monoline.append(None)
#                     try:
#                         debtclass.append(tranche['debtClass'])
#                     except:
#                         debtclass.append(None)
#                     try:
#                         margininfo.append(tranche['marginInfo'])
#                     except:
#                         margininfo.append(None)
#                     try:
#                         marginvalue.append(tranche['marginValue'])
#                     except:
#                         marginvalue.append(None)
#                     try:
#                         facilitytype.append(tranche['facilityType'])
#                     except:
#                         facilitytype.append(None)
#                     try:
#                         maturity.append(tranche['maturityDate'])
#                     except:
#                         maturity.append(None)
#                     try:
#                         lifecyclepoint.append(tranche['lifeCyclePoint'])
#                     except:
#                         lifecyclepoint.append(None)
#                     try:
#                         amountusd.append(tranche['amountUSD'])
#                     except:
#                         amountusd.append(None)
#             except:
#                 pass
#
#     ticketdf = pd.DataFrame([name,type,tenor,amount,role,lenders,dateadded,allocation,estimatedAlloc, estimatedAllocUSD,ratings,retired,borrower,comments,monoline,debtclass,margininfo,marginvalue,facilitytype,maturity,lifecyclepoint,amountusd]).transpose()
#     ticketdf.columns = ['Name','Type','Tenor','Amount','Role','Lender','Date added','Allocation','Estimated Allocation','Estimated Allocation USD','Ratings','Retired','Borrower','Comments','Monoline','Debt Class','Margin info','Margin value','Facility type','Maturity','Life cycle point','Amount USD']
#
#
#     bigdf = pd.merge(dealdf,ticketdf,on='Name')
#     bigdf.drop('fundings',axis=1,inplace=True)
#
#     maxidf = pd.concat([maxidf,bigdf])
#
# bigdf = maxidf
#
# bigdf.to_excel('natixis_deals.xlsx')

##################### File obtained #############################

# st.stop()

##################### File obtained #############################

def getyear(string,dateadd):
    if string[-1]==')':
        string = string[-5:-1]
    else:
        string = string[-4:]
    try:
        string = int(string)
    except:
        string = dateadd.year
    return string

def getfx(a,b):
    if b == 0:
        return 0
    else:
        return a/b


@st.cache(suppress_st_warning=True)
def getdata():
    df = pd.read_excel('natixis_deals.xlsx').iloc[:,1:]
    df['Date added'] = pd.to_datetime(df['Date added'],errors='coerce')
    df['Year'] = df.apply(lambda x:getyear(x['Name'],x['Date added']),axis=1)
    df=df[df['transactionstatus']=='Financial Close']
    df['Allocation'] = pd.to_numeric(df['Allocation'],errors='coerce')
    df['Allocation'] = df['Allocation'].fillna(0)
    df['Estimated Allocation'] = pd.to_numeric(df['Estimated Allocation'],errors='coerce')
    df['Estimated Allocation'] = df['Estimated Allocation'].fillna(0)
    df['Estimated Allocation USD'] = pd.to_numeric(df['Estimated Allocation USD'],errors='coerce')
    df['Estimated Allocation USD'] = df['Estimated Allocation USD'].fillna(0)
    df['Alloc Cur'] = df[['Allocation','Estimated Allocation']].max(axis=1)
    df['Amount'] = pd.to_numeric(df['Amount'],errors='coerce')
    df['Amount'] = df['Amount'].fillna(0)
    df['Amount USD'] = pd.to_numeric(df['Amount USD'],errors='coerce')
    df['Amount USD'] = df['Amount USD'].fillna(0)
    df['Fx'] = df.apply(lambda x: getfx(x['Amount'],x['Amount USD']),axis=1)
    df['Alloc in USD theo'] = df.apply(lambda x:getfx(x['Alloc Cur'],x['Fx']),axis=1)
    df['Ticket USD'] = df[['Estimated Allocation USD','Alloc in USD theo']].max(axis=1)

    return df

df = getdata()


minyear = int(df['Year'].min())
maxyear = int(df['Year'].max())
regions = df['dominantRegion'].unique().tolist()
sectors = df['sector'].unique().tolist()
sectors.insert(0,'All')


yearselect = st.slider('Select period',minyear,maxyear,(2017,maxyear))
df = df[(df['Year']>=yearselect[0])&(df['Year']<=yearselect[1])]

natixis = df[df['Lender'].str.contains('Natixis')]

with st.expander('Show data'):
    natixis

selectlist = ["region, countries, sector, subsectors , Name","sector, subsectors, region, countries, Name","sector, region, countries, subsectors, Name","region, sector, countries, subsectors, Name"]
treechoice = st.selectbox('Select Treemap',selectlist)

if treechoice == selectlist[0]:
    order = ['region','countries','sector','subsectors','Name']
elif treechoice == selectlist[1]:
    order = ['sector','subsectors','region','countries','Name']
elif treechoice == selectlist[2]:
    order = ['sector','region','countries','subsectors','Name']
elif treechoice == selectlist[3]:
    order = ['region','sector','countries','subsectors','Name']

fig = px.treemap(natixis,path=order,values='Ticket USD',color='region')
st.plotly_chart(fig)

deallist = df['Name'].unique().tolist()
lenderlist = []
for deal in deallist:
    dealdf = df[df['Name']==deal]
    nblenders = len(dealdf[dealdf['Ticket USD']>0])
    lenderlist.append(nblenders)

nblendDF = pd.DataFrame({'Name':deallist,'Nb lenders':lenderlist})

df = pd.merge(df,nblendDF,on='Name')
# df = df[df['Nb lenders']>1]

regions.insert(0,'All')
selectregion = st.selectbox('Select a region',regions)

if selectregion != 'All':
    df = df[df['region']==selectregion]

regions = regions[1:]

def topticket(Natixis,Biggest):
    if Natixis == Biggest:
        return 1
    else:
        return 0

def isclub(maxtick,mintick):
    if maxtick==mintick:
        return 1
    else:
        return 0


sectors = sectors[1:]
sectors.sort()

for sector in sectors:
    try:
        sectordf = df[(df['sector']==sector)]
        # output = sectordf.groupby('Lender')['Ticket USD'].mean()
        output = pd.pivot_table(sectordf,values='Ticket USD',index='Lender',columns='Name',aggfunc='sum',)
            # st.write('Number of deals with NLB biggest ticket: ',str(len(output.columns)))

        maxticket = pd.DataFrame(output.max(axis=0))
        maxticket.reset_index(inplace=True)
        maxticket.columns = ['Name','Max ticket']

        minticket = pd.DataFrame(output.min(axis=0))
        minticket.reset_index(inplace=True)
        minticket.columns = ['Name','Min ticket']

        natixis = natixis[['Name','Ticket USD']]
        natixis = pd.DataFrame(natixis.groupby('Name').sum())

        natixis.reset_index(inplace=True)

        maxticket = pd.merge(natixis,maxticket,on='Name')
        maxticket = pd.merge(maxticket,minticket,on='Name')

        maxticket.columns = ['Name','Natixis ticket USDm','Max ticket USDm','Min ticket USDm']

        st.subheader(sector)

        maxticket['Top ticket'] = maxticket.apply(lambda x: topticket(x['Natixis ticket USDm'],x['Max ticket USDm']),axis=1)
        maxticket['Is club deal'] = maxticket.apply(lambda x: isclub(x['Max ticket USDm'],x['Min ticket USDm']),axis=1)

        nbdeals = len(output.columns)
        clubs = maxticket['Is club deal'].sum()
        syndic = nbdeals - clubs
        toptickets = maxticket['Top ticket'].sum()
        topticsynd = maxticket[(maxticket['Top ticket']==1)&(maxticket['Is club deal']==0)]['Top ticket'].sum()

        st.metric('Number of deals:',nbdeals)
        col1,col2,col3 = st.columns(3)
        with col1:
            st.metric('Number of clubs:',clubs)
        with col2:
            st.metric('Number of synd deals:',syndic)
        with col3:
            st.metric('Number of top tickets in syndic deals:',topticsynd)
        # st.write('Number of deals: ',str(len(output.columns)))
        # st.write('Number of top tickets: ',str(maxticket['Top ticket'].sum()))

        col4,col5,col6 = st.columns(3)
        with col4:
            st.metric('Natixis max ticket:','{:,.2f} USDm'.format(maxticket['Natixis ticket USDm'].max()))
        with col5:
            st.metric('Natixis average ticket:','{:,.2f} USDm'.format(maxticket['Natixis ticket USDm'].mean()))
        with col6:
            st.metric('Natixis mean ticket:','{:,.2f} USDm'.format(maxticket['Natixis ticket USDm'].median()))

        over50 = len(maxticket[maxticket['Natixis ticket USDm']>50])
        over75 = len(maxticket[maxticket['Natixis ticket USDm']>75])
        over100 = len(maxticket[maxticket['Natixis ticket USDm']>100])

        col7,col8,col9 = st.columns(3)
        with col7:
            st.metric('Nb tickets > 50mUSD:',over50)
        with col8:
            st.metric('Nb tickets > 75mUSD:',over75)
        with col9:
            st.metric('Nb tickets > 100mUSD:',over100)

        st.write(maxticket)

        with st.expander('Show detail by deal'):
            output
    except:
        pass

with st.form('my_form'):
    regionselect = st.multiselect('Select regions',regions,['Australasia','Asia'])
    sectorselect = st.selectbox('Select sector',sectors,0)
    st.form_submit_button('Submit')

if sectorselect != 'All':
    df = df[df['sector']==sectorselect]

df = df[df['dominantRegion'].isin(regionselect)]

st.subheader('Partner banks')
banks = pd.DataFrame(df['Lender'].value_counts()/df['Lender'].value_counts().max())
st.write(banks['Lender'].iloc[1:])
