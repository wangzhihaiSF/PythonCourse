import openpyxl # 引用第三方库

wb = openpyxl.Workbook() # 创建工作簿
sheet = wb.active # 创建工作表
sheet.title = "春节档票房"
sheet["A1"] = "电影名"
sheet["B1"] = "票房(万)"
# 写入一行数据
row1 = ["流浪地球", "264429.42"]
row2 = ["疯狂的外星人", "164436.82"]
sheet.append(row1)
sheet.append(row2)

wb.save("电影票房.xlsx")