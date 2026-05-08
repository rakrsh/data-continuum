# Ingestion Service

The Ingestion (or Seeding) service is responsible for simulating the high-velocity Smart Logistics environment.

It is a Python-based container that utilizes `Faker`, `SQLAlchemy`, and `PyMongo` to generate realistic mock data across both the SQL and NoSQL databases upon initialization.

## Process

1. **PostgreSQL Seeding**: Connects via SQLAlchemy and inserts 1,000+ `Shipment` records containing customer names, emails, and shipment statuses.
2. **MongoDB Seeding**: Connects via PyMongo and inserts high-frequency `telemetry` payload mimicking GPS coordinates, engine temperatures, and fuel levels.

This ensures the continuum has an immediate flow of data for downstream services to consume and orchestrate.
