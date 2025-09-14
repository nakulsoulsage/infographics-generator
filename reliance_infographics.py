#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Enhanced styling
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

# Enhanced color palette
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

def create_reliance_data():
    """Create Reliance Industries datasets from the extracted financial data"""

    # Revenue and Net Profit data (FY in Rs. Crores)
    financial_data = {
        'Year': ['FY 2022', 'FY 2023', 'FY 2024', 'FY 2025 (P)'],
        'Revenue': [694673, 876396, 899041, 962820],
        'Net_Profit': [67845, 74088, 79020, 81309]
    }

    # Key Financial Ratios
    ratios_data = {
        'Metric': ['P/E Ratio', 'ROCE (%)', 'ROE (%)', 'Operating Margin (%)', 'Dividend Yield (%)'],
        'Value': [25.2, 9.69, 8.40, 17.0, 0.39]
    }

    # Shareholding Pattern
    shareholding_data = {
        'Shareholder_Type': ['Promoters', 'FIIs', 'DIIs', 'Public'],
        'Percentage': [50.13, 19.16, 19.02, 11.52]
    }

    # Growth Rates
    growth_data = {
        'Growth_Type': ['Sales Growth (10Y)', 'Profit Growth (10Y)', 'Stock CAGR (10Y)'],
        'CAGR_Percentage': [10, 12, 22]
    }

    # Quarterly performance (latest)
    quarterly_data = {
        'Metric': ['Sales', 'Operating Profit', 'Net Profit'],
        'Amount_Crores': [231535, 39058, 19323],
        'Margin_Percentage': [100, 17, 8.35]  # Operating and Net profit margins
    }

    return (pd.DataFrame(financial_data), pd.DataFrame(ratios_data),
            pd.DataFrame(shareholding_data), pd.DataFrame(growth_data),
            pd.DataFrame(quarterly_data))

def create_revenue_profit_trend(data, save_path):
    """Create Revenue and Net Profit trend chart with enhanced styling"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 14))
    fig.patch.set_facecolor('white')

    # Revenue Trend with gradient effect
    bars1 = ax1.bar(data['Year'], data['Revenue'],
                     color=COLORS['primary'], alpha=0.9,
                     edgecolor='white', linewidth=2,
                     width=0.6)

    # Add gradient effect
    for bar in bars1:
        bar.set_facecolor(COLORS['primary'])
        bar.set_alpha(0.85)

    ax1.set_title('Reliance Industries - Revenue Growth Trajectory',
                  fontsize=18, fontweight='bold', pad=25, color=COLORS['dark'])
    ax1.set_ylabel('Revenue (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['dark'])

    # Enhanced value labels with background
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 15000,
                f'₹{height/100000:.1f}L Cr', ha='center', va='bottom',
                fontweight='bold', fontsize=12, color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['primary'], alpha=0.8))

    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.1f}L'))
    ax1.set_facecolor('#f8f9fa')
    ax1.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)

    # Net Profit Trend with gradient
    bars2 = ax2.bar(data['Year'], data['Net_Profit'],
                     color=COLORS['secondary'], alpha=0.9,
                     edgecolor='white', linewidth=2,
                     width=0.6)

    for bar in bars2:
        bar.set_facecolor(COLORS['secondary'])
        bar.set_alpha(0.85)

    ax2.set_title('Reliance Industries - Net Profit Growth',
                  fontsize=18, fontweight='bold', pad=25, color=COLORS['dark'])
    ax2.set_ylabel('Net Profit (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax2.set_xlabel('Financial Year', fontsize=14, fontweight='bold', color=COLORS['dark'])

    # Enhanced value labels
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 2000,
                f'₹{height/100000:.1f}L Cr', ha='center', va='bottom',
                fontweight='bold', fontsize=12, color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['secondary'], alpha=0.8))

    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.1f}L'))
    ax2.set_facecolor('#f8f9fa')
    ax2.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Enhanced Revenue and Profit trend chart saved as {save_path}")

def create_shareholding_pie_chart(data, save_path):
    """Create enhanced Shareholding Pattern pie chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('white')

    # Enhanced color palette
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['warning']]
    explode = [0.08 if x == max(data['Percentage']) else 0.02 for x in data['Percentage']]

    # Create pie chart with enhanced styling
    wedges, texts, autotexts = ax.pie(data['Percentage'],
                                     labels=None,  # Remove labels from pie
                                     autopct='%1.1f%%',
                                     colors=colors,
                                     explode=explode,
                                     shadow=True,
                                     startangle=90,
                                     wedgeprops=dict(width=0.8, edgecolor='white', linewidth=3))

    # Style percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(14)
        autotext.set_path_effects([patheffects.withStroke(linewidth=3, foreground='black')])

    ax.set_title('Reliance Industries - Shareholding Distribution',
                 fontsize=20, fontweight='bold', pad=40, color=COLORS['dark'])

    # Enhanced legend with better positioning
    legend_labels = [f'{shareholder}: {percentage}%'
                    for shareholder, percentage in zip(data['Shareholder_Type'], data['Percentage'])]
    legend = ax.legend(wedges, legend_labels,
                      title="Shareholding Breakdown",
                      loc="center left",
                      bbox_to_anchor=(1.1, 0.5),
                      fontsize=12,
                      title_fontsize=14,
                      frameon=True,
                      fancybox=True,
                      shadow=True)

    legend.get_frame().set_facecolor('#f8f9fa')
    legend.get_frame().set_edgecolor(COLORS['dark'])
    legend.get_frame().set_linewidth(1.5)

    # Add center circle for donut effect
    centre_circle = plt.Circle((0,0), 0.40, fc='white', linewidth=2, edgecolor=COLORS['dark'])
    fig.gca().add_artist(centre_circle)

    # Add center text
    ax.text(0, 0, 'RIL\nShares', ha='center', va='center',
            fontsize=16, fontweight='bold', color=COLORS['primary'])

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Enhanced shareholding pattern chart saved as {save_path}")

