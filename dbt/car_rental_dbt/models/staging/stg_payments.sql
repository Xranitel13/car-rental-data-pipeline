select
    cast(payment_id as integer) as payment_id,
    cast(rental_id as integer) as rental_id,

    lower(trim(payment_method)) as payment_method,
    lower(trim(payment_status)) as payment_status,

    cast(payment_amount as decimal(10, 2)) as payment_amount,
    cast(paid_at as timestamp) as paid_at

from {{ source('raw', 'raw_payments') }}