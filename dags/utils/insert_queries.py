from utils.file_util import cargar_datos

# city insertion
def insert_query_city(**kwargs):
    
    insert = f"INSERT INTO city (City_Key,City,State_Province,Country,Continent,Sales_Territory,Region,Subregion,Latest_Recorded_Population) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.City_Key},\'{row.City}\',\'{row.State_Province}\',\'{row.Country}\',\'{row.Continent}\',\'{row.Sales_Territory}\',\'{row.Region}\',\'{row.Subregion}\',{row.Latest_Recorded_Population});\n"
    return insertQuery

# customer insertion
def insert_query_customer(**kwargs):
    
    insert = f"INSERT INTO customer (Customer_Key,Customer,Bill_To_Customer,Category,Buying_Group,Primary_Contact,Postal_Code) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.Customer_Key},\'{row.Customer}\',\'{row.Bill_To_Customer}\',\'{row.Category}\',\'{row.Buying_Group}\',\'{row.Primary_Contact}\',{row.Postal_Code});\n"
    return insertQuery


# date insertion
def insert_query_date(**kwargs):
    # To Do
    insert = f"INSERT INTO date_table (Date_key,Day_Number,Day_val,Month_val,Short_Month,Calendar_Month_Number,Calendar_Year,Fiscal_Month_Number,Fiscal_Year) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"(\'{row.Date_key}\',{row.Day_Number},{row.Day_val},\'{row.Month_val}\',\'{row.Short_Month}\',{row.Calendar_Month_Number},{row.Calendar_Year},{row.Fiscal_Month_Number},{row.Fiscal_Year});\n"
    return insertQuery


# employee insertion
def insert_query_employee(**kwargs):
    insert = f"INSERT INTO employee (Employee_Key,Employee,Preferred_Name,Is_Salesperson) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.Employee_Key},\'{row.Employee}\',\'{row.Preferred_Name}\',{row.Is_Salesperson});\n"
    return insertQuery


# stock item insertion
def insert_query_stock(**kwargs):
    # To Do
    insert = f"INSERT INTO stockitem (Stock_Item_Key,Stock_Item,Color,Selling_Package,Buying_Package,Brand,Size_val,Lead_Time_Days,Quantity_Per_Outer,Is_Chiller_Stock,Tax_Rate,Unit_Price,Recommended_Retail_Price,Typical_Weight_Per_Unit) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.Stock_Item_Key},\'{row.Stock_Item}\',\'{row.Color}\',\'{row.Selling_Package}\',\'{row.Buying_Package}\',\'{row.Brand}\',\'{row.Size_val}\',{row.Lead_Time_Days},{row.Quantity_Per_Outer},{row.Is_Chiller_Stock},{row.Tax_Rate},{row.Unit_Price},{row.Recommended_Retail_Price},{row.Typical_Weight_Per_Unit});\n"
    return insertQuery

    
# fact order insert
def insert_query_fact_order(**kwargs):
    # To Do
    insert = f"INSERT INTO fact_order (order_key,city_key,customer_key,stock_item_key,order_date_key,picked_date_key,salesperson_key,picker_key,package,quantity,unit_price,tax_rate,total_excluding_tax,tax_amount,total_including_tax) VALUES "
    insertQuery = ""
    dataframe =cargar_datos(kwargs['csv_path'])
    for index, row in dataframe.iterrows():
        insertQuery += insert + f"({row.order_key},{row.city_key},{row.customer_key},{row.stock_item_key},\'{row.order_date_key}\',\'{row.picked_date_key}\',{row.salesperson_key},{row.picker_key},\'{row.package}\',{row.quantity},{row.unit_price},{row.tax_rate},{row.total_excluding_tax},{row.tax_amount},{row.total_including_tax});\n"
    return insertQuery

