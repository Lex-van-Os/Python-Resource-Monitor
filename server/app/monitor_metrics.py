import typing
from typing import List
from dataclasses import dataclass

@dataclass
class MonitorMetrics():
    timestamp: str
    processes: int
    cpu_usage: float
    memory_usage: int

    def from_dict(self, monitor_metrics: dict):
        self.timestamp = monitor_metrics["timestamp"]
        self.processes = monitor_metrics["processes"]
        self.cpu_usage = monitor_metrics["cpuUsage"]
        self.memory_usage = monitor_metrics["memoryUsage"]

        return self
