from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

# Create your views here.
def list_view(request):
    conn = MySQLdb.connect(
        user="nakazawalab",
        password="hogehoge",
        host="localhost",
        db="app_data"
    )

    # カーソルの取得
    cur = conn.cursor()

    # SQL実行
    # selfIntroductionテーブルから全レコード取り出す
    sql = "SELECT * from users"
    cur.execute(sql)

    # 実行結果の取得
    rows = cur.fetchall()
    cur.close
    conn.close

    return render(request, 'homepage.html',context={'data':rows})
