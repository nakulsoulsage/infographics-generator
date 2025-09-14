#!/usr/bin/env python3
"""
🎨 Eternal Company Financial Infographics Generator
Beautiful, professional infographics for Eternal company financial data
"""

import matplotlib.pyplot as plt
import matplotlib.patheffects as patheffects
import seaborn as sns
import pandas as pd
import numpy as np
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
    'primary': '#e23744',      # Zomato red
    'secondary': '#2e8b57',    # Growth green
    'accent': '#ff6b35',       # Orange accent
    'success': '#28a745',      # Success green
    'warning': '#ffc107',      # Warning yellow
    'danger': '#dc3545',       # Danger red
    'info': '#17a2b8',         # Info blue
    'light': '#f8f9fa',        # Light background
    'dark': '#343a40'          # Dark text
}

PALETTE = ['#e23744', '#2e8b57', '#ff6b35', '#28a745', '#ffc107', '#dc3545', '#17a2b8', '#6f42c1']

def create_eternal_data():
    """Create Eternal company datasets from extracted financial data"""

    # Revenue trend data
    revenue_data = {
        'Year': ['Mar 2018', 'Mar 2019', 'Mar 2020', 'Mar 2021', 'Mar 2022', 'Mar 2023', 'Mar 2024', 'Mar 2025 (P)', 'TTM'],
        'Revenue': [466, 1313, 2605, 1994, 4192, 7079, 12114, 20243, 23204]
    }

    # Profitability data (focusing on recent years with better data)
    profit_data = {
        'Year': ['Mar 2018', 'Mar 2019', 'Mar 2020', 'Mar 2021', 'Mar 2022', 'Mar 2023', 'Mar 2024', 'Mar 2025 (P)'],
        'Net_Profit': [-107, -1010, -2386, -816, -1222, -971, 351, 527],
        'Revenue': [466, 1313, 2605, 1994, 4192, 7079, 12114, 20243]
    }

    # Operating margins data
    margin_data = {
        'Year': ['Mar 2022', 'Mar 2023', 'Mar 2024', 'Mar 2025 (P)'],
        'Operating_Margin': [-44, -17, 0, 3]
    }

    # Growth rates data
    growth_data = {
        'Metric': ['Sales Growth (5Y)', 'Sales Growth (3Y)', 'Sales Growth (TTM)', 'Stock CAGR (3Y)', 'Stock CAGR (1Y)'],
        'Percentage': [51, 69, 67, 71, 18]
    }

    # ROE data
    roe_data = {
        'Period': ['5 Years', '3 Years', 'Last Year'],
        'ROE': [-3, -1, 2]
    }

    return (pd.DataFrame(revenue_data), pd.DataFrame(profit_data),
            pd.DataFrame(margin_data), pd.DataFrame(growth_data), pd.DataFrame(roe_data))

