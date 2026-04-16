SELECT
	COUNT(*) AS total_trips,
	AVG(trip_distance) AS avg_distance,
	AVG(fare_amount) AS avg_fare,
	AVG(trip_duration) AS avg_duration,
	AVG(tip_pct) AS avg_tip_pct,
	SUM(total_amount) AS total_revenue
FROM clean_table