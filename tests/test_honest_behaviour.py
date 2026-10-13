from faida_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_a_zero_percent_coupon_is_used_as_given_not_replaced_by_a_default():
    r = _fn("treasury_bond_calculator")(100000, 5, 0)
    assert r["coupon_rate_pct"] == 0 and r["annual_interest_kes"] == 0 and r["rate_basis"] == "supplied"


def test_the_rate_basis_distinguishes_a_sample_rate_from_a_generic_default():
    assert _fn("treasury_bond_calculator")(100000, 10, None)["rate_basis"] == "sample table"
    assert _fn("treasury_bond_calculator")(100000, 7, None)["rate_basis"] == "generic default 14.5%"
