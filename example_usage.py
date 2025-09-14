#!/usr/bin/env python3
"""
🎨 Example Usage Scripts for Infographics Generator

This file demonstrates different ways to use the infographics generator
"""

import subprocess
import os

def run_command(cmd):
    """Run command and print output"""
    print(f"🚀 Running: {cmd}")
    print("-" * 50)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"Errors: {result.stderr}")
    print("=" * 50)

def main():
    print("🎨 Infographics Generator - Example Usage")
    print("=" * 60)

    # Example 1: Financial data from web
    print("\n📊 Example 1: Financial Data from Screener.in")
    cmd1 = '''python infographics_generator.py --url "https://www.screener.in/company/RELIANCE/consolidated/" --company "Reliance Industries"'''
    print(f"Command: {cmd1}")

    # Example 2: CSV data
    print("\n📊 Example 2: CSV Data")
    cmd2 = '''python infographics_generator.py --csv "sample_data.csv" --company "Sample Company" --folder "Sample_Analytics"'''
    print(f"Command: {cmd2}")

    # Example 3: Custom folder
    print("\n📊 Example 3: Custom Output Folder")
    cmd3 = '''python infographics_generator.py --url "https://example.com/data" --company "Tech Corp" --folder "Q4_2024_Reports"'''
    print(f"Command: {cmd3}")

    # Create sample CSV for testing
    create_sample_csv()

    print("\n🎯 To run any example:")
    print("1. Copy the command above")
    print("2. Paste it in your terminal")
    print("3. Press Enter")
    print("\n✨ Beautiful infographics will be generated automatically!")

def create_sample_csv():
    """Create sample CSV file for testing"""
    import pandas as pd

    sample_data = {
        'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023'],
        'Revenue': [250000, 280000, 310000, 340000],
        'Profit': [25000, 30000, 35000, 40000],
        'Employees': [1200, 1250, 1300, 1350]
    }

    df = pd.DataFrame(sample_data)
    df.to_csv('sample_data.csv', index=False)
    print("✓ Created sample_data.csv for testing")

if __name__ == "__main__":
    main()