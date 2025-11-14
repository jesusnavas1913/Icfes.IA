import requests
import json
import time

print('Testing API endpoints...')

# Test 1: Health check
print('1. Testing health endpoint...')
try:
    response = requests.get('http://127.0.0.1:5000/health', timeout=10)
    print(f'   Status: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        print(f'   AI API: {data.get("ai_api", "unknown")}')
        print('   ✅ Health check passed')
    else:
        print('   ❌ Health check failed')
except Exception as e:
    print(f'   ❌ Health check error: {e}')

# Test 2: Generate question (first attempt)
print('2. Testing generate-question (first attempt)...')
try:
    payload = {
        'competencia': 'Matemáticas',
        'num_questions': 1,
        'dificultad': 'medio',
        'use_custom_knowledge': False
    }
    response = requests.post('http://127.0.0.1:5000/generate-question',
                           json=payload, timeout=30)
    print(f'   Status: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        if 'questions' in data:
            print('   ✅ First attempt successful')
            print(f'   Response length: {len(data["questions"])} chars')
        else:
            print('   ❌ First attempt failed - no questions in response')
            print(f'   Error: {data.get("error", "unknown")}')
    else:
        print('   ❌ First attempt failed')
        try:
            error_data = response.json()
            print(f'   Error: {error_data.get("error", "unknown")}')
        except:
            print(f'   Response: {response.text[:200]}...')
except Exception as e:
    print(f'   ❌ First attempt error: {e}')

# Wait a bit
time.sleep(2)

# Test 3: Generate question (second attempt)
print('3. Testing generate-question (second attempt)...')
try:
    response = requests.post('http://127.0.0.1:5000/generate-question',
                           json=payload, timeout=30)
    print(f'   Status: {response.status_code}')
    if response.status_code == 200:
        data = response.json()
        if 'questions' in data:
            print('   ✅ Second attempt successful')
            print(f'   Response length: {len(data["questions"])} chars')
        else:
            print('   ❌ Second attempt failed - no questions in response')
            print(f'   Error: {data.get("error", "unknown")}')
    else:
        print('   ❌ Second attempt failed')
        try:
            error_data = response.json()
            print(f'   Error: {error_data.get("error", "unknown")}')
        except:
            print(f'   Response: {response.text[:200]}...')
except Exception as e:
    print(f'   ❌ Second attempt error: {e}')

print('Testing completed.')
