from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import prettytable

def index(request):
    return render(request, "index.html")

def chart(request):
    return render(request, "charts.html")

def devtool(request):
    query_sql = ""
    query_result = None
    if action == "/query":
        query_sql = request.POST["query_sql"]
        if not query_sql.lower().startswith("select"):
            query_result = "You only can do SELECT query!"
        else:
            conn = sqlite3.connect(settings.DB_PATH)
            c = conn.cursor()
            try:
                c.execute(str(query_sql))
                result = PrettyTable()
                for result_item in c.fetchall():
                    result.add_row(result_item)
                query_result = result.get_string()
            except sqlite3.OperationalError as e:
                query_result = e.message
            except sqlite3.IntegrityError as e:
                query_result = e.message
            except sqlite3.DatabaseError as e:
                query_result = e.message
            except:
                query_result = "Unknown Error."
            conn.close()
    return render(request, "devtool.html", {
        "devtool_active": "active",
        "query_result": query_result,
        "query_sql": query_sql,
    })
