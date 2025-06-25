#!/usr/bin/env python3
"""
Demo script to run the Flask application
"""

import os
import sys
import time
import threading
import requests
from app import app

def run_app():
    """Run the Flask app"""
    app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)

def test_endpoints():
    """Test the application endpoints"""
    time.sleep(3)  # Wait for app to start
    
    print("🧪 Testing application endpoints...")
    
    try:
        # Test status endpoint
        response = requests.get('http://localhost:8080/status', timeout=5)
        if response.status_code == 200:
            status_data = response.json()
            print(f"✅ Status endpoint: {status_data}")
        else:
            print(f"❌ Status endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Status endpoint error: {e}")
    
    try:
        # Test main page
        response = requests.get('http://localhost:8080/', timeout=5)
        if response.status_code == 200:
            print("✅ Main page loads successfully")
            print(f"📄 Page content length: {len(response.text)} characters")
        else:
            print(f"❌ Main page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Main page error: {e}")
    
    try:
        # Test sync endpoint (will fail without proper credentials)
        response = requests.post('http://localhost:8080/sync', timeout=10)
        if response.status_code in [200, 500]:
            print("✅ Sync endpoint accessible (credentials needed for full functionality)")
        else:
            print(f"⚠️  Sync endpoint unexpected status: {response.status_code}")
    except Exception as e:
        print(f"⚠️  Sync endpoint error: {e}")

if __name__ == "__main__":
    print("🚀 Starting Two-Way Sync Demo Application")
    print("=" * 50)
    
    # Start the Flask app in a background thread
    app_thread = threading.Thread(target=run_app, daemon=True)
    app_thread.start()
    
    # Test the endpoints
    test_thread = threading.Thread(target=test_endpoints, daemon=True)
    test_thread.start()
    
    print("🌐 Application running at: http://localhost:8080")
    print("📝 Note: Google Sheets and OneDrive services show 'Not configured' due to placeholder credentials")
    print("⏹️  Press Ctrl+C to stop")
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Stopping demo application...")
        sys.exit(0)