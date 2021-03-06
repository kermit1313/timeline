import click
import dateutil.parser as dateparser
import pandas as pd
import plotly.express as px
from openpyxl import load_workbook

from stations.domain.calculations import Calculations
from stations.domain.retriever import Retriever
from stations.helpers import sort_by_order, sort_by_station


@click.group()
def tool():
    pass


@tool.command()
@click.option("--filename", "-f", required=True)
@click.option("--sheetname", "-s", required=True)
@click.option("--start-date-time", "-sdt", required=True)
def calculate(filename, sheetname, start_date_time):
    start_date_time = dateparser.parse(start_date_time)

    wb = load_workbook(filename=filename)
    ws = wb[sheetname]

    retrevier = Retriever(ws)
    a = retrevier.retrive_groups_stations()
    groups = a.groups
    stations = a.stations

    # sort stations by order
    for index, station in stations.items():
        station = sort_by_order(station)
        stations[index] = station

    # sort groups by order
    for index, group in groups.items():
        group = sort_by_order(group)
        groups[index] = group

    calculation = Calculations()
    to_display = calculation.calculate(groups, stations, start_date_time)

    to_display = sort_by_station(to_display)
    df = pd.DataFrame(to_display)

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Station", color="Resource")
    fig.update_yaxes()
    fig.show()


if __name__ == "__main__":
    tool()
