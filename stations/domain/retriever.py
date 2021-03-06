import collections
from typing import List

from stations.domain.task import Task

Task_pair = collections.namedtuple("Task_pair", "time resource")


class Retriever:
    def __init__(self, workbook):
        self._workbook = workbook

    def retrive_groups_stations(self):
        groups = {}
        stations = {}
        for column in self._workbook.iter_cols(values_only=True):
            self._fetch_data_from_column(column, groups, stations)

        Groups_stations = collections.namedtuple("Groups_stations", "groups stations")
        return Groups_stations(groups=groups, stations=stations)

    def _fetch_data_from_column(self, column, groups, stations):
        column_length = len(column)
        p = int(column_length / 2)
        times, tasks = column[:p], column[p + 1 : column_length]
        paired_tasks = self._pair_task_and_time(times, tasks)

        for task_pair in paired_tasks:
            if self._is_pair_filled(task_pair):
                task = Task(task_pair.time, task_pair.resource)
                self._add_task(task, groups, task.index)
                self._add_task(task, stations, task.station_symbol)

    def _pair_task_and_time(self, times, tasks) -> List[Task_pair]:
        print(len(times))
        return [Task_pair(times[i], tasks[i]) for i in range(0, len(times))]

    def _is_pair_filled(self, pair: Task_pair):
        return pair.time and pair.resource

    def _add_task(self, task: Task, add_to, index):
        try:
            add_to[index].append(task)
        except KeyError:
            add_to[index] = [task]