def create_financial_ratios_chart(data, save_path):
    """Create enhanced Financial Ratios horizontal bar chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('white')

    # Enhanced color scheme
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['success'], COLORS['warning']]
    bars = ax.barh(data['Metric'], data['Value'],
                   color=colors, alpha=0.85,
                   edgecolor='white', linewidth=2,
                   height=0.6)

    # Add value labels with enhanced styling
    for i, bar in enumerate(bars):
        width = bar.get_width()
        if 'Ratio' not in data['Metric'][i]:
            label = f'{data["Value"][i]:.2f}%'
        else:
            label = f'{data["Value"][i]:.1f}'

        ax.text(width + 0.8, bar.get_y() + bar.get_height()/2.,
                label, ha='left', va='center',
                fontweight='bold', fontsize=13,
                color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=colors[i], alpha=0.8))

    ax.set_title('Reliance Industries - Key Financial Performance Metrics',
                 fontsize=18, fontweight='bold', pad=25, color=COLORS['dark'])
    ax.set_xlabel('Value', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax.set_facecolor('#f8f9fa')
    ax.grid(axis='x', alpha=0.4, linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)

    # Enhanced y-axis labels
    ax.tick_params(axis='y', labelsize=12, colors=COLORS['dark'])
    ax.tick_params(axis='x', labelsize=11, colors=COLORS['dark'])

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Enhanced financial ratios chart saved as {save_path}")

def create_growth_rates_chart(data, save_path):
    """Create enhanced Growth Rates bar chart"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('white')

    colors = [COLORS['accent'], COLORS['secondary'], COLORS['success']]
    bars = ax.bar(data['Growth_Type'], data['CAGR_Percentage'],
                  color=colors, alpha=0.9,
                  edgecolor='white', linewidth=3,
                  width=0.6)

    # Add gradient effect to bars
    for i, bar in enumerate(bars):
        bar.set_facecolor(colors[i])

    # Enhanced value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height}%', ha='center', va='bottom',
                fontweight='bold', fontsize=16, color='white',
                bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['dark'], alpha=0.8))

    ax.set_title('Reliance Industries - Stellar 10-Year Growth Performance (CAGR)',
                fontsize=18, fontweight='bold', pad=30, color=COLORS['dark'])
    ax.set_ylabel('CAGR Percentage (%)', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax.set_xlabel('Growth Metric', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax.set_facecolor('#f8f9fa')
    ax.grid(axis='y', alpha=0.4, linestyle='-', linewidth=0.5)
    ax.set_axisbelow(True)

    # Enhanced x-axis labels
    labels = ['Sales Growth\n(10 Years)', 'Profit Growth\n(10 Years)', 'Stock CAGR\n(10 Years)']
    ax.set_xticklabels(labels, fontsize=12, color=COLORS['dark'])
    ax.tick_params(axis='y', labelsize=11, colors=COLORS['dark'])

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Enhanced growth rates chart saved as {save_path}")

def create_quarterly_performance_chart(data, save_path):
    """Create enhanced Latest Quarterly Performance chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
    fig.patch.set_facecolor('white')

    # Quarterly amounts with enhanced styling
    colors1 = [COLORS['primary'], COLORS['accent'], COLORS['secondary']]
    bars1 = ax1.bar(data['Metric'], data['Amount_Crores'],
                    color=colors1, alpha=0.9,
                    edgecolor='white', linewidth=2,
                    width=0.6)

    # Enhanced value labels
    for i, bar in enumerate(bars1):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 8000,
                f'₹{height/100000:.1f}L Cr', ha='center', va='bottom',
                fontweight='bold', fontsize=13, color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=colors1[i], alpha=0.8))

    ax1.set_title('Latest Quarter Performance - Revenue Breakdown',
                  fontsize=16, fontweight='bold', color=COLORS['dark'], pad=20)
    ax1.set_ylabel('Amount (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.1f}L'))
    ax1.set_facecolor('#f8f9fa')
    ax1.grid(axis='y', alpha=0.4, linestyle='-', linewidth=0.5)
    ax1.tick_params(axis='x', rotation=15, labelsize=11, colors=COLORS['dark'])
    ax1.tick_params(axis='y', labelsize=11, colors=COLORS['dark'])

    # Margin percentages with enhanced styling
    margin_metrics = ['Operating Profit', 'Net Profit']
    margin_percentages = [17.0, 8.35]
    colors2 = [COLORS['accent'], COLORS['secondary']]

    bars2 = ax2.bar(margin_metrics, margin_percentages,
                    color=colors2, alpha=0.9,
                    edgecolor='white', linewidth=2,
                    width=0.5)

    # Enhanced value labels
    for i, bar in enumerate(bars2):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                f'{height}%', ha='center', va='bottom',
                fontweight='bold', fontsize=14, color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=colors2[i], alpha=0.8))

    ax2.set_title('Latest Quarter - Profit Margins',
                  fontsize=16, fontweight='bold', color=COLORS['dark'], pad=20)
    ax2.set_ylabel('Margin Percentage (%)', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax2.set_facecolor('#f8f9fa')
    ax2.grid(axis='y', alpha=0.4, linestyle='-', linewidth=0.5)
    ax2.tick_params(axis='x', labelsize=11, colors=COLORS['dark'])
    ax2.tick_params(axis='y', labelsize=11, colors=COLORS['dark'])

    plt.suptitle('Reliance Industries - Latest Quarterly Performance Excellence',
                fontsize=20, fontweight='bold', y=0.98, color=COLORS['dark'])
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Enhanced quarterly performance chart saved as {save_path}")

def create_revenue_profit_comparison(data, save_path):
    """Create enhanced Revenue vs Profit comparison line chart"""
    fig, ax = plt.subplots(figsize=(16, 12))
    fig.patch.set_facecolor('white')

    # Create dual y-axis
    ax2 = ax.twinx()

    # Enhanced Revenue line with markers
    line1 = ax.plot(data['Year'], data['Revenue'], 'o-',
                    color=COLORS['primary'], linewidth=4, markersize=12,
                    label='Revenue', markerfacecolor='white',
                    markeredgecolor=COLORS['primary'], markeredgewidth=3)

    # Enhanced Net Profit line with markers
    line2 = ax2.plot(data['Year'], data['Net_Profit'], 's-',
                     color=COLORS['secondary'], linewidth=4, markersize=12,
                     label='Net Profit', markerfacecolor='white',
                     markeredgecolor=COLORS['secondary'], markeredgewidth=3)

    # Enhanced fill areas with gradients
    ax.fill_between(data['Year'], data['Revenue'], alpha=0.2, color=COLORS['primary'])
    ax2.fill_between(data['Year'], data['Net_Profit'], alpha=0.2, color=COLORS['secondary'])

    # Add data point labels
    for i, (year, revenue) in enumerate(zip(data['Year'], data['Revenue'])):
        ax.annotate(f'₹{revenue/100000:.1f}L Cr', (year, revenue),
                   textcoords="offset points", xytext=(0,15), ha='center',
                   fontweight='bold', fontsize=11, color=COLORS['primary'],
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor=COLORS['primary']))

    for i, (year, profit) in enumerate(zip(data['Year'], data['Net_Profit'])):
        ax2.annotate(f'₹{profit/100000:.1f}L Cr', (year, profit),
                    textcoords="offset points", xytext=(0,-25), ha='center',
                    fontweight='bold', fontsize=11, color=COLORS['secondary'],
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor=COLORS['secondary']))

    # Enhanced formatting
    ax.set_xlabel('Financial Year', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax.set_ylabel('Revenue (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['primary'])
    ax2.set_ylabel('Net Profit (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['secondary'])

    ax.tick_params(axis='y', labelcolor=COLORS['primary'], labelsize=12)
    ax2.tick_params(axis='y', labelcolor=COLORS['secondary'], labelsize=12)
    ax.tick_params(axis='x', labelsize=12, colors=COLORS['dark'])

    # Format y-axes
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.1f}L'))
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.1f}L'))

    # Enhanced title and grid
    ax.set_title('Reliance Industries - Revenue vs Net Profit Growth Trajectory',
                fontsize=18, fontweight='bold', pad=30, color=COLORS['dark'])
    ax.set_facecolor('#f8f9fa')
    ax.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)

    # Enhanced legend
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    legend = ax.legend(lines1 + lines2, labels1 + labels2,
                      loc='upper left', fontsize=13,
                      frameon=True, fancybox=True, shadow=True)
    legend.get_frame().set_facecolor('#f8f9fa')
    legend.get_frame().set_edgecolor(COLORS['dark'])

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Enhanced revenue vs profit comparison chart saved as {save_path}")

def create_comprehensive_dashboard(financial_data, ratios_data, shareholding_data,
                                 growth_data, quarterly_data, save_path):
    """Create enhanced comprehensive Reliance Industries dashboard"""
    fig = plt.figure(figsize=(24, 16))
    fig.patch.set_facecolor('white')
    gs = fig.add_gridspec(3, 4, hspace=0.35, wspace=0.3)

    # 1. Revenue trend with enhanced styling
    ax1 = fig.add_subplot(gs[0, 0:2])
    bars = ax1.bar(financial_data['Year'], financial_data['Revenue'],
                   color=COLORS['primary'], alpha=0.9,
                   edgecolor='white', linewidth=2)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 15000,
                f'₹{height/100000:.1f}L', ha='center', va='bottom',
                fontweight='bold', fontsize=10, color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['primary'], alpha=0.8))

    ax1.set_title('Revenue Growth', fontweight='bold', fontsize=14, color=COLORS['dark'], pad=15)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.0f}L'))
    ax1.tick_params(axis='x', rotation=35, labelsize=10, colors=COLORS['dark'])
    ax1.tick_params(axis='y', labelsize=10, colors=COLORS['dark'])
    ax1.set_facecolor('#f8f9fa')
    ax1.grid(True, alpha=0.3)

    # 2. Enhanced shareholding donut
    ax2 = fig.add_subplot(gs[0, 2:4])
    colors_pie = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['warning']]
    wedges, texts, autotexts = ax2.pie(shareholding_data['Percentage'],
                                      labels=None,
                                      autopct='%1.1f%%',
                                      colors=colors_pie,
                                      wedgeprops=dict(width=0.7, edgecolor='white', linewidth=2))

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)

    # Add center circle
    centre_circle = plt.Circle((0,0), 0.3, fc='white', linewidth=2, edgecolor=COLORS['dark'])
    ax2.add_artist(centre_circle)
    ax2.text(0, 0, 'Share\nHolding', ha='center', va='center',
             fontsize=11, fontweight='bold', color=COLORS['primary'])

    ax2.set_title('Shareholding Pattern', fontweight='bold', fontsize=14, color=COLORS['dark'], pad=15)

    # Add legend
    ax2.legend(wedges, shareholding_data['Shareholder_Type'],
               loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)

    # 3. Enhanced financial ratios
    ax3 = fig.add_subplot(gs[1, 0:2])
    colors_ratios = [COLORS['primary'], COLORS['secondary'], COLORS['accent'], COLORS['success'], COLORS['warning']]
    bars = ax3.barh(ratios_data['Metric'], ratios_data['Value'],
                    color=colors_ratios, alpha=0.9,
                    edgecolor='white', linewidth=2)

    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        label = f'{ratios_data["Value"][i]:.1f}%' if 'Ratio' not in ratios_data['Metric'][i] else f'{ratios_data["Value"][i]:.1f}'
        ax3.text(width + 0.5, bar.get_y() + bar.get_height()/2.,
                label, ha='left', va='center',
                fontweight='bold', fontsize=10, color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=colors_ratios[i], alpha=0.8))

    ax3.set_title('Financial Ratios', fontweight='bold', fontsize=14, color=COLORS['dark'], pad=15)
    ax3.tick_params(axis='y', labelsize=10, colors=COLORS['dark'])
    ax3.tick_params(axis='x', labelsize=10, colors=COLORS['dark'])
    ax3.set_facecolor('#f8f9fa')
    ax3.grid(True, alpha=0.3)

    # 4. Enhanced growth rates
    ax4 = fig.add_subplot(gs[1, 2:4])
    colors_growth = [COLORS['accent'], COLORS['secondary'], COLORS['success']]
    bars = ax4.bar(growth_data['Growth_Type'], growth_data['CAGR_Percentage'],
                   color=colors_growth, alpha=0.9,
                   edgecolor='white', linewidth=2)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height}%', ha='center', va='bottom',
                fontweight='bold', fontsize=11, color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['dark'], alpha=0.8))

    ax4.set_title('10-Year CAGR', fontweight='bold', fontsize=14, color=COLORS['dark'], pad=15)

    # Enhanced x-axis labels
    labels = ['Sales\nGrowth', 'Profit\nGrowth', 'Stock\nCAGR']
    ax4.set_xticklabels(labels, fontsize=10, color=COLORS['dark'])
    ax4.tick_params(axis='y', labelsize=10, colors=COLORS['dark'])
    ax4.set_facecolor('#f8f9fa')
    ax4.grid(True, alpha=0.3)

    # 5. Enhanced Net Profit trend
    ax5 = fig.add_subplot(gs[2, 0:2])
    ax5.plot(financial_data['Year'], financial_data['Net_Profit'], 'o-',
             color=COLORS['secondary'], linewidth=3, markersize=8,
             markerfacecolor='white', markeredgecolor=COLORS['secondary'], markeredgewidth=2)
    ax5.fill_between(financial_data['Year'], financial_data['Net_Profit'],
                     alpha=0.3, color=COLORS['secondary'])

    # Add value labels
    for year, profit in zip(financial_data['Year'], financial_data['Net_Profit']):
        ax5.annotate(f'₹{profit/100000:.1f}L', (year, profit),
                    textcoords="offset points", xytext=(0,10), ha='center',
                    fontweight='bold', fontsize=9, color='white',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['secondary'], alpha=0.8))

    ax5.set_title('Net Profit Trend', fontweight='bold', fontsize=14, color=COLORS['dark'], pad=15)
    ax5.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.0f}L'))
    ax5.tick_params(axis='x', rotation=35, labelsize=10, colors=COLORS['dark'])
    ax5.tick_params(axis='y', labelsize=10, colors=COLORS['dark'])
    ax5.set_facecolor('#f8f9fa')
    ax5.grid(True, alpha=0.3)

    # 6. Enhanced quarterly performance
    ax6 = fig.add_subplot(gs[2, 2:4])
    colors_quarterly = [COLORS['primary'], COLORS['accent'], COLORS['secondary']]
    bars = ax6.bar(quarterly_data['Metric'], quarterly_data['Amount_Crores'],
                   color=colors_quarterly, alpha=0.9,
                   edgecolor='white', linewidth=2)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height + 5000,
                f'₹{height/100000:.1f}L', ha='center', va='bottom',
                fontweight='bold', fontsize=10, color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['dark'], alpha=0.8))

    ax6.set_title('Latest Quarter', fontweight='bold', fontsize=14, color=COLORS['dark'], pad=15)
    ax6.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x/100000:.0f}L'))
    ax6.tick_params(axis='x', rotation=25, labelsize=10, colors=COLORS['dark'])
    ax6.tick_params(axis='y', labelsize=10, colors=COLORS['dark'])
    ax6.set_facecolor('#f8f9fa')
    ax6.grid(True, alpha=0.3)

    # Enhanced main title
    plt.suptitle('Reliance Industries Limited - Comprehensive Financial Performance Dashboard',
                fontsize=22, fontweight='bold', y=0.98, color=COLORS['dark'])

    # Enhanced key metrics box
    textstr = '''Market Cap: ₹18,87,779 Crores | Current Price: ₹1,395 | P/E: 25.2
ROCE: 9.69% | ROE: 8.40% | Dividend Yield: 0.39%'''

    fig.text(0.5, 0.02, textstr, fontsize=14, ha='center', fontweight='bold',
             color=COLORS['dark'],
             bbox=dict(boxstyle="round,pad=0.5", facecolor=COLORS['light'],
                      edgecolor=COLORS['primary'], linewidth=2, alpha=0.9))

    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Enhanced comprehensive dashboard saved as {save_path}")

def main():
    """Main function to generate all Reliance Industries infographics"""
    print("🏭 Creating Reliance Industries Financial Infographics...")
    print("=" * 70)

    # Create data
    financial_data, ratios_data, shareholding_data, growth_data, quarterly_data = create_reliance_data()

    # Define save paths
    folder_path = "Reliance Industries"

    # Generate all infographics
    create_revenue_profit_trend(financial_data,
                               f"{folder_path}/Reliance_Revenue_Profit_Trend.png")

    create_shareholding_pie_chart(shareholding_data,
                                 f"{folder_path}/Reliance_Shareholding_Pattern.png")

    create_financial_ratios_chart(ratios_data,
                                 f"{folder_path}/Reliance_Financial_Ratios.png")

    create_growth_rates_chart(growth_data,
                             f"{folder_path}/Reliance_Growth_Performance.png")

    create_quarterly_performance_chart(quarterly_data,
                                      f"{folder_path}/Reliance_Quarterly_Performance.png")

    create_revenue_profit_comparison(financial_data,
                                    f"{folder_path}/Reliance_Revenue_Profit_Comparison.png")

    create_comprehensive_dashboard(financial_data, ratios_data, shareholding_data,
                                  growth_data, quarterly_data,
                                  f"{folder_path}/Reliance_Financial_Dashboard.png")

    print("=" * 70)
    print("✅ All Reliance Industries infographics generated successfully!")
    print(f"\nGenerated files in '{folder_path}' folder:")
    print("• Reliance_Revenue_Profit_Trend.png - Revenue and Net Profit trends")
    print("• Reliance_Shareholding_Pattern.png - Shareholding distribution")
    print("• Reliance_Financial_Ratios.png - Key financial ratios")
    print("• Reliance_Growth_Performance.png - 10-year CAGR performance")
    print("• Reliance_Quarterly_Performance.png - Latest quarter results")
    print("• Reliance_Revenue_Profit_Comparison.png - Revenue vs Profit analysis")
    print("• Reliance_Financial_Dashboard.png - Comprehensive dashboard")
    print("\n📊 Market Cap: ₹18,87,779 Crores | Current Price: ₹1,395")

if __name__ == "__main__":
    main()