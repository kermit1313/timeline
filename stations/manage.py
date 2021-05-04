from collections import OrderedDict
import click
import dateutil.parser as dateparser
import pandas as pd
import plotly.express as px
from openpyxl import load_workbook

from stations.domain.calculations import Calculations
from stations.domain.retriever import Retriever, Retriever2
from stations.helpers import sort_by_order, sort_by_station, sort_by_order_time


@click.group()
def tool():
    pass


@tool.command()
@click.option("--filename", "-f", required=True)
@click.option("--sheetname", "-s", required=True)
@click.option("--start-date-time", "-sdt", required=True)
@click.option("--sort", is_flag=True)
def calculate(filename, sheetname, start_date_time, sort=False):
    start_date_time = dateparser.parse(start_date_time)

    wb = load_workbook(filename=filename)
    ws = wb[sheetname]

    if sort:
        retrevier = Retriever2(ws)
    else:
        retrevier = Retriever(ws)
    a = retrevier.retrive_groups_stations()
    groups = a.groups
    stations = a.stations

    # sort stations by order
    for index, station in stations.items():
        if sort:
            station = sort_by_order_time(station)
        else:
            station = sort_by_order(station)
        stations[index] = station

    if sort:
        order_stations = OrderedDict()
        indexes = list(stations.keys())
        indexes.sort()

        max_station_index = 0
        for index in indexes:
            value = stations[index]
            if len(value)-1 > max_station_index:
                max_station_index = len(value)-1
            order_stations[index] = value

        stations = order_stations

    # sort groups by order
    for index, group in groups.items():
        if sort:
            group = sort_by_order_time(group)
        else:
            group = sort_by_order(group)
        groups[index] = group

    calculation = Calculations()
    to_display = calculation.calculate(groups, stations, start_date_time, sort)

    to_display = sort_by_station(to_display)
    df = pd.DataFrame(to_display)

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Station", color="Resource", text="Text")
    fig.update_yaxes()
    fig.show()


if __name__ == "__main__":
    tool()
