# 🎨 Universal Infographics Generator

**Automatically generate beautiful, professional infographics from any data source with just one command!**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/infographics-generator.git
cd infographics-generator

# Install dependencies
pip install -r requirements.txt
```

### Usage Examples

#### 1. From Website URL (Financial Data)
```bash
python infographics_generator.py --url "https://www.screener.in/company/RELIANCE/consolidated/" --company "Reliance Industries"
```

#### 2. From CSV File
```bash
python infographics_generator.py --csv "sales_data.csv" --company "My Company" --folder "Q4_Reports"
```

#### 3. Custom Folder
```bash
python infographics_generator.py --url "https://example.com/data" --folder "Custom_Analytics"
```

## 🎯 Features

### ✨ **One-Command Generation**
- **Automatic data detection** and structuring
- **Smart chart selection** based on data type
- **Professional styling** with consistent branding
- **High-resolution output** (300 DPI) ready for presentations

### 📊 **Chart Types**
- **📈 Trend Charts** - Line charts with data point labels
- **📊 Bar Charts** - Enhanced bars with value labels
- **🥧 Pie/Donut Charts** - Beautiful distribution charts
- **📋 Dashboards** - Comprehensive multi-chart layouts
- **📉 Comparison Charts** - Side-by-side analysis

### 🎨 **Design Features**
- **Professional color palette** with consistent branding
- **Enhanced text visibility** with contrasting backgrounds
- **Clean, modern styling** suitable for business presentations
- **Responsive layouts** that adapt to data complexity
- **White backgrounds** optimized for documents and slides

## 📁 Project Structure

```
infographics-generator/
├── infographics_generator.py  # Main script
├── config.json               # Customization settings
├── requirements.txt          # Dependencies
├── README.md                # This file
└── examples/                # Sample data and outputs
    ├── sample_data.csv
    └── sample_outputs/
```

## 🔧 Configuration

Customize colors, chart settings, and output preferences in `config.json`:

```json
{
  "colors": {
    "primary": "#1f4e79",
    "secondary": "#2e8b57",
    "accent": "#ff6b35"
  },
  "chart_settings": {
    "figure_size": [14, 10],
    "dpi": 300,
    "font_size": 12
  }
}
```

## 📊 Supported Data Sources

### 🌐 **Web Sources**
- **Screener.in** - Indian stock market data
- **Yahoo Finance** - Global financial data
- **Generic websites** with structured data

### 📄 **File Formats**
- **CSV** - Comma-separated values
- **Excel** - .xlsx files (coming soon)
- **JSON** - Structured data (coming soon)

## 🎨 Sample Output

The generator creates multiple chart types automatically:

### Financial Data Example
```
Reliance_Industries_Infographics/
├── Revenue_Profit_Trend.png        # 📈 Time series analysis
├── Shareholding_Pattern.png        # 🥧 Distribution pie chart
├── Financial_Ratios.png            # 📊 Key metrics bar chart
├── Growth_Performance.png          # 📈 CAGR analysis
├── Quarterly_Performance.png       # 📊 Latest results
└── Comprehensive_Dashboard.png     # 📋 All-in-one view
```

## 💡 Usage Scenarios

### 🏢 **Business Analytics**
```bash
# Generate quarterly reports
python infographics_generator.py --csv "q4_results.csv" --company "TechCorp" --folder "Q4_2024_Reports"
```

### 📈 **Financial Analysis**
```bash
# Analyze stock performance
python infographics_generator.py --url "https://screener.in/company/TCS/" --company "TCS"
```

### 📊 **Sales Reports**
```bash
# Create sales dashboards
python infographics_generator.py --csv "sales_data.csv" --company "Sales Team" --folder "Monthly_Sales"
```

## 🛠️ Advanced Features

### 🔄 **Automatic Data Detection**
The generator automatically:
- Detects data types (numerical, categorical, time-series)
- Chooses appropriate chart types
- Structures data for optimal visualization
- Applies professional styling

### 🎨 **Smart Styling**
- **Consistent color schemes** across all charts
- **Enhanced text visibility** with background boxes
- **Professional typography** with proper hierarchy
- **Grid lines and spacing** optimized for readability

### 📱 **Output Optimization**
- **High-resolution images** (300 DPI) for printing
- **Optimized file sizes** for web sharing
- **White backgrounds** perfect for documents
- **Consistent dimensions** across all charts

## 🚀 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--url` | Web URL to fetch data from | `--url "https://example.com"` |
| `--csv` | CSV file path | `--csv "data.csv"` |
| `--company` | Company/Organization name | `--company "My Company"` |
| `--folder` | Output folder name | `--folder "Analytics_Report"` |

## 📋 Requirements

- **Python 3.8+**
- **matplotlib** - Plotting library
- **pandas** - Data manipulation
- **seaborn** - Statistical visualization
- **requests** - HTTP requests
- **beautifulsoup4** - Web scraping

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/infographics-generator/issues) page
2. Create a new issue with:
   - Your command
   - Expected vs actual output
   - Error messages (if any)

## 🎯 Roadmap

- [ ] **Excel file support** (.xlsx, .xls)
- [ ] **JSON data input**
- [ ] **Interactive charts** (HTML output)
- [ ] **Custom templates**
- [ ] **Batch processing** (multiple files)
- [ ] **API integration** (Google Sheets, etc.)

## 📊 Examples

### Quick Demo
```bash
# Generate infographics for Reliance Industries
python infographics_generator.py \\
  --url "https://www.screener.in/company/RELIANCE/consolidated/" \\
  --company "Reliance Industries" \\
  --folder "RIL_Analysis"
```

**Output**: Beautiful, professional infographics ready for your presentation! 🎨

---

**Made with ❤️ for data visualization enthusiasts**