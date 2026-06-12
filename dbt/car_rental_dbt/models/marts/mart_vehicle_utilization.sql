select
    vehicle_id,
    branch_id,

    vehicle_make,
    vehicle_model,
    vehicle_type,
    fuel_type,

    count(distinct rental_id) as rentals_count,

    sum(
        case when is_completed_rental then 1 else 0 end
    ) as completed_rentals_count,

    sum(
        case when is_completed_rental then rental_days else 0 end
    ) as completed_rental_days,

    sum(paid_revenue) as paid_revenue,

    avg(daily_rate) as avg_daily_rate

from {{ ref('int_rental_financials') }}

group by
    vehicle_id,
    branch_id,
    vehicle_make,
    vehicle_model,
    vehicle_type,
    fuel_type