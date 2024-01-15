from uuid import uuid4
from influxdb_client import Point
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
from influxdb_client.client.write_api import ASYNCHRONOUS
from monitor_metrics import MonitorMetrics
import logging
import asyncio
from datetime import datetime, timedelta


class MonitorInfluxClient():
    logger = logging.getLogger(__name__)

    def __init__(self, influx_url, influx_token, influx_org, influx_bucket):
        self.influx_url = influx_url
        self.influx_token = influx_token
        self.influx_org = influx_org
        self.influx_bucket = influx_bucket
        self.client = None

    async def initialize(self):
        self.client = InfluxDBClientAsync(
            url=self.influx_url, token=self.influx_token, org=self.influx_org, debug=False)

    async def close(self):
        if self.client is not None:
            await self.client.__aexit__(None, None, None)

    async def reset_data(self):
        if self.client is None:
            raise Exception(
                "Client is not initialized. Call initialize() method first.")

        start = datetime.now() - timedelta(days=30)
        stop = datetime.now()

        await self.client.delete_api().delete(
            predicate='_measurement="monitor_metric"',
            bucket=self.influx_bucket,
            start=start,
            stop=stop,
            org=None,
        )

    async def write_monitor_metrics(self, monitor_metrics: MonitorMetrics, user_uid: str):
        if self.client is None:
            raise Exception(
                "Client is not initialized. Call initialize() method first.")

        metrics_point = Point("monitor_metric").tag(
            "device_id", user_uid).field("timestamp", monitor_metrics.timestamp).field("processes", monitor_metrics.processes).field(
            "cpu_usage", monitor_metrics.cpu_usage).field("memory_usage", monitor_metrics.memory_usage)

        try:
            await self.client.write_api().write(
                bucket=self.influx_bucket,
                record=metrics_point,
                record_measurement_name="monitor_metric",
                record_tag_keys=["device_id"],
                record_field_keys=["timestamp", "processes",
                                   "cpu_usage", "memory_usage"],
                record_time_key="timestamp",
            )
        except Exception as e:
            self.logger.error(f"Write operation failed: {e}")
