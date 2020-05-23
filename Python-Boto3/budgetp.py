# !/usr/bin/env python
from pprint import pprint

import config
# import aws.prepare_json as prepare


def describe_budget_purchase():
    conn = config.connect()
    response = conn.describe_budgets(
        AccountId='',
        MaxResults=100,
       # NextToken='string'
    )

    return {
        "Budgets": response ['Budgets']
    }

pprint(describe_budget_purchase())