def create_revenue_growth_chart(data, save_path):
    """Create stunning revenue growth visualization"""
    fig, ax = plt.subplots(figsize=(16, 12))
    fig.patch.set_facecolor('white')

    # Create bars with gradient effect
    colors = [COLORS['primary'] if 'TTM' in year else COLORS['secondary'] if 'P' in year else COLORS['info']
              for year in data['Year']]

    bars = ax.bar(range(len(data['Year'])), data['Revenue'],
                  color=colors, alpha=0.9, edgecolor='white', linewidth=2, width=0.7)

    # Add value labels with enhanced styling
    for i, (bar, revenue) in enumerate(zip(bars, data['Revenue'])):
        height = bar.get_height()
        label = f'₹{revenue:,.0f} Cr'
        if revenue > 10000:
            label = f'₹{revenue/1000:.1f}K Cr'

        ax.text(bar.get_x() + bar.get_width()/2., height + max(data['Revenue'])*0.01,
                label, ha='center', va='bottom',
                fontweight='bold', fontsize=11, color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=colors[i], alpha=0.9))

    # Enhanced styling
    ax.set_title('Eternal Company - Explosive Revenue Growth Journey',
                 fontsize=20, fontweight='bold', pad=30, color=COLORS['dark'])
    ax.set_ylabel('Revenue (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax.set_xlabel('Financial Year', fontsize=14, fontweight='bold', color=COLORS['dark'])

    # Custom x-axis labels
    ax.set_xticks(range(len(data['Year'])))
    ax.set_xticklabels(data['Year'], rotation=45, ha='right', fontsize=11)

    ax.set_facecolor('#f8f9fa')
    ax.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{x:,.0f}'))

    # Add trend line
    x_vals = range(len(data['Year']))
    z = np.polyfit(x_vals, data['Revenue'], 1)
    p = np.poly1d(z)
    ax.plot(x_vals, p(x_vals), "--", alpha=0.8, color=COLORS['danger'], linewidth=3, label='Trend')
    ax.legend(loc='upper left', fontsize=12)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Revenue growth chart saved: {save_path}")

def create_profitability_turnaround_chart(data, save_path):
    """Create profitability turnaround story chart"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 14))
    fig.patch.set_facecolor('white')

    # Net Profit Evolution
    colors = [COLORS['danger'] if profit < 0 else COLORS['success'] for profit in data['Net_Profit']]
    bars1 = ax1.bar(data['Year'], data['Net_Profit'],
                    color=colors, alpha=0.9, edgecolor='white', linewidth=2)

    # Add value labels
    for bar, profit in zip(bars1, data['Net_Profit']):
        height = bar.get_height()
        label = f'₹{profit:,.0f} Cr' if profit >= 0 else f'-₹{abs(profit):,.0f} Cr'
        y_pos = height + 20 if profit >= 0 else height - 50

        ax1.text(bar.get_x() + bar.get_width()/2., y_pos,
                label, ha='center', va='bottom' if profit >= 0 else 'top',
                fontweight='bold', fontsize=11, color='white',
                bbox=dict(boxstyle='round,pad=0.3',
                         facecolor=COLORS['success'] if profit >= 0 else COLORS['danger'], alpha=0.9))

    ax1.set_title('The Great Turnaround: From Losses to Profitability',
                  fontsize=18, fontweight='bold', color=COLORS['dark'], pad=20)
    ax1.set_ylabel('Net Profit (Rs. Crores)', fontsize=14, fontweight='bold')
    ax1.axhline(y=0, color='black', linestyle='-', alpha=0.5, linewidth=1)
    ax1.set_facecolor('#f8f9fa')
    ax1.grid(True, alpha=0.4)
    ax1.tick_params(axis='x', rotation=45)

    # Revenue vs Profit comparison
    ax2_twin = ax2.twinx()

    # Revenue bars (background)
    bars2 = ax2.bar(data['Year'], data['Revenue'], alpha=0.3, color=COLORS['info'], label='Revenue')

    # Profit line
    line = ax2_twin.plot(data['Year'], data['Net_Profit'], 'o-',
                        color=COLORS['primary'], linewidth=4, markersize=10,
                        markerfacecolor='white', markeredgecolor=COLORS['primary'],
                        markeredgewidth=3, label='Net Profit')

    ax2.set_title('Revenue Growth vs Profitability Journey',
                  fontsize=18, fontweight='bold', color=COLORS['dark'], pad=20)
    ax2.set_ylabel('Revenue (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['info'])
    ax2_twin.set_ylabel('Net Profit (Rs. Crores)', fontsize=14, fontweight='bold', color=COLORS['primary'])

    ax2.tick_params(axis='y', labelcolor=COLORS['info'])
    ax2_twin.tick_params(axis='y', labelcolor=COLORS['primary'])
    ax2.tick_params(axis='x', rotation=45)

    # Add zero line for profit
    ax2_twin.axhline(y=0, color=COLORS['dark'], linestyle='--', alpha=0.7)

    ax2.set_facecolor('#f8f9fa')
    ax2.grid(True, alpha=0.4)

    # Combined legend
    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=12)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Profitability turnaround chart saved: {save_path}")

def create_operating_margin_improvement_chart(data, save_path):
    """Create operating margin improvement visualization"""
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('white')

    # Create color gradient from red to green
    colors = []
    for margin in data['Operating_Margin']:
        if margin < -30:
            colors.append(COLORS['danger'])
        elif margin < -10:
            colors.append('#ff8c69')  # Light red
        elif margin < 1:
            colors.append('#ffd700')  # Gold
        else:
            colors.append(COLORS['success'])

    bars = ax.bar(data['Year'], data['Operating_Margin'],
                  color=colors, alpha=0.9, edgecolor='white', linewidth=2, width=0.6)

    # Add value labels
    for bar, margin in zip(bars, data['Operating_Margin']):
        height = bar.get_height()
        label = f'{margin}%'
        y_pos = height + 0.5 if margin >= 0 else height - 1.5

        ax.text(bar.get_x() + bar.get_width()/2., y_pos,
                label, ha='center', va='bottom' if margin >= 0 else 'top',
                fontweight='bold', fontsize=14, color='white',
                bbox=dict(boxstyle='round,pad=0.4',
                         facecolor=COLORS['success'] if margin >= 0 else COLORS['danger'], alpha=0.9))

    # Add zero line
    ax.axhline(y=0, color=COLORS['dark'], linestyle='-', alpha=0.7, linewidth=2)

    # Add trend arrow
    ax.annotate('', xy=(len(data)-0.3, data['Operating_Margin'].iloc[-1]),
                xytext=(0.3, data['Operating_Margin'].iloc[0]),
                arrowprops=dict(arrowstyle='->', lw=3, color=COLORS['success'], alpha=0.7))

    ax.set_title('Eternal Company - Operational Excellence Journey\nFrom Deep Losses to Profitability',
                 fontsize=18, fontweight='bold', color=COLORS['dark'], pad=25)
    ax.set_ylabel('Operating Profit Margin (%)', fontsize=14, fontweight='bold', color=COLORS['dark'])
    ax.set_xlabel('Financial Year', fontsize=14, fontweight='bold', color=COLORS['dark'])

    ax.set_facecolor('#f8f9fa')
    ax.grid(True, alpha=0.4, linestyle='-', linewidth=0.5)
    ax.tick_params(axis='x', rotation=0, labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    # Add text annotation
    ax.text(0.02, 0.98, 'Remarkable turnaround from -44% to +3% margin!',
            transform=ax.transAxes, fontsize=12, fontweight='bold',
            verticalalignment='top', color=COLORS['success'],
            bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light'], alpha=0.9))

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Operating margin improvement chart saved: {save_path}")

def create_growth_metrics_radar_chart(data, save_path):
    """Create growth metrics visualization"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
    fig.patch.set_facecolor('white')

    # Growth rates bar chart
    colors = [COLORS['success'], COLORS['primary'], COLORS['accent'], COLORS['info'], COLORS['warning']]
    bars = ax1.bar(range(len(data)), data['Percentage'],
                   color=colors, alpha=0.9, edgecolor='white', linewidth=2, width=0.7)

    # Add value labels
    for bar, percentage in zip(bars, data['Percentage']):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{percentage}%', ha='center', va='bottom',
                fontweight='bold', fontsize=13, color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['dark'], alpha=0.9))

    ax1.set_title('Exceptional Growth Across All Metrics',
                  fontsize=16, fontweight='bold', color=COLORS['dark'], pad=20)
    ax1.set_ylabel('Growth Percentage (%)', fontsize=14, fontweight='bold')
    ax1.set_xticks(range(len(data)))
    ax1.set_xticklabels([metric.replace(' ', '\n') for metric in data['Metric']],
                        fontsize=10, rotation=0)
    ax1.set_facecolor('#f8f9fa')
    ax1.grid(True, alpha=0.4, axis='y')

    # Performance categories pie chart
    categories = ['Sales Growth', 'Stock Performance']
    sales_avg = np.mean([51, 69, 67])  # Average of sales growth metrics
    stock_avg = np.mean([71, 18])      # Average of stock performance

    sizes = [sales_avg, stock_avg]
    colors_pie = [COLORS['primary'], COLORS['secondary']]
    explode = (0.05, 0.05)

    wedges, texts, autotexts = ax2.pie(sizes, labels=categories, autopct='%1.1f%%',
                                       colors=colors_pie, explode=explode,
                                       shadow=True, startangle=90,
                                       wedgeprops=dict(width=0.8, edgecolor='white', linewidth=3))

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(14)

    # Add center circle
    centre_circle = plt.Circle((0,0), 0.20, fc='white', linewidth=2, edgecolor=COLORS['dark'])
    ax2.add_artist(centre_circle)
    ax2.text(0, 0, 'Growth\nMix', ha='center', va='center',
             fontsize=12, fontweight='bold', color=COLORS['primary'])

    ax2.set_title('Growth Performance Breakdown',
                  fontsize=16, fontweight='bold', color=COLORS['dark'], pad=20)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Growth metrics chart saved: {save_path}")

