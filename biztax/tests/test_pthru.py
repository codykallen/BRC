"""
Test PassThrough class.
"""
# CODING-STYLE CHECKS:
# pycodestyle test_pthru.py
# pylint --disable=locally-disabled test_pthru.py

from copy import deepcopy
import pytest
# pylint: disable=import-error
from biztax import Passthrough


@pytest.mark.parametrize('reform_number, results_type',
                         [(0, 'schc'),
                          (0, 'part'),
                          (0, 'scor'),
                          (1, 'schc'),
                          (1, 'part'),
                          (1, 'scor'),
                          (2, 'schc'),
                          (2, 'part'),
                          (2, 'scor')])
def test_passthrough_results(reform_number, results_type,
                             reforms, actual_vs_expect):
    """
    Test different passthrough results under different reforms.
    """
    pthru = Passthrough(reforms[reform_number])
    pthru.calc_static()
    decimals = 2
    if results_type == 'schc':
        results = deepcopy(pthru.SchC_results).round(decimals)
    elif results_type == 'part':
        results = deepcopy(pthru.partner_results).round(decimals)
    elif results_type == 'scor':
        results = deepcopy(pthru.Scorp_results).round(decimals)
    else:
        assert results_type == 'illegal passthrough results type'
    fname = 'pthru_ref{}_{}_expect.csv'.format(reform_number, results_type)
    actual_vs_expect(results, fname, precision=decimals)
