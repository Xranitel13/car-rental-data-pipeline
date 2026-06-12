select
    cast(vehicle_id as integer) as vehicle_id,
    cast(branch_id as integer) as branch_id,
    cast(owner_id as integer) as owner_id,

    lower(trim(vehicle_make)) as vehicle_make,
    lower(trim(vehicle_model)) as vehicle_model,
    lower(trim(vehicle_type)) as vehicle_type,

    coalesce(upper(trim(fuel_type)), 'UNKNOWN') as fuel_type,

    cast(vehicle_year as integer) as vehicle_year,
    cast(daily_rate as decimal(10, 2)) as daily_rate,
    cast(rating as decimal(3, 2)) as rating,
    cast(renter_trips_taken as integer) as renter_trips_taken,
    cast(review_count as integer) as review_count

from {{ source('raw', 'raw_vehicles') }}