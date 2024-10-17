-- Step 1: Create the metal_bands table if it does not already exist
-- Make sure to define the structure according to the data in the metal_bands.sql dump.

CREATE TABLE IF NOT EXISTS metal_bands (
    id INT AUTO_INCREMENT PRIMARY KEY,           -- Assuming there's an ID column
    origin VARCHAR(255),                          -- Origin of the band
    nb_fans INT                                   -- Number of fans (non-unique)
);

-- Step 2: Import data from the metal_bands.sql dump file
-- This step would typically be done in your database management tool or command line.

-- For example, in MySQL:
-- SOURCE /path/to/metal_bands.sql;

-- Step 3: Query to rank country origins of bands by number of fans
SELECT 
    origin,
    SUM(nb_fans) AS total_fans                    -- Sum the non-unique fans for each origin
FROM 
    metal_bands
GROUP BY 
    origin                                         -- Group by origin to aggregate data
ORDER BY 
    total_fans DESC;                              -- Order by total fans in descending order
