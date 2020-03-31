from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import prettytable
import json
from charts import *

def index(request):
    return render(request, "index.html")

def chart(request):
    new_chart_dataset = ChartDataset(
        '# of Votes',
        [12, 19, 3, 5, 2, 3],
        [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ]
    )
    new_chart_option = ChartOptions(False)
    new_chart = Chart()
    new_chart.add_dataset(new_chart_dataset.export())
    new_chart.set_labels(["A", "B", "C", "D", "E", "F"])
    new_chart.update_options(new_chart_option.export())

    return render(request, "charts.html", {
        "chart_json": json.dumps(new_chart.export())
    })

def devtool(request, action):
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
