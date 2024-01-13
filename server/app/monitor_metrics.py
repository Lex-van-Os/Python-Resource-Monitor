import typing
from typing import List

class MonitorMetrics():
    def __init__(self, timestamp: str, processes: int, cpu_usage: float, memory_usage: int) -> None:
        self.timestamp = timestamp
        self.processes = processes
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage

    def from_dict(self, monitor_metrics: dict):
        self.timestamp = monitor_metrics["timestamp"]
        self.processes = monitor_metrics["processes"]
        self.cpu_usage = monitor_metrics["cpuUsage"]
        self.memory_usage = monitor_metrics["memoryUsage"]

        return self
