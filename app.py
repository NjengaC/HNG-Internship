from start import app, auth_bp, api_bp
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)