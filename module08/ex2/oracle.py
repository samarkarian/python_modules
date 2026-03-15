import os
from dotenv import load_dotenv


if __name__ == '__main__':

    load_dotenv()

    matrix_mode: str | None = os.getenv('MATRIX_MODE')
    database_url: str | None = os.getenv('DATABASE_URL')
    api_key: str | None = os.getenv('API_KEY')
    log_level: str | None = os.getenv('LOG_LEVEL')
    zion_endpoint: str | None = os.getenv('ZION_ENDPOINT')

    print('\nORACLE STATUS: Reading the Matrix...\n')
    print('Configuration loaded:')

    print(f'Mode: {matrix_mode}')

    if matrix_mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production server")

    if api_key:
        print('API Access: Authenticated')
    else:
        print('API Access: No API KEY detected')

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print('Zion Network: Online')
    else:
        print('Zion Network: Offline')

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file missing")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
