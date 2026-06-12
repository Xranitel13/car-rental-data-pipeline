select
    branch_id,
    location_city,
    location_state,
    location_country,
    airport_city,

    count(distinct rental_id) as rentals_count,
    count(distinct vehicle_id) as rented_vehicles_count,

    sum(
        case when is_completed_rental then 1 else 0 end
    ) as completed_rentals_count,

    sum(
        case when rental_status = 'cancelled' then 1 else 0 end
    ) as cancelled_rentals_count,

    sum(paid_revenue) as paid_revenue,

    avg(rental_days) as avg_rental_days,

    sum(paid_revenue) / nullif(count(distinct vehicle_id), 0) as revenue_per_rented_vehicle

from {{ ref('int_rental_financials') }}

group by
    branch_id,
    location_city,
    location_state,
    location_country,
    airport_city