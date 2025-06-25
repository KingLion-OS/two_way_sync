# Two-Way Data Sync

A simple Flask web application that synchronizes data between Google Sheets and OneDrive Excel files. The app provides a clean web interface with a "Sync Now" button that triggers bidirectional data synchronization.

## Features

- 🔄 **Two-way sync** between Google Sheets and OneDrive Excel
- 🚀 **Simple web interface** with Bootstrap styling
- 🔒 **Secure authentication** using Google Service Account and Microsoft MSAL
- ⚡ **Smart sync** - skips sync if no differences detected
- 📊 **Real-time status** monitoring of both data sources
- 🛡️ **Error handling** with user-friendly messages

## Prerequisites

- Python 3.7+
- Google Cloud Project with Sheets API enabled
- Azure App Registration for Microsoft Graph API access
- Google Sheets document
- OneDrive Excel file

## Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone <repository-url>
cd two_way_sync
pip install -r requirements.txt
```

### 2. Google Sheets Setup

1. Create a Google Cloud Project
2. Enable the Google Sheets API
3. Create a Service Account
4. Download the service account credentials as `credentials.json`
5. Share your Google Sheets document with the service account email
6. Copy the Google Sheets ID from the URL

### 3. Microsoft Graph/OneDrive Setup

1. Register an application in Azure Portal
2. Configure API permissions for Microsoft Graph (Files.ReadWrite)
3. Create a client secret
4. Note down: Client ID, Tenant ID, and Client Secret
5. Upload an Excel file to OneDrive and get its file ID

### 4. Configuration

Copy the example environment file and configure:

```bash
cp .env.example .env
```

Edit `.env` with your actual values:

```env
FLASK_SECRET_KEY=your-secret-key-change-in-production
GOOGLE_SHEETS_ID=your-google-sheets-id
GOOGLE_SHEET_RANGE=Sheet1!A:Z
AZURE_CLIENT_ID=your-azure-client-id
AZURE_TENANT_ID=your-azure-tenant-id
AZURE_CLIENT_SECRET=your-azure-client-secret
ONEDRIVE_FILE_ID=your-onedrive-file-id
EXCEL_WORKSHEET_NAME=Sheet1
```

Copy your Google service account credentials:

```bash
cp credentials.json.example credentials.json
# Edit credentials.json with your actual service account credentials
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:12000`

## How It Works

1. **Data Reading**: The app reads data from both Google Sheets and OneDrive Excel
2. **Comparison**: Uses content hashing to detect differences
3. **Smart Sync**: Only syncs when differences are detected
4. **Bidirectional**: Can sync in both directions based on timestamp logic
5. **Error Handling**: Provides clear feedback on success or failure

## Security Considerations

- Service account credentials are stored locally (not in version control)
- MSAL handles OAuth tokens securely in memory
- Environment variables are used for sensitive configuration
- Error messages don't expose sensitive information
- HTTPS should be used in production

## API Endpoints

- `GET /` - Main web interface
- `POST /sync` - Trigger data synchronization
- `GET /status` - Check service status

## File Structure

```
two_way_sync/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── credentials.json       # Google service account credentials (not in repo)
├── .env                  # Environment variables (not in repo)
├── templates/
│   └── index.html        # Web interface template
├── credentials.json.example  # Example credentials file
├── .env.example         # Example environment file
└── README.md           # This file
```

## Troubleshooting

### Common Issues

1. **Google Sheets Access Denied**
   - Ensure the service account email has access to the sheet
   - Check that the Sheets API is enabled

2. **OneDrive Authentication Failed**
   - Verify Azure app registration settings
   - Check client ID, tenant ID, and client secret
   - Ensure proper API permissions are granted

3. **File Not Found**
   - Verify Google Sheets ID and OneDrive file ID
   - Check that files exist and are accessible

### Debug Mode

The app runs in debug mode by default. For production:

```python
app.run(host='0.0.0.0', port=12000, debug=False)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.