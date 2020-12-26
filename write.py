import xlsxwriter
import pandas as pd

name = [
"Smith",
"John",
"Prayuth",
"Prawit",]

last_name = [
"Doe",
"Doe",
"Janocha",
"Wongsuwan"
]

df = pd.DataFrame({
    'Name': name,
    'Last Name': last_name,
})
df.index = range(1,len(df)+1)

writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="page 1")
writer.save()