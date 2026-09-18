-- Grain: satu baris per order untuk semua query laporan order.
WITH deduplicated_orders AS (
    SELECT *
    FROM (
        SELECT o.*, ROW_NUMBER() OVER (
            PARTITION BY order_id ORDER BY order_created_at DESC
        ) AS rn
        FROM orders AS o
    ) AS ranked_orders
    WHERE rn = 1
),
latest_shipments AS (
    SELECT order_id, status, event_time
    FROM (
        SELECT s.*, ROW_NUMBER() OVER (
            PARTITION BY order_id ORDER BY event_time DESC
        ) AS rn
        FROM shipments AS s
    ) AS ranked_shipments
    WHERE rn = 1
)
SELECT o.order_id, o.origin_city, o.order_value_idr, s.status AS latest_status
FROM deduplicated_orders AS o
LEFT JOIN latest_shipments AS s USING (order_id)
WHERE o.payment_status = 'paid'
  AND COALESCE(s.status, 'unknown') <> 'delivered'
ORDER BY o.order_value_idr DESC
LIMIT 10;

-- Raw city counts: intentionally retains inconsistent city labels for audit.
SELECT origin_city, payment_status, COUNT(*) AS order_count
FROM orders
GROUP BY origin_city, payment_status
ORDER BY order_count DESC;

-- Validation checks.
SELECT order_id, COUNT(*) AS row_count
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;

SELECT COUNT(*) AS missing_order_id_count
FROM orders
WHERE order_id IS NULL;
