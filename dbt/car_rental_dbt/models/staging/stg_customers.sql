select
    cast(customer_id as integer) as customer_id,

    trim(first_name) as first_name,
    trim(last_name) as last_name,
    lower(trim(email)) as email,
    trim(cast(phone as varchar)) as phone,
    upper(trim(country)) as country,

    cast(created_at as timestamp) as created_at

from {{ source('raw', 'raw_customers') }}