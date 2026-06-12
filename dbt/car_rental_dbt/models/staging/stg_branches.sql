select
    cast(branch_id as integer) as branch_id,

    lower(trim(location_city)) as location_city,
    upper(trim(location_country)) as location_country,
    upper(trim(location_state)) as location_state,
    lower(trim(airport_city)) as airport_city,

    cast(location_latitude as decimal(10, 6)) as location_latitude,
    cast(location_longitude as decimal(10, 6)) as location_longitude

from {{ source('raw', 'raw_branches') }}