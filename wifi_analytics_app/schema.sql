CREATE TABLE wifi_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    device_type VARCHAR(50),
    location VARCHAR(100),
    device_id VARCHAR(100)
);
