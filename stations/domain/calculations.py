from typing import Dict


class Calculations:
    def calculate(self, groups: dict, stations: Dict, start_date_time, sort):
        to_display = []
        if not sort:
            group_start_time = start_date_time
            for index, group in groups.items():
                start = group_start_time
            
                for task in group:
                    if not self._is_first_task_in_group(task):
                        station = stations[task.station_symbol]
                        previous_task = self._get_previous_task_in_station(task, station)
            
                        if previous_task and previous_task.end_date_time and previous_task.end_date_time > start:
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
                            Text=task.resource,
                        )
                    )
        else:
            start = start_date_time
            not_finished = True

            for index, station in stations.items():
                group_start = start
                for task in station:
                    task.set_times(group_start)
                    group_start = task.end_date_time
            while not_finished:
                not_finished = False
                for index, group in groups.items():
                    task_start = None
                    for task in group:
                        task_station = stations[task.station_symbol]
                        if task.order == 1:
                            task_start = task.end_date_time
                            continue
                        if task.start_date_time < task_start:
                            task.set_times(task_start)
                            self.move_tasks_in_station(task, task_station)
                            not_finished = True
                        task_start = task.end_date_time

                
                for index, station in stations.items():
                    for task in station:
                        prev = self._get_previous_task_in_station(task, station)
                        if prev:
                            if prev.end_date_time > task.start_date_time:
                                task.set_times(prev.end_date_time)
                                not_finished = True

            for index, station in stations.items():
                for task in station:
                        
                    to_display.append(
                    dict(
                        Name=task.resource,
                        Station=f"S{task.station_symbol}",
                        Start=task.start_date_time,
                        Finish=task.end_date_time,
                        Resource=task.index,
                        Station_symbol=task.station_symbol,
                        Text=task.resource,
                        )
                    )
        return to_display

    def _is_first_task_in_group(self, task):
        return task.order == 1

    def _get_previous_task_in_station(self, task, station):
        task_index_in_station = station.index(task)
        previous_task_in_station = station[task_index_in_station - 1]
        if (task_index_in_station) <= 0:
            return None
        previous_task_in_station = station[task_index_in_station - 1]
        return previous_task_in_station

    def move_tasks_in_station(self, task, station):
        task_index_in_station = station.index(task)
        task_start = task.end_date_time

        for x in range(task_index_in_station+1, len(station)-1):
            print(task)
            station_task = station[x]
            print(station_task)
            if station_task.start_date_time < task_start:
                station_task.set_times(task_start)
            task_start = station_task.end_date_time
        
    def set_times(self, task, task_start, to_display):
        task.set_times(task_start)

        to_display.append(
            dict(
                Name=task.resource,
                Station=f"S{task.station_symbol}",
                Start=task.start_date_time,
                Finish=task.end_date_time,
                Resource=task.index,
                Station_symbol=task.station_symbol,
                # Text=task.resource,
            )
        )