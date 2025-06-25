# Quick Setup Guide

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Google Sheets**
   - Create a Google Cloud Project
   - Enable Google Sheets API
   - Create a Service Account
   - Download credentials as `credentials.json`
   - Share your Google Sheet with the service account email

3. **Configure Microsoft Graph/OneDrive**
   - Register an app in Azure Portal
   - Set API permissions: `Files.ReadWrite`
   - Create a client secret
   - Note: Client ID, Tenant ID, Client Secret

4. **Set Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

## 🌐 Access the App

- **Local**: http://localhost:12001
- **Demo**: http://localhost:8080 (using run_demo.py)

## 📋 Configuration Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GOOGLE_SHEETS_ID` | Google Sheets document ID | `1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms` |
| `AZURE_CLIENT_ID` | Azure app client ID | `12345678-1234-1234-1234-123456789012` |
| `AZURE_TENANT_ID` | Azure tenant ID | `87654321-4321-4321-4321-210987654321` |
| `ONEDRIVE_FILE_ID` | OneDrive Excel file ID | `01ABCDEFGHIJKLMNOPQRSTUVWXYZ` |

## 🔧 Testing

Run the demo script to test functionality:
```bash
python run_demo.py
```

## 🛡️ Security Notes

- Never commit `credentials.json` or `.env` files
- Use HTTPS in production
- Regularly rotate client secrets
- Follow principle of least privilege for API permissions