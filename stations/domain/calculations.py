from typing import Dict


class Calculations:
    def calculate(self, groups: dict, stations: Dict, start_date_time):
        to_display = []
        group_start_time = start_date_time

        for index, group in groups.items():
            start = group_start_time
        
            for task in group:
                if not self._is_first_task_in_group(task):
                    station = stations[task.station_symbol]
                    previous_task = self._get_previous_task_in_station(task, station)
        
                    if previous_task.end_date_time and previous_task.end_date_time > start:
                        start = previous_task.end_date_time
        
                task.set_times(start)
                start = task.end_date_time
        
                if task.order == 1:
                    group_start_time = task.end_date_time

                to_display.append(
                    dict(
                        Name=task.resource,
                        Station=f"S{task.station_symbol}",
                        Start=task.start_date_time,
                        Finish=task.end_date_time,
                        Resource=task.index,
                        Station_symbol=task.station_symbol,
                    )
                )
        return to_display

    def _is_first_task_in_group(self, task):
        return task.order == 1

    def _get_previous_task_in_station(self, task, station):
        task_index_in_station = station.index(task)
        previous_task_in_station = station[task_index_in_station - 1]
        return previous_task_in_station
