# bulk-discount-optimizer-skill

> **GenPark AI Agent Skill** -- Tiered bulk discounts and profit margin optimizer.

## Quick Start

```python
from client import BulkDiscountOptimizerClient
client = BulkDiscountOptimizerClient()
result = client.optimize(unit_price=50.00, unit_cost=20.00)
print(result["tiers"])
```
