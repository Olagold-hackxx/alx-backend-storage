--
--
SELECT
	band_name,
	CASE
		WHEN split IS NULL THEN 2022 - formed
		ELSE split - formed
	END AS lifespan
FROMl
	metal_bands
WHERE
	style REGEXP 'Glam'
ORDER BY
	lifespan DESC
