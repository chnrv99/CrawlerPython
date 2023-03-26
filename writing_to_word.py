import docx
import pandas as pd


mydoc = docx.Document()
# for drug shop
website_title = 'aaaaaa'
website_link = 'bbbbbbbbbb'
url='http://k6m3fagp4w4wspmdt23fldnwrmknse74gmxosswvaxf3ciasficpenad.onion/'
dfs = pd.read_html(url)
# print(df)
for df in dfs:
    # print(i)
    # print(str(df.values))
    li = [df.columns.values.tolist()] + df.values.tolist()
    for i,j in l1:
        mydoc.add_paragraph(i + " " + j)

    
mydoc.save('/home/user/Desktop/Crawler/classified.docx')

    


