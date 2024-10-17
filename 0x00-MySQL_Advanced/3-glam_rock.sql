-- Query to list bands with any style containing 'glam', ranked by their longevity
SELECT 
    band_name,
    formed,
    split,
    style
FROM 
    metal_bands
WHERE 
    style LIKE '%glam%'                                          -- Filter for bands where style contains 'glam'
ORDER BY 
    band_name DESC;                                             -- Order by band_name in descending order
