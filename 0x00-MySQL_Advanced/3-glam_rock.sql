-- Query to list bands with Glam rock as their main style, ranked by their longevity
SELECT 
    band_name,
    CASE 
        WHEN split IS NOT NULL THEN split - formed                     -- If the band split, calculate lifespan until split year
        ELSE 2022 - formed                                              -- If the band hasn't split, calculate lifespan until 2022
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'                                               -- Filter for bands with Glam rock style
ORDER BY 
    lifespan DESC;                                                   -- Rank by longevity in descending order
