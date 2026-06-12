select
    rental_start_date,
    rental_start_month,

    count(*) as rentals_count,

    sum(
        case when is_completed_rental then 1 else 0 end
    ) as completed_rentals_count,

    sum(
        case when payment_status = 'paid' then 1 else 0 end
    ) as paid_payments_count,

    sum(paid_revenue) as paid_revenue,

    avg(
        case when paid_revenue > 0 then paid_revenue else null end
    ) as avg_paid_revenue_per_rental

from {{ ref('int_rental_financials') }}

group by
    rental_start_date,
    rental_start_month