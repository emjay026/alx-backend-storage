-- Query to rank country origins of bands by total number of fans
SELECT 
    origin,
    SUM(fans) AS nb_fans                    -- Sum the non-unique fans for each origin
FROM 
    metal_bands
GROUP BY 
    origin                                       -- Group by origin to aggregate data
ORDER BY 
    nb_fans DESC;                            -- Order by total fans in descending order
