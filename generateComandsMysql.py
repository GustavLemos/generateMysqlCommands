import os

#questions 
def index_questions(index):
    if index == "database":
        global database_name
        database_name = input('\n\tWhat is the name of the database?\t')
    if index == "table":
        global table_name
        table_name = input('\n\tWhat is the name of the table?\t')
    elif index == "column":
        global column_name
        column_name = input('\n\tWhat is the name of the table column?\t')
    elif index == "column_2":
        global column_name_2          
        column_name_2 = input('\n\tWhat is the name of the table Second column?\t')
    elif index == "type":
        global var_type, _type, limited_char
        var_type =input('\n\tWhat type of data?\n\t1 - Char(Characters);\n\t2 - Int(Whole);\n\t3 - Float;\n\t4 - Date;\n\t5 - Blob(Files);\n\t6 - Double(Long Numbers).\n\nNumber: ')
        
        if var_type=="1":
            _type = "VARCHAR"
            limited_char = input('\n\tWhat will be the character limit? Ex.: 50\t')
        elif var_type=="2":
            _type = "INT"
        elif var_type=="3":
            _type = "FLOAT"
        elif var_type=="4":
            _type = "DATE"
        elif var_type=="5":
            _type = "BLOB"
        elif var_type=="6":
            _type = "DOUBLE"
    elif index == "value":
        global value
        value = input('\n\tWhat is the name of value?\t')        
    elif index == "value_2":
        global value_2
        value_2 = input('\n\tWhat is the name of Second value?\t')
    elif index == "operation":
        global var_operation
        var_operation =input('\n\tWhat operation of data?\n\t1 - = ;\n\t2 - > ;\n\t3 - < ;\n\t4 - >= ;\n\t5 - <= .\n\nNumber: ')
        


#functions of comands for mysql 
def one():
    return "\tSHOW DATABASES;\n"
 
def two():
    return "\tSHOW TABLES;\n"
 
def three():
    index_questions("table")
    return "\tDESCRIBE + {input_text};\n".format(input_text=table_name)
 
def four():
    index_questions("database")
    return "\tCREATE DATABASE + {input_text};\n".format(input_text=database_name)
 
def five():
    index_questions("table")
    index_questions("column")
    index_questions("type")
    if var_type=="1":
        return "\tCREATE TABLE {input_Text_1}( {input_Text_2} {input_Text_3}({input_Text_4}));\n".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=_type,input_Text_4=limited_char)    
    else:
        return "\tCREATE TABLE {input_Text_1}( {input_Text_2} {input_Text_3});\n".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=_type)
 
def six():
    index_questions("table")
    index_questions("column")
    return "\tSELECT * FROM {input_Text_1} WHERE {input_Text_2};".format(input_Text_1=table_name,input_Text_2=column_name)
 
def seven():
    index_questions("table")
    index_questions("column")
    index_questions("value")

    if type(value) is int:
        index_questions('operation')

        if var_operation=="1":
            _operation = "="
        elif var_operation=="2":
            _operation = ">"
        elif var_operation=="3":
            _operation = "<"
        elif var_operation=="4":
            _operation = ">="
        elif var_operation=="5":
            _operation = "<="
        return "\tSELECT * FROM {input_Text_1} WHERE {input_Text_2} {input_Text_3} {input_Text_4};".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=_operation,input_Text_4=value)   
    elif type(value) is str:
        return "\tSELECT * FROM {input_Text_1} WHERE {input_Text_2} like '%{input_Text_3}%'; ".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=value)
 
def eight():
    index_questions('table')
    return "\tSELECT * FROM {input_Text_1};".format(input_Text_1=table_name)
 
def nine():
    index_questions("table")
    index_questions("column")
    index_questions('value')
    return "\tINSERT INTO {input_Text_1}({input_Text_2})( '{input_Text_3}');".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=value)
 
def ten():
    index_questions("table")
    index_questions("column")
    index_questions('value')
    index_questions("column_2")
    index_questions("value_2")
    return "\tINSERT INTO {input_Text_1}({input_Text_2}), '{input_Text_3}'( '{input_Text_4}', '{input_Text_5}');".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=column_name_2,input_Text_4=value,input_Text_5=value_2)
 
def eleven():
    index_questions("table")
    index_questions("column")
    index_questions('value')
    return "\tDELETE FROM {input_Text_1} WHERE {input_Text_2}='{input_Text_3}';".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=value)
 
def twelve():
    index_questions("table")
    index_questions("column")
    index_questions('value')
    index_questions('value_2')
    return "\tUPDATE {input_Text_1} SET {input_Text_2} = '{input_Text_3}' WHERE '{input_Text_2}' =''{input_Text_4}' ';".format(input_Text_1=table_name,input_Text_2=column_name,input_Text_3=value,input_Text_4=value_2)

def thirteen():
    return "Thanks!"
 
#switchCases 
def cases(option):
    if option=="1":
        print("\nmysql> " + one())
    elif option=="2":
        print("\nmysql> " + two())
    elif option=="3":
        print("\nmysql> " + three())
    elif option=="4":
        print("\nmysql> " + four())
    elif option=="5":
        print("\nmysql> " + five())
    elif option=="6":
        print("\nmysql> " + six())
    elif option=="7":
        print("\nmysql> " + seven())
    elif option=="8":
        print("\nmysql> " + eight())                        
    elif option=="9":
        print("\nmysql> " + nine())
    elif option=="10":
        print("\nmysql> " + ten())
    elif option=="11":
        print("\nmysql> " + eleven())
    elif option=="12":
        print("\nmysql> " + twelve())
    elif option=="13":
        thirteen()                

# main
input_option = input

#loop
while input_option!="13":
    # introduction Text
    print("\t\t\t BEM VINDO AO GERADOR DE COMANDOS MYSQL\n\n")

    # options + input
    input_option = input('Choose the number of the MySQL command to be generated:\n\nSHOW:\t\t 1- Show DataBases;\n\t\t 2- Show Tables;\n\t\t 3- Show Configuration Table\n\nCREATE:\n\t\t 4-Create DataBase;\n\t\t 5-Create Tables in DataBase and Your Columns;\n\nCONSULT:\n\t\t 6- Query Specific Column;\n\t\t 7- Query Specific Data in a Column;\n\t\t 8- List All Tables in Data;\n\nINSERT:\n\t\t 9 - Insert Data Into a Column of a Table;\n\t\t 10 - Insert Various Data in Columns of a Table;\n\nDELETE:\n\t\t 11 - Delete Record From a Table;\n\nUPDATE:\n\t\t 12 - Update a Table Record.\n\n13-EXIT\n\n\nYour Option: ')
    cases(input_option)
    os.system("PAUSE")