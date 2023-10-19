-- ranks country origins of bands,
-- ordered by the number of (non-unique) fans

SELECT origin, fans AS nb_fans FROM metal_bands ORDER BY fans DESC
