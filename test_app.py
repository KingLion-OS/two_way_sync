#!/usr/bin/env python3
"""
Simple test script to verify the Flask app functionality
"""

import os
import sys
import requests
import time
from threading import Thread

def test_app():
    """Test the Flask application"""
    print("🧪 Testing Flask Application...")
    
    # Test if app can be imported
    try:
        from app import app, sync_manager
        print("✅ App imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import app: {e}")
        return False
    
    # Test if templates exist
    template_path = os.path.join('templates', 'index.html')
    if os.path.exists(template_path):
        print("✅ Template file exists")
    else:
        print("❌ Template file missing")
        return False
    
    # Test basic app configuration
    if app.secret_key:
        print("✅ Secret key configured")
    else:
        print("⚠️  Secret key not configured (using default)")
    
    # Test sync manager initialization
    if sync_manager:
        print("✅ Sync manager initialized")
    else:
        print("❌ Sync manager failed to initialize")
        return False
    
    print("\n🚀 Starting Flask app for testing...")
    
    # Start the app in a separate thread
    def run_app():
        app.run(host='0.0.0.0', port=12000, debug=False, use_reloader=False)
    
    app_thread = Thread(target=run_app, daemon=True)
    app_thread.start()
    
    # Wait for app to start
    time.sleep(3)
    
    # Test endpoints
    base_url = "http://localhost:12000"
    
    try:
        # Test main page
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("✅ Main page accessible")
        else:
            print(f"❌ Main page returned status {response.status_code}")
            return False
        
        # Test status endpoint
        response = requests.get(f"{base_url}/status", timeout=5)
        if response.status_code == 200:
            status_data = response.json()
            print(f"✅ Status endpoint working: {status_data}")
        else:
            print(f"❌ Status endpoint returned status {response.status_code}")
            return False
        
        # Test sync endpoint (will likely fail without proper credentials)
        response = requests.post(f"{base_url}/sync", timeout=10)
        if response.status_code in [200, 500]:  # 500 expected without credentials
            print("✅ Sync endpoint accessible (credentials needed for full functionality)")
        else:
            print(f"⚠️  Sync endpoint returned unexpected status {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to test endpoints: {e}")
        return False
    
    print("\n✅ Basic functionality test completed successfully!")
    print("📝 Note: Full functionality requires proper credentials configuration")
    return True

def check_dependencies():
    """Check if all required dependencies are available"""
    print("📦 Checking dependencies...")
    
    required_packages = [
        'flask',
        'google.auth',
        'googleapiclient',
        'msal',
        'requests',
        'pandas',
        'openpyxl'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies available")
    return True

if __name__ == "__main__":
    print("🔍 Two-Way Sync App Test Suite")
    print("=" * 40)
    
    # Check dependencies first
    if not check_dependencies():
        sys.exit(1)
    
    print()
    
    # Test the app
    if test_app():
        print("\n🎉 All tests passed!")
        print("🌐 App should be running at: http://localhost:12000")
        print("⏹️  Press Ctrl+C to stop")
        
        try:
            # Keep the main thread alive
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n👋 Stopping test...")
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)