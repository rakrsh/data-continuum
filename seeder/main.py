import os
import time
import random
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.orm import declarative_base, sessionmaker
from pymongo import MongoClient
from datetime import datetime

fake = Faker()

POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/continuum")
MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:admin@localhost:27017/")

# PostgreSQL Setup
engine = create_engine(POSTGRES_URL)
Base = declarative_base()

class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String)
    customer_email = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Ensure tables exist
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# MongoDB Setup
mongo_client = MongoClient(MONGO_URL)
db = mongo_client['continuum']
telemetry_col = db['telemetry']

def seed_data():
    print("Starting data seeding...")
    statuses = ['PENDING', 'IN_TRANSIT', 'DELIVERED', 'CANCELLED']

    for i in range(1000):
        # Insert into PostgreSQL
        shipment = Shipment(
            customer_name=fake.name(),
            customer_email=fake.email(),
            status=random.choice(statuses),
            created_at=fake.date_time_this_year()
        )
        session.add(shipment)
        session.commit()

        # Insert into MongoDB
        telemetry = {
            "shipment_id": shipment.id,
            "latitude": float(fake.latitude()),
            "longitude": float(fake.longitude()),
            "engine_temp": random.uniform(70.0, 110.0),
            "fuel_level": random.uniform(0.0, 100.0),
            "timestamp": datetime.utcnow()
        }
        telemetry_col.insert_one(telemetry)

        if i % 100 == 0:
            print(f"Seeded {i} records...")

    print("Data seeding completed.")

if __name__ == "__main__":
    # Wait for DBs to be ready (handled by docker-compose depends_on, but just in case)
    time.sleep(5)
    try:
        seed_data()
    except Exception as e:
        print(f"Error seeding data: {e}")
        time.sleep(10)
