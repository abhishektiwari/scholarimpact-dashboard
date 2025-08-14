#!/usr/bin/env python3
"""
Generated ScholarImpact Dashboard
"""

from scholarimpact.dashboard import Dashboard

if __name__ == "__main__":
    dashboard = Dashboard(
        data_dir="./data",
        title="My Citation Dashboard"
    )
    dashboard.run()
