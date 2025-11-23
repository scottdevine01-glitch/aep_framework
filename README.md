# Anti-Entropic Principle (AEP) Framework

Implementation of the Anti-Entropic Principle for physical theory selection based on Kolmogorov complexity minimization.

## Quick Start

```python
from src.complexity_calculator import ComplexityCalculator

calc = ComplexityCalculator()
parameters = {
    'G': {'min': 6.67e-11, 'max': 6.68e-11, 'precision': 1e-15}
}
theory_spec = {
    'lagrangian': 'L = T - V',
    'symmetries': ['galilean'],
    'fields': ['gravitational_field']
}

complexity = calc.total_complexity(parameters, theory_spec)
print(f\"Total complexity: {complexity:.1f}\")
