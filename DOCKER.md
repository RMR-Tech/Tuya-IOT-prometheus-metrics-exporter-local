# Docker Setup Guide

## Quick Start with Docker Compose

### Prerequisites

1. Create the config directory on your host system:
```bash
sudo mkdir -p /data/tuya_exporter
```

2. Create your device configuration file:
```bash
sudo nano /data/tuya_exporter/device_config.py
```

Example configuration (copy from `example/device_config.py`):
```python
from models.device.config.base import BaseDeviceConfig

SOCKET_PLUG_DEVICES: list[BaseDeviceConfig] = [
    # Add your device configurations here
]
```

3. Set proper permissions:
```bash
sudo chown -R 1000:1000 /data/tuya_exporter
```

### Running with Docker Compose

```bash
# Build and start the service
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down

# Rebuild after code changes
docker-compose up -d --build
```

### Running with Docker (without compose)

```bash
# Build the image
docker build -t tuya-metrics-exporter .

# Run the container with volume mount
docker run -d \
  --name tuya-metrics-exporter \
  -p 8000:8000 \
  -v /data/tuya_exporter:/app/config \
  --restart unless-stopped \
  tuya-metrics-exporter
```

## Endpoints

Once running, the following endpoints are available:

- **Health Check**: http://localhost:8000/health
- **Ping**: http://localhost:8000/ping
- **Metrics** (Prometheus): http://localhost:8000/metrics

## Configuration

The application reads device configuration from `/app/config/device_config.py` inside the container, which is mounted from `/data/tuya_exporter` on the host.

### Volume Mount

- **Host Path**: `/data/tuya_exporter`
- **Container Path**: `/app/config`

Any changes to configuration files in `/data/tuya_exporter` will require restarting the container:

```bash
docker-compose restart
```

## Troubleshooting

### Check container logs
```bash
docker-compose logs -f tuya-exporter
```

### Verify config mount
```bash
docker exec tuya-metrics-exporter ls -la /app/config
```

### Check health status
```bash
curl http://localhost:8000/health
```

## Environment Variables

You can add custom environment variables in the `docker-compose.yml` file:

```yaml
environment:
  - TZ=America/New_York
  - LOG_LEVEL=INFO
```

## Resource Limits (Optional)

To add resource limits, update `docker-compose.yml`:

```yaml
services:
  tuya-exporter:
    # ... existing config ...
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
```

