import logging
import os
import pandas as pd
import sys

#Store in log file
def createlogger():
    dir_path = './autolog/'
    filename = 'autocheck.log'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    logging.basicConfig(level=logging.INFO)
    logging.captureWarnings(True)               #Capture python warnings
    logger = logging.getLogger()
    formatter = logging.Formatter(
        '%(asctime)s, %(filename)s, %(name)s, %(levelname)s, %(message)s' ,
        datefmt= '%Y-%m-%d %H:%M:%S'
    )
    fh = logging.FileHandler(dir_path + filename)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

#Store in DB, 0 : FAIL, 1 : SUCCESS, 2 : PENDING
def recordLog(unique_id, record_status, message, mycursor, connection):
    sql_log = '''UPDATE log_file SET status=%s, message=%s
    WHERE unique_id=%s;
    '''
    check = [record_status, message, unique_id]
    mycursor.execute(sql_log, tuple(check))
    connection.commit()

def initialLog(calling_file, record_status, year, semester, mycursor, connection):
    calling_file = calling_file.split('/')[-1]
    sql_log = '''INSERT INTO log_file (calling_file, status, year, semester)
        VALUES (%s,%s,%s,%s);
        '''
    check = [calling_file, record_status, year, semester]
    mycursor.execute(sql_log, tuple(check))
    connection.commit()
    return mycursor.lastrowid

def convertExcelToCsv(input_path, output_path):
    # enter 1 for converting others
    # enter 2 for converting offset file
    convert_type = input("輸入1來轉換其他資料，輸入2來轉換抵免資料：")
    df = None
    if convert_type == '1':
        check_column = '當期課號'
        df_varify = pd.read_excel(input_path)
        df_key = list(df_varify.keys())
        if check_column in df_key:
            df = pd.read_excel(input_path, dtype={'學號': object, '當期課號': object})
        else:
            df = pd.read_excel(input_path, dtype={'學號': object})
    elif convert_type == '2':
        df = pd.read_excel(input_path, encoding = 'utf-8', dtype = {'學號':object, '原修課學年度':object, '原修課學期':object, '原修課當期課號':object})
    else:
        print("錯誤。請輸入1或2")
    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    """./upload/106B、106暑期資訊學院全體學生修課成績資料-資工學院-20181022.xlsx"""
    """./original/on_cos_data_test.csv"""
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convertExcelToCsv(input_path, output_path)