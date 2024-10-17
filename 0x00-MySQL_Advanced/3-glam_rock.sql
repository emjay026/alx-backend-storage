-- Query to list bands with Glam rock as their main style, ranked by their longevity
SELECT 
    band_name,
    formed,
    split,
    style
FROM 
    metal_bands                                             -- Filter for bands with Glam rock style
ORDER BY 
    band_name DESC;                                                   -- Rank by longevity in descending order