def create_comprehensive_dashboard(revenue_data, profit_data, margin_data, growth_data, save_path):
    """Create comprehensive financial dashboard"""
    fig = plt.figure(figsize=(24, 18))
    fig.patch.set_facecolor('white')
    gs = fig.add_gridspec(3, 4, hspace=0.4, wspace=0.3)

    # 1. Revenue trend (top left)
    ax1 = fig.add_subplot(gs[0, 0:2])
    bars = ax1.bar(revenue_data['Year'][-5:], revenue_data['Revenue'][-5:],
                   color=COLORS['primary'], alpha=0.9, edgecolor='white', linewidth=2)
    for bar, revenue in zip(bars, revenue_data['Revenue'][-5:]):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 300,
                f'₹{revenue:,.0f}', ha='center', va='bottom',
                fontweight='bold', fontsize=10, color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=COLORS['primary'], alpha=0.8))
    ax1.set_title('Revenue Growth (Recent 5 Years)', fontweight='bold', fontsize=14)
    ax1.tick_params(axis='x', rotation=45, labelsize=10)
    ax1.set_facecolor('#f8f9fa')
    ax1.grid(True, alpha=0.3)

    # 2. Profitability trend (top right)
    ax2 = fig.add_subplot(gs[0, 2:4])
    recent_profit = profit_data['Net_Profit'][-5:]
    colors_profit = [COLORS['danger'] if p < 0 else COLORS['success'] for p in recent_profit]
    bars = ax2.bar(profit_data['Year'][-5:], recent_profit, color=colors_profit, alpha=0.9)
    ax2.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax2.set_title('Profitability Turnaround', fontweight='bold', fontsize=14)
    ax2.tick_params(axis='x', rotation=45, labelsize=10)
    ax2.set_facecolor('#f8f9fa')
    ax2.grid(True, alpha=0.3)

    # 3. Operating margin improvement (middle left)
    ax3 = fig.add_subplot(gs[1, 0:2])
    margin_colors = [COLORS['danger'] if m < 0 else COLORS['warning'] if m == 0 else COLORS['success']
                     for m in margin_data['Operating_Margin']]
    bars = ax3.bar(margin_data['Year'], margin_data['Operating_Margin'],
                   color=margin_colors, alpha=0.9)
    for bar, margin in zip(bars, margin_data['Operating_Margin']):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2.,
                height + 0.5 if height >= 0 else height - 1,
                f'{margin}%', ha='center',
                va='bottom' if height >= 0 else 'top',
                fontweight='bold', fontsize=11)
    ax3.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax3.set_title('Operating Margin Recovery', fontweight='bold', fontsize=14)
    ax3.set_facecolor('#f8f9fa')
    ax3.grid(True, alpha=0.3)

    # 4. Growth metrics (middle right)
    ax4 = fig.add_subplot(gs[1, 2:4])
    growth_colors = PALETTE[:len(growth_data)]
    bars = ax4.barh(range(len(growth_data)), growth_data['Percentage'],
                    color=growth_colors, alpha=0.9)
    for i, (bar, pct) in enumerate(zip(bars, growth_data['Percentage'])):
        width = bar.get_width()
        ax4.text(width + 1, bar.get_y() + bar.get_height()/2.,
                f'{pct}%', ha='left', va='center', fontweight='bold', fontsize=10)
    ax4.set_yticks(range(len(growth_data)))
    ax4.set_yticklabels([m.replace(' ', '\n') for m in growth_data['Metric']], fontsize=9)
    ax4.set_title('Growth Performance', fontweight='bold', fontsize=14)
    ax4.set_facecolor('#f8f9fa')
    ax4.grid(True, alpha=0.3, axis='x')

    # 5. Key metrics summary (bottom left)
    ax5 = fig.add_subplot(gs[2, 0:2])
    ax5.axis('off')

    metrics_text = f'''
    🏢 ETERNAL COMPANY - KEY HIGHLIGHTS

    💰 Current Revenue (TTM): ₹23,204 Crores
    📈 Revenue Growth (TTM): 67%
    🎯 Market Cap: ₹3,10,162 Crores
    💹 Current Stock Price: ₹321

    📊 REMARKABLE TRANSFORMATION:
    ❌ From -44% Operating Margin (2022)
    ✅ To +3% Operating Margin (2025P)

    🚀 GROWTH STORY:
    • 5-Year Sales CAGR: 51%
    • 3-Year Sales CAGR: 69%
    • First Profitable Year: 2024
    '''

    ax5.text(0.05, 0.95, metrics_text, transform=ax5.transAxes, fontsize=12,
             verticalalignment='top', horizontalalignment='left',
             bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light'],
                      edgecolor=COLORS['primary'], linewidth=2, alpha=0.9),
             color=COLORS['dark'], fontweight='normal')

    # 6. Performance timeline (bottom right)
    ax6 = fig.add_subplot(gs[2, 2:4])

    # Create a simple timeline
    years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025P']
    milestones = [
        'Start', 'Growth', 'Peak Rev', 'COVID Hit', 'Recovery', 'Scale Up', 'PROFITABLE!', 'Expansion'
    ]

    timeline_colors = [COLORS['info'] if i < 6 else COLORS['success'] for i in range(len(years))]

    # Plot timeline as horizontal line with markers
    y_pos = 0.5
    ax6.plot(range(len(years)), [y_pos]*len(years), 'o-', color=COLORS['primary'],
             linewidth=4, markersize=12, markerfacecolor='white',
             markeredgecolor=COLORS['primary'], markeredgewidth=3)

    # Add milestone labels
    for i, (year, milestone) in enumerate(zip(years, milestones)):
        ax6.text(i, y_pos + 0.1, milestone, ha='center', va='bottom',
                fontweight='bold', fontsize=9, rotation=45)
        ax6.text(i, y_pos - 0.1, year, ha='center', va='top',
                fontweight='bold', fontsize=10)

    ax6.set_xlim(-0.5, len(years)-0.5)
    ax6.set_ylim(0, 1)
    ax6.set_title('Journey Timeline', fontweight='bold', fontsize=14)
    ax6.axis('off')

    # Main title
    plt.suptitle('Eternal Company - Complete Financial Performance Dashboard',
                fontsize=24, fontweight='bold', y=0.98, color=COLORS['dark'])

    # Add footer
    fig.text(0.5, 0.01, 'Data Source: Screener.in | Analysis Period: 2018-2025 | Generated with Advanced Analytics',
             ha='center', va='bottom', fontsize=11, style='italic', color=COLORS['dark'])

    plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✓ Comprehensive dashboard saved: {save_path}")

