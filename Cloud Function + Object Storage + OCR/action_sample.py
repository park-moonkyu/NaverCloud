import requests
import time
import uuid
import json

OCR_SECRET_KEY = "직접입력"
OCR_ENDPOINT = "직접입력"
OCR_TEMPLATE_NO = 12372


def main(event):
    bucket = event.get("container_name")             # 버킷 이름
    object_name = event.get("object_name");          # 객체 이름(경로)
    timestamp_start = event.get("timestamp_start");  # 요청 처리를 시작한 시간
  
    try:
        timestamp = int(time.time())
        image_url = f"https://kr.object.ncloudstorage.com/{bucket}/{object_name}" # 청구서 이미지 Object Storage 경로
        request_id = str(uuid.uuid4())
        
        headers = {
            "X-OCR-SECRET": OCR_SECRET_KEY,
            "Content-Type": "application/json"
        }
      
        request_body = {
            "version": "V2",
            "requestId": request_id,
            "timestamp": timestamp,
            "lang": "ko",
            "images": [
                { 
                    "format": "jpg",
                    "url": image_url,
                    "name": object_name,
                    "templateIds": [OCR_TEMPLATE_NO]
                }
            ]
        }
        
        # CLOVA OCR API 호출
        response = requests.post(OCR_ENDPOINT, headers=headers, data=json.dumps(request_body))

        if response.status_code == 200:
            result = response.json()
            images = result.get("images")
            if images is None or len(images) < 0 or images[0].get("inferResult") != "SUCCESS":
                return {"result": "failure", "reason": "Failed to recognize image"}
                
            extractedFields = {}    # 추출된 필드 값
            fields = images[0].get("fields")
            for field in fields:
                f_name = field.get("name")
                f_text = field.get("inferText")
                extractedFields[f_name] = f_text
            
            return {"result": "success", "fields": extractedFields}
        else:
            return {
                "result": "failure",
                "code": str(response.status_code),
                "reason": response.reason,
                "detail": response.json()
            }

    except Exception as ex:
        # 액션 결과 JSON에 ‘error’ 필드가 포함되어 있으면, 액션 실행 실패로 간주
        return {"error": str(ex)}