-- Query to list bands with any style containing 'glam', ranked by their longevity
SELECT 
    band_name,
    CASE 
        WHEN split IS NOT NULL THEN split - formed                     -- If the band split, calculate lifespan until split year
        ELSE 2022 - formed                                              -- If the band hasn't split, calculate lifespan until 2022
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'                                          -- Filter for bands where style contains 'glam'
ORDER BY 
    band_name DESC;                                             -- Order by band_name in descending order
