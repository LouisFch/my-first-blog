from django.shortcuts import render
from machinesql.models import param, three
import pyodbc

def connsql(request):
    conn=pyodbc.connect('DRIVER={SQL Server};SERVER=BRAVE-SQLSERVER;DATABASE=LifeTestSeriesDB;UID=webuser;PWD=Django_123!')
    cursor=conn.cursor()
    cursor.execute("select MachineID, MachineName, Running from Machines")
    result=cursor.fetchall()
    return render(request,'index.html',{'param':result})

def cosql(request):
    con=pyodbc.connect('DRIVER={SQL Server};SERVER=BRAVE-SQLSERVER;DATABASE=HSTRSeriesDB;UID=webuser;PWD=Django_123!')
    cursor=con.cursor()
    cursor.execute("select MachineID, MachineName, Running from Machines")
    result=cursor.fetchall()
    return render(request,'three.html',{'param':result})
'''
def consql(request):  
    conn=pyodbc.connect('DRIVER={SQL Server};SERVER=BRAVE-SQLSERVER;UID=webuser;PWD=Django_123!')
    cur = conn.cursor()
    query1 = 'select * from [LifeTestSeriesDB].[dbo].[Machines]'
    query2 = 'select * from [HSTRSeriesDB].[dbo].[Machines]'
    cur.execute(query1)
    result=cur.fetchall()
    return render(request,'index.html',{'param':result})
    cur.execute(query2)
    result=cur.fetchall()
    return render(request,'index.html',{'param':result})   
    '''