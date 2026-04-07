WITH clean_table AS (
	SELECT
		VendorID,
		tpep_pickup_datetime::VARCHAR AS pickup_datetime,
		tpep_dropoff_datetime::VARCHAR AS dropoff_datetime,
		passenger_count,
		trip_distance,
		DATEDIFF('minute', tpep_pickup_datetime, tpep_dropoff_datetime) AS trip_duration,
		pickup_longitude,
		pickup_latitude,
		RateCodeID,
		store_and_fwd_flag,
		dropoff_longitude,
		dropoff_latitude,
		payment_type,
		fare_amount,
		extra,
		mta_tax,
		tip_amount,
		(tip_amount/total_amount*100) AS tip_pct,
		tolls_amount,
		improvement_surcharge,
		total_amount
	FROM  banco.taxi_data
	WHERE trip_distance BETWEEN 0.1 AND 100
	AND passenger_count BETWEEN 1 AND 6
	AND total_amount > 0
	AND pickup_longitude BETWEEN -74.20 AND -73.70
	AND dropoff_longitude BETWEEN -74.20 AND -73.70
	AND pickup_latitude BETWEEN 40.40 AND 41.00
	AND dropoff_latitude BETWEEN 40.40 AND 41.00
)
SELECT
	COUNT(*) AS total_trips,
	AVG(trip_distance) AS avg_distance,
	AVG(fare_amount) AS avg_fare,
	AVG(trip_duration) AS avg_duration,
	AVG(tip_pct) AS avg_tip_pct,
	SUM(total_amount) AS total_revenue
FROM clean_table