def main():
    """Generate all Eternal company infographics"""
    print("🎨 Creating Eternal Company Financial Infographics...")
    print("=" * 70)

    # Create datasets
    revenue_data, profit_data, margin_data, growth_data, roe_data = create_eternal_data()

    # Output folder
    folder = "Zomato_Financial_Analysis"

    # Generate all charts
    create_revenue_growth_chart(revenue_data, f"{folder}/Eternal_Revenue_Growth_Journey.png")
    create_profitability_turnaround_chart(profit_data, f"{folder}/Eternal_Profitability_Turnaround.png")
    create_operating_margin_improvement_chart(margin_data, f"{folder}/Eternal_Operating_Margin_Recovery.png")
    create_growth_metrics_radar_chart(growth_data, f"{folder}/Eternal_Growth_Performance_Analysis.png")
    create_comprehensive_dashboard(revenue_data, profit_data, margin_data, growth_data,
                                  f"{folder}/Eternal_Complete_Financial_Dashboard.png")

    print("=" * 70)
    print("✅ All Eternal Company infographics generated successfully!")
    print(f"\n📁 Generated files in '{folder}':")
    print("🚀 Eternal_Revenue_Growth_Journey.png - Explosive revenue growth visualization")
    print("💰 Eternal_Profitability_Turnaround.png - From losses to profits story")
    print("📈 Eternal_Operating_Margin_Recovery.png - Operational efficiency improvement")
    print("🎯 Eternal_Growth_Performance_Analysis.png - Multi-metric growth analysis")
    print("📊 Eternal_Complete_Financial_Dashboard.png - Comprehensive overview")

    print(f"\n💡 Key Insights:")
    print("• Revenue grew from ₹466 Cr to ₹23,204 Cr (TTM)")
    print("• Achieved first profitable year in 2024")
    print("• Operating margin improved from -44% to +3%")
    print("• Exceptional growth rates across all metrics")

if __name__ == "__main__":
    main()