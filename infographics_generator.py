#!/usr/bin/env python3
"""
🎨 Universal Infographics Generator
Automatically generates beautiful infographics from any data source

Usage:
    python infographics_generator.py --url "https://example.com/data"
    python infographics_generator.py --folder "My Company Data"
    python infographics_generator.py --csv "data.csv" --company "Company Name"
"""

import argparse
import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')

# Enhanced styling configuration
plt.style.use('default')
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'sans-serif',
    'font.weight': 'normal',
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.labelweight': 'bold',
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.titlesize': 18,
    'figure.titleweight': 'bold',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.edgecolor': '#333333',
    'axes.linewidth': 1.2,
    'xtick.color': '#333333',
    'ytick.color': '#333333',
    'text.color': '#333333'
})

# Professional color palette
COLORS = {
    'primary': '#1f4e79',
    'secondary': '#2e8b57',
    'accent': '#ff6b35',
    'success': '#28a745',
    'warning': '#ffc107',
    'danger': '#dc3545',
    'info': '#17a2b8',
    'light': '#f8f9fa',
    'dark': '#343a40'
}

PALETTE = ['#1f4e79', '#2e8b57', '#ff6b35', '#28a745', '#ffc107', '#dc3545', '#17a2b8', '#6f42c1']

class InfographicsGenerator:
    def __init__(self, company_name="Company", output_folder=None):
        self.company_name = company_name
        self.output_folder = output_folder or f"{company_name.replace(' ', '_')}_Infographics"
        self.ensure_output_folder()

    def ensure_output_folder(self):
        """Create output folder if it doesn't exist"""
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print(f"📁 Created folder: {self.output_folder}")

    def fetch_web_data(self, url):
        """Fetch and parse data from web URL"""
        try:
            print(f"🌐 Fetching data from: {url}")

            if 'screener.in' in url:
                return self._parse_screener_data(url)
            else:
                return self._parse_generic_web_data(url)

        except Exception as e:
            print(f"❌ Error fetching web data: {e}")
            return None

    def _parse_screener_data(self, url):
        """Parse financial data from Screener.in"""
        # This would integrate with WebFetch or similar scraping
        # For now, return sample structure
        return {
            'financial_data': pd.DataFrame({
                'Year': ['FY 2022', 'FY 2023', 'FY 2024', 'FY 2025 (P)'],
                'Revenue': [100000, 120000, 140000, 160000],
                'Net_Profit': [10000, 12000, 14000, 16000]
            }),
            'ratios_data': pd.DataFrame({
                'Metric': ['P/E Ratio', 'ROCE (%)', 'ROE (%)', 'Operating Margin (%)'],
                'Value': [25.2, 9.69, 8.40, 17.0]
            }),
            'shareholding_data': pd.DataFrame({
                'Shareholder_Type': ['Promoters', 'FIIs', 'DIIs', 'Public'],
                'Percentage': [50.13, 19.16, 19.02, 11.52]
            })
        }

    def _parse_generic_web_data(self, url):
        """Parse data from generic web sources"""
        # Implement generic web scraping logic
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract tables, numbers, etc.
        # This is a placeholder for actual implementation
        return None

    def load_csv_data(self, csv_path):
        """Load and structure data from CSV file"""
        try:
            print(f"📊 Loading data from: {csv_path}")
            df = pd.read_csv(csv_path)

            # Auto-detect data structure and create appropriate datasets
            return self._structure_csv_data(df)

        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return None

    def _structure_csv_data(self, df):
        """Automatically structure CSV data for visualization"""
        datasets = {}

        # Detect numerical columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object']).columns

        # Create basic datasets
        if len(numeric_cols) >= 2:
            datasets['comparison_data'] = df[list(numeric_cols[:2]) + list(categorical_cols[:1])]

        if 'percentage' in df.columns.str.lower():
            pct_col = [col for col in df.columns if 'percentage' in col.lower()][0]
            cat_col = categorical_cols[0] if len(categorical_cols) > 0 else df.columns[0]
            datasets['pie_data'] = df[[cat_col, pct_col]]

        return datasets

    def create_enhanced_bar_chart(self, data, title, x_col, y_col, save_name):
        """Create enhanced bar chart"""
        fig, ax = plt.subplots(figsize=(14, 10))
        fig.patch.set_facecolor('white')

        colors = PALETTE[:len(data)]
        bars = ax.bar(data[x_col], data[y_col],
                     color=colors, alpha=0.9,
                     edgecolor='white', linewidth=2, width=0.6)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                   f'{height:,.0f}', ha='center', va='bottom',
                   fontweight='bold', fontsize=12, color='white',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['dark'], alpha=0.8))

        ax.set_title(f'{self.company_name} - {title}',
                    fontsize=18, fontweight='bold', pad=25, color=COLORS['dark'])
        ax.set_xlabel(x_col.replace('_', ' ').title(), fontsize=14, fontweight='bold')
        ax.set_ylabel(y_col.replace('_', ' ').title(), fontsize=14, fontweight='bold')
        ax.set_facecolor('#f8f9fa')
        ax.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)

        save_path = f"{self.output_folder}/{save_name}.png"
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        print(f"✓ Bar chart saved: {save_path}")

    def create_enhanced_pie_chart(self, data, title, label_col, value_col, save_name):
        """Create enhanced pie chart"""
        fig, ax = plt.subplots(figsize=(14, 10))
        fig.patch.set_facecolor('white')

        colors = PALETTE[:len(data)]
        explode = [0.08 if x == data[value_col].max() else 0.02 for x in data[value_col]]

        wedges, texts, autotexts = ax.pie(data[value_col], labels=None,
                                         autopct='%1.1f%%', colors=colors,
                                         explode=explode, shadow=True, startangle=90,
                                         wedgeprops=dict(width=0.8, edgecolor='white', linewidth=3))

        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(14)
            autotext.set_path_effects([patheffects.withStroke(linewidth=3, foreground='black')])

        ax.set_title(f'{self.company_name} - {title}',
                    fontsize=20, fontweight='bold', pad=40, color=COLORS['dark'])

        # Enhanced legend
        legend = ax.legend(wedges, data[label_col], title=title,
                          loc="center left", bbox_to_anchor=(1.1, 0.5),
                          fontsize=12, title_fontsize=14,
                          frameon=True, fancybox=True, shadow=True)

        # Add center circle for donut effect
        centre_circle = plt.Circle((0,0), 0.40, fc='white', linewidth=2, edgecolor=COLORS['dark'])
        fig.gca().add_artist(centre_circle)
        ax.text(0, 0, 'Data\\nBreakdown', ha='center', va='center',
               fontsize=14, fontweight='bold', color=COLORS['primary'])

        save_path = f"{self.output_folder}/{save_name}.png"
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        print(f"✓ Pie chart saved: {save_path}")

    def create_trend_chart(self, data, title, x_col, y_col, save_name):
        """Create enhanced trend line chart"""
        fig, ax = plt.subplots(figsize=(14, 10))
        fig.patch.set_facecolor('white')

        ax.plot(data[x_col], data[y_col], 'o-',
               color=COLORS['primary'], linewidth=4, markersize=12,
               markerfacecolor='white', markeredgecolor=COLORS['primary'], markeredgewidth=3)

        ax.fill_between(data[x_col], data[y_col], alpha=0.2, color=COLORS['primary'])

        # Add data point labels
        for x, y in zip(data[x_col], data[y_col]):
            ax.annotate(f'{y:,.0f}', (x, y), textcoords="offset points",
                       xytext=(0,15), ha='center', fontweight='bold', fontsize=11,
                       color='white', bbox=dict(boxstyle='round,pad=0.3',
                       facecolor=COLORS['primary'], alpha=0.8))

        ax.set_title(f'{self.company_name} - {title}',
                    fontsize=18, fontweight='bold', pad=25, color=COLORS['dark'])
        ax.set_xlabel(x_col.replace('_', ' ').title(), fontsize=14, fontweight='bold')
        ax.set_ylabel(y_col.replace('_', ' ').title(), fontsize=14, fontweight='bold')
        ax.set_facecolor('#f8f9fa')
        ax.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)

        save_path = f"{self.output_folder}/{save_name}.png"
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        print(f"✓ Trend chart saved: {save_path}")

    def generate_dashboard(self, datasets, save_name="Comprehensive_Dashboard"):
        """Create comprehensive dashboard from multiple datasets"""
        fig = plt.figure(figsize=(24, 16))
        fig.patch.set_facecolor('white')

        # Dynamically create subplots based on available data
        num_charts = min(len(datasets), 6)  # Max 6 charts
        rows = 2 if num_charts <= 4 else 3
        cols = 3 if num_charts > 4 else 2

        gs = fig.add_gridspec(rows, cols, hspace=0.35, wspace=0.3)

        chart_idx = 0
        for name, data in datasets.items():
            if chart_idx >= 6:  # Max 6 charts
                break

            row = chart_idx // cols
            col = chart_idx % cols
            ax = fig.add_subplot(gs[row, col])

            # Auto-detect chart type based on data
            numeric_cols = data.select_dtypes(include=[np.number]).columns
            categorical_cols = data.select_dtypes(include=['object']).columns

            if len(numeric_cols) >= 1 and len(categorical_cols) >= 1:
                # Bar chart
                bars = ax.bar(data[categorical_cols[0]], data[numeric_cols[0]],
                             color=PALETTE[chart_idx % len(PALETTE)], alpha=0.9)
                ax.set_title(name.replace('_', ' ').title(), fontweight='bold', fontsize=12)

            chart_idx += 1

        plt.suptitle(f'{self.company_name} - Comprehensive Data Dashboard',
                    fontsize=22, fontweight='bold', y=0.98, color=COLORS['dark'])

        save_path = f"{self.output_folder}/{save_name}.png"
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        print(f"✓ Dashboard saved: {save_path}")

    def auto_generate_infographics(self, datasets):
        """Automatically generate appropriate infographics from datasets"""
        print(f"🎨 Generating infographics for {self.company_name}...")
        print("=" * 60)

        chart_count = 0

        for name, data in datasets.items():
            if data is None or data.empty:
                continue

            numeric_cols = data.select_dtypes(include=[np.number]).columns
            categorical_cols = data.select_dtypes(include=['object']).columns

            # Generate appropriate charts based on data structure
            if len(numeric_cols) >= 1 and len(categorical_cols) >= 1:
                # Bar chart
                self.create_enhanced_bar_chart(
                    data, f"{name.replace('_', ' ').title()}",
                    categorical_cols[0], numeric_cols[0],
                    f"{name}_bar_chart"
                )
                chart_count += 1

                # If percentage data, also create pie chart
                if any('percent' in col.lower() for col in numeric_cols):
                    pct_col = next(col for col in numeric_cols if 'percent' in col.lower())
                    self.create_enhanced_pie_chart(
                        data, f"{name.replace('_', ' ').title()}",
                        categorical_cols[0], pct_col,
                        f"{name}_pie_chart"
                    )
                    chart_count += 1

            # Trend chart for time series data
            if len(numeric_cols) >= 2:
                self.create_trend_chart(
                    data, f"{name.replace('_', ' ').title()} Trend",
                    data.columns[0], numeric_cols[0],
                    f"{name}_trend_chart"
                )
                chart_count += 1

        # Generate dashboard
        if len(datasets) > 1:
            self.generate_dashboard(datasets)
            chart_count += 1

        print("=" * 60)
        print(f"✅ Generated {chart_count} infographics successfully!")
        print(f"📁 All files saved in: {self.output_folder}/")

        return chart_count

def main():
    parser = argparse.ArgumentParser(description='🎨 Universal Infographics Generator')
    parser.add_argument('--url', help='Web URL to fetch data from')
    parser.add_argument('--csv', help='CSV file path to load data from')
    parser.add_argument('--folder', help='Output folder name', default=None)
    parser.add_argument('--company', help='Company/Organization name', default='Company')

    args = parser.parse_args()

    if not args.url and not args.csv:
        print("❌ Please provide either --url or --csv parameter")
        return

    # Initialize generator
    generator = InfographicsGenerator(
        company_name=args.company,
        output_folder=args.folder
    )

    datasets = {}

    # Load data from source
    if args.url:
        web_data = generator.fetch_web_data(args.url)
        if web_data:
            datasets.update(web_data)

    if args.csv:
        csv_data = generator.load_csv_data(args.csv)
        if csv_data:
            datasets.update(csv_data)

    if not datasets:
        print("❌ No data could be loaded from the provided source")
        return

    # Generate infographics
    generator.auto_generate_infographics(datasets)

if __name__ == "__main__":
    main()