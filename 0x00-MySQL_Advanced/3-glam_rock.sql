-- Query to list bands with Glam rock as their main style, ranked by their longevity
SELECT 
    band_name,
    formed,
    split
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'                                               -- Filter for bands with Glam rock style
ORDER BY 
    band_name DESC;                                                   -- Rank by longevity in descending order
