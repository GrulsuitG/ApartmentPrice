from curses import beep
import pymysql
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()


class mysqlDB:

    def __init__(self):
        self.conn = pymysql.connect(
            user='root',
            passwd='hjbrain97',
            host='localhost',
            db='test',
            charset='utf8')
        self.cursor = self.conn.cursor()
        print("connection")

    def DBcontact(self, sql):

        self.cursor.execute(sql)
        self.rows = self.cursor.fetchall()
        data = pd.read_sql_query(sql, self.conn)

        return data

    def InsertDataFrame(self, data, table_name):

        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                               .format(user="root",
                                       pw="hjbrain97",
                                       db="test"))
        self.co = engine.connect()
        data.to_sql(name="zscoredata_market", con=engine,
                    if_exists='append', index=False)
        self.co.close()

    def makeguColumn(self):
        sql = """SELECT doro
                FROM dataset1; 
            """
        data = self.DBcontact(sql)
        data = data['doro'].str.split(" ", 2, expand=True)[1]
        data = pd.DataFrame(data)
        data.columns = ["gu"]
        data_gu = data.drop_duplicates(['gu'])
        # self.InsertDataFrame(data_gu)

        return data_gu

    def makeZ_score_market(self):
        data = self.makeguColumn()

        for j in range(len(data)):
            for i in range(0, 5):
                try:
                    sql = """SELECT areadaprice, market, school, station, bank, cafe, hospital, amenitiesCnt , doro
                            FROM dataset1 
                            WHERE doro like "%{0}%" AND market = {1};
                        """

                    sql = sql.format(data['gu'].iloc[j], i)
                    # print(sql)
                    self.DBcontact(sql)
                    df = pd.DataFrame(self.rows, columns=[
                                    'areadaprice', 'market', 'school', 'station', 'bank', 'cafe', 'hospital', 'amenitiesCnt', 'doro'])
                    df_data = df['areadaprice']
                    mean = np.mean(df_data)
                    std = np.std(df_data)
                    if len(df_data) == 0: continue
                    z_score = [(y-mean)/std for y in df_data]
                    z_score = [x for x in z_score if x<-1.0]
                    if len(z_score) == 0: continue
                    df_z = pd.DataFrame(z_score)
                    df_z.columns = ['zscore_market']
                    df = pd.concat([df, df_z], join = 'inner', axis=1)
                    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                                        .format(user="root",
                                                pw="hjbrain97",
                                                db="test"))
                    self.co = engine.connect()
                    df.to_sql(name="zdata_market", con=engine, if_exists='append', index=False)
                    self.co.close()
                    
                except ZeroDivisionError:
                    continue

                

    def makeZ_score_hospital(self):
        data = self.makeguColumn()
        for j in range(len(data)):
            for i in range(10, 31):
                try:
                    sql = """SELECT areadaprice, market, school, station, bank, cafe, hospital, amenitiesCnt , doro
                            FROM dataset1 
                            WHERE doro like "%{0}%" AND hospital = {1};
                        """

                    sql = sql.format(data['gu'].iloc[j], i)
                    # print(sql)
                    self.DBcontact(sql)
                    df = pd.DataFrame(self.rows, columns=[
                                    'areadaprice', 'market', 'school', 'station', 'bank', 'cafe', 'hospital', 'amenitiesCnt', 'doro'])
                    df_data = df['areadaprice']
                    
                    mean = np.mean(df_data)
                    std = np.std(df_data)
                    if len(df_data) == 0: continue
                    z_score = [(y-mean)/std for y in df_data]
                    z_score = [x for x in z_score if x<-1.0]
                    if len(z_score) == 0: continue
                    df_z = pd.DataFrame(z_score)
                    df_z.columns = ['zscore_hospital']
                    df = pd.concat([df, df_z], join = 'inner', axis=1)
                    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                                        .format(user="root",
                                                pw="hjbrain97",
                                                db="test"))
                    self.co = engine.connect()
                    df.to_sql(name="zdata_hospital", con=engine, if_exists='append', index=False)
                    self.co.close()
                except ZeroDivisionError:
                    continue

    def makeZ_score_amenitiesCnt(self):
        data = self.makeguColumn()
        for j in range(len(data)):
            for i in range(0, 5):
                try:
                    sql = """SELECT areadaprice, market, school, station, bank, cafe, hospital, amenitiesCnt , doro
                            FROM dataset1 
                            WHERE doro like "%{0}%" AND amenitiesCnt = {1};
                        """

                    sql = sql.format(data['gu'].iloc[j], i)
                    # print(sql)
                    self.DBcontact(sql)
                    df = pd.DataFrame(self.rows, columns=[
                                    'areadaprice', 'market', 'school', 'station', 'bank', 'cafe', 'hospital', 'amenitiesCnt', 'doro'])
                    df_data = df['areadaprice']
                    mean = np.mean(df_data)
                    std = np.std(df_data)
                    if len(df_data) == 0: continue
                    z_score = [(y-mean)/std for y in df_data]
                    z_score = [x for x in z_score if x<-1.0]
                    if len(z_score) == 0: continue
                    df_z = pd.DataFrame(z_score)
                    print(df_z)
                    df_z.columns = ['zscore_amen']
                    df = pd.concat([df, df_z], join = 'inner', axis=1)
                    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                                        .format(user="root",
                                                pw="hjbrain97",
                                                db="test"))
                    self.co = engine.connect()
                    df.to_sql(name="zdata_amen", con=engine, if_exists='append', index=False)
                    self.co.close()
                except ZeroDivisionError:
                    continue

    def getUnderhouse(self):
        sql = """SELECT doro
                FROM zdata_amen, zdata_hospital, zdata_market;
        
              """

        self.cursor.execute(sql)
        self.rows = self.cursor.fetchall()
        # columns=['areadaprice', 'market', 'school', 'bank','cafe', 'hospital', 'amenitiesCnt']
        df = pd.DataFrame(self.rows, columns=[
                          'areadaprice', 'market', 'school', 'station', 'bank', 'cafe', 'hospital', 'amenitiesCnt', 'doro'])
        print(df)
        data = df['areadaprice']
        mean = np.mean(data)
        std = np.std(data)

        z_score = [(y-mean)/std for y in data]
        df_z = pd.DataFrame(z_score)
        df_z.columns = ['z_score']
        df_all = pd.concat([df, df_z], axis=1)

        return df_all

    # def insertHouseInfo(self):


if __name__ == '__main__':

    a = mysqlDB()
    a.makeZ_score_amenitiesCnt()
    a.makeZ_score_hospital()
    a.makeZ_score_market()
