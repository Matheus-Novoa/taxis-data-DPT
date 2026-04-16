WITH clean_table AS (
	SELECT
		VendorID,
		tpep_pickup_datetime,--::VARCHAR AS pickup_datetime,
		tpep_dropoff_datetime,--::VARCHAR AS dropoff_datetime,
		passenger_count,
		trip_distance,
		(trip_distance / DATEDIFF('hour', tpep_pickup_datetime, tpep_dropoff_datetime)) AS avg_speed,
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
		total_amount,
		MONTH(tpep_pickup_datetime) AS mes,
		YEAR(tpep_pickup_datetime) AS ano
	FROM banco.taxi_data
	WHERE trip_distance BETWEEN 0.1 AND 100
	AND avg_speed BETWEEN 0 AND 65
	AND trip_duration BETWEEN 1 AND 200
	AND passenger_count BETWEEN 1 AND 4
	AND total_amount BETWEEN 0 AND 3000
	AND pickup_longitude BETWEEN -74.20 AND -73.70
	AND dropoff_longitude BETWEEN -74.20 AND -73.70
	AND pickup_latitude BETWEEN 40.40 AND 41.00
	AND dropoff_latitude BETWEEN 40.40 AND 41.00
	AND total_amount = (fare_amount + extra + mta_tax + tip_amount + tolls_amount + improvement_surcharge)
	AND STRFTIME(tpep_pickup_datetime, '%Y-%m') IN ('2015-01', '2016-01', '2016-02', '2016-03')
	AND STRFTIME(tpep_dropoff_datetime, '%Y-%m') IN ('2015-01', '2016-01', '2016-02', '2016-03')
)

SELECT DISTINCT ON (VendorID, tpep_pickup_datetime, trip_distance, total_amount)
	   *
FROM clean_table;