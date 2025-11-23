"""
AEP Complexity Calculator
Implements computable proxies for Kolmogorov complexity
"""

import numpy as np
import zlib
from typing import Dict

class ComplexityCalculator:
    def __init__(self):
        self.complexity_cache = {}
    
    def parameter_complexity(self, parameters: Dict) -> float:
        """Calculate C_param for a set of parameters"""
        total_bits = 0
        for param_name, param_info in parameters.items():
            min_val = param_info['min']
            max_val = param_info['max'] 
            precision = param_info['precision']
            bits = np.log2((max_val - min_val) / precision)
            total_bits += bits
        return total_bits
    
    def structural_complexity(self, theory_spec: Dict) -> float:
        """Estimate C_struct from theory specification"""
        # Lagrangian complexity via compression
        lagrangian_str = str(theory_spec.get('lagrangian', ''))
        compressed_size = len(zlib.compress(lagrangian_str.encode()))
        
        # Symmetry group complexity (simplified)
        symmetry_complexity = len(theory_spec.get('symmetries', [])) * 5
        
        # Field content complexity (simplified)
        field_complexity = len(theory_spec.get('fields', [])) * 3
        
        return compressed_size + symmetry_complexity + field_complexity
    
    def predictive_complexity(self, simulation_time: float, memory_usage: float) -> float:
        """Estimate C_pred from computational requirements"""
        return np.log(simulation_time + 1) + np.log(memory_usage + 1)
    
    def total_complexity(self, parameters: Dict, theory_spec: Dict, 
                        sim_time: float = 1.0, memory: float = 1.0,
                        weights: tuple = (0.5, 0.3, 0.2)) -> float:
        """Calculate total complexity with weighted components"""
        c_param = self.parameter_complexity(parameters)
        c_struct = self.structural_complexity(theory_spec)
        c_pred = self.predictive_complexity(sim_time, memory)
        
        return (weights[0] * c_param + 
                weights[1] * c_struct + 
                weights[2] * c_pred)
