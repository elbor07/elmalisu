-- PostgreSQL Database Schema for Water Distribution System

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE water_sources (
    source_id SERIAL PRIMARY KEY,
    source_name VARCHAR(100) NOT NULL,
    source_type VARCHAR(50),
    location GEOGRAPHY(POINT),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE distribution_points (
    point_id SERIAL PRIMARY KEY,
    point_name VARCHAR(100) NOT NULL,
    location GEOGRAPHY(POINT),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE water_quality_tests (
    test_id SERIAL PRIMARY KEY,
    source_id INT REFERENCES water_sources(source_id),
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pH DECIMAL(3, 2),
    turbidity DECIMAL(5, 2),
    contaminants VARCHAR(200)
);

CREATE TABLE water_distribution (
    distribution_id SERIAL PRIMARY KEY,
    point_id INT REFERENCES distribution_points(point_id),
    source_id INT REFERENCES water_sources(source_id),
    supply_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    volume DECIMAL(10, 2)
);

CREATE TABLE maintenance_records (
    record_id SERIAL PRIMARY KEY,
    point_id INT REFERENCES distribution_points(point_id),
    maintenance_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT
);
