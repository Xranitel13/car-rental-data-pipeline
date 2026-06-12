select
    cast(rental_id as integer) as rental_id,
    cast(customer_id as integer) as customer_id,
    cast(vehicle_id as integer) as vehicle_id,
    cast(branch_id as integer) as branch_id,

    cast(rental_start_at as timestamp) as rental_start_at,
    cast(rental_end_at as timestamp) as rental_end_at,
    cast(rental_days as integer) as rental_days,

    lower(trim(rental_status)) as rental_status,

    cast(daily_rate as decimal(10, 2)) as daily_rate,
    cast(total_amount as decimal(10, 2)) as total_amount,

    cast(created_at as timestamp) as created_at,
    cast(updated_at as timestamp) as updated_at

from {{ source('raw', 'raw_rentals') }}