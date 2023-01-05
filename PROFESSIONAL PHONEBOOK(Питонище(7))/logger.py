from datetime import datetime as dt
import csv
import controller
import contacts as con

def make_logs():
    with("operations.csv", 'a') as logs:#пока не проблема(потом когда пропишу опозновательные номера операций надо сделать так чтобы они писались в логах)
        writer = csv.writer(logs)
        writer.writerow(dt.now().strftime('%H:%M'))
        writer.writerow(controller.num_choice)
        writer.writerow(format([con.name , con.surname , con.phone]))