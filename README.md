# Tuya Metrics Exporter

**A production-ready Prometheus metrics exporter for Tuya smart home devices, built with FastAPI and TinyTuya.**

## Overview

Tuya Metrics Exporter is a lightweight, high-performance service that bridges Tuya smart devices with Prometheus monitoring infrastructure. It connects to Tuya devices over your local network, collects real-time telemetry data, and exposes it in Prometheus-compatible format for monitoring, alerting, and visualization.

## Key Features

- 🔌 **Local Device Communication**: Direct local network communication with Tuya devices using TinyTuya - no cloud dependencies required
- 📊 **Prometheus Integration**: Native Prometheus metrics format with proper labeling and metadata
- ⚡ **High Performance**: Built on FastAPI with async/await support for efficient concurrent device polling
- 🏗️ **Modular Architecture**: Clean separation of concerns with device models, monitoring data models, and metrics collection layers
- 🔍 **Type Safety**: Fully typed Python codebase using Pydantic models for data validation
- 🐳 **Docker Ready**: Includes Dockerfile for easy containerized deployment
- 📈 **Comprehensive Metrics**: Tracks power consumption, current, voltage, switch states, and device health

## Supported Devices

Currently supports:
- **Smart Switches/Outlets**: Real-time monitoring of:
  - Switch state (on/off)
  - Current draw (amperes)
  - Power consumption (watts)
  - Voltage levels (volts)
  - Device-specific settings (overcharge protection, indicator lights, etc.)

The modular design makes it easy to extend support for additional Tuya device types.

## Requirements

- Python 3.12+
- uv (for dependency management)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd tuya_metrics_exporter

# Install dependencies with uv
uv sync
```

## Configuration

Configure your Tuya device credentials and settings in a configuration file or environment variables.

## Usage

```bash
# Run the exporter
uv run main.py
```

The server will start at `http://localhost:8000`

### Available Endpoints

- **`/ping`** - Simple ping endpoint, returns "pong"
- **`/health`** - Health check endpoint, returns service status
- **`/metrics`** - Prometheus metrics endpoint

## Architecture

The project follows a clean, modular architecture:

- **Device Layer** (`devices/`): Device-specific implementations for communicating with Tuya hardware
- **Models Layer** (`models/`): Pydantic data models for device definitions and monitoring data
- **Metrics Layer** (`metrics/`): Prometheus metric definitions and collection logic
- **API Layer** (`main.py`): FastAPI application with health checks and metrics endpoints
- **Worker Layer** (`worker/`): Background tasks for periodic device polling

## Use Cases

- 📊 Monitor power consumption of smart outlets and switches
- ⚡ Track energy usage patterns across your smart home
- 🚨 Set up alerts for abnormal power draw or device failures
- 📈 Integrate Tuya device metrics with existing Prometheus/Grafana stacks
- 🤖 Build automated energy management systems based on real-time telemetry

## Technology Stack

- **Python 3.12+**: Modern Python with type hints and async support
- **FastAPI**: High-performance async web framework
- **TinyTuya**: Local Tuya device communication library
- **Prometheus Client**: Official Prometheus Python client
- **Pydantic**: Data validation and settings management
- **Loguru**: Advanced logging with structured output
- **UV**: Fast, modern Python package manager

## License

MIT

