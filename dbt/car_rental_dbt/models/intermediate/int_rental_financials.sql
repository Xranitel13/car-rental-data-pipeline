select
    r.rental_id,
    r.customer_id,
    r.vehicle_id,
    r.branch_id,

    b.location_city,
    b.location_country,
    b.location_state,
    b.airport_city,

    v.vehicle_make,
    v.vehicle_model,
    v.vehicle_type,
    v.fuel_type,

    r.rental_start_at,
    r.rental_end_at,
    cast(r.rental_start_at as date) as rental_start_date,
    cast(date_trunc('month', r.rental_start_at) as date) as rental_start_month,

    r.rental_days,
    r.rental_status,

    p.payment_id,
    p.payment_method,
    p.payment_status,

    r.daily_rate,
    r.total_amount as rental_amount,
    p.payment_amount,

    case
        when r.rental_status = 'completed'
            and p.payment_status = 'paid'
        then p.payment_amount
        else 0
    end as paid_revenue,

    case
        when p.payment_status = 'paid' then true
        else false
    end as is_paid,

    case
        when r.rental_status = 'completed' then true
        else false
    end as is_completed_rental

from {{ ref('stg_rentals') }} as r

left join {{ ref('stg_payments') }} as p
    on r.rental_id = p.rental_id

left join {{ ref('stg_vehicles') }} as v
    on r.vehicle_id = v.vehicle_id

left join {{ ref('stg_branches') }} as b
    on r.branch_id = b.branch_id